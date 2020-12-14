from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
from sms.const import API_KEY

class Client():
    def __init__(self, api_key):
        self.client = YunpianClient(api_key)

    def send(self, mobile, text):
        param = {
            YC.MOBILE: mobile,
            YC.TEXT: text
        }
        return self.client.sms().single_send(param)

if __name__ == "__main__":
    client = Client(API_KEY)
    client.send("+8618710206362", "【sealpay】您的手机账户注册登录验证码是8888（若非本人操作，请删除本短信）")