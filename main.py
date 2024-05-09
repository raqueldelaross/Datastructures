import sys
from home_window import Home
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
home = Home()


# Cargar ventana principal
def load():
    home.show()

    app.exec()


load()
