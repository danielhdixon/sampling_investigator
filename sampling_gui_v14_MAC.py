# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sampling_app_v14_MAC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Sampling_Investigator(object):
    def setupUi(self, Sampling_Investigator):
        if not Sampling_Investigator.objectName():
            Sampling_Investigator.setObjectName(u"Sampling_Investigator")
        Sampling_Investigator.resize(900, 850)
        Sampling_Investigator.setMinimumSize(QSize(0, 850))
        font = QFont()
        font.setFamilies([u"Arial"])
        Sampling_Investigator.setFont(font)
        Sampling_Investigator.setStyleSheet(u"background-color: rgb(119, 136, 152);\n"
"")
        self.centralwidget = QWidget(Sampling_Investigator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
#ifndef Q_OS_MAC
        self.verticalLayout_8.setSpacing(-1)
#endif
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(21)
        font1.setBold(True)
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(13)
        self.tabWidget.setFont(font2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 0))
        self.verticalLayout_18 = QVBoxLayout(self.tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: white;")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_3)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.frame_2.setFont(font4)
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(3, 3, 3, 3)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_4)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_15)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setBold(False)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_31.addWidget(self.label_6)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_23)


        self.verticalLayout_24.addLayout(self.horizontalLayout_31)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(12)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_92 = QLabel(self.frame_2)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font7)
        self.label_92.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_4.addWidget(self.label_92)

        self.label_94 = QLabel(self.frame_2)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font7)
        self.label_94.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_4.addWidget(self.label_94)


        self.verticalLayout_24.addLayout(self.verticalLayout_4)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.label_116 = QLabel(self.frame_3)
        self.label_116.setObjectName(u"label_116")
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_116.setFont(font8)
        self.label_116.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_116.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_116)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_117 = QLabel(self.frame_4)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font7)
        self.label_117.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_117.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_4)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font7)
        self.label_118.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_118.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_118)

        self.label_119 = QLabel(self.frame_4)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font7)
        self.label_119.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_119.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_119)


        self.verticalLayout_10.addLayout(self.horizontalLayout_36)

        self.line_19 = QFrame(self.frame_4)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_19)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.radioButton_tcrit_80 = QRadioButton(self.frame_4)
        self.radioButton_tcrit_80.setObjectName(u"radioButton_tcrit_80")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_80.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_80.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_80.setFont(font7)
        self.radioButton_tcrit_80.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.radioButton_tcrit_80)

        self.label_122 = QLabel(self.frame_4)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font7)
        self.label_122.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_39.addWidget(self.label_122)

        self.label_121 = QLabel(self.frame_4)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font7)
        self.label_121.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_39.addWidget(self.label_121)

        self.label_125 = QLabel(self.frame_4)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font7)
        self.label_125.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_39.addWidget(self.label_125)


        self.verticalLayout_10.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.radioButton_tcrit_90 = QRadioButton(self.frame_4)
        self.radioButton_tcrit_90.setObjectName(u"radioButton_tcrit_90")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_90.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_90.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_90.setFont(font7)
        self.radioButton_tcrit_90.setStyleSheet(u"")
        self.radioButton_tcrit_90.setChecked(False)

        self.horizontalLayout_40.addWidget(self.radioButton_tcrit_90)

        self.label_129 = QLabel(self.frame_4)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font7)
        self.label_129.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_40.addWidget(self.label_129)

        self.label_133 = QLabel(self.frame_4)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font7)
        self.label_133.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_40.addWidget(self.label_133)

        self.label_137 = QLabel(self.frame_4)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font7)
        self.label_137.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_40.addWidget(self.label_137)


        self.verticalLayout_10.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.radioButton_tcrit_95 = QRadioButton(self.frame_4)
        self.radioButton_tcrit_95.setObjectName(u"radioButton_tcrit_95")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_95.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_95.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_95.setFont(font7)
        self.radioButton_tcrit_95.setStyleSheet(u"")
        self.radioButton_tcrit_95.setChecked(True)

        self.horizontalLayout_41.addWidget(self.radioButton_tcrit_95)

        self.label_141 = QLabel(self.frame_4)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font7)
        self.label_141.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_41.addWidget(self.label_141)

        self.label_145 = QLabel(self.frame_4)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font7)
        self.label_145.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_41.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_4)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font7)
        self.label_146.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_41.addWidget(self.label_146)


        self.verticalLayout_10.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.radioButton_tcrit_98 = QRadioButton(self.frame_4)
        self.radioButton_tcrit_98.setObjectName(u"radioButton_tcrit_98")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_98.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_98.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_98.setFont(font7)
        self.radioButton_tcrit_98.setStyleSheet(u"")
        self.radioButton_tcrit_98.setChecked(False)

        self.horizontalLayout_42.addWidget(self.radioButton_tcrit_98)

        self.label_147 = QLabel(self.frame_4)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font7)
        self.label_147.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_42.addWidget(self.label_147)

        self.label_148 = QLabel(self.frame_4)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font7)
        self.label_148.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_42.addWidget(self.label_148)

        self.label_149 = QLabel(self.frame_4)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font7)
        self.label_149.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_42.addWidget(self.label_149)


        self.verticalLayout_10.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.radioButton_tcrit_99 = QRadioButton(self.frame_4)
        self.radioButton_tcrit_99.setObjectName(u"radioButton_tcrit_99")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_99.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_99.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_99.setFont(font7)
        self.radioButton_tcrit_99.setStyleSheet(u"")
        self.radioButton_tcrit_99.setChecked(False)

        self.horizontalLayout_43.addWidget(self.radioButton_tcrit_99)

        self.label_150 = QLabel(self.frame_4)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font7)
        self.label_150.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_43.addWidget(self.label_150)

        self.label_151 = QLabel(self.frame_4)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font7)
        self.label_151.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_43.addWidget(self.label_151)

        self.label_152 = QLabel(self.frame_4)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font7)
        self.label_152.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_43.addWidget(self.label_152)


        self.verticalLayout_10.addLayout(self.horizontalLayout_43)


        self.verticalLayout_25.addWidget(self.frame_4)


        self.verticalLayout_15.addWidget(self.frame_3)

        self.frame_17 = QFrame(self.tab)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFont(font7)
        self.frame_17.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_17.setFrameShape(QFrame.WinPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_45 = QLabel(self.frame_17)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font8)
        self.label_45.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_45)

        self.label_93 = QLabel(self.frame_17)
        self.label_93.setObjectName(u"label_93")
        font9 = QFont()
        font9.setPointSize(12)
        self.label_93.setFont(font9)
        self.label_93.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_93.setAlignment(Qt.AlignCenter)
        self.label_93.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_93)

        self.frame_6 = QFrame(self.frame_17)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_17 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.label_46 = QLabel(self.frame_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font7)
        self.label_46.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_6)
        self.label_47.setObjectName(u"label_47")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(12)
        font10.setItalic(True)
        self.label_47.setFont(font10)
        self.label_47.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font7)
        self.label_48.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_48)


        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.line_13 = QFrame(self.frame_6)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_13)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.radioButton_n_10 = QRadioButton(self.frame_6)
        self.radioButton_n_10.setObjectName(u"radioButton_n_10")
        sizePolicy1.setHeightForWidth(self.radioButton_n_10.sizePolicy().hasHeightForWidth())
        self.radioButton_n_10.setSizePolicy(sizePolicy1)
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(11)
        self.radioButton_n_10.setFont(font11)
        self.radioButton_n_10.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.radioButton_n_10)

        self.label_et_11 = QLabel(self.frame_6)
        self.label_et_11.setObjectName(u"label_et_11")
        self.label_et_11.setFont(font7)
        self.label_et_11.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_27.addWidget(self.label_et_11)

        self.label_t_11 = QLabel(self.frame_6)
        self.label_t_11.setObjectName(u"label_t_11")
        self.label_t_11.setFont(font7)
        self.label_t_11.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_27.addWidget(self.label_t_11)

        self.label_RSEcrit_11 = QLabel(self.frame_6)
        self.label_RSEcrit_11.setObjectName(u"label_RSEcrit_11")
        self.label_RSEcrit_11.setFont(font7)
        self.label_RSEcrit_11.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_27.addWidget(self.label_RSEcrit_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.radioButton_n_05 = QRadioButton(self.frame_6)
        self.radioButton_n_05.setObjectName(u"radioButton_n_05")
        sizePolicy1.setHeightForWidth(self.radioButton_n_05.sizePolicy().hasHeightForWidth())
        self.radioButton_n_05.setSizePolicy(sizePolicy1)
        self.radioButton_n_05.setFont(font11)
        self.radioButton_n_05.setStyleSheet(u"")
        self.radioButton_n_05.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radioButton_n_05)

        self.label_et_8 = QLabel(self.frame_6)
        self.label_et_8.setObjectName(u"label_et_8")
        self.label_et_8.setFont(font7)
        self.label_et_8.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_28.addWidget(self.label_et_8)

        self.label_t_6 = QLabel(self.frame_6)
        self.label_t_6.setObjectName(u"label_t_6")
        self.label_t_6.setFont(font7)
        self.label_t_6.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_28.addWidget(self.label_t_6)

        self.label_RSEcrit_6 = QLabel(self.frame_6)
        self.label_RSEcrit_6.setObjectName(u"label_RSEcrit_6")
        self.label_RSEcrit_6.setFont(font7)
        self.label_RSEcrit_6.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_28.addWidget(self.label_RSEcrit_6)


        self.verticalLayout_16.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.radioButton_n_01 = QRadioButton(self.frame_6)
        self.radioButton_n_01.setObjectName(u"radioButton_n_01")
        sizePolicy1.setHeightForWidth(self.radioButton_n_01.sizePolicy().hasHeightForWidth())
        self.radioButton_n_01.setSizePolicy(sizePolicy1)
        self.radioButton_n_01.setFont(font11)
        self.radioButton_n_01.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.radioButton_n_01)

        self.label_et_3 = QLabel(self.frame_6)
        self.label_et_3.setObjectName(u"label_et_3")
        self.label_et_3.setFont(font7)
        self.label_et_3.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_29.addWidget(self.label_et_3)

        self.label_t_4 = QLabel(self.frame_6)
        self.label_t_4.setObjectName(u"label_t_4")
        self.label_t_4.setFont(font7)
        self.label_t_4.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_29.addWidget(self.label_t_4)

        self.label_RSEcrit_2 = QLabel(self.frame_6)
        self.label_RSEcrit_2.setObjectName(u"label_RSEcrit_2")
        self.label_RSEcrit_2.setFont(font7)
        self.label_RSEcrit_2.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_29.addWidget(self.label_RSEcrit_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.radioButton_n_005 = QRadioButton(self.frame_6)
        self.radioButton_n_005.setObjectName(u"radioButton_n_005")
        sizePolicy1.setHeightForWidth(self.radioButton_n_005.sizePolicy().hasHeightForWidth())
        self.radioButton_n_005.setSizePolicy(sizePolicy1)
        self.radioButton_n_005.setFont(font11)
        self.radioButton_n_005.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.radioButton_n_005)

        self.label_et_9 = QLabel(self.frame_6)
        self.label_et_9.setObjectName(u"label_et_9")
        self.label_et_9.setFont(font7)
        self.label_et_9.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_34.addWidget(self.label_et_9)

        self.label_t_7 = QLabel(self.frame_6)
        self.label_t_7.setObjectName(u"label_t_7")
        self.label_t_7.setFont(font7)
        self.label_t_7.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_34.addWidget(self.label_t_7)

        self.label_RSEcrit_7 = QLabel(self.frame_6)
        self.label_RSEcrit_7.setObjectName(u"label_RSEcrit_7")
        self.label_RSEcrit_7.setFont(font7)
        self.label_RSEcrit_7.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_34.addWidget(self.label_RSEcrit_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.radioButton_n_001 = QRadioButton(self.frame_6)
        self.radioButton_n_001.setObjectName(u"radioButton_n_001")
        sizePolicy1.setHeightForWidth(self.radioButton_n_001.sizePolicy().hasHeightForWidth())
        self.radioButton_n_001.setSizePolicy(sizePolicy1)
        self.radioButton_n_001.setFont(font11)
        self.radioButton_n_001.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.radioButton_n_001)

        self.label_et_4 = QLabel(self.frame_6)
        self.label_et_4.setObjectName(u"label_et_4")
        self.label_et_4.setFont(font7)
        self.label_et_4.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_35.addWidget(self.label_et_4)

        self.label_t_5 = QLabel(self.frame_6)
        self.label_t_5.setObjectName(u"label_t_5")
        self.label_t_5.setFont(font7)
        self.label_t_5.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_35.addWidget(self.label_t_5)

        self.label_RSEcrit_3 = QLabel(self.frame_6)
        self.label_RSEcrit_3.setObjectName(u"label_RSEcrit_3")
        self.label_RSEcrit_3.setFont(font7)
        self.label_RSEcrit_3.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_35.addWidget(self.label_RSEcrit_3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_35)


        self.verticalLayout_11.addWidget(self.frame_6)


        self.verticalLayout_15.addWidget(self.frame_17)


        self.horizontalLayout_37.addLayout(self.verticalLayout_15)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalFrame_5 = QFrame(self.tab)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.verticalFrame_5.setFrameShape(QFrame.Panel)
        self.verticalFrame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_98 = QLabel(self.verticalFrame_5)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font8)
        self.label_98.setStyleSheet(u"background-color: transparent;")
        self.label_98.setAlignment(Qt.AlignCenter)
        self.label_98.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_98)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_et_6 = QLabel(self.verticalFrame_5)
        self.label_et_6.setObjectName(u"label_et_6")
        self.label_et_6.setFont(font8)
        self.label_et_6.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_44.addWidget(self.label_et_6)

        self.lineEdit_pilot_mean = QLineEdit(self.verticalFrame_5)
        self.lineEdit_pilot_mean.setObjectName(u"lineEdit_pilot_mean")
        self.lineEdit_pilot_mean.setFont(font7)
        self.lineEdit_pilot_mean.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_44.addWidget(self.lineEdit_pilot_mean)


        self.verticalLayout_9.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_et_7 = QLabel(self.verticalFrame_5)
        self.label_et_7.setObjectName(u"label_et_7")
        self.label_et_7.setFont(font8)
        self.label_et_7.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_46.addWidget(self.label_et_7)

        self.lineEdit_pilot_standard_deviation = QLineEdit(self.verticalFrame_5)
        self.lineEdit_pilot_standard_deviation.setObjectName(u"lineEdit_pilot_standard_deviation")
        self.lineEdit_pilot_standard_deviation.setFont(font7)
        self.lineEdit_pilot_standard_deviation.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_46.addWidget(self.lineEdit_pilot_standard_deviation)


        self.verticalLayout_9.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.pushButton = QPushButton(self.verticalFrame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(62, 123, 252);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QPushButton:pressed {\n"
"color: black;    \n"
"border-style: inset;\n"
"    \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"")

        self.horizontalLayout_45.addWidget(self.pushButton)

        self.label_result_stdev_squared_3 = QLabel(self.verticalFrame_5)
        self.label_result_stdev_squared_3.setObjectName(u"label_result_stdev_squared_3")
        self.label_result_stdev_squared_3.setFont(font8)
        self.label_result_stdev_squared_3.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_45.addWidget(self.label_result_stdev_squared_3)

        self.label_result_required_n_2 = QLabel(self.verticalFrame_5)
        self.label_result_required_n_2.setObjectName(u"label_result_required_n_2")
        font12 = QFont()
        font12.setFamilies([u"Arial"])
        font12.setPointSize(14)
        font12.setBold(True)
        self.label_result_required_n_2.setFont(font12)
        self.label_result_required_n_2.setStyleSheet(u"color: blue; background-color: transparent;")

        self.horizontalLayout_45.addWidget(self.label_result_required_n_2)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_24)


        self.verticalLayout_9.addLayout(self.horizontalLayout_45)

        self.line = QFrame(self.verticalFrame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.verticalFrame_5)

        self.verticalFrame_3 = QFrame(self.tab)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.verticalFrame_3.setFrameShape(QFrame.Panel)
        self.verticalFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.label_99 = QLabel(self.verticalFrame_3)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(16777215, 20))
        self.label_99.setFont(font8)
        self.label_99.setStyleSheet(u"background-color: transparent;")
        self.label_99.setAlignment(Qt.AlignCenter)
        self.label_99.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_99)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.label_1 = QLabel(self.verticalFrame_3)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font9)
        self.label_1.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_1)

        self.label_mean = QLabel(self.verticalFrame_3)
        self.label_mean.setObjectName(u"label_mean")
        self.label_mean.setFont(font9)
        self.label_mean.setStyleSheet(u"color: blue; background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_mean)

        self.label_9 = QLabel(self.verticalFrame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalFrame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.verticalFrame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_11)

        self.label_et = QLabel(self.verticalFrame_3)
        self.label_et.setObjectName(u"label_et")
        self.label_et.setFont(font9)
        self.label_et.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_et)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label_et_2 = QLabel(self.verticalFrame_3)
        self.label_et_2.setObjectName(u"label_et_2")
        self.label_et_2.setFont(font9)
        self.label_et_2.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label_et_2)

        self.label_12 = QLabel(self.verticalFrame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.label_t = QLabel(self.verticalFrame_3)
        self.label_t.setObjectName(u"label_t")
        self.label_t.setFont(font9)
        self.label_t.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label_t)

        self.label_t_2 = QLabel(self.verticalFrame_3)
        self.label_t_2.setObjectName(u"label_t_2")
        self.label_t_2.setFont(font9)
        self.label_t_2.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label_t_2)

        self.label_result_et_t = QLabel(self.verticalFrame_3)
        self.label_result_et_t.setObjectName(u"label_result_et_t")
        self.label_result_et_t.setFont(font9)
        self.label_result_et_t.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label_result_et_t)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_result_et_t_2 = QLabel(self.verticalFrame_3)
        self.label_result_et_t_2.setObjectName(u"label_result_et_t_2")
        self.label_result_et_t_2.setFont(font9)
        self.label_result_et_t_2.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.label_result_et_t_2)

        self.label_result_et_t_squared = QLabel(self.verticalFrame_3)
        self.label_result_et_t_squared.setObjectName(u"label_result_et_t_squared")
        self.label_result_et_t_squared.setFont(font9)
        self.label_result_et_t_squared.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.label_result_et_t_squared)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)


        self.verticalLayout_21.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(3, 3, 3, 3)
        self.label_std_dev = QLabel(self.verticalFrame_3)
        self.label_std_dev.setObjectName(u"label_std_dev")
        self.label_std_dev.setFont(font9)
        self.label_std_dev.setStyleSheet(u"color: blue; background-color: transparent;")

        self.horizontalLayout_47.addWidget(self.label_std_dev)

        self.label_result_3 = QLabel(self.verticalFrame_3)
        self.label_result_3.setObjectName(u"label_result_3")
        self.label_result_3.setFont(font9)
        self.label_result_3.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_47.addWidget(self.label_result_3)

        self.label_result_stdev_squared = QLabel(self.verticalFrame_3)
        self.label_result_stdev_squared.setObjectName(u"label_result_stdev_squared")
        self.label_result_stdev_squared.setFont(font9)
        self.label_result_stdev_squared.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_47.addWidget(self.label_result_stdev_squared)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_18)


        self.verticalLayout_21.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(3, 3, 3, 3)
        self.label_result_stdev_squared_2 = QLabel(self.verticalFrame_3)
        self.label_result_stdev_squared_2.setObjectName(u"label_result_stdev_squared_2")
        self.label_result_stdev_squared_2.setFont(font9)
        self.label_result_stdev_squared_2.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_48.addWidget(self.label_result_stdev_squared_2)

        self.label_result_4 = QLabel(self.verticalFrame_3)
        self.label_result_4.setObjectName(u"label_result_4")
        self.label_result_4.setFont(font9)
        self.label_result_4.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_48.addWidget(self.label_result_4)

        self.label_result_et_t_squared_2 = QLabel(self.verticalFrame_3)
        self.label_result_et_t_squared_2.setObjectName(u"label_result_et_t_squared_2")
        self.label_result_et_t_squared_2.setFont(font9)
        self.label_result_et_t_squared_2.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_48.addWidget(self.label_result_et_t_squared_2)

        self.label_t_3 = QLabel(self.verticalFrame_3)
        self.label_t_3.setObjectName(u"label_t_3")
        self.label_t_3.setFont(font9)
        self.label_t_3.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_48.addWidget(self.label_t_3)

        self.label_result_required_n = QLabel(self.verticalFrame_3)
        self.label_result_required_n.setObjectName(u"label_result_required_n")
        self.label_result_required_n.setFont(font9)
        self.label_result_required_n.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_48.addWidget(self.label_result_required_n)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_48)


        self.verticalLayout_19.addLayout(self.verticalLayout_21)


        self.verticalLayout_2.addWidget(self.verticalFrame_3)


        self.horizontalLayout_37.addLayout(self.verticalLayout_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_37)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_20 = QVBoxLayout(self.tab_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_1 = QFrame(self.tab_2)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(0, 175))
        font13 = QFont()
        font13.setPointSize(4)
        self.frame_1.setFont(font13)
        self.frame_1.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_1.setFrameShape(QFrame.WinPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_64 = QLabel(self.frame_1)
        self.label_64.setObjectName(u"label_64")
        sizePolicy.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)
        self.label_64.setFont(font8)
        self.label_64.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_64)

        self.line_5 = QFrame(self.frame_1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.frame_7 = QFrame(self.frame_1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27.setSpacing(3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.label_66 = QLabel(self.frame_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font7)
        self.label_66.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_66.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_66)

        self.horizontalSpacer_8 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.label_70 = QLabel(self.frame_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font7)
        self.label_70.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_70)

        self.horizontalSpacer_7 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.label_71 = QLabel(self.frame_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 0))
        self.label_71.setFont(font7)
        self.label_71.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_71)


        self.verticalLayout_27.addLayout(self.horizontalLayout_11)

        self.line_11 = QFrame(self.frame_7)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_tcrit_10 = QRadioButton(self.frame_7)
        self.radioButton_tcrit_10.setObjectName(u"radioButton_tcrit_10")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_10.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_10.setSizePolicy(sizePolicy1)
        font14 = QFont()
        font14.setPointSize(11)
        self.radioButton_tcrit_10.setFont(font14)

        self.horizontalLayout_12.addWidget(self.radioButton_tcrit_10)

        self.label_72 = QLabel(self.frame_7)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font7)
        self.label_72.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_12.addWidget(self.label_72)

        self.label_73 = QLabel(self.frame_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font7)
        self.label_73.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_12.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font7)
        self.label_74.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_12.addWidget(self.label_74)


        self.verticalLayout_27.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_tcrit_05 = QRadioButton(self.frame_7)
        self.radioButton_tcrit_05.setObjectName(u"radioButton_tcrit_05")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_05.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_05.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_05.setFont(font14)

        self.horizontalLayout_23.addWidget(self.radioButton_tcrit_05)

        self.label_75 = QLabel(self.frame_7)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font7)
        self.label_75.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_23.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font7)
        self.label_76.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_23.addWidget(self.label_76)

        self.label_77 = QLabel(self.frame_7)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font7)
        self.label_77.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_23.addWidget(self.label_77)


        self.verticalLayout_27.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.radioButton_tcrit_025 = QRadioButton(self.frame_7)
        self.radioButton_tcrit_025.setObjectName(u"radioButton_tcrit_025")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_025.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_025.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_025.setFont(font14)
        self.radioButton_tcrit_025.setStyleSheet(u"")
        self.radioButton_tcrit_025.setChecked(True)

        self.horizontalLayout_24.addWidget(self.radioButton_tcrit_025)

        self.label_78 = QLabel(self.frame_7)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font7)
        self.label_78.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_24.addWidget(self.label_78)

        self.label_79 = QLabel(self.frame_7)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font7)
        self.label_79.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_24.addWidget(self.label_79)

        self.label_80 = QLabel(self.frame_7)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font7)
        self.label_80.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_24.addWidget(self.label_80)


        self.verticalLayout_27.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_tcrit_01 = QRadioButton(self.frame_7)
        self.radioButton_tcrit_01.setObjectName(u"radioButton_tcrit_01")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_01.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_01.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_01.setFont(font14)
        self.radioButton_tcrit_01.setStyleSheet(u"")

        self.horizontalLayout_25.addWidget(self.radioButton_tcrit_01)

        self.label_81 = QLabel(self.frame_7)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font7)
        self.label_81.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_25.addWidget(self.label_81)

        self.label_82 = QLabel(self.frame_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font7)
        self.label_82.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_25.addWidget(self.label_82)

        self.label_83 = QLabel(self.frame_7)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font7)
        self.label_83.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_25.addWidget(self.label_83)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.radioButton_tcrit_005 = QRadioButton(self.frame_7)
        self.radioButton_tcrit_005.setObjectName(u"radioButton_tcrit_005")
        sizePolicy1.setHeightForWidth(self.radioButton_tcrit_005.sizePolicy().hasHeightForWidth())
        self.radioButton_tcrit_005.setSizePolicy(sizePolicy1)
        self.radioButton_tcrit_005.setFont(font14)
        self.radioButton_tcrit_005.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.radioButton_tcrit_005)

        self.label_84 = QLabel(self.frame_7)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font7)
        self.label_84.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_26.addWidget(self.label_84)

        self.label_85 = QLabel(self.frame_7)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font7)
        self.label_85.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_26.addWidget(self.label_85)

        self.label_86 = QLabel(self.frame_7)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font7)
        self.label_86.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_26.addWidget(self.label_86)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_1)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.label_41 = QLabel(self.frame)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setFont(font8)
        self.label_41.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_41)

        self.label_95 = QLabel(self.frame)
        self.label_95.setObjectName(u"label_95")
        sizePolicy.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy)
        self.label_95.setFont(font9)
        self.label_95.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_95.setAlignment(Qt.AlignCenter)
        self.label_95.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_95)

        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_7)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_5)
        self.verticalLayout_22.setSpacing(3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font7)
        self.label_42.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font7)
        self.label_44.setStyleSheet(u"background-color: rgb(207, 216, 231);")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_44)


        self.verticalLayout_22.addLayout(self.horizontalLayout_9)

        self.line_8 = QFrame(self.frame_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_10 = QRadioButton(self.frame_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        sizePolicy1.setHeightForWidth(self.radioButton_10.sizePolicy().hasHeightForWidth())
        self.radioButton_10.setSizePolicy(sizePolicy1)
        self.radioButton_10.setFont(font14)
        self.radioButton_10.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.radioButton_10)

        self.label_et_10 = QLabel(self.frame_5)
        self.label_et_10.setObjectName(u"label_et_10")
        self.label_et_10.setFont(font7)
        self.label_et_10.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_10.addWidget(self.label_et_10)

        self.label_t_10 = QLabel(self.frame_5)
        self.label_t_10.setObjectName(u"label_t_10")
        self.label_t_10.setFont(font7)
        self.label_t_10.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_10.addWidget(self.label_t_10)

        self.label_RSEcrit_10 = QLabel(self.frame_5)
        self.label_RSEcrit_10.setObjectName(u"label_RSEcrit_10")
        self.label_RSEcrit_10.setFont(font7)
        self.label_RSEcrit_10.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_10.addWidget(self.label_RSEcrit_10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.radioButton_05 = QRadioButton(self.frame_5)
        self.radioButton_05.setObjectName(u"radioButton_05")
        sizePolicy1.setHeightForWidth(self.radioButton_05.sizePolicy().hasHeightForWidth())
        self.radioButton_05.setSizePolicy(sizePolicy1)
        self.radioButton_05.setFont(font14)
        self.radioButton_05.setStyleSheet(u"")
        self.radioButton_05.setChecked(True)

        self.horizontalLayout_19.addWidget(self.radioButton_05)

        self.label_et_05 = QLabel(self.frame_5)
        self.label_et_05.setObjectName(u"label_et_05")
        self.label_et_05.setFont(font7)
        self.label_et_05.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_19.addWidget(self.label_et_05)

        self.label_t_05 = QLabel(self.frame_5)
        self.label_t_05.setObjectName(u"label_t_05")
        self.label_t_05.setFont(font7)
        self.label_t_05.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_19.addWidget(self.label_t_05)

        self.label_RSEcrit_05 = QLabel(self.frame_5)
        self.label_RSEcrit_05.setObjectName(u"label_RSEcrit_05")
        self.label_RSEcrit_05.setFont(font7)
        self.label_RSEcrit_05.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_19.addWidget(self.label_RSEcrit_05)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_01 = QRadioButton(self.frame_5)
        self.radioButton_01.setObjectName(u"radioButton_01")
        sizePolicy1.setHeightForWidth(self.radioButton_01.sizePolicy().hasHeightForWidth())
        self.radioButton_01.setSizePolicy(sizePolicy1)
        self.radioButton_01.setFont(font14)
        self.radioButton_01.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.radioButton_01)

        self.label_et_01 = QLabel(self.frame_5)
        self.label_et_01.setObjectName(u"label_et_01")
        self.label_et_01.setFont(font7)
        self.label_et_01.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_20.addWidget(self.label_et_01)

        self.label_t_01 = QLabel(self.frame_5)
        self.label_t_01.setObjectName(u"label_t_01")
        self.label_t_01.setFont(font7)
        self.label_t_01.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_20.addWidget(self.label_t_01)

        self.label_RSEcrit_01 = QLabel(self.frame_5)
        self.label_RSEcrit_01.setObjectName(u"label_RSEcrit_01")
        self.label_RSEcrit_01.setFont(font7)
        self.label_RSEcrit_01.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_20.addWidget(self.label_RSEcrit_01)


        self.verticalLayout_22.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_005 = QRadioButton(self.frame_5)
        self.radioButton_005.setObjectName(u"radioButton_005")
        sizePolicy1.setHeightForWidth(self.radioButton_005.sizePolicy().hasHeightForWidth())
        self.radioButton_005.setSizePolicy(sizePolicy1)
        self.radioButton_005.setFont(font14)
        self.radioButton_005.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.radioButton_005)

        self.label_et_005 = QLabel(self.frame_5)
        self.label_et_005.setObjectName(u"label_et_005")
        self.label_et_005.setFont(font7)
        self.label_et_005.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_21.addWidget(self.label_et_005)

        self.label_t_005 = QLabel(self.frame_5)
        self.label_t_005.setObjectName(u"label_t_005")
        self.label_t_005.setFont(font7)
        self.label_t_005.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_21.addWidget(self.label_t_005)

        self.label_RSEcrit_005 = QLabel(self.frame_5)
        self.label_RSEcrit_005.setObjectName(u"label_RSEcrit_005")
        self.label_RSEcrit_005.setFont(font7)
        self.label_RSEcrit_005.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_21.addWidget(self.label_RSEcrit_005)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_001 = QRadioButton(self.frame_5)
        self.radioButton_001.setObjectName(u"radioButton_001")
        sizePolicy1.setHeightForWidth(self.radioButton_001.sizePolicy().hasHeightForWidth())
        self.radioButton_001.setSizePolicy(sizePolicy1)
        self.radioButton_001.setFont(font14)
        self.radioButton_001.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.radioButton_001)

        self.label_et_001 = QLabel(self.frame_5)
        self.label_et_001.setObjectName(u"label_et_001")
        self.label_et_001.setFont(font7)
        self.label_et_001.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_22.addWidget(self.label_et_001)

        self.label_t_001 = QLabel(self.frame_5)
        self.label_t_001.setObjectName(u"label_t_001")
        self.label_t_001.setFont(font7)
        self.label_t_001.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_22.addWidget(self.label_t_001)

        self.label_RSEcrit_001 = QLabel(self.frame_5)
        self.label_RSEcrit_001.setObjectName(u"label_RSEcrit_001")
        self.label_RSEcrit_001.setFont(font7)
        self.label_RSEcrit_001.setStyleSheet(u"background-color: rgb(207, 216, 231);")

        self.horizontalLayout_22.addWidget(self.label_RSEcrit_001)


        self.verticalLayout_22.addLayout(self.horizontalLayout_22)


        self.verticalLayout_23.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_8.setFrameShape(QFrame.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"background-color: transparent;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font7)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_26)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.lineEdit_standard_deviation = QLineEdit(self.frame_8)
        self.lineEdit_standard_deviation.setObjectName(u"lineEdit_standard_deviation")
        self.lineEdit_standard_deviation.setFont(font7)
        self.lineEdit_standard_deviation.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.lineEdit_standard_deviation)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(10, 16777215))
        font15 = QFont()
        font15.setPointSize(15)
        font15.setBold(True)
        self.label_29.setFont(font15)
        self.label_29.setStyleSheet(u"background-color: transparent;")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(15, 0))
        self.label_30.setMaximumSize(QSize(10, 16777215))
        font16 = QFont()
        font16.setPointSize(12)
        font16.setBold(True)
        self.label_30.setFont(font16)
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_30)

        self.lineEdit_sample_size = QLineEdit(self.frame_8)
        self.lineEdit_sample_size.setObjectName(u"lineEdit_sample_size")
        self.lineEdit_sample_size.setBaseSize(QSize(0, 0))
        self.lineEdit_sample_size.setFont(font7)
        self.lineEdit_sample_size.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.lineEdit_sample_size)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.label_standard_error_result = QLabel(self.frame_8)
        self.label_standard_error_result.setObjectName(u"label_standard_error_result")
        self.label_standard_error_result.setFont(font8)
        self.label_standard_error_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_standard_error_result)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_standard_error = QPushButton(self.frame_8)
        self.pushButton_standard_error.setObjectName(u"pushButton_standard_error")
        sizePolicy1.setHeightForWidth(self.pushButton_standard_error.sizePolicy().hasHeightForWidth())
        self.pushButton_standard_error.setSizePolicy(sizePolicy1)
        self.pushButton_standard_error.setFont(font8)
        self.pushButton_standard_error.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(62, 123, 252);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QPushButton:pressed {\n"
"color: black;    \n"
"border-style: inset;\n"
"    \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_standard_error)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tab_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFont(font)
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_9.setFrameShape(QFrame.WinPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)
        self.label_31.setStyleSheet(u"background-color: transparent;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_31)

        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font9)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_39)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)

        self.lineEdit_standard_error = QLineEdit(self.frame_9)
        self.lineEdit_standard_error.setObjectName(u"lineEdit_standard_error")
        self.lineEdit_standard_error.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_standard_error.setBaseSize(QSize(0, 0))
        self.lineEdit_standard_error.setFont(font7)
        self.lineEdit_standard_error.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.lineEdit_standard_error)

        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(10, 16777215))
        self.label_40.setFont(font15)
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_40)

        self.lineEdit_mean = QLineEdit(self.frame_9)
        self.lineEdit_mean.setObjectName(u"lineEdit_mean")
        self.lineEdit_mean.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_mean.setBaseSize(QSize(0, 0))
        self.lineEdit_mean.setFont(font7)
        self.lineEdit_mean.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.lineEdit_mean)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_5)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.label_relative_standard_error_result = QLabel(self.frame_9)
        self.label_relative_standard_error_result.setObjectName(u"label_relative_standard_error_result")
        self.label_relative_standard_error_result.setFont(font9)
        self.label_relative_standard_error_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_relative_standard_error_result)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_relative_standard_error = QPushButton(self.frame_9)
        self.pushButton_relative_standard_error.setObjectName(u"pushButton_relative_standard_error")
        sizePolicy1.setHeightForWidth(self.pushButton_relative_standard_error.sizePolicy().hasHeightForWidth())
        self.pushButton_relative_standard_error.setSizePolicy(sizePolicy1)
        self.pushButton_relative_standard_error.setFont(font8)
        self.pushButton_relative_standard_error.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(62, 123, 252);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QPushButton:pressed {\n"
"color: black;    \n"
"border-style: inset;\n"
"    \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_relative_standard_error)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.verticalFrame_4 = QFrame(self.tab_2)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.verticalFrame_4.setFrameShape(QFrame.WinPanel)
        self.verticalFrame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.label_63 = QLabel(self.verticalFrame_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font8)
        self.label_63.setStyleSheet(u"background-color: transparent;")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_63)

        self.label_results = QLabel(self.verticalFrame_4)
        self.label_results.setObjectName(u"label_results")
        self.label_results.setFont(font7)
        self.label_results.setStyleSheet(u"background-color: transparent;")
        self.label_results.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_results)

        self.frame_adequate = QFrame(self.verticalFrame_4)
        self.frame_adequate.setObjectName(u"frame_adequate")
        self.frame_adequate.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_adequate = QHBoxLayout(self.frame_adequate)
        self.horizontalLayout_adequate.setObjectName(u"horizontalLayout_adequate")
        self.horizontalLayout_adequate.setContentsMargins(-1, 0, -1, 0)
        self.label_rse_adequate = QLabel(self.frame_adequate)
        self.label_rse_adequate.setObjectName(u"label_rse_adequate")
        self.label_rse_adequate.setFont(font8)
        self.label_rse_adequate.setStyleSheet(u"background-color: transparent;")
        self.label_rse_adequate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_adequate.addWidget(self.label_rse_adequate)

        self.label_68 = QLabel(self.frame_adequate)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font16)
        self.label_68.setStyleSheet(u"background-color: transparent;")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_adequate.addWidget(self.label_68)

        self.label_rse_crit_adequate = QLabel(self.frame_adequate)
        self.label_rse_crit_adequate.setObjectName(u"label_rse_crit_adequate")
        self.label_rse_crit_adequate.setFont(font8)
        self.label_rse_crit_adequate.setStyleSheet(u"background-color: transparent;")
        self.label_rse_crit_adequate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_adequate.addWidget(self.label_rse_crit_adequate)

        self.label_69 = QLabel(self.frame_adequate)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font8)
        self.label_69.setStyleSheet(u"background-color: transparent;")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_adequate.addWidget(self.label_69)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_adequate.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addWidget(self.frame_adequate)

        self.frame_not_adequate = QFrame(self.verticalFrame_4)
        self.frame_not_adequate.setObjectName(u"frame_not_adequate")
        self.frame_not_adequate.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_not_adequate = QHBoxLayout(self.frame_not_adequate)
        self.horizontalLayout_not_adequate.setObjectName(u"horizontalLayout_not_adequate")
        self.horizontalLayout_not_adequate.setContentsMargins(-1, 0, -1, 0)
        self.label_rse_not_adequate = QLabel(self.frame_not_adequate)
        self.label_rse_not_adequate.setObjectName(u"label_rse_not_adequate")
        self.label_rse_not_adequate.setFont(font8)
        self.label_rse_not_adequate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_not_adequate.addWidget(self.label_rse_not_adequate)

        self.label_65 = QLabel(self.frame_not_adequate)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font16)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_not_adequate.addWidget(self.label_65)

        self.label_rse_crit_not_adequate = QLabel(self.frame_not_adequate)
        self.label_rse_crit_not_adequate.setObjectName(u"label_rse_crit_not_adequate")
        self.label_rse_crit_not_adequate.setFont(font8)
        self.label_rse_crit_not_adequate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_not_adequate.addWidget(self.label_rse_crit_not_adequate)

        self.label_67 = QLabel(self.frame_not_adequate)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font8)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_not_adequate.addWidget(self.label_67)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_not_adequate.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addWidget(self.frame_not_adequate)

        self.frame_29 = QFrame(self.verticalFrame_4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: transparent;\n"
"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_30)

        self.pushButton_results = QPushButton(self.frame_29)
        self.pushButton_results.setObjectName(u"pushButton_results")
        sizePolicy1.setHeightForWidth(self.pushButton_results.sizePolicy().hasHeightForWidth())
        self.pushButton_results.setSizePolicy(sizePolicy1)
        self.pushButton_results.setFont(font8)
        self.pushButton_results.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgb(62, 123, 252);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QPushButton:pressed {\n"
"color: black;    \n"
"border-style: inset;\n"
"    \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"")

        self.horizontalLayout_33.addWidget(self.pushButton_results)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_31)


        self.verticalLayout.addWidget(self.frame_29)


        self.verticalLayout_13.addWidget(self.verticalFrame_4)

        self.frame_margin_error = QFrame(self.tab_2)
        self.frame_margin_error.setObjectName(u"frame_margin_error")
        self.frame_margin_error.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_margin_error.setFrameShape(QFrame.WinPanel)
        self.frame_margin_error.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_margin_error)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.label_15 = QLabel(self.frame_margin_error)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"background-color: transparent;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_15)

        self.label_62 = QLabel(self.frame_margin_error)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font7)
        self.label_62.setStyleSheet(u"background-color: transparent;")
        self.label_62.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_62)

        self.label_margin_error = QLabel(self.frame_margin_error)
        self.label_margin_error.setObjectName(u"label_margin_error")
        self.label_margin_error.setFont(font7)
        self.label_margin_error.setStyleSheet(u"background-color: transparent;")
        self.label_margin_error.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_margin_error.setIndent(15)

        self.verticalLayout_17.addWidget(self.label_margin_error)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_confidence_interval_2 = QLabel(self.frame_margin_error)
        self.label_confidence_interval_2.setObjectName(u"label_confidence_interval_2")
        self.label_confidence_interval_2.setFont(font7)
        self.label_confidence_interval_2.setStyleSheet(u"background-color: transparent;")
        self.label_confidence_interval_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_confidence_interval_2.setIndent(15)

        self.horizontalLayout_38.addWidget(self.label_confidence_interval_2)

        self.label_confidence_interval = QLabel(self.frame_margin_error)
        self.label_confidence_interval.setObjectName(u"label_confidence_interval")
        self.label_confidence_interval.setFont(font7)
        self.label_confidence_interval.setStyleSheet(u"background-color: transparent;")
        self.label_confidence_interval.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_confidence_interval)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_38)


        self.verticalLayout_13.addWidget(self.frame_margin_error)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.tab_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFont(font4)
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_10.setFrameShape(QFrame.WinPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_10)
#ifndef Q_OS_MAC
        self.verticalLayout_26.setSpacing(-1)
