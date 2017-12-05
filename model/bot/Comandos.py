import time

from model.bot.Comando import Comando


class Comandos:
    @staticmethod
    def init():

        Comandos.add(
            Comando(
                "hora",
                "Dice la hora del servidor",
                time.strftime("%H:%M:%S")
            )
        )

        Comandos.add(
            Comando(
                "gracias",
                "Da las gracias!",
                "De nada!"
            )
        )

    @staticmethod
    def add(comando):
        try:
            Comandos.lista.append(comando)
        except:
            # si cae en esta excepcion es porque no esta creada
            Comandos.lista = list()
            Comandos.lista.append(comando)

    @staticmethod
    def get(nombreComando):
        for c in Comandos.lista:
            if(c.nombre in nombreComando.lower()):
                return c

        return None

    @staticmethod
    def print():
        str = "Lista de comandos disponibles\n\n"
        str += "/start - Muestra esta lista de comandos\n"
        for c in Comandos.lista:
            print(c)
            str += c.nombre + " - "+ c.descripcion + "\n"

        return str