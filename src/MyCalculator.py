from PyQt5 import QtWidgets, QtGui
from calculator_ui import Ui_MainWindow

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    FirstNumber = None
    UserIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/icon.png'))
        self.setWindowTitle('Calculator')
        self.show()

        # Connecting buttons
        self.button_0.clicked.connect(self.digit_pressed)
        self.button_1.clicked.connect(self.digit_pressed)
        self.button_2.clicked.connect(self.digit_pressed)
        self.button_3.clicked.connect(self.digit_pressed)
        self.button_4.clicked.connect(self.digit_pressed)
        self.button_5.clicked.connect(self.digit_pressed)
        self.button_6.clicked.connect(self.digit_pressed)
        self.button_7.clicked.connect(self.digit_pressed)
        self.button_8.clicked.connect(self.digit_pressed)
        self.button_9.clicked.connect(self.digit_pressed)

        self.button_dot.clicked.connect(self.decimal_pressed)

        self.button_PlusMinus.clicked.connect(self.unary_operation_pressed)
        self.button_percent.clicked.connect(self.unary_operation_pressed)

        self.button_add.clicked.connect(self.binary_operator_pressed)
        self.button_subtract.clicked.connect(self.binary_operator_pressed)
        self.button_multiply.clicked.connect(self.binary_operator_pressed)
        self.button_divide.clicked.connect(self.binary_operator_pressed)
        
        self.button_equals.clicked.connect(self.equals_pressed)

        self.button_clear.clicked.connect(self.clear_pressed)

        self.button_add.setCheckable(True)
        self.button_subtract.setCheckable(True)
        self.button_multiply.setCheckable(True)
        self.button_divide.setCheckable(True)


    def digit_pressed(self):
        button = self.sender()

        if ((self.button_add.isChecked() or self.button_subtract.isChecked() or self.button_multiply.isChecked() or self.button_divide.isChecked()) and (not self.UserIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.UserIsTypingSecondNumber = True
        else:
            if (('.' in self.display.text()) and (button.text() == '0')):
                newLabel = newLabel = format(self.display.text() + button.text(), '.15')
            else:
                newLabel = format(float(self.display.text() + button.text()), '.15g')

        self.display.setText(newLabel)


    def decimal_pressed(self):
        if (not '.' in self.display.text()):
            self.display.setText(self.display.text() + '.')

    
    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.display.text())

        if button.text() == '+/-':
            labelNumber *= (-1)
        elif button.text() == '%':
            labelNumber *= 0.01

        newLabel = format(labelNumber, '.15g')
        self.display.setText(newLabel)


    def binary_operator_pressed(self):
        button = self.sender()

        self.FirstNumber = float(self.display.text())

        button.setChecked(True)


    def equals_pressed(self):
        SecondNumber = float(self.display.text())

        if self.button_add.isChecked():
            labelNumber = self.FirstNumber + SecondNumber
            newLabel = format(labelNumber, '.15g')
            self.display.setText(newLabel)
            self.button_add.setChecked(False)
        elif self.button_subtract.isChecked():
            labelNumber = self.FirstNumber - SecondNumber
            newLabel = format(labelNumber, '.15g')
            self.display.setText(newLabel)
            self.button_subtract.setChecked(False)
        elif self.button_multiply.isChecked():
            labelNumber = self.FirstNumber * SecondNumber
            newLabel = format(labelNumber, '.15g')
            self.display.setText(newLabel)
            self.button_multiply.setChecked(False)
        elif self.button_divide.isChecked():
            labelNumber = self.FirstNumber / SecondNumber
            newLabel = format(labelNumber, '.15g')
            self.display.setText(newLabel)
            self.button_divide.setChecked(False)

        self.UserIsTypingSecondNumber = False


    def clear_pressed(self):

        self.button_add.setChecked(False)
        self.button_subtract.setChecked(False)
        self.button_multiply.setChecked(False)
        self.button_divide.setChecked(False)

        self.UserIsTypingSecondNumber = False

        self.display.setText('0')