import requests

def send_dingtalk_msg(content):
    webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0dd06a7c-e447-4447-a972-84fa9ffa42e9'
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {"content": content}
    }
    r = requests.post(webhook, json=data, headers=headers)
    print("DingTalk response:", r.text)


with open('result.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 你可以根据 test_api.py 的运行结果生成内容，比如：
# 示例直接发静态消息
send_dingtalk_msg(content)



