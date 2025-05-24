
# LinkedIn Auto-Connect Bot 🤖

This Python script automates sending connection requests on [LinkedIn](https://www.linkedin.com) using Selenium WebDriver. It navigates to the "Grow your network" page, clicks "Load more", and sends connect requests to all visible profiles.

---

## 🚀 Features

- Automates login to LinkedIn.
- Navigates to the "Grow Your Network" section.
- Loads more connection suggestions.
- Automatically sends connection requests.
- Bypasses UI overlay issues using JavaScript click.
- Handles exceptions gracefully.

---

## 🛠 Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Python Packages

```bash
pip install selenium pyautogui
```

---

## 📄 Usage

1. **Clone the Repository**

```bash
git clone https://github.com/nabeelalikhan0/LinkdIn-Automatic-Network-Increaser.git
cd linkedin-auto-connect-bot
```

2. **Set your LinkedIn credentials**

Replace these lines in the script with your actual credentials:

```python
email = "your_email@example.com"
password = "your_password"
```

> ⚠️ **Important:** Never commit your credentials to GitHub. Use environment variables or secret managers in real projects.

3. **Run the script**

```bash
python auto_connect.py
```

---

## 📸 Demo
![alt text](image.png)
---

## ⚠️ Disclaimer

- This script is for educational purposes only.
- Use responsibly and avoid spamming users.
- Automation on LinkedIn may violate their Terms of Service. Use at your own risk.

---

## 📬 Contact

Created by Nabeel Ali Khan(https://www.instagram.com/nabeelalikhan_/)  
Feel free to open issues or submit PRs for improvements!
