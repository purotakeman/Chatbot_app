""" 
学んだこと
・辞書：「キー」と「値」がセットになったデータの集まり "{}"を使用する

"""

# 辞書の作成
chat_rules = {
    "こんにちは": "ごきげんよう！元気か？",
    "ありがとう": "気にせんでええでー",
    "さようなら": "ほな、またなー",
    "Python": "Python早くマスターしてくれー",
    "天気": "今日は晴れやで"
}

bot = "ボット: "

while True:
    user_input = input("あなた: ")

    if user_input == "やめる":
        print(bot + "またなー")
        break

    if user_input in chat_rules:
        response = chat_rules[user_input]

    else:
        response = "その言葉はまだ理解しとらんわ、、"

    print(bot + response)



# 辞書からの特定のキーに対応する値を取り出すには、[キー]を使用する
# response_to_hello = chat_rules["こんにちは"]

# user_input = "天気"

# response = chat_rules["天気"]

# print("ボット: " + response)

























""" name = input("あなたの名前を教えてください: ")

print("ボット: " + name + "さん、ようこそ！") """























