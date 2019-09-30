# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークン
TOKEN = 'NjE3NzczMjU3Mjk0MjE3MzI5.'+'XWwAdw.xcRsuBG_b8ZjQ8Rda3Wqdu2SSCA'

# 接続に必要なオブジェクトを生成
client = discord.Client()
list_entry = {}

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global list_entry
    global list_derby
    global flag
    # メッセージ送信者が Bot だった場合は無視する
    if message.author.bot:
        return
    elif(message.content == '抽選パスタ' and message.author.name == 'うめだJAPAN'):
    	list_entry = []
    	flag = 1
    	msg = 'こんパス！新たに抽選を開始します！\n 以下のコマンドをこのチャンネルに書き込んでね！\n \n entry：抽選に参加 \n exit：抽選を辞退 \n list：エントリー者リストの確認 \n chusen(うめだ氏専用)：抽選開始 \n :warning: 必読 :warning: \n 動画内で抽選を行いますが、当選された時点でライブチャットに返信がなければ当選が無効となります。\n また、抽選パスタを呼び出せるのは午後８時～翌朝６時です。\n 追加機能や変更の要望、不具合の報告等はフクナガまで。'
    # 「entry」と書き込んだらその人をエントリーのリストに追加
    elif message.content == 'entry' and flag == 1:
    	list_entry.append(str(message.author.name))
    	msg = message.author.name + ' さんが抽選に参加しました！（現在 ' + str(len(list(set(list_entry)))) + ' 人）'
    # 「exit」と書き込んだらその人をエントリーのリストから削除
    elif message.content == 'exit' and flag == 1:
    	while message.author.name in list_entry:
    		list_entry.remove(str(message.author.name))
    	msg = message.author.name + ' さんが抽選を辞退しました！（現在 ' + str(len(list(set(list_entry)))) + ' 人）'
    # 「list」と書き込んだらエントリー者のリストを出力
    elif message.content == 'list' and flag == 1:
        msg = 'エントリー者一覧（現在 ' + str(len(list(set(list_entry)))) + ' 人）：' + str(list(set(list_entry)))
    # うめださんが「chusen」と書き込んだらリストからランダムで取得
    elif message.content == 'chusen' and message.author.name == 'うめだJAPAN':
    	if len(list_entry) == 0:
            msg = 'エントリー者がいません！'
    	else:
            choice = random.choice(list(set(list_entry)))
            list_entry.remove(choice)
            msg = choice + ' さんが当選されました！（残り ' + str(len(list(set(list_entry)))) + ' 人）\n \n :warning: ただし、生放送チャットで返事がなければ無効になります！'
            flag = 0

    elif message.content == 'ダービーパスタ' and message.author.name == 'うめだJAPAN':
    	list_derby = {}
    	msg = 'こんパス！新たにダービーを開始します！\n 予想を先着順に連続数字(12345など)で書き込んでね！\n \n コマンド一覧\n exit : 予想を辞退\n check : 自分の予想を確認\n list : 参加者と予想の一覧を表示\n 〆切(うめだ氏専用) : ダービーの参加を〆切\n 連番数字(うめだ氏専用) : 予想的中者の発表\n \n :warning: 必読 :warning: \n 2回以上書き込んだ場合、最後に書き込んだ予想があなたの予想になります。\n 当選時にライブチャットに返信がなければ当選無効となります。'
    	flag = 2
    # 予想順位を書き込むと辞書型に名前と予想順位が追加される
    elif str(message.content).isdecimal() and flag == 2:
    	list_derby[message.author.name] = str(message.content)
    	msg = message.author.name + 'さんの予想 : ' + message.content + '（参加者 ' + str(len(list_derby)) + ' 人）'
    # 「exit」と書き込んだらその人を辞書型から削除
    elif message.content == 'exit' and flag == 2:
    	list_derby.pop(str(message.author.name), None)
    	msg = message.author.name + ' さんが予想を辞退しました！（参加者 ' + str(len(list_derby)) + ' 人）'
    # 「check」と書き込むとその人の予想した順位を表示
    elif message.content == 'check' and  flag == 2:
        msg = message.author.name + ' さんの予想は ' + str(list_derby.get(message.author.name)) + ' です！（参加者 ' + str(len(list_derby)) + ' 人）'
    # 「list」と書き込むと参加者と予想を表示
    elif message.content == 'list' and flag == 2:
        msg = '参加者一覧（現在 ' + str(len(list_derby)) + ' 人）：\n' + str(list_derby)
    # 「〆切」と書き込むと参加を〆切
    elif message.content == '〆切' and message.author.name == 'うめだJAPAN':
        msg = '参加が〆切になりました！'
        flag = 0
    # うめださんが結果順位を書き込むと、全的中者と３連単的中者を表示
    elif str(message.content).isdecimal() and message.author.name == 'うめだJAPAN' and flag == 0:
    	if len(list_derby) == 0:
            msg = '参加者がいません！'
    	else:
            msg = '全的中：\n' + str([k for k, v in list_derby.items() if str(v) == str(message.content)]) + '\n \n 3連単：\n' + str([k for k, v in list_derby.items() if str(v).startswith(str(message.content)[:3])]) + '\n \n :warning: ただし、生放送チャットで返事がなければ無効になります！'
    else: return

    await message.channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
