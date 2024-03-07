import sys
import binascii, os
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QPlainTextEdit, QFileDialog, QMessageBox
import joblib
import sqlite3
import requests
from vectorizer import *


class Window1(QDialog):
    def __init__(self):
        super(Window1, self).__init__()
        self.initUI()
    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.title = QtWidgets.QLabel(self)
        self.title.setText("AI INTERVIEW TRAINER")
        self.title.move(220, 30)
        self.title.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.title.setFont(QFont('Arial', 20))

        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.setText("LOGIN")
        self.login_btn.move(220, 250)
        self.login_btn.clicked.connect(self.login)
        self.login_btn.resize(100, 100)

        self.register_btn = QtWidgets.QPushButton(self)
        self.register_btn.setText("REGISTER")
        self.register_btn.move(420, 250)
        self.register_btn.clicked.connect(self.register)
        self.register_btn.resize(100, 100)

    def login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("LOGIN")

    def register(self):
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("REGISTER")

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("USERNAME")
        self.label1.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label1.move(250, 90)



        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(370, 90)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PASSWORD")
        self.label2.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label2.move(250, 180)

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(370, 180)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label3.move(220, 30)

        self.login_btn1 = QtWidgets.QPushButton(self)
        self.login_btn1.setText("LOGIN")
        self.login_btn1.move(300, 280)
        self.login_btn1.clicked.connect(self.loggedin)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(400, 350)
        self.back_btn.clicked.connect(self.back)

    def loggedin(self):

        user = self.lineedit1.text()
        pwd = self.lineedit2.text()
        if len(user) == 0 or len(pwd) == 0:
            self.label3.setText("Please input all fields.")
            self.label3.adjustSize()
        else:
            conn = sqlite3.connect("network.db")
            cur = conn.cursor()
            cur.execute("SELECT name FROM logins WHERE name=(?) AND password=(?)", [(user), (pwd)])
            result_pass = cur.fetchall()
            if len(result_pass) > 0:
                print("Successfully logged in.")
                self.label3.setText("")
                loggedin = Scan()
                widget.addWidget(loggedin)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                widget.setWindowTitle("DETECTION")
            else:
                self.label3.setText("Invalid username or password")
                self.label3.adjustSize()

    def back(self):
        back = Window1()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("AI INTERVIEW TRAINER")


class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("USERNAME")
        self.label1.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label1.move(250, 90)



        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(370, 90)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PASSWORD")
        self.label2.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label2.move(250, 180)

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit2.move(370, 180)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("PASSWORD")
        self.label3.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label3.move(250, 270)

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit3.move(370, 270)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label4.move(220,30)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(700, 20)
        self.back_btn.clicked.connect(self.back)

        self.r_btn = QtWidgets.QPushButton(self)
        self.r_btn.setText("REGISTER")
        self.r_btn.move(300, 350)
        self.r_btn.clicked.connect(self.register)

    def back(self):
        back = Window1()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("AI INTERVIEW TRAINER")

    def register(self):
        user = self.lineedit1.text()
        pwd = self.lineedit2.text()
        cpwd = self.lineedit3.text()
        if len(user) == 0 or len(pwd) == 0 or len(cpwd) == 0:
            self.label4.setText("Please fill in all inputs.")
            self.label4.adjustSize()

        elif pwd != cpwd:
            self.label4.setText("Passwords do not match.")
            self.label4.adjustSize()
        else:
            conn = sqlite3.connect("network.db")
            cur = conn.cursor()

            user_info = [user, pwd]
            cur.execute('INSERT INTO logins (name, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()
            self.label4.setText("Created user please login to continue")
            self.label4.adjustSize()

class Scan(QDialog):
    def __init__(self):
        super(Scan, self).__init__()
        self.initUI()

    def initUI(self):
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0, 0, 640, 480)
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))


        self.label2 = QtWidgets.QLabel(self)
        self.label2.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label2.move(250, 210)


        self.scan_btn = QtWidgets.QPushButton(self)
        self.scan_btn.setText("CHECK")
        self.scan_btn.move(370, 60)
        self.scan_btn.clicked.connect(self.check)
        self.scan_btn.resize(100, 100)

        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setText("BACK")
        self.back_btn.move(400, 350)
        self.back_btn.clicked.connect(self.back)

    def check(self):
        file_path, _ = QFileDialog.getOpenFileName()

        # Read the selected file
        with open(file_path, 'rb') as f:
            user_file = f.read()
        print(user_file)
        reuse(str(user_file))
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Response Status")
        messagebox.setText(f"QUESTIONS GENERATED ")
        messagebox.setIcon(QMessageBox.Information)
        messagebox.exec_()
    def message_cleaning(self, message):
        print('worked')

        #return Test_punc_removed_join_clean

    def back(self):
        back = Login()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("LOGIN")

app = QApplication(sys.argv)
welcome = Window1()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(400)
widget.setFixedWidth(640)
widget.setWindowTitle("AI INTERVIEW TRAINER")
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

