import sqlite3
class Altera_Projeto:
    def altera_proj(self, id_cliente, Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela):
        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()
        
        # alterando os dados da tabela
        cursor.execute("""
        UPDATE projeto
        SET tipodeprojeto = ?, metragem = ?, valorMetro = ?, dataConclusao = ?, dataContratacao = ?, valorTotal = ?, valorRecebido = ?, valorAReceber = ?, quantidadeParcelas = ?, dataParcela = ?
        WHERE id = ?
        """, (Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela, id_cliente))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

        
