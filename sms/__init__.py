from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
from sms.const import API_KEY

class Client():
    def __init__(self):
        self.client = YunpianClient(API_KEY)

    def send(self, receiver, text):
        param = {
            YC.MOBILE: receiver,
            YC.TEXT: text
        }
        return self.client.sms().single_send(param)

if __name__ == "__main__":
    client = Client()
    client.send("+8618710206362", "【Violas】您有一条来自 1 的数据请求需要处理 。")