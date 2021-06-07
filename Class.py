class Usuario:
    def __init__(self, nome, email, telefone,  rgcpf) : #cadastrado
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__rgcpf = rgcpf
        #self.__email = email
        #self.__cadastrado = cadastrado

    def cadastrada(self):
        self.__cadastrado = True
        print(" Os usuarios foram cadastrado com sucesso")

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


if __name__ == "__main__":
    usuario1 = Usuario("WEBSE", "M", "123456", True)
    usuario1.cadastrada()
    usuario1.cadastrado = True
    print(usuario1.cadastrado)

    # Utilizando geters e setters
    usuario1.set_nome("JONAS,PEDRO E WEBSE")
    print(usuario1.get_nome())
