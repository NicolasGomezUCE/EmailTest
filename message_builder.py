from email.message import EmailMessage

def create_email(sender, receiver, subject, body):
    """Constructs and returns an EmailMessage object."""
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    return msg