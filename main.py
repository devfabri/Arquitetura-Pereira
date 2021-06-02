import sqlite3
from altera_projeto import Altera_Projeto
from bd import Novo_BD
from insere_NovoCF import Novo_CF
from insere_novoProjeto import Novo_Projeto
from ler_CF import Ler_CF
from ler_projeto import Ler_Projeto
from novo import Novo

def main():
    Novo_BD.cria_BD()
    Novo.cria()

    if operacao == 1:
        Novo_Projeto.insere_Novo_Projeto(Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO)
        Novo_CF.insere_Novo_CF(NomeCliente, Endereco, Telefone, Email)
    else:
        Ler_Projeto.leia_proj()
        Ler_CF.leia_cf()
        if DesejaProj == 1:
            Altera_Projeto.altera_proj(id_cliente, Tipo, Metragem, DataConclusao, Etapa, NomeCliente, DataContratacao, Telefone, VT, VA, VP, DP, QP, VM, VMO)
            Altera_CF.altera_cf(id_cliente, NomeCliente, Endereco, Telefone, Email)                
        else:
            Altera_CF.altera_cf(id_cliente, NomeCliente, Endereco, Telefone, Email)                

"""
    Side, tem que trocar umas labels: 
        agora quando ele editar o cliente edita o VT (valor total) 
        VP (valor parcelado) agora aparece como Valor gasto em materias de escritorio
        QP (quantidade de parcelas) vira Valor gasto em desenhista
        VM(valor gasto em materiais) vira uma caixa de comentarios
        VMO (Valor de mão de obra) vira valor em salarios do escritorio
        VD = (valor em decoração) deixa de existir 

"""

                            

