from PyQt5 import uic, QtWidgets

class MainMenu(QtWidgets.QMainWindow):
    def toInsertScreen(self):
        stack.setCurrentIndex(1)

    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi("../screens/menu.ui", self)
        self.btn_new.clicked.connect(self.toInsertScreen)

class InsertProject(QtWidgets.QMainWindow):
    def toMenu(self):
        stack.setCurrentIndex(0)

    def sendData(self):
        self.TipoCliente = 2
        self.nome1 = self.nome1.text()
        self.nome2 = self.nome2.text()
        self.telefone1 = self.telefone1.text()
        self.telefone2 = self.telefone2.text()
        if (self.tipo_fisico.checked == True):
            self.TipoProjeto = 1
        

    def __init__(self):
        super(InsertProject, self).__init__()
        uic.loadUi("../screens/new_project.ui", self)
        self.voltar.clicked.connect(self.toMenu)
        self.inserirProjeto.clicked.connect(self.sendData)

class ReadProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(ReadProject, self).__init__()
        uic.loadUi("../screens/read_project.ui", self)

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