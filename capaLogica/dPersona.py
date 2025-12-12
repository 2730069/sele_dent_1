from capaDatos.dPersona import DPersona

class LPersona:
    def __init__(self):
        self.__dPersona = DPersona()

    def insertarPersona(self, persona):
        return self.__dPersona.insertarPersona(persona)

    def mostrarPersona(self):
        return self.__dPersona.mostrarPersona()
