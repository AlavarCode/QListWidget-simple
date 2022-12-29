from PyQt5.QtWidgets import QMainWindow, QApplication
from interfaces.principal import Ui_MainWindow
import sys

class MiAplicacion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Instancias
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicialización de la ventana
        self.setFocus()

        # Control de botones
        self.ui.btn_agregar.clicked.connect(self.agregar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)

    def agregar(self):
        pais = self.ui.pais.text().strip().title()
        if len(pais) > 0:
            filas = self.ui.lista.count()
            self.ui.lista.insertItem(filas, pais)

            self.ui.pais.clear()
            self.ui.pais.setFocus()

    def eliminar(self):
        fila_actual = self.ui.lista.currentRow()
        if fila_actual >= 0:
            self.ui.lista.takeItem(fila_actual) 

app = QApplication(sys.argv)
mi_app = MiAplicacion()
mi_app.show()
sys.exit(app.exec_())