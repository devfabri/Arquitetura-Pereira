import sqlite3
class InsereFinancas:
    def Atualiza_Valortotal(self, ValorTotal, ValorAReceber):

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()
        final = 0
        receber = 0
        # lendo os dados
        cursor.execute("""
        SELECT valorTotal FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            final = Valor + float(ValorTotal)
        
        # lendo os dados
        cursor.execute("""
        SELECT valorAReceber FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            receber = Valor + float(ValorAReceber)
        
        conn.close()    
        
        final = final + float(ValorTotal)

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE financeiro
        SET valorTotal = ?, valorAReceber = ?
        WHERE id = 1
        """, (final, receber))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()
    
   