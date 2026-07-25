import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, login, password, smtp_server="smtp.gmail.com",
                 imap_server="imap.gmail.com", smtp_port=587):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.smtp_port = smtp_port

    def send_email(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp_server, self.smtp_port)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()

    def receive_emails(self, header=None):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = f'(HEADER Subject "{header}")' if header else 'ALL'
        result, data = mail.uid('search', None, criterion)

        if not data[0]:
            print('There are no letters with current header')
            mail.logout()
            return None

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'

    email_client = EmailClient(login, password)

    # Отправка письма
    recipients = ['vasya@email.com', 'petya@email.com']
    subject = 'Subject'
    message = 'Message'
    email_client.send_email(recipients, subject, message)

    # Получение письма
    header = None
    email_client.receive_emails(header)