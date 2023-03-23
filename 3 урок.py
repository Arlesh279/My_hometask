#Исследуй код!

#Давайте разберемся с базовым ботом!
#1. Создай файл .py и попробуй запустить этот код.
#2. Разберись как он работает!

import discord
import random
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("☭Хорошего пути")
    elif message.content.startswith('!pass'):
        def gen_pass(pass_length):
            elements = "+-/*!&$#?=@<>"
            password = ""

            for i in range(pass_length):
                password += random.choice(elements)

            return password
        await message.channel.send(gen_pass(10))
    elif message.content.startswith("!эмодзи"):
        def gen_emodji():
            emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
            return random.choice(emodji)
        await message.channel.send(gen_emodji())
    elif message.content.startswith("!орел"):
        def flip_coin():
            flip = random.randint(0, 1)
            if flip == 0:
                return "ОРЕЛ"
            else:
                return "РЕШКА"   
        await message.channel.send(flip_coin())

client.run("MTA4NDAwNTE2OTI0ODg2NjMwNA.Gy7-pF.4VNuaK7fz3R5G4j9aewGhGN9-JCXRW64DU3dkQ")
 

#Подсказка-теория!

#Любая библиотека содержит внутри себя классы. Что это такое и зачем они нужны, мы поговорим на других уроках... Но пока нам важно знать:

#Что в библиотеке Discord тоже есть классы. Они позволяют нам взаимодействовать с разными частями Discord, такими как каналы, пользователи, сообщения, эмодзи и тд…

#Вот некоторые из них:

#Client- основной класс, который представляет собой бота.
#Он отвечает за установление соединения с Discord API, обработку входящих сообщений и событий, отправку сообщений и многое другое.

#Message  - класс сообщений в Discord.
#Он содержит информацию о тексте сообщения (команда .content), отправителе (команда .author), канале (команда .channel)и другие.

#User  - класс пользователя Discord.
#Он содержит информацию о пользователе, такую как имя, идентификатор, аватар и другие данные.

#Guild  - класс сервера Discord.
#Он содержит информацию о сервере и его настройках, а также о пользователях и каналах, которые находятся на сервере.

#Channel  - класс канала в Discord.
#Он содержит информацию о канале и его настройках, а также о сообщениях и пользователях, которые находятся в данном канале.