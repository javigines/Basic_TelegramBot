#!/usr/bin/env python
# -*- coding: utf-8 -*-

# La librería que usamos para comunicarnos con la API que nos proporciona Telegram es:
# https://github.com/python-telegram-bot/python-telegram-bot
# Para empezar, es necesario tener python y pip.
# Después escribimos en la terminal: pip install python-telegram-bot
# La API donde podremos ver todos los métodos que nos da la librería es:
# https://python-telegram-bot.readthedocs.io/en/stable/

# Incluimos solamente las funciones necesarias de las librerías (Es como el #define en C)
from telegram.ext import Updater, CommandHandler
# Se podría escribir 'import telegram.ext' e importariamos todo la librería directamente.


# Definición de función en python, los parámetros son necesarios para todas las funciones que se ejecuten directamente desde comando de nuestro bot.

def holaMundo(bot, update):
	# Simplemente se obtiene chat_id de una conversación (Es el identificador de la conversación entre tu y el bot).
	chat_id = update.message.chat.id
	# Función de envio de mensajes, estos son los parametros esenciales que hay que introducir para enviarlo.
	bot.sendMessage(chat_id=chat_id, text="Hola Mundo")


# Esto es una lectura del token desde un archivo que esta en la misma carpeta del script.
# with open("token.txt", 'r') as tokenFile:
#	token = tokenFile.read().splitlines()[0]


# En lugar de colocar el token en un archivo, podemos ponerlo directamente en el código.
# Cuidado con subirlo a github o repositorios similares porque es la "llave" de acceso a nuestro bot.
# Comentar linea siguiente y descomentar las 2 de arriba si se quiere usar por archivo.
token = "1234567890:abcdefghijklmnopqrstuvwxyz"

# Inicializamos funciones de nuestra libreria.
# Aquí estamos introduciendo nuestro token y el número de hilos (que van a ser las peticiones simultáneas que aceptamos).
updater = Updater(token, workers=200)
# Estamos guardando el objeto que nos da updater.dispatcher en una variable para acceder más facil.
dispatcher = updater.dispatcher

# Definición del comando al que queremos que el bot responda.
# Le estamos diciendo que responda al /start y que ejecute la función holaMundo que hemos definido arriba.
start_handler = CommandHandler('start', holaMundo)
# Añadimos nuestro objeto comando, que hemos creado arriba, al listado de comandos que ejecuta el bot.
dispatcher.add_handler(start_handler)

# En esta línea es realmente donde damos comienzo a nuestro bot.
# A partir de aquí nuestro bot ya puede empezar a recibir todos los comandos definidos arriba.
updater.start_polling(timeout=1)
# Simplemente hacemos un print para tener una confirmación de que nuestro bot se ha iniciado.
print("Bot Completly Loaded.\nBot Working...")

# Utilizamos esta función que nos da la librería para que nuestro bot siga ejecutandose hasta que decidamos detenerlo.
updater.idle()


# Otros bots de ejemplo:

# Bots Mios (@javigines)
# Bot de los eventos Coredumped (@CoreDumped_EventsBot):
# https://github.com/javigines/EventsBot-CoreDumped
# Bot random utilities (@RandomUtils_bot):
# https://github.com/javigines/Random-TelegramBot

# Bots de @javinator_9889
# Youtube: https://github.com/Javinator9889/telegram-yt_mp3-bot
# Noticias: https://github.com/Javinator9889/NewsBot
