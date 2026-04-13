import os
import json
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


# Accept the actual name directly!
def generate_email_draft(task_name, client_name):
    """Uses Gemini to generate a personalized email based on a task."""

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

    # 1. Load Data from the JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        # Replace target_emails with targets
        tasks = data["tasks"]
        targets = data["targets"]
        print(f"📂 Loaded {len(tasks)} task(s) and {len(targets)} target(s).")
    except FileNotFoundError:
        print("❌ Error: Could not find 'data.json'. Please create it.")
        return  # Stop the program if there is no data

    # 2. Grab the current task (we'll just grab the first one for now)
    current_task = tasks[0]

    # 3. The Automation Loop
    for target in targets:
        print("-" * 40)
        # Extract the specific details for this person
        person_name = target["name"]
        person_email = target["email"]

        # Draft (Pass the Name)
        custom_draft = generate_email_draft(current_task["name"], person_name)

        # Send (Pass the Email)
        send_email_api(custom_draft, person_email)

    print("\n🎉 All tasks complete. Shutting down Agent.")


if __name__ == "__main__":
    main()
