import sqlite3

class Novo_Projeto:
    def insere_Novo_Projeto(self, id_cliente, Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO):

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO clientes (tipo, metragem, dataConclusao, etapa, nomeCliente, dataContratacao, telefone, vt, va, vp, dp, qp, vm, vmo)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')
