# 📸 InstagramApp – Instagram Follower Tracker

InstagramApp is a web-based tool to track your Instagram followers and following using Selenium for scraping, SQLAlchemy for data storage, and Flask for visualization.

---

## 🚀 Features

- 🔐 Secure login via headless Selenium browser  
- 👥 Scrapes all followers and followings  
- 🔄 Identifies:
  - People who don’t follow you back
  - People you don’t follow back  
  - New users who have unfollowed you
- 📊 View all data in a simple Flask web app  
- 🧠 Stores everything in an SQLite database  

---

## 🧱 Project Structure

```
InstaApp/
├── backend/
│   ├── app.py             # Flask app and routes
│   ├── models.py          # SQLAlchemy models
│   ├── script.py          # Selenium scraping utilities
|   ├── __init__.py        # Creates the database tables
├── templates/             # HTML templates for Flask
│   ├── index.html
│   ├── followers.html
│   ├── following.html
|   ├── login.html
|   ├── rescrape_results.html
|   ├── scraping.html
├── static/
|   ├──style.css
├── instagram.db           # SQLite database (created after running)
├── .env                   # IG credentials (not committed)
├── .flaskenv
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Setup

### 1. Clone the repo

```bash
git clone https://github.com/kushlalwani/InstagramApp.git
cd InstagramApp
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App
---

First, type this into the terminal:

```bash
flask run
```

Visit [http://localhost:5000](http://localhost:5000) to explore your follower data.

---

### 5. Log In to Instagram
---

Once the webpage is opened, click on "Set Instagram Credentials" button, then enter your Instagram username and password.

Don't worry, your credentials are only locally saved on your device. 

Wait for the page to load, then you will be able to see all your Instagram information

## ✅ To-Do

- [ ] Make webpage look more visually appealing by adding Instagram-like designs and potentially user's profile pictures
- [ ] Add feature to unfollow and remove users as followers directly from the app
- [ ] Continue to update the Selenium script as Instagram changes

---

## 💡 Tech Stack

- Python 3
- Flask
- SQLAlchemy
- Selenium
- WebDriver Manager
- SQLite
- Dotenv
- HTML
