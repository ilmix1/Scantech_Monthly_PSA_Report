# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage2(object):
    def setupUi(self, PSAPage2):
        PSAPage2.setObjectName("PSAPage2")
        PSAPage2.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage2.sizePolicy().hasHeightForWidth())
        PSAPage2.setSizePolicy(sizePolicy)
        PSAPage2.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage2)
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(74, 260, 653, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(74, 325, 653, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(74, 390, 653, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(20)
        self.psa_report_title_3 = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title_3.setGeometry(QtCore.QRect(74, 230, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.psa_report_title_3.setFont(font)
        self.psa_report_title_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.psa_report_title_3.setObjectName("psa_report_title_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(150, 499, 214, 95))
        self.tableWidget_4.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setShowGrid(True)
        self.tableWidget_4.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(35)
        self.psa_report_title_4 = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title_4.setGeometry(QtCore.QRect(150, 459, 214, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.psa_report_title_4.setFont(font)
        self.psa_report_title_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.psa_report_title_4.setObjectName("psa_report_title_4")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(420, 499, 251, 95))
        self.tableWidget_5.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_5.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_5.setItem(2, 0, item)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_5.verticalHeader().setMinimumSectionSize(20)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(75, 600, 650, 350))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Resources/Detector_Stability.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        PSAPage2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage2)
        self.statusbar.setObjectName("statusbar")
        PSAPage2.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage2)
        self.NextPage.released.connect(PSAPage2.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage2)

    def retranslateUi(self, PSAPage2):
        _translate = QtCore.QCoreApplication.translate
        PSAPage2.setWindowTitle(_translate("PSAPage2", "PSA Report Page 2"))
        self.psa_report_title.setText(_translate("PSAPage2", "PSA Report"))
        self.NextPage.setText(_translate("PSAPage2", "Next"))
        self.Regenerate.setText(_translate("PSAPage2", "Regenerate Report"))
        self.psa_report_title_2.setText(_translate("PSAPage2", "Page 2"))
        self.PreviousPage.setText(_translate("PSAPage2", "Previous"))
        self.label_2.setText(_translate("PSAPage2", "Page Control"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Enabled"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Stable"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Detector 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Detector 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Detector 3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage2", "Detector 4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PSAPage2", "Detector 5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PSAPage2", "Detector 6"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Enabled"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Stable"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Detector 7"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Detector 8"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Detector 9"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage2", "Detector 10"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("PSAPage2", "Detector 11"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("PSAPage2", "Detector 12"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Enabled"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Stable"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Detector 13"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Detector 14"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Detector 15"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage2", "Detector 16"))
        self.psa_report_title_3.setText(_translate("PSAPage2", "Detector Stability (at the time the report was compiled)"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Detector Enclosure"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Electronics Cabinet"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Stable?"))
        self.psa_report_title_4.setText(_translate("PSAPage2", "Temperature Control"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Normal"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Situation Flagged"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Requires Urgent Attention"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Legend"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        item.setText(_translate("PSAPage2", "yt"))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage2 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage2()
    ui.setupUi(PSAPage2)
    PSAPage2.show()
    sys.exit(app.exec_())
