# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークン
TOKEN = 'NjE3MTk5NTk0MzMzNTM2Mjcx.XWuMag.4WCArxg6lSKsQhpQ670hUXw13Ls'

# 接続に必要なオブジェクトを生成
client = discord.Client()
list_entry = []

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global list_entry
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    elif message.content == '抽選パスタ':
    	msg = "こんパス！抽選パスタです！\n 抽選に参加する方は、以下のコマンドを指定のチャンネルに書き込んでください！\n \n entry：抽選に参加 \n exit：抽選を辞退 \n list：エントリー者リストの確認 \n chusen(うめださん専用)：抽選開始 \n reset(うめださん専用)：エントリー者リストをクリア \n \n 二回以上「entry」しても重複しないのでご安心ください。\n 念のため、定期的に「list」でログを残してくださると助かります。"
    # 「entry」と書き込んだらその人をエントリーのリストに追加
    elif message.content == 'entry':
    	list_entry.append(str(message.author.name))
    	msg = message.author.name + " さんが抽選に参加しました！（現在 " + str(len(list(set(list_entry)))) + " 人）"
    # 「exit」と書き込んだらその人をエントリーのリストから削除
    elif message.content == 'exit':
    	while message.author.name in list_entry:
    		list_entry.remove(str(message.author.name))
    	msg = message.author.name + " さんが抽選を辞退しました！（現在 " + str(len(list(set(list_entry)))) + " 人）"
    # 「list」と書き込んだらエントリー者のリストを出力
    elif message.content == 'list':
        msg = "エントリー者（現在 " + str(len(list(set(list_entry)))) + " 人）：" + str(list(set(list_entry)))
    # うめださんが「chusen」と書き込んだらリストからランダムで取得
    elif(message.content == 'chusen' and message.author.name == "うめだJAPAN"):
    	if len(list_entry) == 0:
            msg = "エントリー者がいません！"
    	else:
            choice = random.choice(list(set(list_entry)))
            msg = choice + " さん、当選おめパスタ！"
    # うめださんが「reset」と書き込んだらリストを初期化
    elif(message.content == 'reset' and message.author.name == "うめだJAPAN"):
    	list_entry.clear()
    	msg = "全員のエントリーがリセットされました！"
    else: return

    await message.channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)