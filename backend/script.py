import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("IG_USERNAME", "").strip("'\"")
PASSWORD = os.getenv("IG_PASSWORD", "").strip("'\"")

# Configure Chrome
options = Options()
#options.add_argument("--headless=new")  # Use new headless mode for better stability
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



def login_to_instagram(username, password):
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login form
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for redirection to complete: wait for URL to change to homepage or anything non-login
    WebDriverWait(driver, 15).until(lambda d: "accounts/login" not in d.current_url)

    # Dismiss "Save Your Login Info?" popup if present
    try:
        save_info_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        save_info_btn.click()
    except:
        pass  # popup didn't appear

    # Dismiss "Turn on Notifications" popup if present
    try:
        notif_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        notif_btn.click()
    except:
        pass

    # Now navigate to the profile safely
    #driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(2)

def scrape_usernames():
    users = set()

    # Scrollable container using your confirmed structure
    scroll_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"

    scrollable_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, scroll_xpath))
    )

    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

    while True:
        # Find all <a> tags within the scrollable container
        links = scrollable_div.find_elements(By.XPATH, ".//a[contains(@href, '/')]")

        previous_count = len(users)

        for link in links:
            href = link.get_attribute("href")
            if href:
                try:
                    username = href.split("/")[-2]  # extract 'username' from .../username/
                    if username and username not in users:
                        users.add(username)
                except IndexError:
                    continue  # safety catch

        # Scroll to bottom
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(1.5)

        # Break when no new users loaded
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height and len(users) == previous_count:
            break
        last_height = new_height

    return users

def get_following_and_follower(user=USERNAME, passw=PASSWORD):
    login_to_instagram(user, passw)
    driver.get(f"https://www.instagram.com/{user}/")
    time.sleep(2)

    # Following
    following_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]"))
    )
    following_btn.click()
    time.sleep(2)
    following = scrape_usernames()

    # Back to profile, then followers
    driver.get(f"https://www.instagram.com/{user}/")
    time.sleep(2)
    followers_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))
    )
    followers_btn.click()
    time.sleep(2)
    followers = scrape_usernames()

    driver.quit()
    return following, followers