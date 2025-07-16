# import requests


# def send_dingtalk_msg(content):
#     webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fd9662b6-1aa1-4944-87ff-03f33012dd39'
#     headers = {"Content-Type": "application/json"}
#     data = {
#         "msgtype": "text",
#         "text": {"content": content}
#     }
#     r = requests.post(webhook, json=data, headers=headers)
#     print("DingTalk response:", r.text)


# with open('Gdkjmain/result.json', 'r', encoding='utf-8') as f:
#     content = f.read()
# # 你可以根据 test_api.py 的运行结果生成内容，比如：
# # 示例直接发静态消息
# send_dingtalk_msg('测试结果：',content)



import json
import requests
import os

def parse_allure_summary(summary_path):
    with open(summary_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {
        "总用例数": data['statistic']['total'],
        "成功": data['statistic']['passed'],
        "失败": data['statistic']['failed'],
        "跳过": data['statistic']['skipped'],
        "执行时间": data['time']['duration'] / 1000
    }

def send_wechat_message(webhook_url, summary: dict, report_url=""):
    content = (
        f"📢 自动化测试报告通知\n"
        f"> 总用例数：{summary['总用例数']}\n"
        f"> ✅ 成功：{summary['成功']}\n"
        f"> ❌ 失败：{summary['失败']}\n"
        f"> ⏭️ 跳过：{summary['跳过']}\n"
        f"> 🕒 耗时：{summary['执行时间']:.2f}s\n"
    )
    if report_url:
        content += f"> [点击查看测试报告]({report_url})"

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }

    resp = requests.post(webhook_url, json=data)
    if resp.status_code == 200:
        print("✅ 企业微信发送成功")
    else:
        print("❌ 企业微信发送失败:", resp.text)

if __name__ == "__main__":
    # 1. Allure 汇总数据路径（默认路径）
    summary_path = "allure-report/widgets/summary.json"

    # 2. 企业微信 webhook
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2ad33809-3916-48f3-ab3b-891b8e486581"

    # 3. 可选：你把报告部署到某处后的地址
    report_url = "https://cmd-is-xka.github.io/gdkj/"

    # 执行发送
    summary = parse_allure_summary(summary_path)
    send_wechat_message(webhook, summary,report_url)

