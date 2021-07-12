from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate, Qt

## Import Database & Functions
from insere_novoProjeto import Novo_Projeto
from insere_NovoCF import Novo_CF

class MainMenu(QtWidgets.QMainWindow):
    def toInsertScreen(self):
        stack.setCurrentIndex(1)

    def toReadScreen(self):
        stack.setCurrentIndex(2)

    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi("screens/menu.ui", self)
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

        self.clientData = (
            self.nome1.text(),
            self.nome2.text(),
            self.telefone1.text(),
            self.telefone2.text(),
            self.tipoCliente,
            self.email1.text(),
            self.email2.text(),
            self.endereco.toPlainText()
        )

        self.jobData = (
            self.tipoObra,
            self.tamanho_obra.text(),
            self.valor_m2.text(),
            self.data_finalizacao.date().toString("yyyy-MM-dd"),
            self.data_contratacao.date().toString("yyyy-MM-dd"),
            self.valor_obra.text(),
            self.valor_recebido.text(),
            self.valor_areceber.text(),
            self.qnt_parcelas.text(),
            self.data_vencimento.date().toString("yyyy-MM-dd")
        )

        self.insere_Novo_Projeto(
            self.tipoObra,
            self.tamanho_obra.text(),
            self.valor_m2.text(),
            self.data_finalizacao.date().toString("yyyy-MM-dd"),
            self.data_contratacao.date().toString("yyyy-MM-dd"),
            self.valor_obra.text(),
            self.valor_recebido.text(),
            self.valor_areceber.text(),
            self.qnt_parcelas.text(),
            self.data_vencimento.date().toString("yyyy-MM-dd"))

        self.insere_Novo_CF(
            self.nome1.text(),
            self.nome2.text(),
            self.telefone1.text(),
            self.telefone2.text(),
            self.tipoCliente,
            self.email1.text(),
            self.email2.text(),
            self.endereco.toPlainText())

        print(self.clientData)
        print(self.jobData)
        

    def __init__(self):
        super(InsertProject, self).__init__()
        uic.loadUi("screens/new_project.ui", self)
        self.voltar.clicked.connect(self.toMenu)
        self.inserirProjeto.clicked.connect(self.collectData)

class ReadProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(ReadProject, self).__init__()
        uic.loadUi("screens/read_project.ui", self)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,200)

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