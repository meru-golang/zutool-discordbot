import interactions
from datetime import datetime, timedelta
import fetch_api
import os
from dotenv import load_dotenv

bot = interactions.Client(
    token=os.environ['bot_token'],
    default_scope=os.environ['server_id'],
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
    ],
)

async def fetch_command(ctx: interactions.CommandContext, city: str):
    city_code = fetch_api.get_point_id(city)
    today_weather_data = fetch_api.get_pressure_status(city_code, "today")
    #print("市区町村コード: " + city_code)
    #print(today_weather_data)
    await ctx.send(f"{today_weather_data}")

bot.start()