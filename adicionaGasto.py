import sqlite3
class Novo_Gasto:
    def Atualiza_Valortotal(self,ValorAReceber, ValorDesenhista, ValorImpostos, ValorContabilidade, ValorFuncionarios, ValorPapelaria, ValorFaxina, OutrosGastos, DetalhesGastos):

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT valorTotal FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            final = Valor
        
        final = final - ValorDesenhista - ValorImpostos - valorContabilidade - valorFuncionarios - ValorPapelaria - valorFaxina - OutrosGastos

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE financeiro
        SET valorTotal = ?
        WHERE id = 1
        """, (final))

        conn.commit()
        
        conn.close()
    
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO financeiro (valorTotal, valorAReceber, valorDesenhista, valorImpostos, valorContabilidade, valorFuncionarios, valorPapelaria, valorFaxina, outrosGastos, detalhesGastos)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (final, ValorAReceber, ValorDesenhista, ValorImpostos, ValorContabilidade, ValorFuncionarios, ValorPapelaria, ValorFaxina, OutrosGastos, DetalhesGastos))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')

