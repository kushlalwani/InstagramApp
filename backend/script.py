import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_to_instagram(username, password, driver):
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login form
    try:
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
    except:
        driver.save_screenshot("login_timeout.png")
        raise Exception("Login page failed to load.")

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click login
    login_button = WebDriverWait(driver, 6).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
    login_button.click()

    # Wait for redirection to complete: wait for URL to change to homepage or anything non-login
    WebDriverWait(driver, 5).until(lambda d: "accounts/login" not in d.current_url)

    # Dismiss "Save Your Login Info?" popup if present
    try:
        save_info_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        save_info_btn.click()
    except:
        pass  # popup didn't appear

    # Dismiss "Turn on Notifications" popup if present
    try:
        notif_btn = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        notif_btn.click()
    except:
        pass

    # Now navigate to the profile safely
    #driver.get(f"https://www.instagram.com/{username}/")

def scrape_usernames(driver):
    users = set()

    # Scrollable container using your confirmed structure
    scroll_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"

    scrollable_div = WebDriverWait(driver, 6).until(
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
        time.sleep(1.2)

        # Break when no new users loaded
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height and len(users) == previous_count:
            break
        last_height = new_height

    return users

def get_following_and_follower(username, password):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    
    try:
        login_to_instagram(username, password, driver)

        driver.get(f"https://www.instagram.com/{username}/following/")
        time.sleep(2)

        # Following
        following_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]"))
        )
        following_btn.click()
        time.sleep(1)
        following = scrape_usernames(driver)

        # Back to profile, then followers
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(1)
        followers_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))
        )
        followers_btn.click()
        time.sleep(1)
        followers = scrape_usernames(driver)

        driver.quit()
        return following, followers
    finally:
        driver.quit()