import config   
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустити бота"),
        types.BotCommand("help", "Допомога"),
        types.BotCommand("rozklad", "Розклад автобусів")])


@dp.message_handler(commands=['start'], commands_prefix='/')
async def text(message: types.Message):
 await message.reply("Привіт, я бот спеціально створений для цієї групи. Мене написали на PYTHON. Я ще в стані розробки, якщо у вас є ідеї для моєї адаптації, то звертайтесь в особисті повідомлення до 👉 @vladisllav") 

@dp.message_handler(commands=['help'], commands_prefix='/')
async def text(message: types.Message):
    await message.reply("Я можу:\nЗа допомогою команди 'all' можу призвати всіх.\nЗа допомогою команди 'rozklad' скину розклад автобусів на Київ та Бровари. \n Також я можу відповідати на деякі повідомлення (лише на ті в, яких для мене є 'тригер' слово).")
@dp.message_handler(commands=['all'], commands_prefix='/@!')
async def text(message: types.Message):
    await message.answer('ПРИЗИВ! @vladisllav @Sanyarutman @PavlentiK @Ba40kpotik @sxSAKURA @Chilly_Willy01 @qqvinki @ann_adkins <a href="tg://user?id=854314976">Андрій</a> <a href="tg://user?id=545108994">Владосік</a> <a href="tg://user?id=1118223964">Слуц</a> <a href="tg://user?id=419836994">Олександр</a>',parse_mode="HTML")
@dp.message_handler(commands=['rozklad'], commands_prefix='/')
async def text(massage: types.Message):
  photoroz1 = open('pho\kyiv.jpg', 'rb')
  photoroz2 = open('pho\ova.jpg', 'rb')
  await bot.send_photo(massage.chat.id, photoroz1)
  await bot.send_photo(massage.chat.id, photoroz2)
@dp.message_handler()
async def filter_messages(massage: types.Message):


    if "Шо ви?" in massage.text:
        await massage.reply("Не знаю шо вони, але мені заєбато)👍")

#*****************Україна*****************

    if "Слава Україні" in massage.text:
        await massage.reply("Героям слава!🇺🇦")
    if "слава Україні" in massage.text:
        await massage.reply("Героям слава!🇺🇦")
    if "слава" in massage.text:
        await massage.reply("Україні!🇺🇦")
    if "Слава" in massage.text:
        await massage.reply("Україні!🇺🇦")
    if "СЛАВА" in massage.text:
        await massage.reply("Україні!🇺🇦")
    if "слава україні" in massage.text:
        await massage.reply("Героям слава!🇺🇦, але бля слово Україна пишеться з великої!")
    if "Україна" in massage.text:
        await massage.reply("Україна понад усе!")
    if "україна" in massage.text:
        await massage.reply("Україна понад усе!")

#*****************Хуйло*****************
    if "Путін" in massage.text:
        await massage.reply("Путін ХУЙЛО")
    if "путін" in massage.text:
        await massage.reply("путін ХУЙЛО")
    if "путин" in massage.text:
        await massage.reply("путін ХУЙЛО")
    if "Путин" in massage.text:
        await massage.reply("путін ХУЙЛО")

#*****************прЕколи*****************

    if "Кардаун" in massage.text:
        await massage.reply("Нахуй ти чорниш на чорниша?")
    if "кардаун" in massage.text:
        await massage.reply("Нахуй ти чорниш на чорниша?")
    if "Славута"  in massage.text:
        await massage.reply("Еххх, хароша машина була")
    if "cлавута"  in massage.text:
        await massage.reply("Еххх, хароша машина була")

#*****************Де?*****************

    if "Це де?"  in massage.text:
        await massage.reply("👈 ТАМ")
    if "це де?"  in massage.text:
        await massage.reply("👈 ТАМ")
    if "Хутор де?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "ХУТОР ДЕ?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "Дачна де?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "ДАЧНА ДЕ?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "Анішара де?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "АНІШАРА ДЕ?"  in massage.text:
        await massage.reply("ТУТ ❤️")
    if "Паша де?"  in massage.text:
        await massage.reply("Охороняє Надію")
    if "ПАША ДЕ?"  in massage.text:
        await massage.reply("Охороняє Надію")

#*****************раша параша*****************

    if "Росия"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)
    if "Раша"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)
    if "Россия"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1) 
    if "россия"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)
    if "росия"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1) 
    if "раша"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)
    if "росія"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)
    if "Росія"  in massage.text:
        vid1 = open('idi/uus.gif', 'rb')
        await bot.send_animation(massage.chat.id, vid1)  

#*****************Повітряна тривога!*****************

    if "БРОВАРИ! Повітряна тривога!" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)
    if "Бровари! Повітряна тривога!" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)
    if "БРОВАРИ, повітряна тривога!" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)
    if "БРОВАРИ, ТРИВОГА!" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)
    if "Бровари повітряна тривога" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)
    if "КИЇВСЬКА ОБЛАСТЬ – ПОВІТРЯНА ТРИВОГА" in massage.text:
        aud1 = open('aud\pov.ogg', 'rb')
        await bot.send_audio(massage.chat.id, aud1)

#*****************Голосові*****************

    if "Пиздабол" in massage.text:
        pizdabol = open('aud\pizdabol.ogg', 'rb')
        await bot.send_audio(massage.chat.id, pizdabol)


    if "третя передача" in massage.text:
        per3 = open('aud\per3.ogg', 'rb')
        await bot.send_audio(massage.chat.id, per3)

#*****************Фото*****************

    if "Бот усипи мене прошу" in massage.text:
        photo1 = open('pho\gun.webp', 'rb')
        await bot.send_photo(massage.chat.id, photo1, "Останне бажання?")

#*****************хто такій....*****************
     
    if "Бот хто такій Паша?" in massage.text:
        photo2 = open('pho\pav.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo2, "Паша, також відомий, як 'Гектар'.  Майбутній депутат. Любить піво.")
    if "Бот хто такій Андрій?" in massage.text:
        photo3 = open('pho\gnd.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo3, "Андрій-білосніжка, зробить любу машину за бутилку пива.")
    if "Бот хто такій Влад?" in massage.text:
        photo4 = open('pho\lad.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo4, "Владос ака Король, колись був чудовим футболістом, аж покі не переїхав на ХУТОР.")
    if "Бот хто такій Коля?" in massage.text:
        photo5 = open('pho\kol.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo5, "Колян-длінна шпага, працює на НП. Катає на красній шистьрці.")
    if "Бот хто такій Саня?" in massage.text:
        photo6 = open('pho\san.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo6, "Саня, брат Андрія, любить свою машину так само, як і піво, а піво любить піздец, як сильно.")
    if "Бот хто такій Бохан?" in massage.text:
        photo7 = open('pho\oha.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo7, "Бохан, полторашка роста, всегда просить на пиво, одседів на Лукяновке.")
    if "Бот хто такій Левадний?" in massage.text:
        photo8 = open('pho\lev.jpg', 'rb')
        await bot.send_photo(massage.chat.id, photo8, "Левадний, девяточна скотина, пробитий профіль. Мені даже ")



    
    


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)