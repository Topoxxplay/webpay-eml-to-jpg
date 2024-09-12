import sys
import os.path as path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QMessageBox)
from frontend.main_ui import Ui_MainWindow
from backend.functions import crear_csv, crear_img
from get_eml import eml_from_gmail
from PyQt6.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    señal = pyqtSignal(str)
    def __init__(self):
        self.dir_eml = ""
        self.dir_csv = ""
        self.dir_img = ""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bad_msg = QMessageBox()
        self.bad_msg.setWindowTitle("Algo salió mal")
        self.bad_msg.setIcon(QMessageBox.Icon.Critical)
        self.good_msg = QMessageBox()
        self.good_msg.setWindowTitle("Todo salió como esperado")
        widget = self.ui
        widget.boton_directorio_img.clicked.connect(self.boton_imagenes)
        widget.boton_directorio_eml.clicked.connect(self.boton_eml)
        widget.boton_directorio_csv.clicked.connect(self.boton_csv)
        widget.boton_crear_csv.clicked.connect(self.boton_crear_csv)
        widget.boton_crear_img.clicked.connect(self.boton_crear_img)
        widget.boton_obtener_eml.clicked.connect(self.boton_obtener_eml)
        
    def boton_imagenes(self):
        widget = self.ui
        options = QFileDialog.getExistingDirectory(None, "Selecciona una carpeta")
        if options:
            widget.label_directorio_img.setText(options)
            self.dir_img = options
    
    def boton_eml(self):
        widget = self.ui
        options = QFileDialog.getExistingDirectory(None, "Selecciona una carpeta")
        if options:
            widget.label_directorio_eml.setText(options)
            self.dir_eml = options
    
    def boton_csv(self):
        widget = self.ui
        options = QFileDialog.getExistingDirectory(None, "Selecciona una carpeta")
        if options:
            widget.label_directorio_csv.setText(options)
            self.dir_csv = options
    
    def boton_crear_csv(self):
        if (self.dir_csv != "...") and (self.dir_eml != "..."):
            if path.exists(self.dir_csv) and path.exists(self.dir_eml):
                crear_csv(self.dir_eml, self.dir_csv)
                self.good_msg.setText("El proceso terminó correctamente")
                self.good_msg.exec()
            else:
                self.bad_msg.setText("No existe ese directorio")
                self.bad_msg.exec()
        elif ((self.dir_csv == "...") and (self.dir_eml != "...")) or ((self.dir_csv != "...") and (self.dir_eml == "...")):
            self.bad_msg.setText("Falta escoger un directorio")

    def boton_crear_img(self):
        if (self.dir_img != "...") and (self.dir_eml != "..."):
            if path.exists(self.dir_img) and path.exists(self.dir_eml):
                crear_img(self.dir_eml, self.dir_img)
                self.good_msg.setText("El proceso terminó correctamente")
                self.good_msg.exec()
            else:
                self.bad_msg.setText("No existe ese directorio")
                self.bad_msg.exec()
        else:
            self.bad_msg.setText("Falta escoger un directorio")
            self.bad_msg.exec()
    
    def boton_obtener_eml(self):
        if (self.dir_eml != "..."):
            eml_from_gmail(self.dir_eml)
            self.good_msg.setText("El proceso terminó correctamente")
            self.good_msg.exec()
        else:
            self.bad_msg.setText("Falta escoger un directorio")
            self.bad_msg.exec()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())