#endif
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.label_115 = QLabel(self.frame_10)
        self.label_115.setObjectName(u"label_115")
        font17 = QFont()
        font17.setFamilies([u"Arial"])
        font17.setPointSize(14)
        font17.setStrikeOut(False)
        self.label_115.setFont(font17)
        self.label_115.setStyleSheet(u"background-color: transparent;")
        self.label_115.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_115.setWordWrap(True)
        self.label_115.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_26.addWidget(self.label_115)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.frame_25 = QFrame(self.centralwidget)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.994045, y1:0.034, x2:0.005, y2:1, stop:0 rgba(176, 196, 221, 255), stop:1 rgba(245, 245, 245, 255));")
        self.frame_25.setFrameShape(QFrame.Panel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_25)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_87 = QLabel(self.frame_25)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font7)
        self.label_87.setStyleSheet(u"background-color: transparent;")
        self.label_87.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_87.setWordWrap(True)
        self.label_87.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_25)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font7)
        self.label_88.setStyleSheet(u"background-color: transparent;")
        self.label_88.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_88.setWordWrap(True)
        self.label_88.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.label_88)

        self.line_14 = QFrame(self.frame_25)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_14)

        self.label_61 = QLabel(self.frame_25)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font7)
        self.label_61.setStyleSheet(u"background-color: transparent;")
        self.label_61.setWordWrap(True)
        self.label_61.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.label_61)


        self.verticalLayout_8.addWidget(self.frame_25)

        Sampling_Investigator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Sampling_Investigator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 37))
        Sampling_Investigator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Sampling_Investigator)
        self.statusbar.setObjectName(u"statusbar")
        Sampling_Investigator.setStatusBar(self.statusbar)

        self.retranslateUi(Sampling_Investigator)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Sampling_Investigator)
    # setupUi

    def retranslateUi(self, Sampling_Investigator):
        Sampling_Investigator.setWindowTitle(QCoreApplication.translate("Sampling_Investigator", u"Sampling Investigator", None))
        self.label_16.setText(QCoreApplication.translate("Sampling_Investigator", u"Sampling Investigator", None))
        self.label_3.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>A priori <span style=\" font-style:italic;\">N </span>size analysis</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Sampling_Investigator", u"The formula for estimating the required n size:", None))
        self.label_6.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">N </span><span style=\" font-size:14pt; font-weight:600;\">=</span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\"> s</span><span style=\" font-size:14pt; font-weight:600; font-style:italic; vertical-align:super;\">2 </span><span style=\" font-size:14pt; font-weight:600;\">/ ( </span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">e</span><span style=\" font-size:14pt; font-weight:600; font-style:italic; vertical-align:sub;\">t </span><span style=\" font-size:14pt; font-weight:600;\">/</span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\"> t </span><span style=\" font-size:14pt; font-weight:600;\">)</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">2</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">s </span>= estimated standard deviation for the population; directly related to <span style=\" font-style:italic;\">N. </span>Obtained from the following: a pilot study, a similar data set, or published research on the variable of interest</p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">e</span><span style=\" font-style:italic; vertical-align:sub;\">t</span><span style=\" font-style:italic;\"> = </span>tolerable error which is equal to 1/2 the desired confidence interval level</p></body></html>", None))
        self.label_94.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">t </span>=<span style=\" font-style:italic;\"> t</span>-value for the desired probability level <span style=\" font-style:italic;\">(z</span> values are proxies for <span style=\" font-style:italic;\">t</span> values)</p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("Sampling_Investigator", u"Step 1: Choose the critical value of t", None))
        self.label_117.setText(QCoreApplication.translate("Sampling_Investigator", u"\u03b1 = tail area", None))
        self.label_118.setText(QCoreApplication.translate("Sampling_Investigator", u"1 - 2\u03b1", None))
        self.label_119.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>z<span style=\" vertical-align:sub;\">\u03b1</span> = <span style=\" font-style:italic;\">t</span></p></body></html>", None))
        self.radioButton_tcrit_80.setText("")
        self.label_122.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.10</p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.80</p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.28</p></body></html>", None))
        self.radioButton_tcrit_90.setText("")
        self.label_129.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.05</p></body></html>", None))
        self.label_133.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.90</p></body></html>", None))
        self.label_137.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.645</p></body></html>", None))
        self.radioButton_tcrit_95.setText("")
        self.label_141.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.025</p></body></html>", None))
        self.label_145.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.95</p></body></html>", None))
        self.label_146.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.radioButton_tcrit_98.setText("")
        self.label_147.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.01</p></body></html>", None))
        self.label_148.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.98</p></body></html>", None))
        self.label_149.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>2.33</p></body></html>", None))
        self.radioButton_tcrit_99.setText("")
        self.label_150.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.005</p></body></html>", None))
        self.label_151.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.99</p></body></html>", None))
        self.label_152.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>2.58</p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("Sampling_Investigator", u"Step 2: Choose the tolerable error level", None))
        self.label_93.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">e</span><span style=\" font-style:italic; vertical-align:sub;\">t</span> / <span style=\" font-style:italic;\">t = RSE</span><span style=\" font-style:italic; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">e</span><span style=\" font-style:italic; vertical-align:sub;\">t</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("Sampling_Investigator", u"t", None))
        self.label_48.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">RSE</span><span style=\" font-style:italic; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.radioButton_n_10.setText("")
        self.label_et_11.setText(QCoreApplication.translate("Sampling_Investigator", u".10", None))
        self.label_t_11.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_RSEcrit_11.setText(QCoreApplication.translate("Sampling_Investigator", u".0510", None))
        self.radioButton_n_05.setText("")
        self.label_et_8.setText(QCoreApplication.translate("Sampling_Investigator", u".05", None))
        self.label_t_6.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_RSEcrit_6.setText(QCoreApplication.translate("Sampling_Investigator", u".0255", None))
        self.radioButton_n_01.setText("")
        self.label_et_3.setText(QCoreApplication.translate("Sampling_Investigator", u".01", None))
        self.label_t_4.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_RSEcrit_2.setText(QCoreApplication.translate("Sampling_Investigator", u".0051", None))
        self.radioButton_n_005.setText("")
        self.label_et_9.setText(QCoreApplication.translate("Sampling_Investigator", u".005", None))
        self.label_t_7.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_RSEcrit_7.setText(QCoreApplication.translate("Sampling_Investigator", u".0026", None))
        self.radioButton_n_001.setText("")
        self.label_et_4.setText(QCoreApplication.translate("Sampling_Investigator", u".001", None))
        self.label_t_5.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_RSEcrit_3.setText(QCoreApplication.translate("Sampling_Investigator", u".0005", None))
        self.label_98.setText(QCoreApplication.translate("Sampling_Investigator", u"Step 3: Enter mean and standard deviation from a previous/pilot study", None))
        self.label_et_6.setText(QCoreApplication.translate("Sampling_Investigator", u"Mean", None))
        self.lineEdit_pilot_mean.setText("")
        self.lineEdit_pilot_mean.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"mean in pilot sample", None))
        self.label_et_7.setText(QCoreApplication.translate("Sampling_Investigator", u"Standard deviation", None))
        self.lineEdit_pilot_standard_deviation.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"std. dev. in pilot sample", None))
        self.pushButton.setText(QCoreApplication.translate("Sampling_Investigator", u"Calculate result", None))
        self.label_result_stdev_squared_3.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>Required <span style=\" font-style:italic;\">N </span>=</p></body></html>", None))
        self.label_result_required_n_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(<span style=\" font-style:italic;\">N </span>size)</p></body></html>", None))
        self.label_99.setText(QCoreApplication.translate("Sampling_Investigator", u"Formula in action", None))
        self.label_1.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>e<span style=\" vertical-align:sub;\">t</span> = </p></body></html>", None))
        self.label_mean.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>&lt;mean&gt;</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Sampling_Investigator", u"*", None))
        self.label_10.setText(QCoreApplication.translate("Sampling_Investigator", u".05", None))
        self.label_11.setText(QCoreApplication.translate("Sampling_Investigator", u"=", None))
        self.label_et.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(e<span style=\" vertical-align:sub;\">t</span> result)</p></body></html>", None))
        self.label_et_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>e<span style=\" vertical-align:sub;\">t</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Sampling_Investigator", u"/", None))
        self.label_t.setText(QCoreApplication.translate("Sampling_Investigator", u"1.96", None))
        self.label_t_2.setText(QCoreApplication.translate("Sampling_Investigator", u"=", None))
        self.label_result_et_t.setText(QCoreApplication.translate("Sampling_Investigator", u"(result)", None))
        self.label_result_et_t_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(result)<span style=\" vertical-align:super;\">2</span> = </p></body></html>", None))
        self.label_result_et_t_squared.setText(QCoreApplication.translate("Sampling_Investigator", u"(result)", None))
        self.label_std_dev.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>&lt;standard deviation&gt;</p></body></html>", None))
        self.label_result_3.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" vertical-align:super;\">2</span> = </p></body></html>", None))
        self.label_result_stdev_squared.setText(QCoreApplication.translate("Sampling_Investigator", u"(result)", None))
        self.label_result_stdev_squared_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(standard deviation<span style=\" vertical-align:super;\">2</span>)</p></body></html>", None))
        self.label_result_4.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>/</p></body></html>", None))
        self.label_result_et_t_squared_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(e<span style=\" vertical-align:sub;\">t</span> / <span style=\" font-style:italic;\">t</span>)<span style=\" vertical-align:super;\">2</span></p></body></html>", None))
        self.label_t_3.setText(QCoreApplication.translate("Sampling_Investigator", u"=", None))
        self.label_result_required_n.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>(<span style=\" font-style:italic;\">N </span>size)</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Sampling_Investigator", u"N size", None))
        self.label.setText(QCoreApplication.translate("Sampling_Investigator", u"Sampling adequacy analysis", None))
        self.label_64.setText(QCoreApplication.translate("Sampling_Investigator", u"Choose the critical value of t", None))
        self.label_66.setText(QCoreApplication.translate("Sampling_Investigator", u"\u03b1 = tail area", None))
        self.label_70.setText(QCoreApplication.translate("Sampling_Investigator", u"1 - 2\u03b1", None))
        self.label_71.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>z<span style=\" vertical-align:sub;\">\u03b1</span> = <span style=\" font-style:italic;\">t</span></p></body></html>", None))
        self.radioButton_tcrit_10.setText("")
        self.label_72.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.10</p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.80</p></body></html>", None))
        self.label_74.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.28</p></body></html>", None))
        self.radioButton_tcrit_05.setText("")
        self.label_75.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.05</p></body></html>", None))
        self.label_76.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.90</p></body></html>", None))
        self.label_77.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.645</p></body></html>", None))
        self.radioButton_tcrit_025.setText("")
        self.label_78.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.025</p></body></html>", None))
        self.label_79.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.95</p></body></html>", None))
        self.label_80.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.radioButton_tcrit_01.setText("")
        self.label_81.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.01</p></body></html>", None))
        self.label_82.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.98</p></body></html>", None))
        self.label_83.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>2.33</p></body></html>", None))
        self.radioButton_tcrit_005.setText("")
        self.label_84.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.005</p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>0.99</p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>2.58</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("Sampling_Investigator", u"Choose the tolerable error level", None))
        self.label_95.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">e</span><span style=\" font-style:italic; vertical-align:sub;\">t</span> / <span style=\" font-style:italic;\">t = RSE</span><span style=\" font-style:italic; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">e</span><span style=\" font-style:italic; vertical-align:sub;\">t</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">t</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">RSE</span><span style=\" font-style:italic; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.radioButton_10.setText("")
        self.label_et_10.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.10</p></body></html>", None))
        self.label_t_10.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.label_RSEcrit_10.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.0510</p></body></html>", None))
        self.radioButton_05.setText("")
        self.label_et_05.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.05</p></body></html>", None))
        self.label_t_05.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.label_RSEcrit_05.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.0255</p></body></html>", None))
        self.radioButton_01.setText("")
        self.label_et_01.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.01</p></body></html>", None))
        self.label_t_01.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.label_RSEcrit_01.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.0051</p></body></html>", None))
        self.radioButton_005.setText("")
        self.label_et_005.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.005</p></body></html>", None))
        self.label_t_005.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.label_RSEcrit_005.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.0026</p></body></html>", None))
        self.radioButton_001.setText("")
        self.label_et_001.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.001</p></body></html>", None))
        self.label_t_001.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>1.96</p></body></html>", None))
        self.label_RSEcrit_001.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>.0005</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Sampling_Investigator", u"Standard Error", None))
        self.label_26.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_26.setText(QCoreApplication.translate("Sampling_Investigator", u"Standard error = SD / \u221an", None))
        self.lineEdit_standard_deviation.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"standard deviation", None))
        self.label_29.setText(QCoreApplication.translate("Sampling_Investigator", u"/", None))
        self.label_30.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_30.setText(QCoreApplication.translate("Sampling_Investigator", u"\u221a", None))
        self.lineEdit_sample_size.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"sample size", None))
        self.label_standard_error_result.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_standard_error_result.setText(QCoreApplication.translate("Sampling_Investigator", u"SE = (enter info above)", None))
        self.pushButton_standard_error.setText(QCoreApplication.translate("Sampling_Investigator", u"Calculate standard error", None))
        self.label_31.setText(QCoreApplication.translate("Sampling_Investigator", u"Relative standard error", None))
        self.label_39.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_39.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>Relative standard error = <span style=\" font-style:italic;\">SE</span> / mean</p></body></html>", None))
        self.lineEdit_standard_error.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"standard error", None))
        self.label_40.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_40.setText(QCoreApplication.translate("Sampling_Investigator", u"/", None))
        self.lineEdit_mean.setPlaceholderText(QCoreApplication.translate("Sampling_Investigator", u"mean", None))
        self.label_relative_standard_error_result.setStyleSheet(QCoreApplication.translate("Sampling_Investigator", u"background-color: transparent;", None))
        self.label_relative_standard_error_result.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic;\">RSE</span> = (enter info above)</p></body></html>", None))
        self.pushButton_relative_standard_error.setText(QCoreApplication.translate("Sampling_Investigator", u"Calculate relative standard error", None))
        self.label_63.setText(QCoreApplication.translate("Sampling_Investigator", u"Results", None))
        self.label_results.setText(QCoreApplication.translate("Sampling_Investigator", u"Complete information above. Then click \"see results\"", None))
        self.label_rse_adequate.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic; color:#005d00;\">RSE</span></p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" color:#005d00;\">&lt;</span></p></body></html>", None))
        self.label_rse_crit_adequate.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic; color:#005d00;\">RSE</span><span style=\" font-style:italic; color:#005d00; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" color:#005d00;\">(sample is adequate)</span></p></body></html>", None))
        self.label_rse_not_adequate.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic; color:#7c0000;\">RSE</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" color:#7c0000;\">&gt;</span></p></body></html>", None))
        self.label_rse_crit_not_adequate.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" font-style:italic; color:#7c0000;\">RSE</span><span style=\" font-style:italic; color:#7c0000; vertical-align:sub;\">crit</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p><span style=\" color:#7c0000;\">(sample is not adequate)</span></p></body></html>", None))
        self.pushButton_results.setText(QCoreApplication.translate("Sampling_Investigator", u"See results", None))
        self.label_15.setText(QCoreApplication.translate("Sampling_Investigator", u"Confidence Intervals", None))
        self.label_62.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>We can use<span style=\" font-style:italic;\"> t</span> and <span style=\" font-style:italic;\">SE</span> values to create a confidence interval around the mean:</p></body></html>", None))
        self.label_margin_error.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>95% CI = [-<span style=\" font-style:italic;\">t</span>*<span style=\" font-style:italic;\">SE</span>, +<span style=\" font-style:italic;\">t</span>*<span style=\" font-style:italic;\">SE</span>]</p></body></html>", None))
        self.label_confidence_interval_2.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>CI = [lower, upper]</p></body></html>", None))
        self.label_confidence_interval.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>CI = [lower, upper]</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Sampling_Investigator", u"Adequacy", None))
        self.label_115.setText(QCoreApplication.translate("Sampling_Investigator", u"Prose and formulas adapted from Egbert, J., Biber, D., & Gray, B. (2022). Designing and evaluating language corpora. Cambridge. \n"
"https://doi.org/10.1017/9781316584880", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Sampling_Investigator", u"Additional information", None))
        self.label_87.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>Please use the following to reference <span style=\" font-style:italic;\">Sampling Investigator</span>:</p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>Dixon, D. H. &amp; Dixon, T. (2023). Sampling Investigator (Version 3.0) [Computer Software]. Available from https://sites.google.com/view/danielhdixon/software</p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("Sampling_Investigator", u"<html><head/><body><p>Sampling Investigator by <a href=\"https://sites.google.com/view/danielhdixon/software\"><span style=\" text-decoration: underline; color:#0000ff;\">Daniel H Dixon and T\u00fclay Dixon</span></a> is licensed under a <a href=\"http://creativecommons.org/licenses/by-nc-nd/4.0/\"><span style=\" text-decoration: underline; color:#0000ff;\">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</span></a></p></body></html>", None))
    # retranslateUi

