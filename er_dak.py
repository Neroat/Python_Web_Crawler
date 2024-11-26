# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'er_dak.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 740)
        font = QFont()
        font.setFamilies([u"HY\uacac\uace0\ub515"])
        font.setPointSize(12)
        Form.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 50, 681, 641))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nickname = QLineEdit(self.layoutWidget)
        self.nickname.setObjectName(u"nickname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nickname)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(self.layoutWidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setFont(font)

        self.verticalLayout.addWidget(self.start_btn)

        self.reset_btn = QPushButton(self.layoutWidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setFont(font)

        self.verticalLayout.addWidget(self.reset_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.quit_btn = QPushButton(self.layoutWidget)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setFont(font)

        self.verticalLayout.addWidget(self.quit_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uc774\ud130\ub110 \ub9ac\ud134 \ucd5c\uadfc \uc804\uc801 \uac80\uc0c9\uae30", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ub2c9\ub124\uc784", None))
        self.start_btn.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\ub9ac\uc14b", None))
        self.quit_btn.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

