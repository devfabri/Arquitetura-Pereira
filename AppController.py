from financeiro import FinanceiroController
import sqlite3
import datetime
from datetime import date
from PyQt5 import QtGui, uic, QtWidgets
from PyQt5.QtCore import QDate, Qt

## Import Database & Functions
from novo import Novo
from insere_novoProjeto import Novo_Projeto
from insere_NovoCF import Novo_CF
from bd import Novo_BD
from novo import Novo
from ler_CF import Ler_CF
from ler_projeto import Ler_Projeto
from altera_projeto import Altera_Projeto
from altera_CF import Altera_CF

class LoginPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        uic.loadUi("screens/login.ui", self)
        self.getPassword()
        self.entrar.clicked.connect(self.validar)
        self.altera_senha.clicked.connect(self.changePassword)

    def getPassword(self):
        conn = sqlite3.connect('usuario.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT password FROM usuario WHERE id = 1 """)
        self.password = cursor.fetchone()[0]

    def changePassword(self):
        oldPass, pressed = QtWidgets.QInputDialog.getText(self, "Atualização de Senha", "Insira a senha atual:", QtWidgets.QLineEdit.Password)

        if pressed and oldPass == self.password:
            newPass, pressed = QtWidgets.QInputDialog.getText(self, "Atualização de Senha", "Insira a nova senha:", QtWidgets.QLineEdit.Normal)
            conn = sqlite3.connect("usuario.db")
            cursor = conn.cursor()

            cursor.execute(""" UPDATE usuario SET password = ? WHERE id = 1 """, [newPass])

            conn.commit()
            conn.close()
        self.getPassword()
    def validar(self):
        passinput = self.senha.text()
        
        if passinput == self.password:
            stack.setCurrentIndex(1)

class MainMenu(QtWidgets.QMainWindow, Novo_BD, Novo):
    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi("screens/menu.ui", self)
        self.cria_BD()
        self.cria()
        self.btn_new.clicked.connect(self.toInsertScreen)
        self.btn_read.clicked.connect(self.toReadScreen)
        self.btn_financeiro.clicked.connect(self.toReadDebts)
        
              
        
    def closeApp(self):
        app.quit()
        
    def toInsertScreen(self):
        stack.setCurrentIndex(2)

    def toReadScreen(self):
        stack.setCurrentIndex(3)
    
    def toReadDebts(self):
        stack.setCurrentIndex(4)

class InsertProject(QtWidgets.QMainWindow, Novo_Projeto, Novo_CF):
    def toMenu(self):
        stack.setCurrentIndex(1)

    def collectData(self):
        accepted = QtWidgets.QMessageBox.question(self,"Confirmação","Tem certeza que deseja Inserir o Projeto?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
        if accepted == QtWidgets.QMessageBox.Yes:

            ## Coleta de informações dos radio buttons
            self.tipoCliente = 0
            self.tipoObra = 0
            if self.tipo_fisico.isChecked():
                self.tipoCliente = "Físico"
            elif self.tipo_juridico.isChecked():
                self.tipoCliente = "Jurídico"
            
            if self.obratype_residencial.isChecked(): 
                self.tipoObra = "Residencial" 
            elif self.obratype_comercio.isChecked(): 
                self.tipoObra = "Comércio" 
            elif self.obratype_consultoria.isChecked():
                self.tipoObra = "Consultoria"
            elif self.obratype_empresarial.isChecked():
                self.tipoObra = "Empresarial"

            self.insere_Novo_Projeto(
                self.tipoObra,
                self.tamanho_obra.value(),
                self.valor_m2.value(),
                self.data_finalizacao.date().toString("yyyy-MM-dd"),
                self.data_contratacao.date().toString("yyyy-MM-dd"),
                self.valor_obra.value(),
                self.valor_recebido.value(),
                self.valor_areceber.value(),
                self.qnt_parcelas.value(),
                self.data_vencimento.date().toString("yyyy-MM-dd"))

            self.insere_Novo_CF(
                self.nome1.text(),
                self.nome2.text(),
                self.telefone1.text(),
                self.telefone2.text(),
                self.email1.text(),
                self.email2.text(),
                self.endereco.toPlainText(),
                self.tipoCliente,
                self.cpf.text()
                )
            # Clear Form
            self.nome1.clear()
            self.nome2.clear()
            self.telefone1.clear()
            self.telefone2.clear()
            self.email1.clear()
            self.email2.clear()
            self.endereco.clear()
            self.tamanho_obra.clear()
            self.valor_m2.clear()
            self.valor_obra.clear()
            self.valor_recebido.clear()
            self.valor_areceber.clear()
            self.qnt_parcelas.clear()
            self.cpf.clear()

    def __init__(self):
        super(InsertProject, self).__init__()
        uic.loadUi("screens/new_project.ui", self)
        self.voltar.clicked.connect(self.toMenu)
        self.inserirProjeto.clicked.connect(self.collectData)
        
        self.data_contratacao.setDate(datetime.datetime.now().date())
        self.data_finalizacao.setDate(datetime.datetime.now().date())

        self.valor_obra.valueChanged.connect(self.resto_calculator)
        self.valor_recebido.valueChanged.connect(self.resto_calculator)  

    def resto_calculator(self):
        final = 0
        final = self.valor_obra.value() - self.valor_recebido.value()
        self.valor_areceber.setValue(final)
        self.valor_recebido.setMaximum(self.valor_obra.value())

class ReadProject(QtWidgets.QMainWindow, Ler_Projeto, Ler_CF):
    def __init__(self):
        super(ReadProject, self).__init__()
        uic.loadUi("screens/read_project.ui", self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setColumnHidden(9,False)
        self.tableWidget.setRowCount(50)
        self.btn_voltar.clicked.connect(self.backToMenu)
        self.btn_reload.clicked.connect(self.loadData)
        self.loadData()
        #functions
        self.loadData()
        '''self.loadJobData()'''
    
    def backToMenu(self):
        stack.setCurrentIndex(1)

    def deleteData(self):
        getId = (self.tableWidget.item(self.tableWidget.currentRow(), 9).text())

        accepted = QtWidgets.QMessageBox.question(self,"Confirmação","Tem certeza que deseja deletar?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
        if accepted == QtWidgets.QMessageBox.Yes:
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            # deletando dados da tabela clientes
            conn = sqlite3.connect('cliente.db')
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM cliente WHERE id = (?)
            """, [getId])
            conn.commit()
            conn.close()
            # salvando valor a receber e deletando dados da tabela projetos
            conn = sqlite3.connect('projeto.db')
            cursor = conn.cursor()
            cursor.execute(""" SELECT valorAReceber from projeto WHERE id = ? """, getId)
            a_receber = cursor.fetchone()
            areceber = -a_receber[0]
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM projeto WHERE id = (?)
            """, [getId])
            conn.commit()
            conn.close()
            # ATUALIZANDO FINANCEIRO
            conn = sqlite3.connect('financeiro.db')
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO financeiro (valorAReceber, detalhesGastos, data, idProjeto) VALUES (?,?,?,?) """, (areceber, "Projeto Deletado", datetime.datetime.now(), getId))
            conn.commit()
            conn.close()
        
    def showProject(self):
        pop = ShowProject((self.tableWidget.item(self.tableWidget.currentRow(), 9).text()), self)
        pop.show()

    def loadData(self):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT nomeCliente,  telefone,  tipodecliente 
        FROM cliente;
        """)
        rows_qnt = len(cursor.fetchall())
        self.tableWidget.setRowCount(rows_qnt)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT nomeCliente,  telefone,  tipodecliente 
        FROM cliente;
        """)
        tablerow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
        
        conn.close()

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # lendo dados do banco Projetos
        cursor.execute("""SELECT tipodeprojeto, strftime('%d/%m/%Y', dataContratacao), strftime('%d/%m/%Y', dataConclusao), printf("%.2f",valorRecebido), printf("%.2f",valorAReceber), printf("%.2f",valorTotal), id FROM projeto""")
        tablerow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[6])))
            self.btn_delete = QtWidgets.QPushButton("Deletar", self)
            self.btn_update = QtWidgets.QPushButton("Alterar", self)
            self.btn_addParcela = QtWidgets.QPushButton("Add. Parcela", self)

            self.tableWidget.setCellWidget(tablerow, 10,self.btn_addParcela)
            self.tableWidget.setCellWidget(tablerow,12,self.btn_delete)
            self.tableWidget.setCellWidget(tablerow,11,self.btn_update)

            self.btn_delete.clicked.connect(self.deleteData)
            self.btn_update.clicked.connect(self.showProject) 
            self.btn_addParcela.clicked.connect(self.payParcel)        
            
            
            tablerow+=1

        conn.close()
    
    def payParcel(self):
        id = ((self.tableWidget.item(self.tableWidget.currentRow(), 9).text()))

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT valorAReceber FROM projeto WHERE id = ?""", [id])
        valor_restante = cursor.fetchone()[0]
        conn.close()



        paydialog, pressed = QtWidgets.QInputDialog.getDouble(self, "Abater Parcela", "Quantidade restante: R$"+ str(valor_restante) + "\nQuantidade da Parcela:", 0, 0, valor_restante, 2 )
        if pressed:
            novo_recebido = paydialog

            conn = sqlite3.connect('projeto.db')
            cursor = conn.cursor()

            cursor.execute(""" SELECT valorRecebido, valorTotal from projeto WHERE id = ? """, (id))
            valorRecebido = cursor.fetchone()[0]
            cursor.execute(""" SELECT valorRecebido, valorTotal from projeto WHERE id = ? """, (id))
            valorTotal = cursor.fetchone()[1]
            cursor.execute(""" SELECT valorAReceber from projeto WHERE id = ? """, (id))
            valorAReceber = cursor.fetchone()[0]
            
            input_value = novo_recebido
            novo_recebido = novo_recebido + valorRecebido
            novo_areceber = valorTotal - novo_recebido
            

            cursor.execute(""" UPDATE projeto SET valorAReceber = ?, valorRecebido = ? WHERE id = ? """, (novo_areceber, novo_recebido, id))
            conn.commit()
            conn.close()

            conn = sqlite3.connect('financeiro.db')
            cursor = conn.cursor()

            cursor.execute(""" INSERT INTO financeiro (valorAReceber, detalhesGastos, data, idProjeto) VALUES (?,?,?, ?)  """, ((-input_value), "Parcela abatida", datetime.datetime.now(), id))
            conn.commit()
            conn.close()
            self.loadData()
        
class ReadDebts(QtWidgets.QMainWindow):
    def toMenu(self):
        stack.setCurrentIndex(1)

    def loadDebts(self):
        mes = self.month.date().toString('MM')
        ano = self.year.date().toString('yyyy')

        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        sql = """SELECT printf("%.2f",SUM(valorAReceber)), printf("%.2f",SUM(valorDesenhista)), printf("%.2f",SUM(valorImpostos)), printf("%.2f",SUM(valorContabilidade)), printf("%.2f",SUM(valorFuncionarios)), printf("%.2f",SUM(valorPapelaria)), printf("%.2f",SUM(valorFaxina)), printf("%.2f",SUM(outrosGastos)), printf("%.2f",SUM(valorAReceber)+ SUM(valorExtra) + SUM(valorDesenhista) + SUM(valorImpostos) + SUM(valorContabilidade) + SUM(valorFuncionarios) + SUM(valorPapelaria) + SUM(valorFaxina) + SUM(outrosGastos)) FROM financeiro WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ?;"""
        cursor.execute(sql, [ano, mes])
        
        row = cursor.fetchall()
        
        self.valor_a_receber.setText(str(row[0][0]))
        self.valor_desenhista.setText(str(row[0][1]))
        self.valor_impostos.setText(str(row[0][2]))
        self.valor_contabilidade.setText(str(row[0][3]))
        self.valor_funcionarios.setText(str(row[0][4]))
        self.valor_papelaria.setText(str(row[0][5]))
        self.valor_faxina.setText(str(row[0][6]))
        self.valor_outros.setText(str(row[0][7]))
        self.valor_total.setText(str(row[0][8]))

        conn.commit()
        conn.close()
    
    def adicionarGasto(self):
        pop = AdicionaGasto(self)
        pop.show()
        rsp = pop.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            self.loadDebts()

    def abrirRelatorio(self):
        pop = RelatorioFinanceiro(self)
        pop.show()

    def __init__(self):
        super(ReadDebts, self).__init__()
        uic.loadUi("screens/financeiro.ui", self)
        self.btn_voltar.clicked.connect(self.toMenu)
        self.btn_reload.clicked.connect(self.loadDebts)
        self.btn_adicionar_gasto.clicked.connect(self.adicionarGasto)
        self.btn_relatorio.clicked.connect(self.abrirRelatorio)
        self.month.setDate(datetime.datetime.now().date())
        self.year.setDate(datetime.datetime.now().date())
        self.loadDebts()

class AdicionaGasto(QtWidgets.QDialog, FinanceiroController):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("screens/adicionar_gasto.ui", self)
        self.btn_alterar.clicked.connect(self.insereGastos)
        self.visualisar.clicked.connect(self.watchProjects)

    def watchProjects(self):
        pop = ProjetosPopup(self)
        pop.show()

    def insereGastos(self):
        self.dividaGeral(datetime.datetime.now(), self.val_desenhista.value(), self.val_impostos.value(),self.val_contabilidade.value(), self.val_funcionarios.value(), self.val_papelaria.value(), self.val_faxina.value(), self.val_outros.value(), self.entry_relatorio.toPlainText(), (-(self.val_comissao.value())), (self.id_projeto.text()))
        self.accept()

class RelatorioFinanceiro(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("screens/relatorio_financeiro.ui", self)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
        self.month.setDate(datetime.datetime.now().date())
        self.year.setDate(datetime.datetime.now().date())
        self.loadRelatorio()
        self.btn_reload.clicked.connect(self.loadRelatorio)
        self.visualisar.clicked.connect(self.openProjects)
    
    def openProjects(self):
        pop = ProjetosPopup(self)
        pop.show()

    def loadRelatorio(self):
        id_projeto = self.id_projeto.text()
        mes = self.month.date().toString('MM')
        ano = self.year.date().toString('yyyy')
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        if id_projeto == '':
            cursor.execute("""SELECT * FROM financeiro WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ? ORDER BY data DESC;""", [ano,mes])
        else:
            cursor.execute("""SELECT * FROM financeiro WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ? AND idProjeto = ? ORDER BY data DESC;""", [ano,mes, id_projeto])
        rows_qnt = len(cursor.fetchall())
        self.tableWidget.setRowCount(rows_qnt)

        cursor = conn.cursor()
        if id_projeto == '':
            cursor.execute("""SELECT id,
            strftime('%d/%m/%Y', data),
            printf("%.2f",valorAReceber),
            printf("%.2f",valorDesenhista),
            printf("%.2f",valorImpostos),
            printf("%.2f",valorContabilidade),
            printf("%.2f",valorFuncionarios),
            printf("%.2f",valorPapelaria),
            printf("%.2f",valorFaxina),
            printf("%.2f",outrosGastos),
            detalhesGastos,
            printf("%.2f",valorExtra),
            idProjeto FROM financeiro WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ? ORDER BY data DESC;""", [ano, mes])
        else:
            cursor.execute("""SELECT id,
            strftime('%d/%m/%Y', data),
            printf("%.2f",valorAReceber),
            printf("%.2f",valorDesenhista),
            printf("%.2f",valorImpostos),
            printf("%.2f",valorContabilidade),
            printf("%.2f",valorFuncionarios),
            printf("%.2f",valorPapelaria),
            printf("%.2f",valorFaxina),
            printf("%.2f",outrosGastos),
            detalhesGastos,
            printf("%.2f",valorExtra),
            idProjeto FROM financeiro WHERE strftime('%Y', data) = ? AND strftime('%m', data) = ? AND idProjeto = ? ORDER BY data DESC;""", [ano, mes, id_projeto])
        tableRow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tableRow, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(tableRow, 7, QtWidgets.QTableWidgetItem(str(row[8])))
            self.tableWidget.setItem(tableRow, 8, QtWidgets.QTableWidgetItem(str(row[9])))
            self.tableWidget.setItem(tableRow, 9, QtWidgets.QTableWidgetItem(str(row[11])))
            self.tableWidget.setItem(tableRow, 11, QtWidgets.QTableWidgetItem(str(row[10])))
            self.tableWidget.setItem(tableRow, 10, QtWidgets.QTableWidgetItem(str(row[12])))
            tableRow += 1
        

        conn.close()
        
class ShowProject(QtWidgets.QDialog):
        
    def __init__(self, id, parent):
        super().__init__(parent)
        uic.loadUi("screens/show_project.ui", self)
        localid = id
        self.loadData(localid)   
        self.btn_alterar2.clicked.connect(lambda: self.atualizaProjeto(localid))

        self.valor_total.valueChanged.connect(self.resto_calculator)
        self.valor_recebido.valueChanged.connect(self.resto_calculator)

    def resto_calculator(self):
        final = self.valor_total.value() - self.valor_recebido.value()
        self.valor_a_receber.setValue(final)
        self.valor_recebido.setMaximum(self.valor_total.value())

    def loadData(self, id):
        projectData = []
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM cliente WHERE id = ?;
        """,[id])

        for row in cursor.fetchall():
            projectData.append(row)

        conn.close()


        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projeto WHERE id = ?",[id] )

        for row in cursor.fetchall():
            projectData.append(row)
        conn.close()
        data = projectData
        self.nome1.setText(data[0][1])
        self.nome2.setText(data[0][2])
        self.telefone1.setText(data[0][3])
        self.telefone2.setText(data[0][4])
        self.email1.setText(data[0][5])
        self.email2.setText(data[0][6])
        self.endereco.setText(data[0][7])
        self.tipo_cliente.setText(data[0][8])
        self.cpf.setText(data[0][9])

        self.tipo_obra.setText(data[1][1])
        self.metragem.setText(str(data[1][2]))
        self.valor_metro.setText(str(data[1][3]))
        self.data_conclusao.setDate(QDate.fromString(data[1][4], "yyyy-MM-dd"))
        self.data_contratacao.setDate(QDate.fromString(data[1][5], "yyyy-MM-dd"))
        self.valor_total.setValue(data[1][6])
        self.valor_recebido.setValue((data[1][7]))
        self.valor_a_receber.setValue((data[1][8]))
        self.qnt_parcelas.setValue(int(data[1][9]))
        self.vencimento_parcela.setDate(QDate.fromString(data[1][10], "yyyy-MM-dd"))
    
    def atualizaProjeto(self, id_cliente):
        # RESGATANDO VALOR A RECEBER PARA ATUALIZAR
        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        sql = """ SELECT valorAReceber from projeto WHERE id = ? """
        cursor.execute(sql, [id_cliente])
        areceber = cursor.fetchone()
        a_receber = self.valor_a_receber.value() - areceber[0]
        conn.close()

        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()
        sql = """ UPDATE cliente SET nomeCliente = ?, nomeCliente2 = ?, telefone = ?, telefone2 = ?, email = ?, email2 = ?, endereco = ?, tipodecliente = ? WHERE id = ? """
        cursor.execute(sql, (self.nome1.text(), self.nome2.text(), self.telefone1.text(), self.telefone2.text(), self.email1.text(), self.email2.text(), self.endereco.toPlainText(), self.tipo_cliente.text(), id_cliente))

        conn.commit()
        conn.close()

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()
        sql = """ UPDATE projeto SET tipodeprojeto = ?, metragem = ?, valorMetro = ?, dataConclusao = ?, dataContratacao = ?, valorTotal = ?, valorRecebido = ?, valorAReceber = ?, quantidadeParcelas = ?, dataParcela = ? WHERE id = ? """
        cursor.execute(sql, (self.tipo_obra.text(), self.metragem.text(), self.valor_metro.text(), self.data_conclusao.date().toString("yyyy-MM-dd"), self.data_contratacao.date().toString("yyyy-MM-dd"), self.valor_total.value(), self.valor_recebido.value(), self.valor_a_receber.value(), self.qnt_parcelas.value(), self.vencimento_parcela.date().toString("yyyy-MM-dd"), id_cliente))

        conn.commit()
        conn.close()

        
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()
        sql = """ INSERT INTO financeiro (valorAReceber, detalhesGastos, data, idProjeto) VALUES (?,?,?,?)"""
        cursor.execute(sql, (a_receber, "Atualização de Projeto", datetime.datetime.now(), id_cliente))
        conn.commit()
        conn.close()
        self.accept()
        
class ProjetosPopup(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("screens/popread.ui", self) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setColumnHidden(9,False)
        self.tableWidget.setColumnHidden(10,True)
        self.tableWidget.setColumnHidden(11,True)
        self.tableWidget.setColumnHidden(12,True)
        self.tableWidget.setRowCount(50)
        self.btn_reload.clicked.connect(self.loadData)
        #functions
        self.loadData()

    def loadData(self):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT nomeCliente,  telefone,  tipodecliente 
        FROM cliente;
        """)
        rows_qnt = len(cursor.fetchall())
        self.tableWidget.setRowCount(rows_qnt)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT nomeCliente,  telefone,  tipodecliente 
        FROM cliente;
        """)
        tablerow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
        
        conn.close()

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # lendo dados do banco Projetos
        cursor.execute("""SELECT tipodeprojeto, strftime('%d/%m/%Y', dataContratacao), strftime('%d/%m/%Y', dataConclusao), printf("%.2f",valorRecebido), printf("%.2f",valorAReceber), printf("%.2f",valorTotal), id FROM projeto""")
        tablerow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[6])))


                   
            
            
            tablerow+=1

        conn.close()
# main stack
app = QtWidgets.QApplication([])
app.setApplicationName("Controle Financeiro Arquitetura Pereira")
app.setWindowIcon(QtGui.QIcon('src/logo.jpeg'))
stack = QtWidgets.QStackedWidget()
# starting classes
loginpage = LoginPage()
mainmenu = MainMenu()
insert_project = InsertProject()
read_project = ReadProject()
read_debts = ReadDebts()
# adding to stack
stack.addWidget(loginpage)
stack.addWidget(mainmenu)
stack.addWidget(insert_project)
stack.addWidget(read_project)
stack.addWidget(read_debts)

# initializing project
stack.showMaximized()

app.exec()