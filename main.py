import sqlite3
import telebot
from telebot import types

info = None
user = None
vac_val = None
name = None
age = None
skills = None
exp = None
phone = None

bot = telebot.TeleBot('token')
bot.set_webhook()

con = sqlite3.connect('DataBase.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (vac_val TEXT, name TEXT, age INT, skills TEXT, exp INT, phone INT, photo BLOB NOT NULL, user_id INT PRIMARY KEY)')
con.commit()
cur.close()
con.close()


@bot.message_handler(commands=['start', 'help'])
def main(message):

    Markup = types.InlineKeyboardMarkup()
    btn_newcv = types.InlineKeyboardButton('Новое резюме', callback_data='NewCV')
    btn_cv = types.InlineKeyboardButton('Моё резюме', callback_data='CV')
    btn_site = types.InlineKeyboardButton('Сайт компании',url='https://yandex.ru/search/?clid=2380813&text=rhenfz+fqqnb+rjvgfybz&l10n=ru&lr=22')
    Markup.row(btn_newcv)
    Markup.row(btn_cv, btn_site)
    bot.send_message(message.chat.id, 'Наша компания ищет программистов на офциальное трудоустройство. Мы разрабатываем ИТ-решения для клиентов, хорошо знающих особенности своего бизнеса. Возможно именно Вы станете частью нашего дружного коллектива!', reply_markup=Markup)

