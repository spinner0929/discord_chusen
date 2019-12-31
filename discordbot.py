# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークン
TOKEN = 'NjE3MTk5NTk0MzMzNTM2Mjcx.'+'XgtdhQ.YEYrbubhZ_Q1tmMnVyDMHTiL9E4'

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
    elif(message.content == '抽選パスタ' and message.author.guild_permissions.administrator):
    	list_entry = []
    	flag = 1
    	msg = 'こんパス！新たに抽選を開始します！\n entry と書き込んで抽選に参加してね！\n \n :small_blue_diamond: コマンド一覧\n entry：抽選に参加 \n exit：抽選を辞退 \n list：参加者リストの確認 \n chusen：抽選開始(管理者専用) \n \n :warning: 必読 :warning: \n 当選者はすぐに生放送のチャットで返信してください。返信がない場合は無効となります。\n BOTの呼び出しは午後８時～翌朝６時です。\n 追加機能や仕様変更、報告等はフクナガまで。'
    # 「entry」と書き込んだらその人をエントリーのリストに追加
    elif message.content == 'entry' and flag == 1:
    	list_entry.append(str(message.author.name))
    	msg = message.author.name + ' さんが参加しました！(現在 ' + str(len(list(set(list_entry)))) + ' 人)'
    # 「exit」と書き込んだらその人をエントリーのリストから削除
    elif message.content == 'exit' and flag == 1:
    	while message.author.name in list_entry:
    		list_entry.remove(str(message.author.name))
    	msg = message.author.name + ' さんが辞退しました！(現在 ' + str(len(list(set(list_entry)))) + ' 人)'
    # 「list」と書き込んだらエントリー者のリストを出力
    elif message.content == 'list' and flag == 1:
        msg = '参加者一覧(現在 ' + str(len(list(set(list_entry)))) + ' 人)：' + str(list(set(list_entry)))
    # うめださんが「chusen」と書き込んだらリストからランダムで取得
    elif message.content == 'chusen' and message.author.guild_permissions.administrator:
    	if len(list_entry) == 0:
            msg = '参加者がいません！'
    	else:
            choice = random.choice(list(set(list_entry)))
            list_entry.remove(choice)
            msg = choice + ' さんが当選しました！(残り ' + str(len(list(set(list_entry)))) + ' 人)\n \n :warning: ただし、生放送のチャットで返信がなければ無効になります！'
            flag = 0

    elif message.content == 'ダービーパスタ' and message.author.guild_permissions.administrator:
    	list_derby = {}
    	msg = 'こんパス！新たにダービーを開始します！\n 予想を先着順に数字で書き込んでね！\n \n :small_blue_diamond: コマンド一覧\n 12345(例) : 結果を予想\n exit : 予想を辞退\n check : 自分の予想を確認\n list : 参加者と予想の一覧を表示\n 〆切 : ダービーの参加を〆切(管理者専用)\n 12345(例) : ダービー結果の発表(管理者専用)\n \n :warning: 必読 :warning: \n 予想を２回以上書き込んだ場合、最後に書き込んだ予想のみが有効となります。\n BOTの呼び出しは午後８時～翌朝６時です。\n 追加機能や仕様変更、報告等はフクナガまで。'
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
    elif message.content == '〆切' and message.author.guild_permissions.administrator:
        msg = '参加が〆切になりました！'
        flag = 0
    # うめださんが結果順位を書き込むと、全的中者と３連単的中者を表示
    elif str(message.content).isdecimal() and message.author.guild_permissions.administrator and flag == 0:
    	if len(list_derby) == 0:
            msg = '参加者がいません！'
    	else:
            msg = '全的中：\n' + str([k for k, v in list_derby.items() if str(v) == str(message.content)]) + '\n \n 3連単：\n' + str([k for k, v in list_derby.items() if(str(v).startswith(str(message.content)[:3]) and str(v) != str(message.content))]) + '\n \n :warning: ただし、生放送のチャットで返信がなければ無効になります！\n \n :red_circle: 新たにダービーを開始する場合は、「ダービーパスタ」と書き込んでリセットしてください！'
    else: return

    await message.channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
