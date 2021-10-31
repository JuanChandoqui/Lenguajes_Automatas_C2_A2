import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from Models.evaluate_expression import match_expression 


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Views/main.ui', self) 
        self.button_evaluate.clicked.connect(self.evaluateExpression)
        self.button_exit.clicked.connect(self.close)
    
    def evaluateExpression(self):
        regular_expression = self.input_regular_expression.text()
        expression = self.input_value.text()
        print(expression)

        status = match_expression(regular_expression, expression)

        if (status):
            self.label_status.setText('VALIDATE EXPRESSION!')
            self.label_status.setStyleSheet('background-color: green; color: white; font-size: 12px; font-weight: bold')
        else:
            self.label_status.setText('INVALIDATE EXPRESSION!')
            self.label_status.setStyleSheet('background-color: red; color: white; font-size: 12px; font-weight: bold')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')