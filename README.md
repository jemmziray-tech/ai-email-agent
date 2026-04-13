<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=9B59B6&center=true&vCenter=true&width=435&lines=🤖+AI+Email+Automation+Agent;🚀+Powered+by+Gemini+Flash;✉️+Seamless+Gmail+Integration" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/commit-activity/m/jemmziray-tech/ai-email-agent?style=for-the-badge&color=9B59B6" alt="Activity" />
  <img src="https://img.shields.io/github/stars/jemmziray-tech/ai-email-agent?style=for-the-badge&color=9B59B6" alt="Stars" />
  <img src="https://img.shields.io/github/forks/jemmziray-tech/ai-email-agent?style=for-the-badge&color=9B59B6" alt="Forks" />
</p>

<h3 align="center">Transform simple task reminders into highly personalized, professional emails automatically using Google's Gemini AI and the official Gmail API.</h3>

---

## 📖 Overview
The **AI Email Automation Agent** is an autonomous digital assistant designed to streamline your communication workflow. By feeding it a simple list of tasks and recipients, the agent leverages Google's `gemini-flash-latest` model to draft context-aware, highly personalized emails, and dispatches them directly via your authenticated Gmail account.

## 🚀 Key Features

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/Gmail%20API-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
</p>

* **🧠 Intelligent Drafting:** Generates natural-sounding, contextually accurate messages using state-of-the-art AI.
* **📬 Seamless Dispatch:** Fully integrated with the official Gmail API via secure OAuth 2.0 authentication.
* **📂 Data-Driven Architecture:** Business logic is strictly separated from contact data using an external `data.json` file.
* **🔒 Secure by Design:** Utilizes `.env` files for robust API key and credential management.
* **🛡️ API-Friendly:** Built-in rate limiting and cooldown periods to respect Google's API constraints and prevent spam flagging.

---

## 🛠️ Architecture & Workflow

The agent follows a strict, modular pipeline to ensure efficiency and data privacy:
1. **Data Ingestion:** Parses `data.json` to extract recipient details and specific task instructions.
2. **AI Prompting:** Data is formatted and sent to the Gemini AI to generate a polished email draft tailored to each recipient.
3. **Authentication:** Authenticates your session via Google OAuth 2.0 (generating a local `token.json` for subsequent runs).
4. **Delivery:** The drafted email is securely encoded and dispatched through the Gmail API.

---

## ⚙️ Getting Started

### Prerequisites
Before running the agent, ensure you have the following:
* **Python 3.8+** installed on your machine.
* A **Google Gemini API Key** (obtainable from Google AI Studio).
* A Google Cloud Console project with the **Gmail API** enabled and OAuth 2.0 credentials (`credentials.json`) downloaded.

### Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/jemmziray-tech/ai-email-agent.git
cd ai-email-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure Environment Variables**
```bash
cp .env.example .env
```

**4. Add Google Credentials**
```bash
Place your downloaded credentials.json file directly into the root directory of the project.
```

**5. Define Your Data**
```bash
Populate the data.json file with your target recipients and their corresponding tasks.
(Example format):
[
  {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "task": "Remind her to submit the Q3 marketing analytics report by Friday noon."
  }
]
```

**6. Execute the Agent**
```bash
python main.py

Note: On the very first run, a browser window will automatically open asking you to authorize the application with your Google account. This will generate a token.json file so you don't have to re-authenticate every time.
```

<p align="center">
Built with love by <a href="https://www.google.com/search?q=https://github.com/jemmziray-tech">John Mziray</a>
</p>
