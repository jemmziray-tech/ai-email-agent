# 🤖 AI To-Do Email Automation Agent

## Purpose
Turn simple task reminders into professional emails automatically using Python, Google's Gemini AI, and the official Gmail API. 

This project acts as an autonomous digital assistant that reads a list of tasks, writes highly personalized, context-aware emails for each task, and dispatches them directly from a Gmail account.

## Deliverables & Features
* **🧠 LLM Integration:** Utilizes `gemini-flash-latest` for high-speed, intelligent email drafting.
* **✉️ Gmail API:** Securely authenticates via OAuth 2.0 to send emails on the user's behalf.
* **⚙️ Standalone Architecture:** Runs as a lightweight, automated `.py` script rather than a manual notebook.
* **🔒 Secure Secrets:** Implements `.env` for safe API key management.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jemmziray-tech/ai-email-agent.git cd ai-email-agent

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
