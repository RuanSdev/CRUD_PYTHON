import sqlite3 as lite
if __name__ == '__main__':
    print('Sistema  pode ser executado na main')
else: 
    class Banco_dados():
        def __init__(self,nome_db):
            self.nome_db = nome_db
            self.con = None
            self.cursor = None
        def conectando(self):
            self.con = lite.connect(self.nome_db)
            self.cursor = self.con.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS USUARIO (NOME TEXT PRIMARY KEY NOT NULL , SENHA TEXT NOT NULL);')
        def Inserir_Dados(self,nome,senha):
            self.conectando()
            with self.con:
                self.cursor.execute('INSERT INTO USUARIO (NOME,SENHA) VALUES (?,?)',(nome,senha))
                self.con.commit()
        def Atualizar_Dados(self,nome,NOVO,SENHA):
            self.conectando()
            with self.con:
                self.cursor.execute('UPDATE USUARIO SET NOME = ? WHERE NOME = ?',(NOVO,nome))
                self.cursor.execute('UPDATE USUARIO SET SENHA = ? WHERE NOME = ?',(SENHA,NOVO))
        def Consulta_Dados(self):
            self.conectando()
            with self.con:
                return self.cursor.execute('SELECT * FROM USUARIO').fetchall()
        def Consulta_Nome(self,nome):
            self.conectando()
            with self.con:
                return self.cursor.execute('SELECT * FROM USUARIO WHERE NOME = ?',(nome,)).fetchall()
        def Deletar_Dados(self,NOME):
            self.conectando()
            with self.con:
                self.cursor.execute('DELETE  FROM USUARIO WHERE NOME = ?',(NOME,))
        




