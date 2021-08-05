import sqlite3
from datetime import datetime

class FinanceiroController():
    def dividaProjeto(self, valorReceber, id):
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO financeiro (valorAReceber, data, detalhesGastos, idProjeto) VALUES (?,?,?,?)""", (valorReceber, datetime.now(), "Gastos em Novo Projeto", id))

        conn.commit()
        conn.close()

        print("dados inseridos em -financeiro- com sucesso")

    def dividaGeral(self, data, valorDesenhista, valorImpostos, valorContabilidade, valorFuncionarios, valorPapelaria, valorFaxina, otrosGastos, detalhesGastos, valorExtra, id):
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()
        sql = """ INSERT INTO financeiro (data, valorDesenhista, valorImpostos, valorContabilidade, valorFuncionarios, valorPapelaria, valorFaxina, outrosGastos, detalhesGastos, valorExtra, idProjeto) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

        cursor.execute(sql, (data, valorDesenhista, valorImpostos, valorContabilidade, valorFuncionarios, valorPapelaria, valorFaxina, otrosGastos, detalhesGastos, valorExtra, id))
        conn.commit()
        conn.close()