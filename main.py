import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETANDO NOME E TAMANHO DA JANELA PRINCIPAL
        self.setWindowTitle("Pomodoro")
        self.setFixedSize(QSize(400,420))

        self.container = QFrame()


        self.main_layout = QVBoxLayout(self.container)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        self.main_frame = QFrame()
        self.main_frame.setStyleSheet("background-color: blue")
        self.main_frame.setMinimumHeight(50)
        self.main_frame.setMaximumHeight(50)

        self.coloca_aqui = QHBoxLayout(self.main_frame)

        self.teste = QFrame()
        self.teste.setStyleSheet("background-color: purple")

        
        self.main_layout.addWidget(self.main_frame)
        self.main_layout.addWidget(self.teste)

        self.lbl_foco = QLabel("Foco")
        self.lbl_foco.setStyleSheet("color: black")

        self.tempo_foco = QSpinBox()
        self.tempo_foco.setStyleSheet("color: black")
        self.tempo_foco.setValue(25)
        self.tempo_foco.setRange(0,30)

        self.lbl_descanso = QLabel("Descanso")
        self.lbl_descanso.setStyleSheet("color: black")

        self.tempo_descanso = QSpinBox()
        self.tempo_descanso.setStyleSheet("color: black")
        self.tempo_descanso.setValue(5)
        self.tempo_descanso.setRange(0,15)

        self.coloca_aqui.addWidget(self.lbl_foco)
        self.coloca_aqui.addWidget(self.tempo_foco)
        self.coloca_aqui.addWidget(self.lbl_descanso)
        self.coloca_aqui.addWidget(self.tempo_descanso)


        self.setCentralWidget(self.container)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()