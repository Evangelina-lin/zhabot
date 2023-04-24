import logging
import random
from random import choice
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram.ext import CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
test = [['Итак, первый квапросик. Какое квачество в человеке в цените больше всего?', ['открытость', 'честность',
                                                                                       'дружелюбие', 'верность',
                                                                                       'целеустремленность'], 'https://mobimg.b-cdn.net/v3/fetch/a8/a8f7919d08aaf2dd6b4b39ccb06f6a09.jpeg'],
        ['Кваш любимый цвет?', ['красный', 'синий',
                                'желтый', 'другой цвет',
                                'цвет влюбленной жабы'], 'https://agro-market24.ru/upload/medialibrary/f57/f572853962ba361a60429dd05f2f3da4.jpg'],
        ['Как квастроение?', ['эм жив(а) вроде', 'я умер прости',
                              'депрессия грустной жабки', 'у меня все супер!',
                              '...no comments...'], 'https://i.pinimg.com/originals/b0/cf/db/b0cfdb305215afe5db1d7ba184ddd87e.jpg'],
        ['Твое жабье хобби?', ['Моргать в стену', 'Проницать жабьим взглядм',
                               'Прыгать', 'лежать в сочной травке',
                               'кушац'], 'https://krasivosti.pro/uploads/posts/2022-09/1662736690_5-krasivosti-pro-p-zhaba-milaya-zhivotnie-5.jpg'],
        ['Лягушечки или жабки?', ['никто...', 'мне нравятся другие животные(',
                                  'Люблю лягушек!', 'Люблю жабок!',
                                  'Обожаю обоих!'], 'https://krasivosti.pro/uploads/posts/2021-11/1635911403_42-krasivosti-pro-p-pucheglazaya-lyagushka-zhivotnie-krasivo-f-47.jpg'],
        ['Финальный квапросик! Ква?', ['че?', 'квака',
                                       'КВА', 'ква!',
                                       'квак'], 'https://funart.pro/uploads/posts/2022-08/thumbs/1660166313_65-funart-pro-p-estetik-art-lyagushka-krasivo-70.jpg'],
        ]
ansewrs = {'6 7 8 9': ['Вы depression жабка. Самая не жабка из жабок', 'https://damion.club/uploads/posts/2022-02/1644077380_2-damion-club-p-grustnaya-lyagushka-zhivotnie-2.jpg'],
           '10 11 12 13 14': ['Вы спортик жабка. Перепрыгаете любого', 'https://i.pinimg.com/originals/6f/48/79/6f48790d48c0cff34982a69eac9a9de4.jpg'],
           '20 21 22 23 24': ['Вы самая милая жабка КВААААК', 'https://sun9-17.userapi.com/impg/haAr85GBtgvXFvF8ru7JfHWnXKUs4Oszrgrfyw/FuvNohe-WfA.jpg?size=888x1280&quality=95&sign=bd746e2270812ef5bf74fab92de44876&c_uniq_tag=Nu31y94SldBA9puVmRi11FBjGkY_LydmT1rehnxiQl0&type=album'],
           '15 16 17 18 19': ['Вы жабка ориджинал. Просто жабка', 'https://kartinkin.net/uploads/posts/2022-12/1670436009_54-kartinkin-net-p-milie-kartinki-zhabok-vkontakte-57.jpg'],
           '25 26 27 28 29 30': ['Вы ХЛЕЕЕЕЕЕБНАЯ ЖАААБААА Квак!!!!', 'https://sun9-52.userapi.com/c856228/u362041773/d4/-3/z_9bf2097731.jpg']}


async def echo(update, context):
    await context.bot.sendPhoto(chat_id=update.message.chat.id, photo="http://risovach.ru/upload/2014/07/mem/merzkaya"
                                                                      "-zhaba_57183350_orig_.jpg",
                                caption='Я понимаю только на жабьем квак')


def frog():
    ra = str(random.randint(1, 54))
    if len(ra) == 1:
        ra = '0' + ra
    url = 'http://www.allaboutfrogs.org/funstuff/random/00'
    url += ra + '.jpg'
    r = requests.get(url)
    url = r.url
    return url


async def start(update, context):
    await update.message.reply_text('Квак!!!! Привекккква, чтобы смотреть жабок квакни на /frog, а если хочешь '
                                    'узнать, какая ты жаба, наквакай на /test')


async def zhabka(update, context):
    a = ['жабка', 'это жаба', "точно жаба", "лучшая жаба", "жабочка", "квак", "квааааааа",
         "квакушечка", "агрессивное ква", "КВАААААААК"]
    keyboard = [
        [
            InlineKeyboardButton(f'ква', callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.sendPhoto(chat_id=update.message.chat.id, photo=frog(),
                                caption=choice(a), reply_markup=reply_markup)


async def testik(update, context):
    await context.bot.sendPhoto(chat_id=update.message.chat.id, photo="https://krasivosti.pro/uploads/posts/2021-09"
                                                                      "/1631129806_7-krasivosti-pro-p-milaya"
                                                                      "-malenkaya-zhaba-zhivotnie-krasivo-f-7.jpg",
                                caption='КВА! ВЫ начали жабий тестик! Хорошего прокваждения)')
    context.user_data['test'] = test
    context.user_data['counter'] = 0
    keyboard = []
    for i in context.user_data['test'][0][1]:
        keyboard.append([InlineKeyboardButton(i, callback_data=i)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.sendPhoto(chat_id=update.message.chat.id, photo=context.user_data['test'][0][2],
                                caption=context.user_data['test'][0][0], reply_markup=reply_markup)


async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == '2':
        a = ['жабка', 'это жаба', "точно жаба", "лучшая жаба", "жабочка", "квак", "квааааааа",
             "квакушечка", "агрессивное ква", "КВАААААААК"]
        keyboard = [
            [
                InlineKeyboardButton(f'ква', callback_data='2')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.sendPhoto(chat_id=query.message.chat.id, photo=frog(),
                                    caption=choice(a), reply_markup=reply_markup)
    else:
        if len(context.user_data['test']) > 1:
            context.user_data['counter'] += context.user_data['test'][0][1].index(query.data) + 1
            context.user_data['test'] = context.user_data['test'][1:]
            keyboard = []
            for i in context.user_data['test'][0][1]:
                keyboard.append([InlineKeyboardButton(i, callback_data=i)])
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.sendPhoto(chat_id=query.message.chat.id, photo=context.user_data['test'][0][2],
                                        caption=context.user_data['test'][0][0], reply_markup=reply_markup)
        else:
            for i in ansewrs.keys():
                if str(context.user_data['counter']) in i.split(' '):
                    await context.bot.sendPhoto(chat_id=query.message.chat.id, photo=ansewrs[i][1],
                                                caption=ansewrs[i][0])
            await context.bot.sendPhoto(chat_id=query.message.chat.id,
                                        photo="https://shutniks.com/wp-content/uploads/2020/05"
                                              "/smeshnaya_zhaba_10_06073854.jpg",
                                        caption='КВА! Спасибо за тестик)')
            await query.message.reply_text('Квак!!!! Чтобы смотреть жабок квакни на /frog, а если хочешь '
                                            'узнать, какая ты жаба, наквакай на /test')


def main():
    application = Application.builder().token('6180239111:AAG6dVTh0JRy4UZA0Y9fm128YsFas3F2R_o').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(catalog))
    application.add_handler(CommandHandler("frog", zhabka))
    application.add_handler(CommandHandler("test", testik))
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()