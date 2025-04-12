# 📸 InstaApp - Instagram Follower Tracker

InstaApp is a backend tool that automates the process of tracking Instagram followers and followings using Selenium, with plans to expand into a full web application using Flask and SQLAlchemy.

---

## 🚀 Features

- 🔐 Secure login to Instagram via Selenium WebDriver
- 👥 Automatically scrape your followers and followings
- 🔍 Identify who **doesn’t follow you back** or who **you don’t follow back**
- 📦 Environment variables loaded securely from `.env`
- 🛠️ Built with Python, Selenium, and Flask (coming soon)

---

## 📁 Project Structure

```
InstaApp/
├── .env                  # Secrets (Instagram credentials, DB URI)
├── .gitignore
├── venv/                 # Virtual environment
├── script.py             # Main scraping script
├── requirements.txt      # Python dependencies
├── README.md             # You are here :)
```

---

## 🔧 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/InstaApp.git
cd InstaApp
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

```
INSTA_USERNAME=your_instagram_username
INSTA_PASSWORD=your_instagram_password
```

> ⚠️ Do NOT commit this file to GitHub — it's in `.gitignore`.

---

## ▶️ Usage

Make sure your virtual environment is activated, then run:

```bash
python script.py
```

Your script will:
- Log in to your Instagram account
- Scroll through all followers and following
- Print or process the data accordingly

---

## 📌 To-Do

- [ ] Store results in SQLite or PostgreSQL
- [ ] Build REST API using Flask
- [ ] Add web dashboard to view follower stats
- [ ] Schedule automatic scraping (e.g., using `cron` or `APScheduler`)

---

## 🧠 Tech Stack

- Python 3.x
- Selenium
- Flask (WIP)
- SQLAlchemy (WIP)
- python-dotenv


