Birthday Email Wisher

Automated script that sends personalized happy birthday emails to people listed in a CSV file on their actual birthday.

## Features
    - Reads birthdays from a CSV file
    - Selects a random letter template
    - Replaces placeholder `[NAME]` with the recipient's name
    - Sends email via Gmail SMTP using secure TLS connection
    - Only triggers on the current day (month + day match)

## Setup Instructions

1. Add your email address in MY_EMAIL.
   - Go to your Google Account settings → Security.
   - Turn on 2-Step Verification (if not already enabled).
   - Once 2-Step Verification is active, return to Security → search for or select App passwords.
   - Create a new app password:
   - Select app: Mail (or Other and type e.g. "Birthday Wisher")
   - Click Generate
   - Copy the 16-character password displayed (no spaces).
   - Paste it into PASSWORD in the script.

2. Configure your Gmail credentials
   - Open the script and update the following variables:
   - MY_EMAIL = "your.email@gmail.com"
   - PASSWORD = "your-16-character-app-password"

3. Use 'pythonanywhere' to launch it in a cloud platform.