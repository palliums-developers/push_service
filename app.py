from flask import Flask, request

from mail import Client as MailClient
from sms import Client as SMSClient

app = Flask(__name__)

CODE_OK = 200
CODE_ERROR = 500

def make_response(code, msg="success"):
    return {
        "msg": msg,
        "code": code
    }

@app.route("/email", methods=["POST"])
def send_email():
    try:
        pdata = request.form
        receiver = pdata.get("receiver")
        text = pdata.get("text")
        subject = pdata.get("subject")
        client = MailClient()
        client.send(receiver=receiver, text=text, subject=subject)
        return make_response(CODE_OK)
    except Exception as e:
        return make_response(CODE_ERROR, str(e))

@app.route("/sms", methods=["POST"])
def send_sms():
    try:
        pdata = request.form
        receiver = pdata.get("receiver")
        text = pdata.get("text")
        client = SMSClient()
        client.send(receiver, text)
        return make_response(CODE_OK)
    except Exception as e:
        return make_response(CODE_ERROR, str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)