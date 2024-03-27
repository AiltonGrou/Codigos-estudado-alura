
class Cliente:

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        print("Chamando o @property")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando o Setter")
        self.__nome = nome