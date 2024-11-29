# 
# 
# 
# 

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title:str = "Название"
        
        self._initUI()
        
    def _initUI(self):
        '''
        Инициализация пользовательского интерфейса.
        
        '''
        
        self.setWindowTitle(self.title)
        # self.setGeometry()


if __name__=="__main__":
    # Запуск основного тела UI приложения
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    app.exec_()