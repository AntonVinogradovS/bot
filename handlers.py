from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
# from kb import kb_client
# from database import sqlite_db
# from kb import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlite3 as sq
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


storage = MemoryStorage()

TOKEN = "6580626601:AAGp2kcs2HNyUqWVHB61nh_YzMnuUVxvpZs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    #q5 = State()
    q6 = State()
    q66 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()
    q12 = State()
    


async def start(message:types.Message):
    await bot.send_chat_action(chat_id=message.from_user.id, action=types.ChatActions.UPLOAD_VIDEO)
    with open("v1.mp4", "rb") as video_file:
        await bot.send_video_note(message.from_user.id, video_file)
    greeting = '''
            Привет! ❤️
Меня зовут <U>Ксения Самарина</U>, я — женский трансформационный коуч, и я очень рада, что ты решила мне довериться и пройти эту практику под моим руководством 🫶🏻

<b>Для чего она нужна?</b>

Практика нацелена на то, чтобы ты смогла взглянуть на мир и на себя под другим углом. Ты <b>всего за 2-3 минуты</b> сможешь сделать первый шаг к своей цели, копнуть поглубже и чётко понять, какой у тебя сейчас запрос к самой себе.

Практика будет творческой, но уверена, что любая девушка сможет с ней справиться! 🤞🏼

<b>Важно!</b> Не останавливайся на полпути. Ответь на все вопросы, так, результат будет более ярким и полным!
            '''
    await message.answer(text=greeting, parse_mode=types.ParseMode.HTML)
    await message.answer(text="Ну что, поехали?", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Да! Начинаем!", callback_data="go")).add(InlineKeyboardButton(text="Мне неактуально, спасибо", callback_data="no")))

async def rejection(callback_query:types.CallbackQuery):
    farewellMessage = '''
Очень жаль, что ты не решилась попробовать, но я буду надеяться, что мой блог поможет тебе более глубоко погрузиться в такие темы как проявление своей уникальности и самопознание. Пока ты можешь ознакомиться с моей папкой актуальных “Что такое коучинг”, чтобы понять всю природу этого понятия и чем он может помочь тебе. 

Спасибо, что уделила время!
Твоя Ксюша

'''
    await callback_query.message.answer(text=farewellMessage)

async def next(callback_query:types.CallbackQuery):
    await callback_query.message.answer(text="Если бы вы были цветком, то каким?\n(Вопрос: 1/9)")
    await FSMAdmin.q1.set()

async def cancel_handler(message: types.Message, state: FSMContext):
    # Отменяем текущую машину состояний и возвращаемся в начальное состояние
    await state.finish()
    
    # Отправляем сообщение о том, что операция отменена
    await message.reply("Ответы на вопросы прерваны.")

async def q1(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q1'] = message.text
    await FSMAdmin.next() #Что вам нравится в этом цветке? Опишите несколькими словами или фразами:
    await message.reply(text="Что вам нравится в этом цветке? Опишите несколькими словами или фразами:\n(Вопрос: 2/9)")


async def q2(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q2'] = message.text
    await FSMAdmin.next()
   
    await message.reply(text="Что вам в нем нравится <U>БОЛЬШЕ</U> всего? <b>1 элемент</b>, за который вы уже готовы бесконечно ценить этот цветок?\n(Вопрос: 3/9)", parse_mode=types.ParseMode.HTML)
    
async def q3(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q3'] = message.text
    await FSMAdmin.next()
    await message.reply(text="Попробуйте описать, почему это именно этот элемент?\n(Вопрос: 4/9)")

async def q4(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q4'] = message.text
    await FSMAdmin.next()
    #Тут будет кружок
    await bot.send_chat_action(chat_id=message.from_user.id, action=types.ChatActions.UPLOAD_VIDEO)
    with open("v2.mp4", "rb") as video_file:
        await bot.send_video_note(message.from_user.id, video_file)
    await message.reply(text="Если то, что ценно больше всего, перевести обратно на вас, то как это проявляется в вас?\n(Вопрос: 5/9)")



async def q6(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q6'] = message.text
    await FSMAdmin.next()
    await message.reply(text="Насколько это в вас проявлено сейчас?\n(Вопрос: 6/9)", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="1-10%", callback_data="1-10%")).add(InlineKeyboardButton(text="10-30%", callback_data="10-30%")).add(InlineKeyboardButton(text="30-50%", callback_data="30-50%")).add(InlineKeyboardButton(text="50-70%", callback_data="50-70%")).add(InlineKeyboardButton(text="70-90%", callback_data="70-90%")).add(InlineKeyboardButton(text="90-100%", callback_data="90-100%")))

async def q66(callback_query:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['q66'] = callback_query.data
    await FSMAdmin.next()
    await callback_query.message.reply(text="Хотелось бы усилить это проявление?", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Да", callback_data="Да")).add(InlineKeyboardButton(text="Нет", callback_data="Нет")))

async def q7(callback_query:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['q7'] = callback_query.data
    await FSMAdmin.next()
    await bot.send_chat_action(chat_id=callback_query.from_user.id, action=types.ChatActions.UPLOAD_VIDEO)
    with open("v3.mp4", "rb") as video_file:
        await bot.send_video_note(callback_query.from_user.id, video_file)
    await callback_query.message.answer(text="Что узнали о себе за эти 2-3 минуты?💫\n(Вопрос: 7/9)")


async def q8(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q8'] = message.text
    await FSMAdmin.next()
    #Тут будет кружок
    
    await message.answer(text="Как это знание <b>О СЕБЕ</b> продвигает вас к вашей цели/желанию?\n(Вопрос: 8/9)", parse_mode=types.ParseMode.HTML)


async def q9(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q9'] = message.text
    await FSMAdmin.next()
    
    await message.reply(text="Что готовы с этим <b>СДЕЛАТЬ</b> уже сейчас? Как намерены применить?\n(Вопрос: 9/9)", parse_mode=types.ParseMode.HTML)


# async def q10(message:types.Message, state:FSMContext):
#     async with state.proxy() as data:
#         data['q10'] = message.text
#     await FSMAdmin.next()
#     #Тут будет кружок
#     await message.reply(text="Что готовы с этим СДЕЛАТЬ уже сейчас? Как намерены применить?")

async def q11(callback_query: types.CallbackQuery, state:FSMContext):
    good = 'Оставляй <b>свой ник в instagram</b> в окошке, и я добавлю тебя в "лучшие друзья" в сторис, и именно там буду постить бонусные практики только для тех, кто дошёл до этого этапа вместе со мной💥\n\n❗️ <b>Формат</b>: ссылкой или через @ (например, мой ник: @samarina_ksenya)'
    notGood = 'Очень жаль, что ты не решилась попробовать, но я буду надеяться, что мой блог поможет тебе более глубоко погрузиться в такие темы как проявление своей уникальности и самопознание.\n\nПока ты можешь ознакомиться <b>с моим видео "Что такое коучинг"</b>, чтобы понять всю природу этого понятия и чем он может помочь именно тебе 💌\n\nСпасибо, что уделила время! 💞\nТвоя Ксюша'
    if callback_query.data == "Нет, спасибо":
        await bot.send_message(chat_id=callback_query.from_user.id, text=notGood, parse_mode=types.ParseMode.HTML)
        user = '@' + str(callback_query.from_user.username) + '\n'
        if user == None:
            user = "Пользователь не указал свой ник\n"
        reply = "Пользователь не указал инстаграм"
        contact = f'Контактные данные:\n{user} {reply}\n'
        async with state.proxy() as data:
            data['q11'] = contact
        await state.finish()
        await bot.send_message(chat_id=callback_query.from_user.id, text="Спасибо! До встречи в моём блоге!")
        print(list(data.values()))
        await sql_write(callback_query.from_user.id, list(data.values()))
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text=good,parse_mode=types.ParseMode.HTML)
        await FSMAdmin.next()


async def q12(message: types.Message, state:FSMContext):
    user = '@' + str(message.from_user.username) + '\n'
    if user == None:
        user = "Пользователь не указал свой ник\n"
    reply = message.text
    contact = f'Контактные данные:\n{user} {reply}\n'
    async with state.proxy() as data:
        data['q11'] = contact
        
    
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text="Спасибо! До встречи в моём блоге!")
    print(list(data.values()))
    await sql_write(message.from_user.id, list(data.values()))



async def q10(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['q10'] = message.text
    await FSMAdmin.next()
    #Тут будет кружок
    await bot.send_chat_action(chat_id=message.from_user.id, action=types.ChatActions.UPLOAD_VIDEO)
    with open("v4.mp4", "rb") as video_file:
        await bot.send_video_note(message.from_user.id, video_file)
    final = f'{message.from_user.first_name}, спасибо, что решилась принять участие в моей небольшой авантюре и потратила своё время!❣️\n\nНадеюсь, что ты смогла подчерпнуть для себя что-то новое и посмотрела на себя/ситуацию под другим углом.\n\nПоздравляю! Ты сделала <b>первый шаг</b> <span class="tg-spoiler">(а он всегда самый важный и сложный)</span> к поиску настоящей себя!\n\nА теперь возвращайся 👉🏼 <a href="https://instagram.com/samarina_ksenya?igshid=MzRlODBiNWFlZA=="><b style="color: blue;">ко мне в сторис</b></a> 👈🏼 и смотри профессиональный разбор этой практики'
    await bot.send_message(chat_id=message.from_user.id, text=final, parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id= message.from_user.id, text="Хотела бы ты получать от меня бесплатные экспресс практики раз в 1-2 недели? 😏", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Да, было бы круто!",callback_data="Да, было бы круто!")).add(InlineKeyboardButton(text="Нет, спасибо", callback_data="Нет, спасибо")))
IDADMIN = [293457853, 182390082, 1313463136]
async def admin(message:types.Message):
    if message.from_user.id in IDADMIN:
        await message.answer(text='Вы администратор этого бота', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Посмотреть ответы")))
async def check(message:types.Message):
    if message.from_user.id in IDADMIN:
        res = await sql_read()
        for i in res:
            await message.answer(text=i[1], parse_mode=types.ParseMode.HTML)
def sql_start():
    global base, cur
    base = sq.connect('survey.db')
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute('CREATE TABLE IF NOT EXISTS answers(user TEXT, description TEXT)')
    base.commit()

async def sql_write(us, data):
    values_list = data
    my_string = '\n'.join(values_list)

    # Используем INSERT ON CONFLICT REPLACE для обновления или вставки записи
    cur.execute('INSERT INTO answers (user, description) VALUES (?, ?)', (us, my_string))
    base.commit()


async def sql_read():
    cur.execute('SELECT * FROM answers')
    rows = cur.fetchall()
    return rows



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands = ['start'])
    dp.register_message_handler(cancel_handler, commands = ['cancel'], state="*")
    dp.register_callback_query_handler(rejection, text="no")
    dp.register_callback_query_handler(next, text="go")
    dp.register_message_handler(q1, state=FSMAdmin.q1)
    dp.register_message_handler(q2, state=FSMAdmin.q2)
    dp.register_message_handler(q3, state=FSMAdmin.q3)
    dp.register_message_handler(q4, state=FSMAdmin.q4)
    #dp.register_message_handler(q5, state=FSMAdmin.q5)
    dp.register_message_handler(q6, state=FSMAdmin.q6)
    dp.register_callback_query_handler(q66, state=FSMAdmin.q66)
    dp.register_callback_query_handler(q7, state=FSMAdmin.q7)
    dp.register_message_handler(q8, state=FSMAdmin.q8)
    dp.register_message_handler(q9, state=FSMAdmin.q9)
    dp.register_message_handler(q10, state=FSMAdmin.q10)
    dp.register_callback_query_handler(q11, state=FSMAdmin.q11)
    dp.register_message_handler(q12, state=FSMAdmin.q12)
    dp.register_message_handler(admin, commands = ['admin'])
    dp.register_message_handler(check, text = "Посмотреть ответы")

async def on_startup(_):
    print("Бот вышел на связь")
    sql_start()

register_handlers(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
