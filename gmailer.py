import smtplib #inbuilt module of Python

email = 'sender_email@gmail.com'
password = 'password'
to_mail = 'recipient_mail@gmail.com'
subject = 'Code executed'
message = 'Code execution is complete.'


def gmailer(to_email, message):

    class Gmail(object):
        def __init__(self, email, password):
            self.email = email
            self.password = password
            self.server = 'smtp.gmail.com'
            self.port = 587
            session = smtplib.SMTP(self.server, self.port)
            session.ehlo()
            session.starttls()
            session.ehlo
            session.login(self.email, self.password)
            self.session = session

        def send_message(self, subject, to_mail, message):
            name = to_mail.split('@')[0].title()
            if '.' in name:
                name = to_mail.split('.')[0].title()
            if '_' in name:
                name = to_mail.split('_')[0].title()

            body = 'Hey %s, <br/> <br/> %s' % (name, message)

            headers = [
                "From: " + self.email,
                "Subject: " + subject,
                "To: " + to_mail,
                "MIME-Version: 1.0",
                "Content-Type: text/html"]
            headers = "\r\n".join(headers)
            self.session.sendmail(
                self.email,
                to_mail,
                headers + "\r\n\r\n" + body)

    gm = Gmail(email, password)

    gm.send_message(subject, to_email, message)


if __name__ == '__main__':
    gmailer(to_email, message)
