import interactions
from datetime import datetime, timedelta
import fetch_api
import os
from dotenv import load_dotenv

load_dotenv()

bot = interactions.Client(
    token = os.environ['bot_token'],
    #default_scope=os.environ('server_id'), 特定のサーバー限定にするときはコメントアウトを外す。
)

@bot.command(
    name="fetch",
    description="今日の頭痛ーるを表示するよ。",
    options = [
        interactions.Option(
            name="city",
            description="あなたの市区町村名は？",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="date",
            description="表示する日付は？",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="今日", value='today'),
                interactions.Choice(name="明日", value='tommorow'),
                interactions.Choice(name="明後日", value='dayaftertomorrow')
            ],
        ),
    ],
)

async def fetch_command(ctx: interactions.CommandContext, city, date: str):
    city_code = fetch_api.get_point_id(city)
    weather_data = fetch_api.get_pressure_status(city_code, date)
    dating = fetch_api.check_date(date)
    #print("市区町村コード: " + city_code)
    #print("選択された日付： " + date)
    #print(weather_data)
    await ctx.send(f"{dating}の{city}の気圧は\n{weather_data}")

bot.start()