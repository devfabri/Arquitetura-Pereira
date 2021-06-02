import sqlite3
class Altera_Projeto:
    def altera_proj(self, id_cliente, Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO):
        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()
        """
        id_cliente = input('Digite id do cliente: ')
        Tipo = input('Digite 1 para reforma ou 2 para nova construção: ')		
        Metragem = input('Digite a primeira metragem')
        DataConclusao = input('Digite a data de conclusão no seguinte formato DD/MM/AAAA')
        Etapa = input('Digite a etapa atual do projeto')
        NomeCliente = input('Digite o nome do cliente')
        DataContratacao = input('Digite a data de contratação no seguinte Formato DD/MM/AAAA')
        Telefone = input('Digite o telefone de contato do cliente')
        VT = input('Digite o valor do projeto')
        VA = input('Digite o valor pago ja pago')
        VP = input('Digite o valor a ser parcelado') vai virar escritotio 
        DP = input('Digite o dia do mes de vencimento da parcela')
        QP = input('Digite o a quantidade de parcelas') vai virar desenhista
        VM = input('Digite o valor pago em materiais') comentarios
        VMO = input('Digite o valor pago em mão de obra') salarios escritorio
        VD = input('Digite o valor pago em decoração') some
        """
        
        # alterando os dados da tabela
        cursor.execute("""
        UPDATE clientes
        SET tipo = ?, metragem = ?, dataConclusao = ?, etapa = ?, nomeCliente = ?, dataContratacao = ?, telefone = ?, vt = ?, va = ?, vp = ?, dp = ?, qp = ?, vm = ?, vmo = ?
        WHERE id = ?
        """, (Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO, id_cliente))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()