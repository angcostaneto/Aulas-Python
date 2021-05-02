from abc import abstractmethod, ABC


class InterfaceAnimal:
    @abstractmethod
    def raca(self) -> str: raise NotImplementedError

    @abstractmethod
    def nome(self) -> str: raise NotImplementedError

    @abstractmethod
    def tipo(self) -> str: raise NotImplementedError


class Animal(InterfaceAnimal):
    def __init__(self, raca: str, nome: str, tipo: str):
        self.raca = raca
        self.nome = nome
        self.tipo = tipo

    def raca(self) -> str:
        return self.raca

    def nome(self) -> str:
        return self.nome

    def tipo(self) -> str:
        return self.tipo

    @abstractmethod
    def mia(self) -> str: raise NotImplementedError

    @abstractmethod
    def latir(self) -> str: raise NotImplementedError


class Dog(Animal):

    def mia(self) -> str:
        return 'nao'

    def latir(self) -> str:
        return 'late'


class Cat(Animal):

    def mia(self) -> str:
        return 'miau'

    def latir(self) -> str:
        return 'nao'


class Veterinario:

    def __init__(self, animal: InterfaceAnimal):
        self.animal = animal

    def pacienteAnimal(self):
        return self.animal


dog = Dog("labrador", "putlo", "cachorro sarnento")
cat = Cat("persa", "garfield", "pulguento")

vetenario1 = Veterinario(dog)
vetenario2 = Veterinario(cat)
