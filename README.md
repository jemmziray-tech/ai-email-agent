# 🤖 AI To-Do Email Automation Agent

## Purpose
Turn simple task reminders into professional emails automatically using Python and the official Gmail API. 

This is my first AI Engineering project, built as a digital assistant to help automate my workflow!

## Deliverables & Features
- ✅ **Task Memory:** Saves a list of tasks and due dates.
- ✅ **AI Drafter:** Automatically drafts professional follow-up emails based on the task name.
- ✅ **Gmail API Integration:** Securely connects to Google Cloud to send emails directly from my account.
- ✅ **Jupyter Notebook Setup:** Runs in an interactive `.ipynb` environment for fast testing and execution.

## Prerequisites
To run this code on your own machine, you will need:
* Python 3.x installed.
* A Google Cloud Project with the **Gmail API** enabled.
* A `credentials.json` file downloaded from Google Cloud (OAuth 2.0 Client ID) placed in the main folder.

## Setup Instructions
1. Clone this repository to your computer.
2. Create a virtual environment and install the required tools:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib