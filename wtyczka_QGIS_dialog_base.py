# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_QGIS_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_moja_wtyczka_QGISDialogBase(object):
    def setupUi(self, moja_wtyczka_QGISDialogBase):
        moja_wtyczka_QGISDialogBase.setObjectName("moja_wtyczka_QGISDialogBase")
        moja_wtyczka_QGISDialogBase.resize(210, 180)
        moja_wtyczka_QGISDialogBase.setMaximumSize(QtCore.QSize(210, 180))
        moja_wtyczka_QGISDialogBase.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.verticalLayoutWidget = QtWidgets.QWidget(moja_wtyczka_QGISDialogBase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.mMapLayerComboBox = QgsMapLayerComboBox(self.verticalLayoutWidget)
        self.mMapLayerComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);")
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.verticalLayout.addWidget(self.mMapLayerComboBox)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)

        self.retranslateUi(moja_wtyczka_QGISDialogBase)
        QtCore.QMetaObject.connectSlotsByName(moja_wtyczka_QGISDialogBase)

    def retranslateUi(self, moja_wtyczka_QGISDialogBase):
        _translate = QtCore.QCoreApplication.translate
        moja_wtyczka_QGISDialogBase.setWindowTitle(_translate("moja_wtyczka_QGISDialogBase", "wtyczkaQGIS"))
        self.label.setText(_translate("moja_wtyczka_QGISDialogBase", "Wybierz aktywną warstwe"))
        self.radioButton.setText(_translate("moja_wtyczka_QGISDialogBase", "Obliczenie różnnicy wysokości"))
        self.radioButton_2.setText(_translate("moja_wtyczka_QGISDialogBase", "Obliczenie wybranego obszaru"))
        self.radioButton_3.setText(_translate("moja_wtyczka_QGISDialogBase", "Odklik"))

from qgsmaplayercombobox import QgsMapLayerComboBox
