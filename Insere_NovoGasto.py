import sqlite3
class InsereFinancas:
    def Atualiza_Valortotal(self, ValorTotal):

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT valorTotal FROM financeiro WHERE id = 1;
        """)

        for Valor in cursor.fetchall():
            final = Valor
        
        conn.close()    
        
        final = final + ValorTotal

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE financeiro
        SET valorTotal = ?
        WHERE id = 1
        """, (final))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()
    
   