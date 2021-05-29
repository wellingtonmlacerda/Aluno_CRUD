import mysql.connector
from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="senha",
  database="escola"
)

connect = mydb.cursor("")

class Aluno:

    def __init__(self, nome, email, cpf):  # Assim, você pode facilmente criar um aluno
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def insert_aluno(self):
        connect.execute("Insert Into escola.alunos (Nome, Email, CPF) Values ('"+ self.nome +"', '"+ self.email +"', '"+ self.cpf +"')")
        mydb.commit()
        print(connect.rowcount, "Salvo com sucesso.")
    
    def select_aluno(id = ""):
        if id == "":
            connect.execute("Select * From escola.alunos")
            result = connect.fetchall()
            for i in result:
                print(i)
        else:
            connect.execute("Select * From escola.alunos Where ID_Aluno = " + id)
            result = connect.fetchall()
            for i in result:
                print(i)

    def update_aluno(self, id):
        command = ("Update escola.alunos Set Nome = '"+ self.nome +"', Email = '"+ self.email +"', CPF = '"+ self.cpf +"' Where ID_Aluno = "+ id)
        connect.execute(command)
        mydb.commit()
        print(connect.rowcount, "Registro alterado com sucesso.")

    def delete_aluno(id):
        connect.execute("Delete From escola.alunos Where ID_Aluno = "+ id)
        mydb.commit()
        print(connect.rowcount, "Registro deletado com sucesso.")

class Interface:

    connect = mydb.cursor("")

    def cadastrar_aluno(self):
        aluno = Aluno(input('Qual é o nome do aluno?\n'), input('Qual é o e-mail desejada?\n'), input('Qual é o CPF desejada?\n'))
        aluno.insert_aluno()

    def listar_alunos(self):
        id = input("Digite o número do aluno ou aperte enter para todos:\n")
        Aluno.select_aluno(id)

    def altera_aluno(self):
        numero_aluno = input('Qual é o número de listagem do aluno?\n')
        aluno = Aluno(input('Alterar nome para: \n'), input('Alterar e-mail para:\n'), input('Alterar CPF para:\n'))
        aluno.update_aluno(numero_aluno)

    def excluir_aluno(self):
        numero_aluno = input("Qual o número do aluno que deseja excluir?\n")
        Aluno.delete_aluno(numero_aluno)
        
    def loop(self):
        while True:
            cmd = input('\n1 - Listar alunos\n2 - Cadastrar aluno\n3 - Alterar Aluno\n4 - Exluir Aluno\n')
            if cmd == '1':
                self.listar_alunos()
            elif cmd == '2':
                self.cadastrar_aluno()
            elif cmd == '3':
                self.altera_aluno()
            elif cmd == '4':
                self.excluir_aluno()
            else:
                print('Não entendi!')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()