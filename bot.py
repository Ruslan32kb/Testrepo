import logging, sqlite3
from aiogram import Bot, Dispatcher, executor, types, filters

# Initialize bot and dispatcher

bot = Bot(token='5150073772:AAHDjsRlC3JJ9zFlNntaacLx3Db0-DsUciU')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
# ADMIN = 535396191

                                       # Body my bot

# menu in bot Maestro

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
    buttons = ["/eat", "/walk", "/xxx", "/hide"]
    keyboard.add(*buttons)
    await  message.answer("Обирай правильно мій друже", reply_markup=keyboard)


# feature eats

@dp.message_handler(commands=['eat'])
async def cmd_eats_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Смачно поїсти", url="https://www.google.com/maps/place/%D0%A8%D0%BE%D0%A8%D0%BE+%D0%9F%D1%96%D1%86%D0%B0/@48.2667195,25.9369824,16.19z/data=!4m5!3m4!1s0x473409becbcc7c43:0xcf29077cc987893c!8m2!3d48.26778!4d25.9410247"),
        types.InlineKeyboardButton(text="Дешево та багато", url="https://www.google.com/maps/place/CherAmi/@48.2874365,25.9317256,18z/data=!4m5!3m4!1s0x473409e01da70653:0x7082e43d80ad2df5!8m2!3d48.2874365!4d25.932444")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Обери чого душа бажає", reply_markup=keyboard)

# feature go

@dp.message_handler(commands=['walk'])
async def cmd_save_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Архітектура міста", url="https://ru.guide.cv.ua/what-to-see"),
        types.InlineKeyboardButton(text="Гастро тур", url="https://ru.guide.cv.ua/eat-and-drink"),
        types.InlineKeyboardButton(text="Розваги", url="https://ru.guide.cv.ua/things-to-do")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Обирай маршрут", reply_markup=keyboard)

# feature sex

@dp.message_handler(commands=['xxx'])
async def cmd_sex_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Класика", url="https://www.google.com/search?tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=APq-WBsJfm4Mm6ggZnWvfzIiKKaXEcF1hA:1649027158511&q=%D1%81%D0%B5%D0%BA%D1%81+%D1%88%D0%BE%D0%BF+%D1%87%D0%B5%D1%80%D0%BD%D1%96%D0%B2%D1%86%D1%96&rflfq=1&num=10&rldimm=4633021535535150528#rlfi=hd:;si:2413904827129001093;mv:[[48.2953335133018,25.944749340319813],[48.27351573731087,25.91788433482665],null,[48.2844257902604,25.93131683757323],15]"),
        types.InlineKeyboardButton(text="Дещо пікантне", url="https://www.google.com/search?tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=APq-WBsJfm4Mm6ggZnWvfzIiKKaXEcF1hA:1649027158511&q=%D1%81%D0%B5%D0%BA%D1%81+%D1%88%D0%BE%D0%BF+%D1%87%D0%B5%D1%80%D0%BD%D1%96%D0%B2%D1%86%D1%96&rflfq=1&num=10&rldimm=4633021535535150528#rlfi=hd:;si:17925138949679402122;mv:[[48.296628899999995,25.937395100000003],[48.267477899999996,25.9233503]]")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Обирай не пожалкуєш !", reply_markup=keyboard)

# feature save

@dp.message_handler(commands=['hide'])
async def cmd_save_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Бомбосховища", url="https://www.google.com/maps/d/u/0/viewer?mid=1oYvZrZg3VwPbRWtabOPfaMyI6Bk&ll=48.275937266096186%2C25.941081630455553&z=13"),
        types.InlineKeyboardButton(text="Повітряна тривога", url="https://war.ukrzen.in.ua/alerts/#")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Швидко в укриття !!", reply_markup=keyboard)

# Bot Communication

@dp.message_handler()
async def echo_and_request(message: types.Message):
    if message.text=="Слава Україні":
       await message.answer("Героям Слава")
    elif message.text=="Путін":
       await message.answer("Хуйло погане")
    elif message.text=="Росія":
       await message.answer("Країна агресор")
    elif message.text=="Україна":
       await message.answer("Понад усе!")
    elif message.text=="Украина":
       await message.answer("Понад усе!")
    elif message.text=="Кот":
       await message.answer("Пушыстый пидар!")
    elif message.text=="Серега":
       await message.answer("Гей")
    elif message.text=="Хто твій батько":
       await message.answer("Батько мій Бандера! Україна Мати!")
    elif message.text=="Сергій":
       await message.answer("Гей")
    elif message.text=="Сережа":
       await message.answer("Гей")
    elif message.text=="Что делать":
       await message.answer("Введи слово /")
    elif message.text=="что делать":
       await message.answer("Введи слово /")
    elif message.text=="Привет":
       await message.answer("Введи слово /")
    else:
        await message.answer("Впишіть /")

# Polling Telegram servers
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

