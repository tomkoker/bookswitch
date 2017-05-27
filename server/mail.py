
import smtplib
from email.mime.text import MIMEText


class Mail:

    def __init__(self, app=None):
        if app is not None:
            init_app(app)

    def init_app(self, app):
        self.host = app.config.get('MAIL_HOST', 'localhost')
        self.username = app.config.get('MAIL_USERNAME')
        self.password = app.config.get('MAIL_PASSWORD')
        self.port = app.config.get('MAIL_PORT')
        self.tls = app.config.get('MAIL_TLS', False)
        self.ssl = app.config.get('MAIL_SSL', False)
        self.debug = app.config.get('MAIL_DEBUG', False)
        self.sender = app.config.get('MAIL_SENDER')

    def connect_server():
        server = None
        if self.sll:
            server = smtplib.SMTP_SSL(self.host, self.port)
        else:
            server = smtplib.SMTP(self.host, self.port)

        if self.tls:
            server.starttls()

        if self.username and self.password:
            server.login(self.username, self.password)

        return server

    def send(message):
        if self.debug:
            print('---------- MESSAGE FOLLOWS ----------')
            print(message.as_string())
            print('------------ END MESSAGE ------------')
        else:
            server = connect_server()
            server.sendmail(message.sender,
                            message.recipients,
                            message.as_string())

            server.close()

mail = Mail()


class Message:

    def __init__(self, subject='', recipients=[], body=None):

        self.recipients = recipients
        self.sender = sender

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        self.msg = msg

    def as_string(self):
        return self.msg.as_string()
