class Pessoa:
    def __init__(self, nome, email, senha, contato, endereco, cpf, genero):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.contato = contato
        self.endereco = endereco
        self.cpf = cpf
        self.genero = genero

    @property
    def get_nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
             self._nome

    @property
    def get_email(self,email):
        return self._email
    @email.setter
    def set_email(self, email):
        self._email = email

    @property
    def get_senha(self):
       self.get_senha
    @senha
    def set_senha(self, senha):
        self._senha = senha
    @property
    def get_contato(self):
        self.get_contato
    @contato
    def set_contato(self, contato):
        self._contato = contato

    @property
    def get_(self):
        self._nome
    @nome.setter
    def nome(self, nome):
             self._nome


    def Falar (self):
        print("bla bla bla")

    def Ouvir (self):
        print("ouvindo")

    def Andar (self):
        print("andando")

    def Informacoes (self):
        print("Nome: {}".format(self.nome))
        print("Email: {}".format(self.email))
        print("Senha: ******** ".format(self.senha))
        print("Contato: {}".format(self.contato))


p1 = Pessoa("Rodrigo", "rodrigo1@email.com", "123456R", "(87) 98826-1364")
p1.Falar()
p1.Ouvir()
p1.Andar()
p1.Informacoes()