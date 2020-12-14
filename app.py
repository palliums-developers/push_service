from flask import Flask, request, make_response

from mail import Client as MailClient
from sms import Client as SMSClient

app = Flask(__name__)


def handle_error(actual_do):
    def catch_exception(*args, **kwargs):
        try:
            actual_do(*args, **kwargs)
            return make_response("success", 200)
        except Exception as e:
            print(e)
            return make_response("error", 500)
    return catch_exception

@handle_error
@app.route("/email", methods=["POST"])
def send_email():
    pdata = request.form
    receiver = pdata.get("receiver")
    text = pdata.get("text")
    subject = pdata.get("subject")
    client = MailClient()
    client.send(receiver=receiver, text=text, subject=subject)

@handle_error
@app.route("/sms", methods=["POST"])
def send_sms():
    pdata = request.form
    receiver = pdata.get("receiver")
    text = pdata.get("text")
    client = SMSClient()
    client.send(receiver, text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)