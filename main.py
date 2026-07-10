from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)


print("=" * 40)
print("        AI Terminal")
print("=" * 40)


name = input("请输入你的名字：")

print(f"你好，{name}！")


messages = [
    {"role": "system", "content": f"用户名字叫{name}，以后称呼用户时使用这个名字。"}
]


while True:

    question = input("\n你：").strip()

    if question in ["exit", "quit", "退出"]:
        print("AI：再见！")
        break

    if not question:
        print("AI：请输入内容！")
        continue

    if question == "help":
        print("""
========帮助========

exit / quit / 退出
退出程序

help
查看帮助

===================
""")
        continue

    messages.append({"role": "user", "content": question})

    print("AI：正在思考...")

    response = client.chat.completions.create(model="deepseek-chat", messages=messages)

    answer = response.choices[0].message.content

    messages.append({"role": "assistant", "content": answer})

    print("\nAI：")
    print(answer)
