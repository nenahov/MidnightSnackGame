import telebot
from colorama import init, Fore
from telebot import types

from games_impl.kitchen_game import KitchenGame
from my_keys import API_TOKEN

# словарь для хранения Персонажей (Person) для каждого user_id
user_person_dict = dict()
game = KitchenGame()
init(autoreset=True)

bot = telebot.TeleBot(API_TOKEN)

ids = [cond.id for cond in game.get_all_conditions()]
if len(game.get_all_conditions()) != len(set(ids)):
    print(Fore.RED + "Есть повторяющиеся id у состояний!")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_person_dict[chat_id] = None

    markup = get_markup(get_person(chat_id))

    bot.send_message(chat_id, "Ой, я проснулся в своей комнате от жуткого голода. Мне срочно нужно поесть!",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    removePrevMenu(message)
    print(f'Получено сообщение от {message.chat.first_name} {message.chat.last_name}: ' + Fore.CYAN + f'{message.text}')
    bot.reply_to(message, "Ой, как же кушать хочется. Надо что-то придумать!",
                 reply_markup=get_markup(get_person(message.chat.id)))


@bot.message_handler(commands=['about', 'help'])
def send_help(message):
    chat_id = message.chat.id
    removePrevMenu(message)
    person = get_person(chat_id)
    text = f'{message.chat.first_name}, Вы управляете "{person.name}". Сейчас вы находитесь в локации "{person.location}". Вам нужно "{person.goal}"'
    bot.send_message(chat_id, text, reply_markup=get_markup(person))


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    chat_id = call.message.chat.id
    # Убираем меню
    removePrevMenu(call.message)
    person = get_person(chat_id)
    print(
        f'Получено сообщение от {call.message.chat.first_name} {call.message.chat.last_name}: ' + Fore.LIGHTYELLOW_EX + f'{call.data}')
    condition = game.get_condition_by_id(call.data, person)
    if condition is not None:
        condition.apply_state_condition(person)
        bot.send_message(call.message.chat.id, condition.text, reply_markup=get_markup(person))
        return

    send_help(call.message)


def get_markup(person):
    markup = types.InlineKeyboardMarkup()
    # В цикле перебрать все game_conditions, которые удовлетворяют условия для персонажа
    for condition in game.get_conditions_for_person(person):
        # Добавить меню для перехода в это состояние
        button = types.InlineKeyboardButton(condition.name, callback_data=condition.id)
        markup.add(button)
    return markup


def get_person(chat_id):
    person = user_person_dict.get(chat_id)
    if person is None:
        person = game.create_person()
        user_person_dict[chat_id] = person
    return person


def removePrevMenu(message):
    try:
        bot.edit_message_reply_markup(message.chat.id, message.message_id - 1)
    except:
        pass
    try:
        bot.edit_message_reply_markup(message.chat.id, message.message_id)
    except:
        pass


# Запуск бота
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            pass
