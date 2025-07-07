import requests


def send_dingtalk_msg(content):
    webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fd9662b6-1aa1-4944-87ff-03f33012dd39'
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {"content": content}
    }
    r = requests.post(webhook, json=data, headers=headers)
    print("DingTalk response:", r.text)


with open('Gdkjmain/result.json', 'r', encoding='utf-8') as f:
    content = f.read()
# 你可以根据 test_api.py 的运行结果生成内容，比如：
# 示例直接发静态消息
send_dingtalk_msg(content)




