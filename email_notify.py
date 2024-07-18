import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# use 163 email as sender
class EmailSender:
    def __init__(self, sender_email: str, pass_word: str,
                 smtp_server="smtp.163.com", smtp_port=25):
        self.sender_email = sender_email
        self.password = pass_word
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, receiver_email: str, subject: str, detial: str):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(detial, "plain"))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            # server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())


default_msg = "Notice msg"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument Parsing.")
    parser.add_argument('--FROM', type=str, required=True, help="FROM")
    parser.add_argument('--PASSWORD', type=str, required=True, help="PASSWORD")
    parser.add_argument('--TO', type=str, required=True, help="RECIVE")
    parser.add_argument('--SUBJECT', type=str, required=True, help="SUBJECT")
    parser.add_argument('--DETAIL_FILE', type=str, required=False, help="FILE FOR DETAIL")
    args = parser.parse_args()

    send_msg = default_msg
    if args.DETAIL_FILE:
        send_msg = ""
        with open(args.DETAIL_FILE, 'r') as f:
            for line in f:
                send_msg = send_msg + line
    email_sender = EmailSender(args.FROM, args.PASSWORD)
    email_sender.send_email(args.TO, args.SUBJECT, send_msg)
