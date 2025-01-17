# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage3(object):
    def setupUi(self, PSAPage3):
        PSAPage3.setObjectName("PSAPage3")
        PSAPage3.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage3.sizePolicy().hasHeightForWidth())
        PSAPage3.setSizePolicy(sizePolicy)
        PSAPage3.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Resources/ScantechReportHeader.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.psa_report_title = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title.setGeometry(QtCore.QRect(300, 150, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title.setFont(font)
        self.psa_report_title.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title.setObjectName("psa_report_title")
        self.NextPage = QtWidgets.QPushButton(self.centralwidget)
        self.NextPage.setGeometry(QtCore.QRect(700, 180, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.NextPage.setFont(font)
        self.NextPage.setObjectName("NextPage")
        self.Regenerate = QtWidgets.QPushButton(self.centralwidget)
        self.Regenerate.setGeometry(QtCore.QRect(10, 160, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.Regenerate.setFont(font)
        self.Regenerate.setObjectName("Regenerate")
        self.psa_report_title_2 = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title_2.setGeometry(QtCore.QRect(350, 195, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title_2.setFont(font)
        self.psa_report_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title_2.setObjectName("psa_report_title_2")
        self.PreviousPage = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousPage.setGeometry(QtCore.QRect(610, 180, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.PreviousPage.setFont(font)
        self.PreviousPage.setObjectName("PreviousPage")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(645, 150, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Temps = QtWidgets.QLabel(self.centralwidget)
        self.Temps.setGeometry(QtCore.QRect(75, 235, 650, 350))
        self.Temps.setText("")
        self.Temps.setPixmap(QtGui.QPixmap(":/Resources/Temperatures.png"))
        self.Temps.setScaledContents(True)
        self.Temps.setObjectName("Temps")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(75, 600, 650, 350))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Resources/Daily_Tonnes.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        PSAPage3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage3)
        self.statusbar.setObjectName("statusbar")
        PSAPage3.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage3)
        self.NextPage.released.connect(PSAPage3.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage3)

    def retranslateUi(self, PSAPage3):
        _translate = QtCore.QCoreApplication.translate
        PSAPage3.setWindowTitle(_translate("PSAPage3", "PSA Report Page 3"))
        self.psa_report_title.setText(_translate("PSAPage3", "PSA Report"))
        self.NextPage.setText(_translate("PSAPage3", "Next"))
        self.Regenerate.setText(_translate("PSAPage3", "Regenerate Report"))
        self.psa_report_title_2.setText(_translate("PSAPage3", "Page 3"))
        self.PreviousPage.setText(_translate("PSAPage3", "Previous"))
        self.label_2.setText(_translate("PSAPage3", "Page Control"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage3 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage3()
    ui.setupUi(PSAPage3)
    PSAPage3.show()
    sys.exit(app.exec_())
