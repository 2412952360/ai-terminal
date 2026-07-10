print("=" * 40)
print("        AI Terminal")
print("=" * 40)

name = input("请输入你的名字：")

print(f"你好，{name}！")

while True:
    question = input("\n你：").strip()

    if question in ["exit", "quit", "退出"]:
        print("AI：再见！")
        break

    if question == "":
        print("AI：请重新输入！")
        continue

    if question == "help":
        print("======== 帮助 ========")
        print("exit   退出程序")
        print("quit   退出程序")
        print("help   查看帮助")
        print("======================")
        continue


    print("AI：")
    print("你刚刚说的是：")
    print(question)