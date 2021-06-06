#as subclasses aluno, professor e administrador herdaram todos os atributos e metodos da superclasse usuário
class Usuario:
    def __init__(self, nome, email, telefone,  rgcpf, genero, usuario, senha) : #cadastrado
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__rgcpf = rgcpf
        self.__genero = genero
        self.__usuario = usuario
        self.__senha = senha
class aluno (Usuario):
    def __init__(self,nome, email, telefone,  rgcpf, genero, usuario, senha, status, matricula, notas) :
        aluno.__init__(self, nome, email, telefone,  rgcpf, genero, usuario, senha)#método __init__ da superclasse, para ela iniciar os parâmetros
        self.__status = status#self.status = pois esse atributo é novo, existe somente na classe aluno
        self.__matricula = matricula#self.matricula = pois esse atributo é novo, existe somente na classe aluno
        self.__notas = notas#self.notas = pois esse atributo é novo, existe somente na classe aluno
    def exibe(self):
        print(self.nome, self.email, self.telefone, self.rgcpf, self.genero,self.usuario, self.senha,self.status,self.matricula,self.notas)
        areaAluno = aluno(" WEBSE_PEDRO_JONAS", "poo@ufg.edu.br", "62_9999_9999", 3)
        areaAluno.exibe()

class professor (Usuario):
    def __init__(self,nome, email, telefone,  rgcpf, genero, usuario, senha, cursos=None) :
        usuario.__init__(self, nome, email, telefone,  rgcpf, genero, usuario, senha)
        areaProfessor = professor("Professores_WEBSE_PEDRO_JONAS", "poo@ufg.edu.br", "62_9999_9999", 3)
        areaProfessor.exibe()

        if cursos is None:
            self.cursos = []
        else:
            self.cursos = cursos

    def add_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)

    def rem_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)


class administrador (Usuario):
    def __init__(self, nome, email, telefone, rgcpf, genero, usuario, senha):
        usuario.__init__(self, nome, email, telefone, rgcpf, genero, usuario, senha)
        areaAdministrador = administrador("WEBSE_Costa", "ADM.@ufg.edu.br", "62_9999_9999", 3)
        areaAdministrador.exibe()