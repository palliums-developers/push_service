import smtplib
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

from mail.const import email_config, test_email_config

class Client():
    def __init__(self):
        config = email_config
        self.user = config.get("user")
        self.host = config.get("host")
        self.ssl = config.get("ssl")
        self.sender = config.get("sender")
        self.password = config.get("password")
        self.port = 465 if self.ssl else 5

    def send(self, receiver, text, subject):
        msg = MIMEText(text, "plain", "utf-8")
        msg["From"] = self._format_addr(self.sender, "")
        msg["To"] = self._format_addr(receiver, "")
        msg["Subject"] = Header(subject, 'utf-8').encode()
        self.server = smtplib.SMTP_SSL(host=self.host, timeout=5) if self.ssl == True else smtplib.SMTP(host=self.host, timeout=5)
        self.server.set_debuglevel(1)
        self.server.connect(self.host, self.port)
        self.server.login(self.user, self.password)
        self.server.sendmail(self.sender, [receiver], msg.as_string())
        self.server.close()

    def _format_addr(self,addr,name):
        name, addr = parseaddr(u"%s<%s>"%(name, addr))
        return formataddr((Header(name, 'utf-8').encode(), addr))

if __name__ == "__main__":
    client = Client()
    client.send("hxg@palliums.org", "this is test", "test")