import sqlite3
class Atualiza_Gasto:
    def Atualiza_Gastos(self,ValorAReceber, ValorDesenhista, ValorImpostos, ValorContabilidade, ValorFuncionarios, ValorPapelaria, ValorFaxina, OutrosGastos, DetalhesGastos):

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT valorTotal FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            final = Valor
        
        final = final - ValorDesenhista - ValorImpostos - ValorContabilidade - ValorFuncionarios - ValorPapelaria - ValorFaxina - OutrosGastos

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

       # lendo os dados
        cursor.execute("""
        SELECT valorAReceber FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            receber = Valor + ValorAReceber
        
        # lendo os dados
        cursor.execute("""
        SELECT valorDesenhista FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            desenhista = Valor + ValorDesenhista
        
        # lendo os dados
        cursor.execute("""
        SELECT valorImpostos FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            impostos = Valor + ValorImpostos
        
        # lendo os dados
        cursor.execute("""
        SELECT valorContabilidade FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            contabil = Valor + ValorContabilidade

        # lendo os dados
        cursor.execute("""
        SELECT valorFuncionarios FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            funcionario = Valor + ValorFuncionarios
                
        # lendo os dados
        cursor.execute("""
        SELECT valorPapelaria FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            papelaria = Valor + ValorPapelaria
                
        # lendo os dados
        cursor.execute("""
        SELECT valorFaxina FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            faxina = Valor + ValorFaxina

        # lendo os dados
        cursor.execute("""
        SELECT outrosGastos FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            outros = Valor + OutrosGastos
                    
        # inserindo dados na tabela
        cursor.execute("""
        UPDATE INTO financeiro    
        SET valorTotal = ?, valorAReceber = ?, valorDesenhista = ?, valorImpostos = ?, valorContabilidade = ?, valorFuncionarios = ?, valorPapelaria = ?, valorFaxina = ?, outrosGastos = ?, detalhesGastos = ?
        WHERE id = 1
        """, (final, receber, desenhista, impostos, contabil, funcionario, papelaria, faxina, outros, DetalhesGastos))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')