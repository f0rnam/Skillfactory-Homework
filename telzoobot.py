import telebot
from telebot import types

# Your bot's token
API_TOKEN = '8022466350:AAFLDBUIMDRydgS7WO2GV-fT5r40kBxkuYs'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Define the animals and their descriptions
animals = {
    "Енот-полоскун 🦝": {
        "description": "Вы любите исследовать мир и находить необычные решения.",
        "image_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRcUIZpCqkuD6nHC34GFjTcnc2vQ4qVReakcKpdCFkTuqqohZU8pI3BtOIjWmNHikwCjPamRHJcBzsKbIb7XidNtg"
    },
    "Амурский тигр 🐯": {
        "description": "Вы сильный и грациозный человек, символ храбрости.",
        "image_url": "https://www.zoo-penza.ru/upload/iblock/178/1780045c0b972cef442bcfd5d1eb56be.jpg"
    },
    "Медведь белый 🐻‍❄️": {
        "description": "Мощный, уравновешенный, воплощение силы и выносливости.",
        "image_url": "https://www.ttelegraf.ru/wp-content/uploads/2021/10/0d027787-74c5-4303-ae3d-de77443084dd-gettyimages-184113999.jpg"
    },
    "Сурикат 🦦": {
        "description": "Вы отличный командный игрок и общительный.",
        "image_url": "https://www.pittsburghzoo.org/wp-content/uploads/2024/03/Mearkat_bubble2.webp"
    },
    "Лемур катта 🐾": {
        "description": "Вы активный и семейный человек, любите веселье.",
        "image_url": "https://mountpanther.com/wp-content/uploads/2022/07/lemur1.jpg.webp"
    },
    "Фенек 🦊": {
        "description": "Вы быстрый и адаптивный, полны энергии.",
        "image_url": "https://otmetka.tv/wp-content/uploads/2018/11/iDXrB6etzNY-848x477.jpg"
    },
    "Капибара 🦫": {
        "description": "Вы спокойный и дружелюбный, любите воду.",
        "image_url": "https://womenofrussia.online/upload/iblock/363/96vakce82nnh6rrz80803wx93lzsjaee.jpg"
    },
    "Фламинго красный 🦩": {
        "description": "Вы элегантны и утончены, символ страсти.",
        "image_url": "https://animalfactguide.com/wp-content/uploads/2023/12/american-flamingo-1-725x575.jpg"                 
    },
    "Сова белая 🦉": {
        "description": "Вы мудрый и спокойный, любите ночное время.",
        "image_url": "https://yasavey.ru/wp-content/uploads/2020/06/Polyarnaya-sova.jpg"
    },
    "Тукан 🦜": {
        "description": "Вы яркий и харизматичный, любите общение.",
        "image_url": "https://www.tierchenwelt.de/images/stories/fotos/voegel/spechte/tukan/tukan_riesentukan_steckbrief_l.jpg"
    },
    "Каймановая черепаха 🐢": {
        "description": "Вы сильны и выносливы, настоящий охранник.",
        "image_url": "https://fanfishka.ru/uploads/posts/2018-03/thumbs/1521043242_foto1.jpg"
    },
    "Игуана зелёная 🦎": {
        "description": "Вы экзотичны, расслаблены и солнечны.",
        "image_url": "https://cdn.botanichka.ru/wp-content/uploads/2021/06/zelenaya-iguana-kak-soderzhat-domashnego-drakonchika-01.jpg"
    },
    "Выдра обыкновенная 🦦": {
        "description": "Вы энергичны и весёлы, любите воду.",
        "image_url": "https://paksitanosvenyek.hu/wp-content/uploads/2023/01/vidra.jpg.webp"
    },
    "Морской котик 🦭": {
        "description": "Вы игривы, общительны и с сильным характером.",
        "image_url": "https://anapa.media/wp-content/uploads/2018/05/k2_items_cache_8190821423b6ae5349e76b06feb28cec_XL.jpg"
        }
}

