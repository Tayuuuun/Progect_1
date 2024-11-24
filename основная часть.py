 """
       Обрабатывает запрос на добавление нового блюда.
       Запрашивает у пользователя ввести название нового блюда.
       """

@bot.message_handler(func=lambda message: message.text == 'новенькое блюдо') #
def new_dish(message):
    bot.send_message(message.chat.id, 'Давайте придумаем название будущему шедевру')
    user_states[message.chat.id] = WAITING_FOR_DISH_NAME

"""
    Обрабатывает запрос на получение рецепта.
    Запрашивает у пользователя ввести название блюда, рецепт которого он хочет получить.
    """

#ответ на 2ю кнопку + сохранение состояния
@bot.message_handler(func=lambda message: message.text == 'рецептик')
def get_recipe(message):
    bot.send_message(message.chat.id, 'Введите название этого шедевра')
    user_states[message.chat.id] = WAITING_FOR_RECIPE_NAME


"""
   Обрабатывает введенное название нового блюда.
   Запрашивает у пользователя ввести рецепт для указанного блюда.
   """

#обрабатываем и схораняем название блюда
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == WAITING_FOR_DISH_NAME)
def handle_dish_name(message):
    dish_name = message.text
    bot.send_message(message.chat.id, f"Оо супер, звучит вкусно, теперь напишите рецепт '{dish_name}':")#запрашиваем рецепт
    user_states[message.chat.id] = WAITING_FOR_RECIPE #сохраняем состояние
    dish_recipes[dish_name] = None  #создаем запись для блюда

    """
        Обрабатывает введенный рецепт для блюда.
        Сохраняет рецепт в словаре и подтверждает добавление блюда.
        """

#обрабатываем и сохраняем рецепт
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == WAITING_FOR_RECIPE)
def handle_recipe(message):
    recipe = message.text
    dish_name = [key for key, value in dish_recipes.items() if value is None][0]  #получаем новое блюдо
    dish_recipes[dish_name] = recipe  #сохраняем рецептик
    bot.send_message(message.chat.id, f"Буду ждать, когда вы захотите приготовить '{dish_name}': {recipe}")
    user_states[message.chat.id] = None

"""
   Обрабатывает запрос на получение рецепта по названию блюда.
   Отправляет рецепт пользователю, если блюдо найдено, или уведомляет о его отсутствии.
   """

#обрабатываем запрос на рецепт и проверяем есть ли он в словаре
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == WAITING_FOR_RECIPE_NAME)
def handle_recipe_name(message):
    dish_name = message.text
    if dish_name in dish_recipes:
        recipe = dish_recipes[dish_name]
        bot.send_message(message.chat.id, f"Вот рецепт блюда '{dish_name}' , приятного аппетита🤍: {recipe}")
    else:
        bot.send_message(message.chat.id, f"Блюда '{dish_name}' тут нет(")
    user_states[message.chat.id] = None  #убираем состояния


