# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warSimUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import warCalc


class Ui_warSim(object):
    def setupUi(self, warSim):
        warSim.setObjectName("warSim")
        warSim.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(warSim)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoSimular = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSimular.setGeometry(QtCore.QRect(140, 200, 111, 41))
        self.botaoSimular.setObjectName("botaoSimular")
        self.logoWar = QtWidgets.QLabel(self.centralwidget)
        self.logoWar.setGeometry(QtCore.QRect(70, 30, 260, 50))
        self.logoWar.setAutoFillBackground(False)
        self.logoWar.setStyleSheet("background-image: url(:/newPrefix/warlogo.png);")
        self.logoWar.setText("")
        self.logoWar.setScaledContents(True)
        self.logoWar.setObjectName("logoWar")
        self.botaoSair = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSair.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.botaoSair.setObjectName("botaoSair")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(90, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName("Titulo")
        self.entradaAtaque = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaAtaque.setGeometry(QtCore.QRect(80, 160, 81, 21))
        self.entradaAtaque.setObjectName("entradaAtaque")
        self.entradaDefesa = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaDefesa.setGeometry(QtCore.QRect(230, 160, 81, 21))
        self.entradaDefesa.setObjectName("entradaDefesa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 140, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 140, 91, 16))
        self.label_2.setObjectName("label_2")
        warSim.setCentralWidget(self.centralwidget)
        warSim.setWindowIcon(QtGui.QIcon("waricon.png"))

        self.retranslateUi(warSim)
        self.botaoSair.clicked.connect(warSim.close)
        QtCore.QMetaObject.connectSlotsByName(warSim)
        
        self.botaoSimular.clicked.connect(self.simula)
        
    def simula(self):
        ataque = self.entradaAtaque.text()
        defesa = self.entradaDefesa.text()
        if ataque.isnumeric() and defesa.isnumeric():
            ataque = int(ataque)
            defesa = int(defesa)
            resultado = warCalc.war(ataque, defesa)
            msg = QMessageBox()
            msg.setWindowTitle("Resultado")
            msg.setText("Probabilidade de sucesso de %i%%"%(resultado*100))
            msg.exec()
        else:
            msgError = QMessageBox()
            msgError.setIcon(msgError.Warning)
            msgError.setWindowTitle("Erro")
            msgError.setText("Insira valores numéricos inteiros.")
            msgError.exec()

    def retranslateUi(self, warSim):
        _translate = QtCore.QCoreApplication.translate
        warSim.setWindowTitle(_translate("warSim", "War Simulator"))
        self.botaoSimular.setText(_translate("warSim", "Simular"))
        self.botaoSair.setText(_translate("warSim", "Sair"))
        self.Titulo.setText(_translate("warSim", "<html><head/><body><p>Simulador de ataque</p></body></html>"))
        self.label.setText(_translate("warSim", "Tropas de ataque"))
        self.label_2.setText(_translate("warSim", "Tropas de defesa"))
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warSim = QtWidgets.QMainWindow()
    ui = Ui_warSim()
    ui.setupUi(warSim)
    warSim.show()
    sys.exit(app.exec_())