# Define the questions, answers, and their scoring for each animal
questions = [
    {
        "question": "Где вы чувствуете себя наиболее комфортно?",
        "answers": {
            "🌲 В лесу": {"Енот-полоскун 🦝": 2, "Амурский тигр 🐯": 1, "Медведь белый 🐻‍❄️": 3, "Сурикат 🦦": 1},
            "🏜 В пустыне": {"Фенек 🦊": 3, "Каймановая черепаха 🐢": 1, "Игуана зелёная 🦎": 2, "Амурский тигр 🐯": 2},
            "🌊 У воды": {"Капибара 🦫": 3, "Выдра обыкновенная 🦦": 2, "Морской котик 🦭": 3},
            "🏞 В горах": {"Сова белая 🦉": 2, "Амурский тигр 🐯": 3, "Медведь белый 🐻‍❄️": 2}
        }
    },
    {
        "question": "Как вы предпочитаете проводить свободное время?",
        "answers": {
            "🛋 Лениво отдыхая": {"Игуана зелёная 🦎": 3, "Капибара 🦫": 2, "Сова белая 🦉": 1},
            "🏃‍♂️ Активно исследуя новые места": {"Енот-полоскун 🦝": 3, "Сурикат 🦦": 2, "Фенек 🦊": 3},
            "📚 Занимаясь интеллектуальными делами": {"Сова белая 🦉": 3, "Тукан 🦜": 2, "Лемур катта 🐾": 1},
            "👫 В кругу друзей и семьи": {"Лемур катта 🐾": 3, "Капибара 🦫": 2, "Морской котик 🦭": 1}
        }
    },
    {
        "question": "Какая еда вам нравится больше всего?",
        "answers": {
            "🍎 Фрукты и овощи": {"Енот-полоскун 🦝": 2, "Лемур катта 🐾": 3, "Тукан 🦜": 2},
            "🍖 Мясо": {"Амурский тигр 🐯": 3, "Медведь белый 🐻‍❄️": 2, "Каймановая черепаха 🐢": 1},
            "🌾 Зерновые и орехи": {"Капибара 🦫": 3, "Сурикат 🦦": 2, "Фенек 🦊": 1},
            "🍳 Что-то необычное и редкое": {"Игуана зелёная 🦎": 3, "Фламинго красный 🦩": 2, "Выдра обыкновенная 🦦": 1}
        }
    },
    {
        "question": "Какой ваш главный талант?",
        "answers": {
            "🦸‍♂️ Быть сильным и защищать": {"Амурский тигр 🐯": 3, "Медведь белый 🐻‍❄️": 3, "Каймановая черепаха 🐢": 2},
            "🎨 Быть креативным": {"Фламинго красный 🦩": 3, "Тукан 🦜": 2, "Игуана зелёная 🦎": 1},
            "🤝 Уметь ладить с другими": {"Капибара 🦫": 3, "Сурикат 🦦": 3, "Морской котик 🦭": 2},
            "🧗 Быть упорным": {"Сова белая 🦉": 2, "Амурский тигр 🐯": 3, "Енот-полоскун 🦝": 1}
        }
    }
]

# Store user data
user_results = {}

# Start command
@bot.message_handler(commands=["start"])
def start(message):
    user_results[message.chat.id] = {"scores": {animal: 0 for animal in animals}, "current_question": 0}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Начать викторину")
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! 🐾 Я помогу узнать, какое животное из зоопарка станет вашим тотемом. ", reply_markup=markup)

# Handle quiz start
@bot.message_handler(func=lambda message: message.text == "Начать викторину")
def start_quiz(message):
    ask_question(message.chat.id)

# Ask a question
def ask_question(user_id):
    current_question = user_results[user_id]["current_question"]
    question_data = questions[current_question]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for answer in question_data["answers"].keys():
        markup.add(types.KeyboardButton(answer))
    bot.send_message(user_id, question_data["question"], reply_markup=markup)

# Handle the "Попробовать снова" button
@bot.message_handler(func=lambda message: message.text == "Попробовать снова")
def restart_quiz(message):
    user_id = message.chat.id
    # Reset the user's progress
    user_results[user_id] = {"scores": {animal: 0 for animal in animals}, "current_question": 0}
    bot.send_message(user_id, "Начинаем заново!")
    ask_question(user_id)

@bot.message_handler(func=lambda message: message.text == "Узнать больше о программе опеки")
def guardianship_info(message):
    bot.send_message(
        message.chat.id,
        "Программа опеки Московского зоопарка позволяет вам поддерживать выбранное животное, обеспечивая его питанием и уходом. Подробнее вы можете узнать на сайте: [Программа опеки](https://moscowzoo.ru/about/guardianship)\nИли свяжитесь с нами для консультации!\n+7-499-252-29-51",
        parse_mode="Markdown",
    )


# Handle user answers
@bot.message_handler(func=lambda message: message.chat.id in user_results)
def handle_answer(message):
    user_id = message.chat.id
    current_question = user_results[user_id]["current_question"]
    
    # Check if the user is within the range of questions
    if current_question < len(questions):
        question_data = questions[current_question]
        if message.text in question_data["answers"]:
            # Update scores
            for animal, points in question_data["answers"][message.text].items():
                user_results[user_id]["scores"][animal] += points

            # Move to the next question or finish
            user_results[user_id]["current_question"] += 1
            if user_results[user_id]["current_question"] < len(questions):
                ask_question(user_id)
            else:
                # Calculate the result
                scores = user_results[user_id]["scores"]
                top_animal = max(scores, key=scores.get)
                animal_data = animals[top_animal]
                
                # Send result photo and description
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                restart_button = types.KeyboardButton("Попробовать снова")
                info_button = types.KeyboardButton("Узнать больше о программе опеки")
                markup.add(restart_button, info_button)
                
                bot.send_photo(
                    user_id,
                    photo=animal_data["image_url"],
                    caption=f"Ваш тотем – {top_animal}! {animal_data['description']}",
                    reply_markup=markup
                )
        else:
            bot.send_message(user_id, "Пожалуйста, выберите один из предложенных вариантов.")
    else:
        bot.send_message(user_id, "Пожалуйста, начните заново, нажав 'Попробовать снова'.")

# Run the bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
