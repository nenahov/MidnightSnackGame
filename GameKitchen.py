import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from colorama import init, Fore

from domain.abstract_game import AbstractGame
from games_impl.kitchen_game import KitchenGame
from my_keys import API_TOKEN

# Авто-восстановление цвета шрифта в выводе на консоль
init(autoreset=True)

dp = Dispatcher()

# словарь для хранения Персонажей (Person) для каждого user_id
user_person_dict = dict()
game: AbstractGame
game = KitchenGame()

ids = [cond.id for cond in game.get_all_conditions()]
if len(game.get_all_conditions()) != len(set(ids)):
    print(Fore.RED + "Есть повторяющиеся id у состояний!")


@dp.message(CommandStart())
async def send_welcome(message):
    chat_id = message.chat.id
    user_person_dict[chat_id] = None

    markup = get_markup(get_person(chat_id))

    await message.answer(text="Ой, я проснулся в своей комнате от жуткого голода. Мне срочно нужно поесть!",
                         reply_markup=markup)


@dp.message(Command(commands=['about', 'help']))
async def send_help(message):
    chat_id = message.chat.id
    removePrevMenu(message)
    person = get_person(chat_id)
    end_text = game.check_game_end(person)
    if end_text is not None and end_text != "":
        await message.answer(text=end_text)
        return
    text = f'{message.chat.first_name}, Вы управляете "{person.name}". Сейчас вы находитесь в локации "{person.location}". Вам нужно "{person.goal}"'
    await message.answer(text=text, reply_markup=get_markup(person))


@dp.callback_query()
async def handle_query(call):
    chat_id = call.message.chat.id
    # Убираем меню
    removePrevMenu(call.message)
    person = get_person(chat_id)
    print(
        f'Получено сообщение от {call.message.chat.first_name} {call.message.chat.last_name}: ' + Fore.LIGHTYELLOW_EX + f'{call.data}')
    condition = game.get_condition_by_id(call.data, person)
    if condition is not None:
        condition.apply_state_condition(person)
        end_text = game.check_game_end(person)
        if end_text is not None and end_text != "":
            await call.message.answer(text=end_text)
            return
        if condition.img is not None:
            photo_file = types.FSInputFile(condition.img)
            await call.message.answer_photo(caption=condition.text, photo=photo_file, reply_markup=get_markup(person))
        else:
            await call.message.answer(text=condition.text, reply_markup=get_markup(person))
        return

    await send_help(call.message)


@dp.message()
async def echo_all(message):
    """
    Обработка текстовых сообщений
    Должна идти после остальных обработчиков
    :param message:
    :return:
    """
    removePrevMenu(message)
    print(f'Получено сообщение от {message.chat.first_name} {message.chat.last_name}: ' + Fore.CYAN + f'{message.text}')
    person = get_person(message.chat.id)
    end_text = game.check_game_end(person)
    if end_text is not None and end_text != "":
        await message.reply(text=end_text)
        return
    await message.reply(text="Ой, как же кушать хочется. Надо что-то придумать!",
                        reply_markup=get_markup(get_person(message.chat.id)))


def get_markup(person):
    buttons = list()
    # В цикле перебрать все game_conditions, которые удовлетворяют условия для персонажа
    sorted_conditions = sorted(game.get_conditions_for_person(person), key=lambda cond: cond.order)

    # Group conditions by their 'order'
    result = {}

    for cond in sorted_conditions:
        if cond.order not in result:
            result[cond.order] = []
        result[cond.order].append(types.InlineKeyboardButton(text=cond.name, callback_data=cond.id))

    markup = types.InlineKeyboardMarkup(inline_keyboard=list(result.values()))
    return markup


def get_person(chat_id):
    person = user_person_dict.get(chat_id)
    if person is None:
        person = game.create_person()
        user_person_dict[chat_id] = person
    return person


def removePrevMenu(message):
    t = 2
    # try:
    #     message.edit_message_reply_markup(message.chat.id, message.message_id - 1)
    # except:
    #     pass
    # try:
    #     message.edit_message_reply_markup(message.chat.id, message.message_id)
    # except:
    #     pass


# Запуск бота
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