def menu(message):
    Markup = types.InlineKeyboardMarkup()
    btn_newcv = types.InlineKeyboardButton('Новое резюме', callback_data='NewCV')
    btn_cv = types.InlineKeyboardButton('Моё резюме', callback_data='CV')
    btn_site = types.InlineKeyboardButton('Сайт компании',url='https://yandex.ru/search/?clid=2380813&text=rhenfz+fqqnb+rjvgfybz&l10n=ru&lr=22')
    Markup.row(btn_newcv)
    Markup.row(btn_cv, btn_site)
    bot.send_message(message.chat.id, "Данные обновлены!", reply_markup=Markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global vac_val
    global user
    global info
    if callback.data == 'backup':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    if callback.data == 'NewCV':
        Markup = types.InlineKeyboardMarkup()
        btn_vac = types.InlineKeyboardButton('Вакансия', callback_data='vacancy')
        Markup.row(btn_vac)
        btn_back = types.InlineKeyboardButton('Назад', callback_data='backup')
        Markup.row(btn_back)
        bot.send_message(callback.message.chat.id, 'Заполните анкету:', reply_markup=Markup)
    if callback.data == 'vacancy':
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute('DELETE FROM users WHERE user_id = ?', (callback.message.chat.id, ))
        con.commit()
        cur.close()
        con.close()
        Markup = types.InlineKeyboardMarkup()
        btn_business = types.InlineKeyboardButton('Бизнес-аналитик', callback_data='business')
        btn_fullstack = types.InlineKeyboardButton('Fullstack', callback_data='fullstack')
        btn_java = types.InlineKeyboardButton('Java', callback_data='java')
        btn_ios = types.InlineKeyboardButton('iOS', callback_data='ios')
        btn_android = types.InlineKeyboardButton('Android', callback_data='android')
        Markup.row(btn_business)
        Markup.row(btn_fullstack, btn_java)
        Markup.row(btn_ios, btn_android)
        bot.send_message(callback.message.chat.id, 'Выберите вакансию:', reply_markup=Markup)
    if callback.data == 'business':
        vac_val = 'Бизнес-аналитик'
        Markup = types.InlineKeyboardMarkup()
        btn_name = types.InlineKeyboardButton('Продолжить', callback_data='name')
        Markup.row(btn_name)
        bot.send_message(callback.message.chat.id, 'Основные требования: Опыт работы аналитика в IT компании от 2-х лет, знание методологий управления требованиями и владение нотациями BPMN и UML для моделирования бизнес-процессов, навыки проведения презентаций и переговоров с клиентом, умение работать в команде, проявлять гибкость и инициативность.', reply_markup=Markup)
    elif callback.data == 'fullstack':
        vac_val = 'Fullstack'
        Markup = types.InlineKeyboardMarkup()
        btn_name = types.InlineKeyboardButton('Продолжить', callback_data='name')
        Markup.row(btn_name)
        bot.send_message(callback.message.chat.id, 'Основные требования: Есть опыт командной работы в коммерческом проекте на .NET от 2 лет, есть опыт работы с базами данных; хорошо, если он включает PostgreSQL, обязателен опыт разработки на React/Angular/Vue от 1 года, умение работать в команде, проявлять гибкость и инициативность.', reply_markup=Markup)
    elif callback.data == 'java':
        vac_val = 'Java'
        Markup = types.InlineKeyboardMarkup()
        btn_name = types.InlineKeyboardButton('Продолжить', callback_data='name')
        Markup.row(btn_name)
        bot.send_message(callback.message.chat.id, 'Основные требования: Знание бэкэнда Java, Spring, SQL, опыт работы в коммерческих проектах от 2 лет, опыт работы с современными инструментами программирования и совместной работы, знание и умение применять принципы ООП и ООД, опыт работы с системами контроля версий (Git), умение работать в команде, проявлять гибкость и инициативность.', reply_markup=Markup)
    elif callback.data == 'ios':
        vac_val = 'iOS'
        Markup = types.InlineKeyboardMarkup()
        btn_name = types.InlineKeyboardButton('Продолжить', callback_data='name')
        Markup.row(btn_name)
        bot.send_message(callback.message.chat.id, 'Основные требования: Есть опыт командной работы в коммерческом проекте на iOS от года, есть опыт программирования на Swift, Objective-C, знакомство с основными библиотеками iOS (UIKit, SwiftUI, Foundation, Quartz Core, Core Graphics), понимание принципов ООП и паттернов проектирования, умение пользоваться сторонними библиотеками и CocoaPods, уверенное владение Git, умение работать в команде, проявлять гибкость и инициативность.', reply_markup=Markup)
    elif callback.data == 'android':
        vac_val = 'Android'
        Markup = types.InlineKeyboardMarkup()
        btn_name = types.InlineKeyboardButton('Продолжить', callback_data='name')
        Markup.row(btn_name)
        bot.send_message(callback.message.chat.id, 'Основные требования: Есть опыт командной работы в коммерческом проекте на Android от двух лет, есть опыт программирования на Kotlin, Java, знакомство с основными библиотеками, будет плюсом, если есть опыт работы с Flutter, Kotlin Multiplatform, понимание принципов ООП и SOLID, знание принципов построения архитектуры мобильных приложений и основных компонентов Android-приложения, уверенное владение Git, умение работать в команде, проявлять гибкость и инициативность.', reply_markup=Markup)
    if callback.data == 'name':
        bot.send_message(callback.message.chat.id,'Введите ФИО:')
        bot.register_next_step_handler(callback.message, user_name)
    if callback.data == 'CV':
        Markup = types.InlineKeyboardMarkup()
        btn_change = types.InlineKeyboardButton('Изменить', callback_data='change')
        Markup.row(btn_change)
        btn_back = types.InlineKeyboardButton('Назад', callback_data='backup')
        Markup.row(btn_back)
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (callback.message.chat.id, ))
        user = cur.fetchone()
        cur.close()
        con.close()
        if user:
            info = (f'•Вакансия: {user[0]}\n•ФИО: {user[1]}\n•Возраст: {user[2]}\n•Хард скиллы: {user[3]}\n•Опыт работы: {user[4]}\n•Телефон: {user[5]}\n')
            if user[6]:
                bot.send_photo(callback.message.chat.id, user[6], caption=info, reply_markup=Markup)
            else:
                bot.send_message(callback.message.chat.id, info)
        else:
            bot.send_message(callback.message.chat.id, 'Вы еще не добавили своё резюме')
    if callback.data == 'change':
        Markup = types.InlineKeyboardMarkup()
        btn_photo_ch = types.InlineKeyboardButton('Фото', callback_data='photo_ch')
        btn_vac_ch = types.InlineKeyboardButton('Вакансия', callback_data='vac_ch')
        btn_name_ch = types.InlineKeyboardButton('ФИО', callback_data='name_ch')
        btn_age_ch = types.InlineKeyboardButton('Возраст', callback_data='age_ch')
        btn_skills_ch = types.InlineKeyboardButton('Хард скилы', callback_data='skills_ch')
        btn_exp_ch = types.InlineKeyboardButton('Опыт', callback_data='exp_ch')
        btn_phone_ch = types.InlineKeyboardButton('Телефон', callback_data='phone_ch')
        Markup.row(btn_photo_ch)
        Markup.row(btn_vac_ch,btn_name_ch)
        Markup.row(btn_age_ch, btn_skills_ch)
        Markup.row(btn_exp_ch, btn_phone_ch)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        if user:
            info = (f'•Вакансия: {user[0]}\n•ФИО: {user[1]}\n•Возраст: {user[2]}\n•Хард скиллы: {user[3]}\n•Опыт работы: {user[4]}\n•Телефон: {user[5]}\n')
            if user[6]:
                bot.send_photo(callback.message.chat.id, user[6], caption=info, reply_markup=Markup)
            else:
                bot.send_message(callback.message.chat.id, info)
    if callback.data == 'vac_ch':
        Markup = types.InlineKeyboardMarkup()
        btn_business = types.InlineKeyboardButton('Бизнес-аналитик', callback_data='business_ch')
        btn_fullstack = types.InlineKeyboardButton('Fullstack', callback_data='fullstack_ch')
        btn_java = types.InlineKeyboardButton('Java', callback_data='java_ch')
        btn_ios = types.InlineKeyboardButton('iOS', callback_data='ios_ch')
        btn_android = types.InlineKeyboardButton('Android', callback_data='android_ch')
        Markup.row(btn_business)
        Markup.row(btn_fullstack, btn_java)
        Markup.row(btn_ios, btn_android)
        bot.send_message(callback.message.chat.id, 'Выберите вакансию:', reply_markup=Markup)
    if callback.data == 'business_ch':
        vac_val = 'Бизнес-аналитик'
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET vac_val = ? WHERE user_id = ?", (vac_val, callback.message.chat.id))
        con.commit()
        cur.close()
        con.close()
        bot.send_message(callback.message.chat.id, 'Основные требования: Опыт работы аналитика в IT компании от 2-х лет, знание методологий управления требованиями и владение нотациями BPMN и UML для моделирования бизнес-процессов, навыки проведения презентаций и переговоров с клиентом, умение работать в команде, проявлять гибкость и инициативность.')
        menu(callback.message)
    elif callback.data == 'fullstack_ch':
        vac_val = 'Fullstack'
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET vac_val = ? WHERE user_id = ?", (vac_val, callback.message.chat.id))
        con.commit()
        cur.close()
        con.close()
        bot.send_message(callback.message.chat.id, 'Основные требования: Есть опыт командной работы в коммерческом проекте на .NET от 2 лет, есть опыт работы с базами данных; хорошо, если он включает PostgreSQL, обязателен опыт разработки на React/Angular/Vue от 1 года, умение работать в команде, проявлять гибкость и инициативность.')
        menu(callback.message)
    elif callback.data == 'java_ch':
        vac_val = 'Java'
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET vac_val = ? WHERE user_id = ?", (vac_val, callback.message.chat.id))
        con.commit()
        cur.close()
        con.close()
        bot.send_message(callback.message.chat.id, 'Основные требования: Знание бэкэнда Java, Spring, SQL, опыт работы в коммерческих проектах от 2 лет, опыт работы с современными инструментами программирования и совместной работы, знание и умение применять принципы ООП и ООД, опыт работы с системами контроля версий (Git), умение работать в команде, проявлять гибкость и инициативность.')
        menu(callback.message)
    elif callback.data == 'ios_ch':
        vac_val = 'iOS'
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET vac_val = ? WHERE user_id = ?", (vac_val, callback.message.chat.id))
        con.commit()
        cur.close()
        con.close()
        bot.send_message(callback.message.chat.id, 'Основные требования: Есть опыт командной работы в коммерческом проекте на iOS от года, есть опыт программирования на Swift, Objective-C, знакомство с основными библиотеками iOS (UIKit, SwiftUI, Foundation, Quartz Core, Core Graphics), понимание принципов ООП и паттернов проектирования, умение пользоваться сторонними библиотеками и CocoaPods, уверенное владение Git, умение работать в команде, проявлять гибкость и инициативность.')
        menu(callback.message)
    elif callback.data == 'android_ch':
        vac_val = 'Android'
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET vac_val = ? WHERE user_id = ?", (vac_val, callback.message.chat.id))
        con.commit()
        cur.close()
        con.close()
        bot.send_message(callback.message.chat.id,'Основные требования: Есть опыт командной работы в коммерческом проекте на Android от двух лет, есть опыт программирования на Kotlin, Java, знакомство с основными библиотеками, будет плюсом, если есть опыт работы с Flutter, Kotlin Multiplatform, понимание принципов ООП и SOLID, знание принципов построения архитектуры мобильных приложений и основных компонентов Android-приложения, уверенное владение Git, умение работать в команде, проявлять гибкость и инициативность.')
        menu(callback.message)

    if callback.data == 'name_ch':
        bot.send_message(callback.message.chat.id, 'Введите ФИО:')
        bot.register_next_step_handler(callback.message, update_name)

    if callback.data == 'age_ch':
        bot.send_message(callback.message.chat.id, 'Введите свой возраст:')
        bot.register_next_step_handler(callback.message, update_age)

    if callback.data == 'skills_ch':
        bot.send_message(callback.message.chat.id, 'Введите свой хард скилы:')
        bot.register_next_step_handler(callback.message, update_skills)

    if callback.data == 'exp_ch':
        bot.send_message(callback.message.chat.id, 'Введите свой опыт:')
        bot.register_next_step_handler(callback.message, update_exp)

    if callback.data == 'phone_ch':
        bot.send_message(callback.message.chat.id, 'Введите свой телефон:')
        bot.register_next_step_handler(callback.message, update_phone)

    if callback.data == 'photo_ch':
        bot.send_message(callback.message.chat.id, 'Отправьте ваше фото:')
        bot.register_next_step_handler(callback.message, user_photo)

