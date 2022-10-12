from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin Chào {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_news()
    x = 1
    print(data)
    for item in data:
        await update.message.reply_text(f'{item}')
        #await update.message.reply_text(f' 123 ')
        x = x + 1
        if x == 7: break


def get_news():
    list_news = []
    r = requests.get('https://vnexpress.net/')
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})
    print(mydivs)

    for new in mydivs:
        newdict = {}
        #newdict["link]"] = new.a.get("href")
        newdict["title]"] = new.a.get("title")

        list_news.append(newdict)
    return list_news



app = ApplicationBuilder().token("5435752958:AAFPTdbfqUAumSaBj-3B6PnpZhQ-mHR50MQ").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("tintuc", news))
app.add_handler(CommandHandler("tintuc", news))
app.run_polling()
