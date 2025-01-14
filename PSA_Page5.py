# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page5.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage5(object):
    def setupUi(self, PSAPage5):
        PSAPage5.setObjectName("PSAPage5")
        PSAPage5.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage5.sizePolicy().hasHeightForWidth())
        PSAPage5.setSizePolicy(sizePolicy)
        PSAPage5.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage5)
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
        self.Results2 = QtWidgets.QLabel(self.centralwidget)
        self.Results2.setGeometry(QtCore.QRect(100, 225, 625, 725))
        self.Results2.setText("")
        self.Results2.setPixmap(QtGui.QPixmap(":/Resources/Results2.png"))
        self.Results2.setScaledContents(True)
        self.Results2.setObjectName("Results2")
        PSAPage5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage5)
        self.statusbar.setObjectName("statusbar")
        PSAPage5.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage5)
        self.NextPage.released.connect(PSAPage5.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage5)

    def retranslateUi(self, PSAPage5):
        _translate = QtCore.QCoreApplication.translate
        PSAPage5.setWindowTitle(_translate("PSAPage5", "PSA Report Page 5"))
        self.psa_report_title.setText(_translate("PSAPage5", "PSA Report"))
        self.NextPage.setText(_translate("PSAPage5", "Next"))
        self.Regenerate.setText(_translate("PSAPage5", "Regenerate Report"))
        self.psa_report_title_2.setText(_translate("PSAPage5", "Page 5"))
        self.PreviousPage.setText(_translate("PSAPage5", "Previous"))
        self.label_2.setText(_translate("PSAPage5", "Page Control"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage5 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage5()
    ui.setupUi(PSAPage5)
    PSAPage5.show()
    sys.exit(app.exec_())
