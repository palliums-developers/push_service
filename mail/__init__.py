import smtplib
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

from mail.const import email_config

class Client():
    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.ssl = kwargs.get("ssl")
        self.sender = kwargs.get("sender")
        self.password = kwargs.get("password")

    def send(self, address, txt, subject):
        msg = MIMEText(txt, "plain", "utf-8")
        msg["From"] = self._format_addr(self.sender, "")
        msg["To"] = self._format_addr(address, "")
        msg["Subject"] = Header(subject,'utf-8').encode()
        self.server = smtplib.SMTP_SSL(timeout=5) if self.ssl == True else smtplib.SMTP(timeout=5)
        self.server.connect(self.host, self.port)
        self.server.login(self.user, self.password)
        self.server.sendmail(self.sender, [address], msg.as_string())
        self.server.close()

    def _format_addr(self,addr,name):
        name, addr = parseaddr(u"%s<%s>"%(name, addr))
        return formataddr((Header(name, 'utf-8').encode(), addr))


if __name__ == "__main__":
    client = Client(**email_config)
    client.send("842269331@qq.com", "this is test", "test")