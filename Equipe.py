from Aluno import aluno

class equipe:
    def __init__(self,projeto):
        self.projeto = projeto
        self.lista = []

    def getProjeto(self):
        return self.projeto

    def outroProjeto (self):
        return  self.projeto

    def cadastrar_Aluno (self,nome,cpf):
        a = aluno(nome,cpf)
        self.lista.append(a)

    def imprimir(self):
        for i in range(len(self.lista)):
            print "Aluno: %s Cpf: %i" % (self.lista[i].getNome(),self.lista[i].getCpf())

    def remover(self,cpf):
        al = self.procura(cpf)
        if al == None:
            return
        else:
            self.lista.remove(al)
    def procura(self,cpf):
        for i in range(len(self.lista)):
            if self.lista[i].getCpf() == cpf:
                return self.lista[i]
        return None



equi = equipe('DLEI')
while True:
    print "\n = = = = Bemvindo(a)= = = = \n"
    print "Digite a opcao desejada:\n"
    print "Cadastrar um Aluno: 1"
    print  "Mostrar os alunos: 2"
    print "Remover um aluno: 3"
    print "Sair: 4\n"
    try:
        opcao = int(raw_input("Opcao: "))
    except:
        print 'Valor invalido, tente novamente'
        continue

    if opcao == 1:
        while True:
            print "\n = = = = Cadastrao de alunos = = = = \n"
            nome = raw_input("Digite o nome do aluno: ")
            cpf = int(raw_input("Digite o cpf: "))

            equi.cadastrar_Aluno(nome,cpf)

            novo_cadastro = raw_input("Deseja cadastrar outro aluno? sim/nao ")
            if novo_cadastro.upper() == "SIM":
                continue
            elif novo_cadastro.upper() == "NAO":
                break
    elif opcao == 2:
            print "\n= = = = Mastrar alunos = = = = \n"
            equi.imprimir()
    elif opcao == 3:
        print "\n= = = = Remover aluno = = = = \n"
        remove = int(raw_input("Informe o CPF do aluno que se deseja remover: "))
        equi.remover(remove)
    elif opcao == 4:
        break