def update_name(message):
    new = message.text.strip()
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET name = ? WHERE user_id = ?", (new, message.chat.id))
    con.commit()
    cur.close()
    con.close()
    menu(message)

def update_age(message):
    new = message.text.strip()
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET age = ? WHERE user_id = ?", (new, message.chat.id))
    con.commit()
    cur.close()
    con.close()
    menu(message)

def update_skills(message):
    new = message.text.strip()
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET skills = ? WHERE user_id = ?", (new, message.chat.id))
    con.commit()
    cur.close()
    con.close()
    menu(message)

def update_exp(message):
    new = message.text.strip()
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET exp = ? WHERE user_id = ?", (new, message.chat.id))
    con.commit()
    cur.close()
    con.close()
    menu(message)

def update_phone(message):
    new = message.text.strip()
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("UPDATE users SET phone = ? WHERE user_id = ?", (new, message.chat.id))
    con.commit()
    cur.close()
    con.close()
    menu(message)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите свой возраст:')
    bot.register_next_step_handler(message, user_age)

def user_age(message):
    global age
    age = message.text.strip()
    bot.send_message(message.chat.id, 'Кратко опишите хард скилы:')
    bot.register_next_step_handler(message, user_skills)

def user_skills(message):
    global skills
    skills = message.text.strip()
    bot.send_message(message.chat.id, 'Введите ваш стаж работы:')
    bot.register_next_step_handler(message, user_exp)

