import sqlite3
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

class MainMenu(QtWidgets.QMainWindow, Novo_BD, Novo):
    def toInsertScreen(self):
        stack.setCurrentIndex(1)

    def toReadScreen(self):
        stack.setCurrentIndex(2)
        

    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi("screens/menu.ui", self)
        self.cria_BD()
        self.cria()
        self.btn_new.clicked.connect(self.toInsertScreen)
        self.btn_read.clicked.connect(self.toReadScreen)

class InsertProject(QtWidgets.QMainWindow, Novo_Projeto, Novo_CF):
    def toMenu(self):
        stack.setCurrentIndex(0)

    def collectData(self):
        ## Coleta de informações dos radio buttons
        self.tipoCliente = 0
        self.tipoObra = 0
        if self.tipo_fisico.isChecked():
            self.tipoCliente = 1
        elif self.tipo_juridico.isChecked():
            self.tipoCliente = 2
        
        if self.obratype_residencial.isChecked(): 
            self.tipoObra = 1 
        elif self.obratype_comercio.isChecked(): 
            self.tipoObra = 2 
        elif self.obratype_consultoria.isChecked():
            self.tipoObra = 3
        elif self.obratype_empresarial.isChecked():
            self.tipoObra = 4

        self.insere_Novo_Projeto(
            self.tipoObra,
            self.tamanho_obra.text(),
            self.valor_m2.text(),
            self.data_finalizacao.date().toString("yyyy-MM-dd"),
            self.data_contratacao.date().toString("yyyy-MM-dd"),
            self.valor_obra.text(),
            self.valor_recebido.text(),
            self.valor_areceber.text(),
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
            self.tipoCliente)
        

    def __init__(self):
        super(InsertProject, self).__init__()
        uic.loadUi("screens/new_project.ui", self)
        self.voltar.clicked.connect(self.toMenu)
        self.inserirProjeto.clicked.connect(self.collectData)

class ReadProject(QtWidgets.QMainWindow, Ler_Projeto, Ler_CF):
    def backToMenu(self):
        stack.setCurrentIndex(0)
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
        self.tableWidget.setRowCount(50)
        self.btn_voltar.clicked.connect(self.backToMenu)
        self.btn_reload.clicked.connect(self.loadData)
        #functions
        self.loadData()
        '''self.loadJobData()'''

    def loadData(self):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT nomeCliente,  telefone,  tipoDeObra 
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
        cursor.execute("SELECT tipo, dataContratacao, dataConclusao, valorRecebido, valorAReceber, valorTotal FROM projeto")
        tablerow = 0
        for row in cursor.fetchall():
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[5])))
            
            
            tablerow+=1

        conn.close()

# main stack
app = QtWidgets.QApplication([])
stack = QtWidgets.QStackedWidget()
# starting classes
mainmenu = MainMenu()
insert_project = InsertProject()
read_project = ReadProject()
# adding to stack
stack.addWidget(mainmenu)
stack.addWidget(insert_project)
stack.addWidget(read_project)
# initializing project
stack.showMaximized()
app.exec()