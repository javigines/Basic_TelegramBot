#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Se utiliza la librería de telegram
# https://github.com/python-telegram-bot/python-telegram-bot
# Para instalar: pip install python-telegram-bot
# La API
# https://python-telegram-bot.readthedocs.io/en/stable/

# Incluir librerias necesarias (Es como el #define en C)
from telegram.ext import Updater, CommandHandler

# Definición de función en python, los parámetros son necesarios para ciertas funciones mas abajo explico cuales


def holaMundo(bot, update):
    # Simplemente se obtiene chat_id de una conversación (Es el identificador de la conversación entre tu y el bot)
    chat_id = update.message.chat.id
    # Función de envio de mensajes, estos son los parametros esenciales que hay que introducir
    bot.sendMessage(chat_id=chat_id, text="Hola Mundo")


# Esto es una lectura del token desde un archivo que esta en la misma carpeta del script
# with open("token.txt", 'r') as tokenFile:
#	token = tokenFile.read().splitlines()[0]


# En lugar de colocar el token en un archivo aparte podemos ponerlo directamente en el código el token pero cuidado con subirlo a github o cosas asi porque es la forma de controlar nuestro bot.
# Comentar linea siguiente y descomentar las 2 de arriba si se quiere usar así
token = "1234567890:abcdefghijklmnopqrstuvwxyz"

# Inicializamos vfunciones de nuestra libreria.
# Aquí estamos introduciendo nuestro token y el número de hilos (que son algo asi como peticiones a la vez) que aceptamos.
updater = Updater(token, workers=200)
# Estamos guardando el objeto que nos da updater.dispatcher en una variabel más fácil
dispatcher = updater.dispatcher

# Definición del comando al que queremos que el bot responda. Le estamos diciendo que responda al /start y que ejecute la función holaMundo que hemos definido arriba.
# Lo que os comentaba arriba es que es necesarío incluir los parametros de bot y update en todas las funciones que son llamadas desde aquí, como nuestra función holaMundo
start_handler = CommandHandler('start', holaMundo)
# Añadimos nuestro objeto comando (lo de arriba) a los comandos que ejecuta el bot.
dispatcher.add_handler(start_handler)

# En esta línea es realmente donde damos comienzo a nuestro bot.A partir de aquí nuestro bot ya puede emepzar a recibir todos los comandos definidos arriba
updater.start_polling(timeout=1)
# Esto es un print una cosa muy compleja en python y que tarddaría horas en explicar :D
print("MainBot Completly Loaded.\nBot Working...")

# Ejecutamos un bucle infinito para que nuestro bot este corriendo hasta que los servidores dcde coredumped decidan apagarlos, es decir, el bot te aguantará vivo un par de minutos
updater.idle()


# Otros bots de ejemplo

# Bot de los eventos Coredumped:
# https://github.com/javigines/EventsBot-CoreDumped
# Bot random utilities:
# https://github.com/javigines/Random-TelegramBot

# Bots de @javinator_9889
# Youtube: https://github.com/Javinator9889/telegram-yt_mp3-bot
# Noticias: https://github.com/Javinator9889/NewsBot
