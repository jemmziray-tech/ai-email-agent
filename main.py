import os
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import google.generativeai as genai
from dotenv import load_dotenv

# ==========================================
# 1. SETUP AND CONFIGURATION
# ==========================================

# Load hidden secrets from the .env vault
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini Brain
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-flash-latest")

# Configure Gmail Access
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# ==========================================
# 2. CORE FUNCTIONS
# ==========================================


def generate_email_draft(task_name, recipient_email):
    """Uses Gemini to generate a personalized email based on a task."""
    client_name = (
        "client"  # In a real scenario, you'd extract this from your CRM or task data
    )
    print(f"🧠 Drafting custom email for: '{client_name}'...")

    prompt = f"Write a short, professional follow-up email addressed to '{client_name}' regarding this task: '{task_name}'. Do not include a Subject line. Sign the email as 'Your Market Manager'."

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini Error: {e}"


def send_email_api(draft_text, recipient_email):
    """Connects to Gmail and sends the generated draft."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()
        message.set_content(draft_text)
        message["To"] = recipient_email
        message["From"] = "me"
        message["Subject"] = "Task Follow-Up"

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {"raw": encoded_message}

        send_message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f"✅ Email sent to {recipient_email}! (ID: {send_message['id']})")
    except Exception as error:
        print(f"❌ Oops! Error sending to {recipient_email}: {error}")


# ==========================================
# 3. MAIN EXECUTION
# ==========================================


def main():
    print("🚀 Starting AI Email Agent...\n")

    # Define our data
    tasks = [
        {
            "name": "Ads performance is down. Please follow up with the client and offer assistance to improve results.",
            "due_date": "2026-04-20",
        }
    ]
    target_emails = ["mzirayjohn4@gmail.com", "john@nm-aist.ac.tz"]

    # Grab the current task
    current_task = tasks[-1]

    # The Automation Loop
    for email in target_emails:
        print("-" * 40)
        # 1. Draft
        custom_draft = generate_email_draft(current_task["name"], email)
        # 2. Send
        send_email_api(custom_draft, email)

    print("\n🎉 All tasks complete. Shutting down Agent.")


# This tells Python to run the main() function when we start the script
if __name__ == "__main__":
    main()
