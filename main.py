import os
from dotenv import load_dotenv
from message_builder import create_email
from email_sender import send_email_smtp

load_dotenv()

def is_valid_email(email):
    # Simple check for @ and a dot
    return "@" in email and "." in email

def main():
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        print("Error: Configuration missing in .env file.")
        return

    print("--- Professional Email CLI ---")
    
    recipient = input("Receiver Email: ").strip()
    if not is_valid_email(recipient):
        print("Error: Invalid email format.")
        return

    subject = input("Subject: ").strip()
    
    # Multi-line Body Input
    print("Enter message body (Type 'END' on a new line to finish):")
    body_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        body_lines.append(line)
    body = "\n".join(body_lines)

    if not body:
        print("Error: Email body cannot be empty.")
        return

    # Process
    email_obj = create_email(sender, recipient, subject, body)
    success, result_message = send_email_smtp(sender, password, email_obj)
    print(f"\n{result_message}")

if __name__ == "__main__":
    main()