def user_exp(message):
    global exp
    exp = message.text.strip()
    bot.send_message(message.chat.id, 'Введите телефон для связи:')
    bot.register_next_step_handler(message, user_phone)

def user_phone(message):
    global phone
    phone = message.text.strip()
    bot.send_message(message.chat.id, 'Отправьте ваше фото:')
    bot.register_next_step_handler(message, user_photo)


def convert_to_binary_data(file_path):
    with open(file_path, 'rb') as file:
        blob_data = file.read()
    return blob_data

@bot.message_handler(content_types=['photo'])
def user_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = f'photo_{message.chat.id}.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.execute(' UPDATE users SET vac_val = ?, name = ?, age = ?, skills = ?, exp = ?, phone = ?, photo = ? WHERE user_id = ?', (vac_val, name, age, skills, exp, phone, downloaded_file, message.chat.id))
    else:
        cur.execute('INSERT INTO users (vac_val, name, age, skills, exp, phone, photo, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (vac_val, name, age, skills, exp, phone, downloaded_file, message.chat.id))
    con.commit()
    cur.close()
    con.close()

    import os
    os.remove(save_path)

    Markup = types.InlineKeyboardMarkup()
    btn_newcv = types.InlineKeyboardButton('Новое резюме', callback_data='NewCV')
    btn_cv = types.InlineKeyboardButton('Моё резюме', callback_data='CV')
    btn_site = types.InlineKeyboardButton('Сайт компании', url='https://yandex.ru/search/?clid=2380813&text=rhenfz+fqqnb+rjvgfybz&l10n=ru&lr=22')
    Markup.row(btn_newcv)
    Markup.row(btn_cv, btn_site)
    bot.send_message(message.chat.id, 'Спасибо за оформление! Ваше резюме было отправлено на рассмотрение. Также Вы можете в любой момент посмотреть или изменить его.', reply_markup=Markup)

bot.infinity_polling()