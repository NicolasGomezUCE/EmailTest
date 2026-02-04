import smtplib
import ssl

def send_email_smtp(sender_email, password, msg):
    """Handles the SMTP connection and authentication."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            return True, "Success: Email sent!"
    except smtplib.SMTPAuthenticationError:
        return False, "Error: Authentication failed. Check App Password."
    except Exception as e:
        return False, f"Error: {str(e)}"