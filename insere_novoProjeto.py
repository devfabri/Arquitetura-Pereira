from Insere_NovoGasto import InsereFinancas
import sqlite3

class Novo_Projeto:
    def insere_Novo_Projeto(self, Tipo, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela):

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO projeto (tipo, metragem, valorMetro, dataConclusao, dataContratacao, valorTotal, valorRecebido, valorAReceber, quantidadeParcelas, dataParcela)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (Tipo, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')
        
        InsereFinancas.Atualiza_Valortotal(ValorTotal)
        InsereFinancas.Atualiza_ValorRecebido(ValorRecebido)
