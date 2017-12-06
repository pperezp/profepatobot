import time

import telegram
from telegram.ext import *

from model.bot.Comandos import Comandos
from model.bd.Data      import Data
from model.bd.Alumno    import Alumno
from model.bd.Mensaje   import Mensaje

class Bot:
    @staticmethod
    def init():
        Bot.data = Data()
        Bot.save = False
        Comandos.init()
        Bot.bot = telegram.Bot(token="406813267:AAEvEQwnHNvwYXNuI0C2v9Ub9n6s7iRx_qA")
        Bot.bot_updater = Updater(Bot.bot.token)
        Bot.dispatcher = Bot.bot_updater.dispatcher

        start_handler = CommandHandler("start", Bot.start)

        listener_handler = MessageHandler(Filters.text, Bot.listener)
        Bot.dispatcher.add_handler(start_handler)
        Bot.dispatcher.add_handler(listener_handler)

        Bot.bot_updater.start_polling()
        print("Bot iniciado!")
        Bot.bot_updater.idle()

    # Método que se llama cuando el usuario pone /start
    @staticmethod
    def start(bot, update, pass_chat_data=True):
        Bot.id = update.message.chat_id
        Bot.enviarMensaje(Comandos.print())



    @staticmethod
    def listener(bot, update):
        try:
            mensaje = update.message.text
            Bot.id = update.message.chat_id
            print("ID: " + str(Bot.id) + " Mensaje:" + mensaje)

            alumno = Bot.data.get_alumno(Bot.id)

            if alumno is None:
                Bot.enviarMensaje("No te conozco. Pero te estoy conociendo.")

                info = bot.getChat(update.message.chat_id)
                print(info['id'])
                print(info['first_name'])
                print(info['last_name'])

                if(info['last_name'] is None):
                    alumno = Alumno(info['id'], info['first_name'])
                else:
                    alumno = Alumno(info['id'], info['first_name'] + " " + info['last_name'])

                Bot.data.crear_alumno(alumno)

                Bot.enviarMensaje("Hola "+alumno.nombre+". En que te puedo ayudar?")
            else:
                Bot.enviarMensaje("Ya te conozco "+alumno.nombre)
                """
                c = Comandos.get(mensaje)

                if c is None:
                    Bot.enviarMensaje("No te entiendo viejo")
                elif c.accion is None:
                    Bot.enviarMensaje(c.mensaje)
                else:
                    c.accion()
                """
            mensaje = Mensaje(alumno.id, mensaje)
            Bot.data.reg_mensaje(mensaje)
        except BaseException as b:
            print(str(b))

    @staticmethod
    def enviarMensaje(mensaje):
        Bot.bot.send_chat_action(
            chat_id=Bot.id,
            action=telegram.ChatAction.TYPING
        )
        Bot.bot.sendMessage(
            chat_id=Bot.id,
            text="[" + time.strftime("%H:%M:%S") + "] " + mensaje
        )