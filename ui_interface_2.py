# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_2LHtSOv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 766)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none; \n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	paddiing:0;\n"
"	margin: 0;\n"
"	color:rgb(255, 255, 255);\n"
"	text-color:rgb(244, 244, 244);\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(8, 8, 8);\n"
"}\n"
"\n"
"#header{\n"
"\n"
"	background-color: #ffc4b5;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"#mainbody{\n"
"\n"
"	background-color:#ffc4b5;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#accountbtn{\n"
"\n"
"	border: 2px solid rgb(1, 4, 8);\n"
"	border-radius:17px\n"
"}\n"
"\n"
"#leftmenu, #rightmenu{\n"
"\n"
" 	background-color: #818181;\n"
"\n"
"}\n"
"#comboSort{\n"
"	text-align:center;\n"
"	background-color: #62918f;\n"
"	border-left-radius: 12px;\n"
"	border-right-radius:12px;\n"
"	border: 2px solid #ffffe9;\n"
"	border-top-left-radius: 10px  ; \n"
"	border-bottom-left-radius: 10px ;\n"
"}\n"
"QPushButton{\n"
"\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px  ; \n"
"	border-bottom-left-radius: 10px ;\n"
"	color"
                        ": rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(103, 103, 103);\n"
"	padd ing: 3px 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(103, 103, 103);\n"
"	padd ing: 3px 5px;\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"#homebtn{\n"
"\n"
"	border-left: 2px solid rgb(138, 25, 15);\n"
"	font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet(
"	background-color: #48523D;\n"
"	color: rgb(255, 255, 255)\n")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.selectbtn = QPushButton(self.frame)
        self.selectbtn.setObjectName(u"selectbtn")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.selectbtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.selectbtn.setIcon(icon)
        self.selectbtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.selectbtn)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchbtn = QPushButton(self.frame_2)
        self.searchbtn.setObjectName(u"searchbtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbtn.setIcon(icon1)
        self.searchbtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.searchbtn)

        self.search = QLineEdit(self.frame_2)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 32))
        font1 = QFont()
        font1.setFamily(u"Myanmar Text")
        font1.setPointSize(11)
        self.search.setFont(font1)
        self.search.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.search)

        self.accountbtn = QPushButton(self.frame_2)
        self.accountbtn.setObjectName(u"accountbtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountbtn.setIcon(icon2)
        self.accountbtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.accountbtn, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        sizePolicy.setHeightForWidth(self.mainbody.sizePolicy().hasHeightForWidth())
        self.mainbody.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.mainbody)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QCustomSlideMenu(self.mainbody)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMinimumSize(QSize(150, 0))
        self.leftmenu.setStyleSheet(u"QPushButton{\n"
"\n"
"	text-align: left;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.leftmenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.homebtn = QPushButton(self.frame_3)
        self.homebtn.setObjectName(u"homebtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homebtn.setIcon(icon3)
        self.homebtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homebtn)

        self.completedbtn = QPushButton(self.frame_3)
        self.completedbtn.setObjectName(u"completedbtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.completedbtn.setIcon(icon4)
        self.completedbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.completedbtn)

        self.calendarbtn = QPushButton(self.frame_3)
        self.calendarbtn.setObjectName(u"calendarbtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendarbtn.setIcon(icon5)
        self.calendarbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.calendarbtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.leftmenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingsbtn = QPushButton(self.frame_4)
        self.settingsbtn.setObjectName(u"settingsbtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsbtn.setIcon(icon6)
        self.settingsbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsbtn)

        self.helpbtn = QPushButton(self.frame_4)
        self.helpbtn.setObjectName(u"helpbtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpbtn.setIcon(icon7)
        self.helpbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpbtn)

        self.aboutbtn = QPushButton(self.frame_4)
        self.aboutbtn.setObjectName(u"aboutbtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutbtn.setIcon(icon8)
        self.aboutbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aboutbtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.leftmenu, 0, Qt.AlignLeft)

        self.mainmenu = QWidget(self.mainbody)
        self.mainmenu.setObjectName(u"mainmenu")
        sizePolicy.setHeightForWidth(self.mainmenu.sizePolicy().hasHeightForWidth())
        self.mainmenu.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.mainmenu)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mstackedWidget = QCustomStackedWidget(self.mainmenu)
        self.mstackedWidget.setObjectName(u"mstackedWidget")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_6 = QVBoxLayout(self.homepage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.homepage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	text-align:center;\n"
"	background-color: #62918f;\n"
"	border-left-radius: 12px;\n"
"	border-right-radius:12px;\n"
"	border: 2px solid #ffffe9;\n"
"\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.sorttaskbtn = QPushButton(self.frame_5)
        self.sorttaskbtn.setObjectName(u"sorttaskbtn")
        self.sorttaskbtn.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setFamily(u"Myanmar Text")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.sorttaskbtn.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sorttaskbtn.setIcon(icon9)
        self.sorttaskbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.sorttaskbtn)

        self.deletetaskbtn = QPushButton(self.frame_5)
        self.deletetaskbtn.setObjectName(u"deletetaskbtn")
        self.deletetaskbtn.setMaximumSize(QSize(150, 16777215))
        self.deletetaskbtn.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deletetaskbtn.setIcon(icon10)
        self.deletetaskbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.deletetaskbtn)

        self.addtaskdetailbtn = QPushButton(self.frame_5)
        self.addtaskdetailbtn.setObjectName(u"addtaskdetailbtn")
        self.addtaskdetailbtn.setMaximumSize(QSize(150, 16777215))
        self.addtaskdetailbtn.setFont(font3)
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addtaskdetailbtn.setIcon(icon11)
        self.addtaskdetailbtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.addtaskdetailbtn)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(70, 90, 6));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(70, 90, 6));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(70, 90, 6));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(70, 90, 6));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setInputMethodHints(Qt.ImhNone)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.widget)

        self.mstackedWidget.addWidget(self.homepage)
        self.aboutpage = QWidget()
        self.aboutpage.setObjectName(u"aboutpage")
        self.label_6 = QLabel(self.aboutpage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 190, 47, 13))
        self.mstackedWidget.addWidget(self.aboutpage)
        self.helppage = QWidget()
        self.helppage.setObjectName(u"helppage")
        self.label_5 = QLabel(self.helppage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 180, 47, 13))
        self.mstackedWidget.addWidget(self.helppage)
        self.calendarpage = QWidget()
        self.calendarpage.setObjectName(u"calendarpage")
        self.calendarpage.setStyleSheet(u"#calendarpage{\n"
"\n"
"	background-color: #9ac1ed;\n"
"	color: #9fa2a6;\n"
"	text-color: #edeef0;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.calendarpage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.calendarWidget = QCalendarWidget(self.calendarpage)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setStyleStrategy(QFont.PreferDefault)
        self.calendarWidget.setFont(font4)
        self.calendarWidget.setFocusPolicy(Qt.StrongFocus)
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setStyleSheet(u"#calendarWidget{\n"
"\n"
"	background-color: #9ac1ed;\n"
"	color: #9fa2a6;\n"
"	text-color: #edeef0;\n"
"}")
        self.calendarWidget.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhEmailCharactersOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhHiddenText|Qt.ImhLatinOnly|Qt.ImhLowercaseOnly|Qt.ImhNoTextHandles|Qt.ImhSensitiveData|Qt.ImhUppercaseOnly|Qt.ImhUrlCharactersOnly)
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setDateEditAcceptDelay(1500)

        self.horizontalLayout_9.addWidget(self.calendarWidget)

        self.mstackedWidget.addWidget(self.calendarpage)
        self.completedpage = QWidget()
        self.completedpage.setObjectName(u"completedpage")
        self.verticalLayout_8 = QVBoxLayout(self.completedpage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.completedpage)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Completed = QLabel(self.frame_8)
        self.Completed.setObjectName(u"Completed")
        font5 = QFont()
        font5.setFamily(u"Myanmar Text")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(True)
        font5.setWeight(75)
        self.Completed.setFont(font5)

        self.horizontalLayout_8.addWidget(self.Completed)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget_2 = QTableWidget(self.frame_7)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_7.addWidget(self.tableWidget_2)


        self.verticalLayout_9.addWidget(self.frame_7)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.mstackedWidget.addWidget(self.completedpage)
        self.settinpage = QWidget()
        self.settinpage.setObjectName(u"settinpage")
        self.label_7 = QLabel(self.settinpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 190, 47, 13))
        self.mstackedWidget.addWidget(self.settinpage)

        self.horizontalLayout_5.addWidget(self.mstackedWidget)


        self.horizontalLayout_3.addWidget(self.mainmenu)

        self.rightmenu = QCustomSlideMenu(self.mainbody)
        self.rightmenu.setObjectName(u"rightmenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rightmenu.sizePolicy().hasHeightForWidth())
        self.rightmenu.setSizePolicy(sizePolicy1)
        self.rightmenu.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(255, 148, 148);\n"
"	border: 2px solid rgb(6, 251, 255);\n"
"	border-right-radius: 19px;\n"
"	border-left-radius: 19px;\n"
"}\n"
"\n"
"#addtask, #deletetask, #sorttask{\n"
"\n"
"	background-color: rgb(255, 148, 148);\n"
"	border: 2px solid rgb(6, 251, 255);\n"
"	border-right-radius: 19px;\n"
"	border-left-radius: 19px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.rightmenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.rightmenu)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(53, 53))
        self.label.setBaseSize(QSize(49, 49))
        font6 = QFont()
        font6.setPointSize(8)
        self.label.setFont(font6)
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setPixmap(QPixmap(u":/icons/Icons/edit.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.taskname = QLineEdit(self.rightmenu)
        self.taskname.setObjectName(u"taskname")
        self.taskname.setMinimumSize(QSize(0, 32))
        font7 = QFont()
        font7.setPointSize(10)
        self.taskname.setFont(font7)
        self.taskname.setMaxLength(32767)
        self.taskname.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.taskname)

        self.description = QLineEdit(self.rightmenu)
        self.description.setObjectName(u"description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy2)
        self.description.setMinimumSize(QSize(0, 32))
        self.description.setFont(font7)
        self.description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.description)

        self.dateEdit = QDateEdit(self.rightmenu)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy1.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy1)
        self.dateEdit.setMinimumSize(QSize(122, 33))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(False)
        font8.setWeight(50)
        self.dateEdit.setFont(font8)
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setDateTime(QDateTime(QDate(2000, 3, 1), QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit.setDisplayFormat(u"M/d/yyyy")

        self.verticalLayout_5.addWidget(self.dateEdit, 0, Qt.AlignHCenter)

        self.importance = QCheckBox(self.rightmenu)
        self.importance.setObjectName(u"importance")
        self.importance.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.importance.sizePolicy().hasHeightForWidth())
        self.importance.setSizePolicy(sizePolicy3)
        self.importance.setMinimumSize(QSize(24, 24))
        self.importance.setBaseSize(QSize(10, 10))
        font9 = QFont()
        font9.setPointSize(8)
        font9.setBold(True)
        font9.setWeight(75)
        self.importance.setFont(font9)
        self.importance.setCursor(QCursor(Qt.PointingHandCursor))
        self.importance.setMouseTracking(True)
        self.importance.setFocusPolicy(Qt.StrongFocus)
        self.importance.setAcceptDrops(True)
        self.importance.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importance.setIcon(icon12)
        self.importance.setIconSize(QSize(24, 25))
        self.importance.setChecked(False)
        self.importance.setAutoRepeat(False)
        self.importance.setAutoExclusive(False)
        self.importance.setAutoRepeatDelay(300)
        self.importance.setTristate(False)

        self.verticalLayout_5.addWidget(self.importance)

        self.addtask = QPushButton(self.rightmenu)
        self.addtask.setObjectName(u"addtask")
        self.addtask.setMinimumSize(QSize(120, 0))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.addtask.setFont(font10)
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addtask.setIcon(icon13)
        self.addtask.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.addtask, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.rightmenu, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mstackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectbtn.setText(QCoreApplication.translate("MainWindow", u"My APP", None))
        self.searchbtn.setText("")
        self.search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task ", None))
        self.accountbtn.setText("")
        self.homebtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.completedbtn.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.calendarbtn.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.settingsbtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpbtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutbtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TodoList", None))
        self.sorttaskbtn.setText(QCoreApplication.translate("MainWindow", u"Sort Task", None))
        self.deletetaskbtn.setText(QCoreApplication.translate("MainWindow", u"Delete Task ", None))
        self.addtaskdetailbtn.setText(QCoreApplication.translate("MainWindow", u"Add Task Detail", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Task Name ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Deadline", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Importance", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"aboutpage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"helpage", None))
        self.Completed.setText(QCoreApplication.translate("MainWindow", u"Completed Task", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Deadline", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Important", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"setting page", None))
        self.label.setText("")
        self.taskname.setText("")
        self.taskname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.description.setText("")
        self.description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
#if QT_CONFIG(accessibility)
        self.importance.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.importance.setText(QCoreApplication.translate("MainWindow", u"Importance", None))
        self.addtask.setText(QCoreApplication.translate("MainWindow", u"Add Task ", None))
    # retranslateUi

