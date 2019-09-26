# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークン
TOKEN = 'NjE3MTk5NTk0MzMzNTM2Mjcx.' + 'XWukUQ.YV9NolMGkJiYvADkl4-MSsGyrhU'

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
    global flag
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    elif(message.content == '抽選パスタ' and message.author.name == 'うめだJAPAN'):
    	list_entry.clear()
    	flag = 1
    	msg = 'こんパス！新たに抽選を開始します！\n 以下のコマンドをこのチャンネルに書き込んでね！\n \n entry：抽選に参加 \n exit：抽選を辞退 \n list：エントリー者リストの確認 \n chusen(うめだ氏専用)：抽選開始 \n 〆切(うめだ氏専用)：エントリーを〆切\n \n :warning: 必読 :warning: \n 動画内で抽選を行いますが、当選された時点でライブチャットに返信がなければ当選が無効となります。\n また、抽選パスタを呼び出せるのは午後８時～翌朝６時です。\n 追加機能や変更の要望、不具合の報告等はフクナガまで。'
    # 「entry」と書き込んだらその人をエントリーのリストに追加
    elif message.content == 'entry' and flag == 1:
    	list_entry.append(str(message.author.name))
    	msg = message.author.name + ' さんが抽選に参加しました！（現在 ' + str(len(list(set(list_entry)))) + ' 人）'
    # 「exit」と書き込んだらその人をエントリーのリストから削除
    elif message.content == 'exit':
    	while message.author.name in list_entry:
    		list_entry.remove(str(message.author.name))
    	msg = message.author.name + ' さんが抽選を辞退しました！（現在 ' + str(len(list(set(list_entry)))) + ' 人）'
    # 「list」と書き込んだらエントリー者のリストを出力
    elif message.content == 'list' :
        msg = 'エントリー者一覧（現在 ' + str(len(list(set(list_entry)))) + ' 人）：' + str(list(set(list_entry)))
    # うめださんが「chusen」と書き込んだらリストからランダムで取得
    elif(message.content == 'chusen' and message.author.name == 'うめだJAPAN'):
    	if len(list_entry) == 0:
            msg = 'エントリー者がいません！'
    	else:
            choice = random.choice(list(set(list_entry)))
            list_entry.remove(choice)
            msg = choice + ' さんが当選されました！（残り ' + str(len(list(set(list_entry)))) + ' 人）\n \n :warning: ただし、生放送チャットで返事がなければ無効になります！'
    # うめださんが「reset」と書き込んだらリストを初期化
    elif(message.content == '〆切' and message.author.name == 'うめだJAPAN'):
    	flag = 0
    	msg = 'エントリーが〆切になりました！'
    else: return

    await message.channel.send(msg)

    if(len(list(set(list_entry))) % 5 == 0 and len(list(set(list_entry))) != 0 and flag == 1):
    	await message.channel.send('\n 現在エントリー中：\n' + str(list(set(list_entry))) + '\n \n まだまだエントリーお待ちしてます！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)