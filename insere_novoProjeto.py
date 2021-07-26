from Insere_NovoGasto import InsereFinancas
import sqlite3

class Novo_Projeto(InsereFinancas):
    def insere_Novo_Projeto(self, Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela):

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO projeto (tipodeprojeto, metragem, valorMetro, dataConclusao, dataContratacao, valorTotal, valorRecebido, valorAReceber, quantidadeParcelas, dataParcela)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')
       
        InsereFinancas.Atualiza_Valortotal(ValorTotal, ValorAReceber)
