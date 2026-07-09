print("=" * 40)
print("        AI Terminal")
print("=" * 40)

name = input("请输入你的名字：")

print(f"你好，{name}！")

question = input("请输入一句话：")

print()
print("你输入的内容长度是：", len(question))   # 新增这一行
print("你刚刚输入的是：")
print(question)