# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(103, 144, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_izquierda = QtWidgets.QWidget(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_izquierda.sizePolicy().hasHeightForWidth())
        self.widget_izquierda.setSizePolicy(sizePolicy)
        self.widget_izquierda.setObjectName("widget_izquierda")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_izquierda)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(parent=self.widget_izquierda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_izquierda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boton_obtener_eml = QtWidgets.QPushButton(parent=self.widget_4)
        self.boton_obtener_eml.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
" color: rgb(0, 0, 0);\n"
"")
        self.boton_obtener_eml.setObjectName("boton_obtener_eml")
        self.verticalLayout_2.addWidget(self.boton_obtener_eml)
        self.boton_crear_csv = QtWidgets.QPushButton(parent=self.widget_4)
        self.boton_crear_csv.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
" color: rgb(0, 0, 0);\n"
"")
        self.boton_crear_csv.setObjectName("boton_crear_csv")
        self.verticalLayout_2.addWidget(self.boton_crear_csv)
        self.boton_crear_img = QtWidgets.QPushButton(parent=self.widget_4)
        self.boton_crear_img.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
" color: rgb(0, 0, 0);\n"
"")
        self.boton_crear_img.setObjectName("boton_crear_img")
        self.verticalLayout_2.addWidget(self.boton_crear_img)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_izquierda)
        self.widget_derecha = QtWidgets.QWidget(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_derecha.sizePolicy().hasHeightForWidth())
        self.widget_derecha.setSizePolicy(sizePolicy)
        self.widget_derecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_derecha.setObjectName("widget_derecha")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_derecha)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_eml = QtWidgets.QWidget(parent=self.widget_derecha)
        self.widget_eml.setObjectName("widget_eml")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_eml)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_eml)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("  font-size: 16px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_eml)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_directorio_eml = QtWidgets.QLabel(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directorio_eml.sizePolicy().hasHeightForWidth())
        self.label_directorio_eml.setSizePolicy(sizePolicy)
        self.label_directorio_eml.setMaximumSize(QtCore.QSize(16777215, 66))
        self.label_directorio_eml.setAutoFillBackground(False)
        self.label_directorio_eml.setStyleSheet("width: 100%;\n"
"  padding: 12px 20px;\n"
"  margin: 8px 0;\n"
"border: 2px solid rgb(103, 144, 255);\n"
"  font-size: 16px;\n"
"")
        self.label_directorio_eml.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_directorio_eml.setObjectName("label_directorio_eml")
        self.horizontalLayout_4.addWidget(self.label_directorio_eml)
        self.boton_directorio_eml = QtWidgets.QPushButton(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_directorio_eml.sizePolicy().hasHeightForWidth())
        self.boton_directorio_eml.setSizePolicy(sizePolicy)
        self.boton_directorio_eml.setStyleSheet("background-color: rgb(103, 144, 255);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"")
        self.boton_directorio_eml.setObjectName("boton_directorio_eml")
        self.horizontalLayout_4.addWidget(self.boton_directorio_eml)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.verticalLayout_3.addWidget(self.widget_eml)
        self.widget_csv = QtWidgets.QWidget(parent=self.widget_derecha)
        self.widget_csv.setObjectName("widget_csv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_csv)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_csv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("  font-size: 16px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_csv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_directorio_csv = QtWidgets.QLabel(parent=self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directorio_csv.sizePolicy().hasHeightForWidth())
        self.label_directorio_csv.setSizePolicy(sizePolicy)
        self.label_directorio_csv.setMaximumSize(QtCore.QSize(16777215, 66))
        self.label_directorio_csv.setAutoFillBackground(False)
        self.label_directorio_csv.setStyleSheet("width: 100%;\n"
"  padding: 12px 20px;\n"
"  margin: 8px 0;\n"
"border: 2px solid rgb(103, 144, 255);\n"
"  font-size: 16px;\n"
"")
        self.label_directorio_csv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_directorio_csv.setObjectName("label_directorio_csv")
        self.horizontalLayout_5.addWidget(self.label_directorio_csv)
        self.boton_directorio_csv = QtWidgets.QPushButton(parent=self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_directorio_csv.sizePolicy().hasHeightForWidth())
        self.boton_directorio_csv.setSizePolicy(sizePolicy)
        self.boton_directorio_csv.setStyleSheet("background-color: rgb(103, 144, 255);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"")
        self.boton_directorio_csv.setObjectName("boton_directorio_csv")
        self.horizontalLayout_5.addWidget(self.boton_directorio_csv)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.verticalLayout_3.addWidget(self.widget_csv)
        self.widget_img = QtWidgets.QWidget(parent=self.widget_derecha)
        self.widget_img.setObjectName("widget_img")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_img)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.widget_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("  font-size: 16px;")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_directorio_img = QtWidgets.QLabel(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directorio_img.sizePolicy().hasHeightForWidth())
        self.label_directorio_img.setSizePolicy(sizePolicy)
        self.label_directorio_img.setMaximumSize(QtCore.QSize(16777215, 66))
        self.label_directorio_img.setAutoFillBackground(False)
        self.label_directorio_img.setStyleSheet("width: 100%;\n"
"  padding: 12px 20px;\n"
"  margin: 8px 0;\n"
"border: 2px solid rgb(103, 144, 255);\n"
"  font-size: 16px;\n"
"")
        self.label_directorio_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_directorio_img.setObjectName("label_directorio_img")
        self.horizontalLayout_2.addWidget(self.label_directorio_img)
        self.boton_directorio_img = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_directorio_img.sizePolicy().hasHeightForWidth())
        self.boton_directorio_img.setSizePolicy(sizePolicy)
        self.boton_directorio_img.setStyleSheet("background-color: rgb(103, 144, 255);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"")
        self.boton_directorio_img.setObjectName("boton_directorio_img")
        self.horizontalLayout_2.addWidget(self.boton_directorio_img)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.verticalLayout_3.addWidget(self.widget_img)
        self.horizontalLayout.addWidget(self.widget_derecha)
        self.horizontalLayout_3.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Webpay eml converter"))
        self.titulo.setText(_translate("MainWindow", "Webpay eml to\n"
"csv and image"))
        self.boton_obtener_eml.setText(_translate("MainWindow", "Obtener .eml\'s"))
        self.boton_crear_csv.setText(_translate("MainWindow", "Crear csv"))
        self.boton_crear_img.setText(_translate("MainWindow", "Crear imágenes"))
        self.label_2.setText(_translate("MainWindow", "Escoge el directorio de los .eml:"))
        self.label_directorio_eml.setText(_translate("MainWindow", "..."))
        self.boton_directorio_eml.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Escoge el directorio de guardado del csv:"))
        self.label_directorio_csv.setText(_translate("MainWindow", "..."))
        self.boton_directorio_csv.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Escoge el directorio para el guardado de las imágenes:"))
        self.label_directorio_img.setText(_translate("MainWindow", "..."))
        self.boton_directorio_img.setText(_translate("MainWindow", "..."))
