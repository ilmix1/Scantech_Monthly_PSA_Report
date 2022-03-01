# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage1(object):
    def setupUi(self, PSAPage1):
        PSAPage1.setObjectName("PSAPage1")
        PSAPage1.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage1.sizePolicy().hasHeightForWidth())
        PSAPage1.setSizePolicy(sizePolicy)
        PSAPage1.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Resources/ScantechReportHeader.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.psa_report_title = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title.setGeometry(QtCore.QRect(0, 150, 800, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title.setFont(font)
        self.psa_report_title.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title.setObjectName("psa_report_title")
        self.site_name = QtWidgets.QLabel(self.centralwidget)
        self.site_name.setGeometry(QtCore.QRect(0, 200, 800, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.site_name.setFont(font)
        self.site_name.setAlignment(QtCore.Qt.AlignCenter)
        self.site_name.setObjectName("site_name")
        self.period = QtWidgets.QLabel(self.centralwidget)
        self.period.setGeometry(QtCore.QRect(235, 320, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.period.setFont(font)
        self.period.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.period.setObjectName("period")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(235, 340, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email.setObjectName("email")
        self.next_psa_visit = QtWidgets.QLabel(self.centralwidget)
        self.next_psa_visit.setGeometry(QtCore.QRect(235, 362, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.next_psa_visit.setFont(font)
        self.next_psa_visit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_psa_visit.setObjectName("next_psa_visit")
        self.src_topup_due = QtWidgets.QLabel(self.centralwidget)
        self.src_topup_due.setGeometry(QtCore.QRect(235, 382, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.src_topup_due.setFont(font)
        self.src_topup_due.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.src_topup_due.setObjectName("src_topup_due")
        self.period_data = QtWidgets.QLabel(self.centralwidget)
        self.period_data.setGeometry(QtCore.QRect(395, 320, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.period_data.setFont(font)
        self.period_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.period_data.setObjectName("period_data")
        self.rep_serv_eng_data = QtWidgets.QLabel(self.centralwidget)
        self.rep_serv_eng_data.setGeometry(QtCore.QRect(395, 280, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.rep_serv_eng_data.setFont(font)
        self.rep_serv_eng_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rep_serv_eng_data.setObjectName("rep_serv_eng_data")
        self.email_data = QtWidgets.QLabel(self.centralwidget)
        self.email_data.setGeometry(QtCore.QRect(395, 340, 400, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.email_data.setFont(font)
        self.email_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_data.setObjectName("email_data")
        self.rep_analyser_data = QtWidgets.QLabel(self.centralwidget)
        self.rep_analyser_data.setGeometry(QtCore.QRect(395, 260, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.rep_analyser_data.setFont(font)
        self.rep_analyser_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rep_analyser_data.setObjectName("rep_analyser_data")
        self.rep_app_data = QtWidgets.QLabel(self.centralwidget)
        self.rep_app_data.setGeometry(QtCore.QRect(395, 300, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.rep_app_data.setFont(font)
        self.rep_app_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rep_app_data.setObjectName("rep_app_data")
        self.rep_date_data = QtWidgets.QLabel(self.centralwidget)
        self.rep_date_data.setGeometry(QtCore.QRect(395, 240, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.rep_date_data.setFont(font)
        self.rep_date_data.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rep_date_data.setAutoFillBackground(False)
        self.rep_date_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rep_date_data.setObjectName("rep_date_data")
        self.rep_date = QtWidgets.QLabel(self.centralwidget)
        self.rep_date.setGeometry(QtCore.QRect(235, 240, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.rep_date.setFont(font)
        self.rep_date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rep_date.setAutoFillBackground(False)
        self.rep_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rep_date.setObjectName("rep_date")
        self.rep_app = QtWidgets.QLabel(self.centralwidget)
        self.rep_app.setGeometry(QtCore.QRect(235, 300, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.rep_app.setFont(font)
        self.rep_app.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rep_app.setObjectName("rep_app")
        self.rep_analyser = QtWidgets.QLabel(self.centralwidget)
        self.rep_analyser.setGeometry(QtCore.QRect(235, 260, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.rep_analyser.setFont(font)
        self.rep_analyser.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rep_analyser.setObjectName("rep_analyser")
        self.rep_serv_eng = QtWidgets.QLabel(self.centralwidget)
        self.rep_serv_eng.setGeometry(QtCore.QRect(235, 280, 150, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.rep_serv_eng.setFont(font)
        self.rep_serv_eng.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rep_serv_eng.setObjectName("rep_serv_eng")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 405, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.label_endiskspc = QtWidgets.QLabel(self.centralwidget)
        self.label_endiskspc.setGeometry(QtCore.QRect(10, 570, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_endiskspc.setFont(font)
        self.label_endiskspc.setIndent(5)
        self.label_endiskspc.setObjectName("label_endiskspc")
        self.label_stduptodate = QtWidgets.QLabel(self.centralwidget)
        self.label_stduptodate.setGeometry(QtCore.QRect(10, 545, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_stduptodate.setFont(font)
        self.label_stduptodate.setIndent(5)
        self.label_stduptodate.setObjectName("label_stduptodate")
        self.label_elecenctempstab = QtWidgets.QLabel(self.centralwidget)
        self.label_elecenctempstab.setGeometry(QtCore.QRect(10, 520, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_elecenctempstab.setFont(font)
        self.label_elecenctempstab.setIndent(5)
        self.label_elecenctempstab.setObjectName("label_elecenctempstab")
        self.label_detenctempstab = QtWidgets.QLabel(self.centralwidget)
        self.label_detenctempstab.setGeometry(QtCore.QRect(10, 495, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_detenctempstab.setFont(font)
        self.label_detenctempstab.setIndent(5)
        self.label_detenctempstab.setObjectName("label_detenctempstab")
        self.label_endetstab = QtWidgets.QLabel(self.centralwidget)
        self.label_endetstab.setGeometry(QtCore.QRect(10, 470, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_endetstab.setFont(font)
        self.label_endetstab.setIndent(5)
        self.label_endetstab.setObjectName("label_endetstab")
        self.label_anopcor = QtWidgets.QLabel(self.centralwidget)
        self.label_anopcor.setGeometry(QtCore.QRect(10, 445, 250, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_anopcor.setFont(font)
        self.label_anopcor.setIndent(5)
        self.label_anopcor.setObjectName("label_anopcor")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 440, 10, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, 440, 10, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(5, 440, 10, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 435, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 585, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_5.setFont(font)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 560, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_6.setFont(font)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 535, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_7.setFont(font)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 510, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_8.setFont(font)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(1)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 485, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_9.setFont(font)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(1)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(10, 460, 405, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.line_10.setFont(font)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(1)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.comboBox_anopcor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_anopcor.setGeometry(QtCore.QRect(266, 441, 148, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_anopcor.setFont(font)
        self.comboBox_anopcor.setAutoFillBackground(False)
        self.comboBox_anopcor.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.comboBox_anopcor.setObjectName("comboBox_anopcor")
        self.comboBox_anopcor.addItem("")
        self.comboBox_anopcor.addItem("")
        self.comboBox_anopcor.addItem("")
        self.comboBox_endetstab = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_endetstab.setGeometry(QtCore.QRect(266, 466, 148, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_endetstab.setFont(font)
        self.comboBox_endetstab.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.comboBox_endetstab.setObjectName("comboBox_endetstab")
        self.comboBox_endetstab.addItem("")
        self.comboBox_endetstab.addItem("")
        self.comboBox_endetstab.addItem("")
        self.comboBox_detenctempstab = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_detenctempstab.setGeometry(QtCore.QRect(266, 491, 148, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_detenctempstab.setFont(font)
        self.comboBox_detenctempstab.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.comboBox_detenctempstab.setObjectName("comboBox_detenctempstab")
        self.comboBox_detenctempstab.addItem("")
        self.comboBox_detenctempstab.addItem("")
        self.comboBox_detenctempstab.addItem("")
        self.comboBox_elecenctempstab = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_elecenctempstab.setGeometry(QtCore.QRect(266, 516, 148, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_elecenctempstab.setFont(font)
        self.comboBox_elecenctempstab.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.comboBox_elecenctempstab.setObjectName("comboBox_elecenctempstab")
        self.comboBox_elecenctempstab.addItem("")
        self.comboBox_elecenctempstab.addItem("")
        self.comboBox_elecenctempstab.addItem("")
        self.disp_stduptodate = QtWidgets.QLabel(self.centralwidget)
        self.disp_stduptodate.setGeometry(QtCore.QRect(266, 545, 148, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.disp_stduptodate.setFont(font)
        self.disp_stduptodate.setIndent(3)
        self.disp_stduptodate.setObjectName("disp_stduptodate")
        self.disp_endiskspc = QtWidgets.QLabel(self.centralwidget)
        self.disp_endiskspc.setGeometry(QtCore.QRect(266, 570, 148, 15))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.disp_endiskspc.setFont(font)
        self.disp_endiskspc.setIndent(3)
        self.disp_endiskspc.setObjectName("disp_endiskspc")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(395, 360, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(485, 360, 72, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(395, 380, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(485, 380, 72, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.ActionTakenTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ActionTakenTable.setGeometry(QtCore.QRect(0, 635, 800, 130))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.ActionTakenTable.setFont(font)
        self.ActionTakenTable.setFrameShape(QtWidgets.QFrame.Box)
        self.ActionTakenTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ActionTakenTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ActionTakenTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ActionTakenTable.setAlternatingRowColors(True)
        self.ActionTakenTable.setShowGrid(True)
        self.ActionTakenTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ActionTakenTable.setObjectName("ActionTakenTable")
        self.ActionTakenTable.setColumnCount(4)
        self.ActionTakenTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.ActionTakenTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionTakenTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionTakenTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionTakenTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionTakenTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.ActionTakenTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ActionTakenTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ActionTakenTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ActionTakenTable.setHorizontalHeaderItem(3, item)
        self.ActionTakenTable.horizontalHeader().setVisible(True)
        self.ActionTakenTable.horizontalHeader().setCascadingSectionResizes(False)
        self.ActionTakenTable.horizontalHeader().setDefaultSectionSize(110)
        self.ActionTakenTable.horizontalHeader().setMinimumSectionSize(25)
        self.ActionTakenTable.horizontalHeader().setStretchLastSection(True)
        self.ActionTakenTable.verticalHeader().setVisible(True)
        self.ActionTakenTable.verticalHeader().setDefaultSectionSize(20)
        self.label_ActionTaken = QtWidgets.QLabel(self.centralwidget)
        self.label_ActionTaken.setGeometry(QtCore.QRect(10, 605, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ActionTaken.setFont(font)
        self.label_ActionTaken.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_ActionTaken.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_ActionTaken.setLineWidth(1)
        self.label_ActionTaken.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ActionTaken.setIndent(0)
        self.label_ActionTaken.setObjectName("label_ActionTaken")
        self.ActionRequiredTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ActionRequiredTable.setGeometry(QtCore.QRect(0, 815, 800, 130))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.ActionRequiredTable.setFont(font)
        self.ActionRequiredTable.setFrameShape(QtWidgets.QFrame.Box)
        self.ActionRequiredTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ActionRequiredTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ActionRequiredTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ActionRequiredTable.setAlternatingRowColors(True)
        self.ActionRequiredTable.setShowGrid(True)
        self.ActionRequiredTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ActionRequiredTable.setObjectName("ActionRequiredTable")
        self.ActionRequiredTable.setColumnCount(3)
        self.ActionRequiredTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.ActionRequiredTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionRequiredTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionRequiredTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionRequiredTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ActionRequiredTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(180, 180, 180))
        self.ActionRequiredTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ActionRequiredTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ActionRequiredTable.setHorizontalHeaderItem(2, item)
        self.ActionRequiredTable.horizontalHeader().setVisible(True)
        self.ActionRequiredTable.horizontalHeader().setCascadingSectionResizes(False)
        self.ActionRequiredTable.horizontalHeader().setDefaultSectionSize(110)
        self.ActionRequiredTable.horizontalHeader().setStretchLastSection(True)
        self.ActionRequiredTable.verticalHeader().setVisible(True)
        self.ActionRequiredTable.verticalHeader().setDefaultSectionSize(20)
        self.label_ActionTaken_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ActionTaken_2.setGeometry(QtCore.QRect(10, 785, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_ActionTaken_2.setFont(font)
        self.label_ActionTaken_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_ActionTaken_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_ActionTaken_2.setLineWidth(1)
        self.label_ActionTaken_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ActionTaken_2.setIndent(0)
        self.label_ActionTaken_2.setObjectName("label_ActionTaken_2")
        self.NextPage = QtWidgets.QPushButton(self.centralwidget)
        self.NextPage.setGeometry(QtCore.QRect(680, 160, 75, 25))
        self.NextPage.setObjectName("NextPage")
        self.Regenerate = QtWidgets.QPushButton(self.centralwidget)
        self.Regenerate.setGeometry(QtCore.QRect(10, 160, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.Regenerate.setFont(font)
        self.Regenerate.setObjectName("Regenerate")
        PSAPage1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage1)
        self.statusbar.setObjectName("statusbar")
        PSAPage1.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage1)
        self.NextPage.released.connect(PSAPage1.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage1)

    def retranslateUi(self, PSAPage1):
        _translate = QtCore.QCoreApplication.translate
        PSAPage1.setWindowTitle(_translate("PSAPage1", "PSA Report Page 1"))
        self.psa_report_title.setText(_translate("PSAPage1", "PSA Report"))
        self.site_name.setText(_translate("PSAPage1", "site_name"))
        self.period.setText(_translate("PSAPage1", "Period Covered:"))
        self.email.setText(_translate("PSAPage1", "Email:"))
        self.next_psa_visit.setText(_translate("PSAPage1", "Next PSA Visit:"))
        self.src_topup_due.setText(_translate("PSAPage1", "Source Top-up due:"))
        self.period_data.setText(_translate("PSAPage1", "Period Covered:"))
        self.rep_serv_eng_data.setText(_translate("PSAPage1", "Service Engineer"))
        self.email_data.setText(_translate("PSAPage1", "Email:"))
        self.rep_analyser_data.setText(_translate("PSAPage1", "Analyser:"))
        self.rep_app_data.setText(_translate("PSAPage1", "Application"))
        self.rep_date_data.setText(_translate("PSAPage1", "Date:"))
        self.rep_date.setText(_translate("PSAPage1", "Date:"))
        self.rep_app.setText(_translate("PSAPage1", "Application:"))
        self.rep_analyser.setText(_translate("PSAPage1", "Analyser:"))
        self.rep_serv_eng.setText(_translate("PSAPage1", "Service Engineer:"))
        self.label_2.setText(_translate("PSAPage1", "Summary"))
        self.label_endiskspc.setText(_translate("PSAPage1", "Is there enough (>10%) disk space available?"))
        self.label_stduptodate.setText(_translate("PSAPage1", "Is the standardisation up to date?"))
        self.label_elecenctempstab.setText(_translate("PSAPage1", "Is the electronics enclosure temperature stable?"))
        self.label_detenctempstab.setText(_translate("PSAPage1", "Is the detector enclosure temperature stable? "))
        self.label_endetstab.setText(_translate("PSAPage1", "Are all enable detectors stable?"))
        self.label_anopcor.setText(_translate("PSAPage1", "Is the analayser operating correctly?"))
        self.comboBox_anopcor.setItemText(0, _translate("PSAPage1", "Yes"))
        self.comboBox_anopcor.setItemText(1, _translate("PSAPage1", "No"))
        self.comboBox_anopcor.setItemText(2, _translate("PSAPage1", "N/A"))
        self.comboBox_endetstab.setItemText(0, _translate("PSAPage1", "Yes"))
        self.comboBox_endetstab.setItemText(1, _translate("PSAPage1", "No"))
        self.comboBox_endetstab.setItemText(2, _translate("PSAPage1", "N/A"))
        self.comboBox_detenctempstab.setItemText(0, _translate("PSAPage1", "Yes"))
        self.comboBox_detenctempstab.setItemText(1, _translate("PSAPage1", "No"))
        self.comboBox_detenctempstab.setItemText(2, _translate("PSAPage1", "N/A"))
        self.comboBox_elecenctempstab.setItemText(0, _translate("PSAPage1", "Yes"))
        self.comboBox_elecenctempstab.setItemText(1, _translate("PSAPage1", "No"))
        self.comboBox_elecenctempstab.setItemText(2, _translate("PSAPage1", "N/A"))
        self.disp_stduptodate.setText(_translate("PSAPage1", "TextLabel"))
        self.disp_endiskspc.setText(_translate("PSAPage1", "TextLabel"))
        self.comboBox.setItemText(0, _translate("PSAPage1", "January"))
        self.comboBox.setItemText(1, _translate("PSAPage1", "February"))
        self.comboBox.setItemText(2, _translate("PSAPage1", "March"))
        self.comboBox.setItemText(3, _translate("PSAPage1", "April"))
        self.comboBox.setItemText(4, _translate("PSAPage1", "May"))
        self.comboBox.setItemText(5, _translate("PSAPage1", "June"))
        self.comboBox.setItemText(6, _translate("PSAPage1", "July"))
        self.comboBox.setItemText(7, _translate("PSAPage1", "August"))
        self.comboBox.setItemText(8, _translate("PSAPage1", "September"))
        self.comboBox.setItemText(9, _translate("PSAPage1", "October"))
        self.comboBox.setItemText(10, _translate("PSAPage1", "November"))
        self.comboBox.setItemText(11, _translate("PSAPage1", "December"))
        self.comboBox_2.setCurrentText(_translate("PSAPage1", "2022"))
        self.comboBox_2.setItemText(0, _translate("PSAPage1", "2022"))
        self.comboBox_2.setItemText(1, _translate("PSAPage1", "2023"))
        self.comboBox_2.setItemText(2, _translate("PSAPage1", "2024"))
        self.comboBox_2.setItemText(3, _translate("PSAPage1", "2025"))
        self.comboBox_2.setItemText(4, _translate("PSAPage1", "2025"))
        self.comboBox_2.setItemText(5, _translate("PSAPage1", "2026"))
        self.comboBox_2.setItemText(6, _translate("PSAPage1", "2027"))
        self.comboBox_2.setItemText(7, _translate("PSAPage1", "2028"))
        self.comboBox_3.setItemText(0, _translate("PSAPage1", "January"))
        self.comboBox_3.setItemText(1, _translate("PSAPage1", "February"))
        self.comboBox_3.setItemText(2, _translate("PSAPage1", "March"))
        self.comboBox_3.setItemText(3, _translate("PSAPage1", "April"))
        self.comboBox_3.setItemText(4, _translate("PSAPage1", "May"))
        self.comboBox_3.setItemText(5, _translate("PSAPage1", "June"))
        self.comboBox_3.setItemText(6, _translate("PSAPage1", "July"))
        self.comboBox_3.setItemText(7, _translate("PSAPage1", "August"))
        self.comboBox_3.setItemText(8, _translate("PSAPage1", "September"))
        self.comboBox_3.setItemText(9, _translate("PSAPage1", "October"))
        self.comboBox_3.setItemText(10, _translate("PSAPage1", "November"))
        self.comboBox_3.setItemText(11, _translate("PSAPage1", "December"))
        self.comboBox_4.setCurrentText(_translate("PSAPage1", "2022"))
        self.comboBox_4.setItemText(0, _translate("PSAPage1", "2022"))
        self.comboBox_4.setItemText(1, _translate("PSAPage1", "2023"))
        self.comboBox_4.setItemText(2, _translate("PSAPage1", "2024"))
        self.comboBox_4.setItemText(3, _translate("PSAPage1", "2025"))
        self.comboBox_4.setItemText(4, _translate("PSAPage1", "2025"))
        self.comboBox_4.setItemText(5, _translate("PSAPage1", "2026"))
        self.comboBox_4.setItemText(6, _translate("PSAPage1", "2027"))
        self.comboBox_4.setItemText(7, _translate("PSAPage1", "2028"))
        item = self.ActionTakenTable.verticalHeaderItem(0)
        item.setText(_translate("PSAPage1", "1"))
        item = self.ActionTakenTable.verticalHeaderItem(1)
        item.setText(_translate("PSAPage1", "2"))
        item = self.ActionTakenTable.verticalHeaderItem(2)
        item.setText(_translate("PSAPage1", "3"))
        item = self.ActionTakenTable.verticalHeaderItem(3)
        item.setText(_translate("PSAPage1", "4"))
        item = self.ActionTakenTable.verticalHeaderItem(4)
        item.setText(_translate("PSAPage1", "5"))
        item = self.ActionTakenTable.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage1", "Date"))
        item = self.ActionTakenTable.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage1", "Time"))
        item = self.ActionTakenTable.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage1", "Action"))
        item = self.ActionTakenTable.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage1", "Description"))
        self.label_ActionTaken.setText(_translate("PSAPage1", "Action Taken"))
        item = self.ActionRequiredTable.verticalHeaderItem(0)
        item.setText(_translate("PSAPage1", "1"))
        item = self.ActionRequiredTable.verticalHeaderItem(1)
        item.setText(_translate("PSAPage1", "2"))
        item = self.ActionRequiredTable.verticalHeaderItem(2)
        item.setText(_translate("PSAPage1", "3"))
        item = self.ActionRequiredTable.verticalHeaderItem(3)
        item.setText(_translate("PSAPage1", "4"))
        item = self.ActionRequiredTable.verticalHeaderItem(4)
        item.setText(_translate("PSAPage1", "5"))
        item = self.ActionRequiredTable.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage1", "By Whom"))
        item = self.ActionRequiredTable.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage1", "By When"))
        item = self.ActionRequiredTable.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage1", "Action"))
        self.label_ActionTaken_2.setText(_translate("PSAPage1", "Action Required"))
        self.NextPage.setText(_translate("PSAPage1", "Close"))
        self.Regenerate.setText(_translate("PSAPage1", "Regenerate Report"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage1 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage1()
    ui.setupUi(PSAPage1)
    PSAPage1.show()
    sys.exit(app.exec_())
