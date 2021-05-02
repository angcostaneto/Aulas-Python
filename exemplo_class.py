class matematica:

    def __init__(self, nome):
        self.__nome = nome

    # Isto é um get safado
    @property
    def nome(self):
        return self.__nome

    # Isto é set safado
    @nome.setter
    def nome(self, value):
        self.__nome = value


