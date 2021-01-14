import schedule as sc
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込みます。
load_dotenv()

# 接続に必要なオブジェクトを生成
schedule = sc.Schedule()

#botのコマンドプレフィックスを設定(コマンドを打つときにはじめに打つ文字)
bot = commands.Bot(command_prefix = '/')


#botが接続を完了したときの処理
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#コマンド一覧を表示するコマンド
@bot.command()
async def commands(ctx):
    text = '/work_space : スケジュール、進捗管理、コマンドセンターを生成します。\n/add_sc :スケジュールを追加します。\n/sc_list :現在のスケジュールのリストを表示します。'
    await ctx.send(text)

#ワークスペースを作成するコマンド
@bot.command()
async def work_space(ctx):
    category_id = ctx.channel.category_id
    category = ctx.guild.get_channel(category_id)
    text = 'スケジュール'
    new_channel = await category.create_text_channel(name=text)
    schedule.set_channel_id(new_channel.id)

#スケジュールを追加するときのコマンド
@bot.command()
async def add_sc(ctx,a: str,b: str):
    schedule.add(data =a,message =b)
    print(schedule.get_channnel_id())
    if schedule.get_channnel_id() == 0:
        schedule.set_channel_id(ctx.channel.id)
    print(ctx.channel.id)
    schedule.add(a,b)
    await ctx.send('スケジュールの追加に成功しました')

@bot.command()
async def sc_list(ctx):
    for itr in schedule.get_list().items():
        await ctx.send(itr)

#######################################################
#スケジュール通知のためのループ処理
#######################################################
@tasks.loop(seconds=15)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d/%H/%M')
    if now in schedule.get_list():
        print(schedule.get_channnel_id())
        channel = bot.get_channel(schedule.get_channnel_id())
        await channel.send(schedule.get_list()[now])
        schedule.delete_date(now)

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
bot.run(os.getenv('TOKEN'))
