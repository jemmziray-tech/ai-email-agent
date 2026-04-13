<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=9B59B6&center=true&vCenter=true&width=435&lines=🤖+AI+Email+Automation+Agent;🚀+Powered+by+Gemini+Flash;✉️+Seamless+Gmail+Integration" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/commit-activity/m/jemmziray-tech/ai-email-agent?style=flat-square&color=9B59B6" alt="Activity" />
  <img src="https://img.shields.io/github/stars/jemmziray-tech/ai-email-agent?style=flat-square&color=9B59B6" alt="Stars" />
</p>

---

## 📖 Purpose
Turn simple task reminders into professional emails automatically using Python, Google's Gemini AI, and the official Gmail API. 

This project acts as an autonomous digital assistant that reads a list of tasks, writes highly personalized, context-aware emails for each task, and dispatches them directly from a Gmail account.

## 🚀 Features

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)

* **🧠 Smart Drafting:** Utilizes `gemini-flash-latest` for context-aware messaging.
* **📬 Automated Dispatch:** Direct integration with Gmail API via OAuth 2.0.
* **📂 Data-Driven:** Logic is strictly separated from data using an external `data.json`.
* **🔒 Secure Secrets:** Implements `.env` for safe API key management.

---

## 🛠️ How It Works
The agent follows a modular workflow to ensure data privacy and processing efficiency:
1. **Data Load:** Reads recipients and tasks from `data.json`.
2. **AI Drafting:** For each recipient, Gemini generates a personalized email.
3. **Dispatch:** The script authenticates via Google OAuth and sends the email.
4. **Safety:** Built-in rate limiting and cooldown periods to respect API constraints.

---

## ⚙️ Setup Instructions

1. Clone the Repository
```bash
git clone [https://github.com/jemmziray-tech/ai-email-agent.git](https://github.com/jemmziray-tech/ai-email-agent.git)
cd ai-email-agent

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Environment Setup:**
   ```bash
   -Rename .env.example to .env.
   -Add your Google Gemini API key to the .env file.
   -Place your Google Cloud credentials.json file in the root directory (for Gmail API access).

4. **Run the Agent:**
   ```bash
   python main.py

<p align="center">
Built with  by <a href="https://www.google.com/search?q=https://github.com/jemmziray-tech">John Mziray</a>
</p>
