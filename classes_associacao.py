class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__descrição = None

    @property
    def nome(self):
        return self.__nome

    @property
    def descrição(self):
        return self.__descrição

    @descrição.setter
    def descrição(self, descrição):
        self.__descrição = descrição


class Curso:
    def __init__(self, ativo):
        self.__ativo = ativo

    @property
    def ativo(self):
        return self.__ativo

    def cursista(self):
        print('Aluno esta matriculado...')

class Turma:
    def cursista(self):
        print('Turma do aluno...')

