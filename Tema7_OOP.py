# Exercitiul 1

from abc import ABC, abstractmethod
PI=3.14
class FormaGeometrica(ABC):


    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print(f'Cel mai probabil am colturi.')

    def descrie_nou(self):
        print(f'Eu nu am colturi.')

class Patrat(FormaGeometrica):


    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    def aria(self):
        print(f'Aria patratului este {self.__latura **2}')

    @latura.getter
    def latura(self):
        print(f'Getter: latura este: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: noua latura este: {latura}')
        self.__latura = latura

    @latura.deleter
    def sterge(self):
        print('Sterge latura!')
        self.__latura = None

    def descrie(self):
        print(f'Cel mai probabil am colturi.')

    def descrie_nou(self):
        print(f'Eu am colturi.')

class Cerc(FormaGeometrica):


    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        self.aria = PI * self.__raza ** 2
        print(f'Aria cercului este: {self.aria}')

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: raza este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: noua raza este: {raza}')
        self.__raza = raza

    @raza.deleter
    def sterge(self):
        print('Sterge raza!')
        self.__raza = None

    def descrie(self):
        print(f'Cel mai probabil nu am colturi.')

    def descrie_nou(self):
        print(f'Eu nu am colturi.')


p = Patrat(10)
p.aria()
p.descrie()
p.descrie_nou() #polimorfism
p.latura = '8'
p.latura
# del p.latura
# p.latura

print(" ")
c = Cerc(5)
c.aria()
c.descrie()
c.descrie_nou() #polimorfism
c.raza = '3'
c.raza
# del c.raza
# c.raza



