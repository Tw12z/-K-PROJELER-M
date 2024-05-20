import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QComboBox
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Öğrenci ve Öğretmen Girişi'
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        font = QFont()
        font.setPointSize(10)

        self.lbl_username = QLabel('Kullanıcı Adı:', self)
        self.lbl_username.setFont(font)
        self.lbl_username.move(50, 50)

        self.lbl_password = QLabel('Şifre:', self)
        self.lbl_password.setFont(font)
        self.lbl_password.move(50, 100)

        self.txt_username = QLineEdit(self)
        self.txt_username.setFont(font)
        self.txt_username.move(150, 50)
        self.txt_username.resize(200, 30)

        self.txt_password = QLineEdit(self)
        self.txt_password.setFont(font)
        self.txt_password.move(150, 100)
        self.txt_password.resize(200, 30)
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton('Giriş', self)
        self.btn_login.setFont(font)
        self.btn_login.move(150, 150)
        self.btn_login.resize(100, 30)
        self.btn_login.clicked.connect(self.login)

    def login(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        # Örnek kullanıcı adı ve şifreleri
        student_credentials = {'öğrenci1': '123', 'öğrenci2': '456'}
        teacher_credentials = {'öğretmen1': 'abc', 'öğretmen2': 'def'}

        if (username, password) in student_credentials.items():
            self.openStudentMenu()
        elif (username, password) in teacher_credentials.items():
            self.openTeacherMenu()
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre!')

    def openStudentMenu(self):
        self.student_window = StudentWindow()
        self.student_window.show()
        self.close()

    def openTeacherMenu(self):
        self.teacher_window = TeacherWindow()
        self.teacher_window.show()
        self.close()

class StudentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Öğrenci Menüsü'
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        font = QFont()
        font.setPointSize(10)

        self.lbl_material = QLabel('Konu Anlatımı:', self)
        self.lbl_material.setFont(font)
        self.lbl_material.move(50, 50)

        self.cmb_subjects = QComboBox(self)
        self.cmb_subjects.setFont(font)
        self.cmb_subjects.addItems(['Matematik', 'Geometri', 'Fizik'])
        self.cmb_subjects.move(150, 50)
        self.cmb_subjects.resize(200, 30)

        self.txt_material = QTextEdit(self)
        self.txt_material.setFont(font)
        self.txt_material.move(50, 100)
        self.txt_material.resize(500, 200)
        self.txt_material.setReadOnly(True)

        self.btn_view = QPushButton('Görüntüle', self)
        self.btn_view.setFont(font)
        self.btn_view.move(250, 320)
        self.btn_view.resize(100, 30)
        self.btn_view.clicked.connect(self.view_material)

        self.btn_logout = QPushButton('Çıkış Yap', self)
        self.btn_logout.setFont(font)
        self.btn_logout.move(400, 320)
        self.btn_logout.resize(100, 30)
        self.btn_logout.clicked.connect(self.logout)

    def view_material(self):
        subject = self.cmb_subjects.currentText()
        # Öğretmenden alınan konu anlatımını burada göster
        if subject in TeacherWindow.materials:
            self.txt_material.setText(TeacherWindow.materials[subject])
        else:
            QMessageBox.warning(self, 'Hata', 'Konu anlatımı bulunamadı!')

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class TeacherWindow(QWidget):
    materials = {}

    def __init__(self):
        super().__init__()
        self.title = 'Öğretmen Menüsü'
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        font = QFont()
        font.setPointSize(10)

        self.lbl_upload = QLabel('Konu Anlatımı Yükle:', self)
        self.lbl_upload.setFont(font)
        self.lbl_upload.move(50, 50)

        self.cmb_subjects = QComboBox(self)
        self.cmb_subjects.setFont(font)
        self.cmb_subjects.addItems(['Matematik', 'Geometri', 'Fizik'])
        self.cmb_subjects.move(200, 50)
        self.cmb_subjects.resize(200, 30)

        self.txt_upload = QTextEdit(self)
        self.txt_upload.setFont(font)
        self.txt_upload.move(50, 100)
        self.txt_upload.resize(500, 200)

        self.btn_upload = QPushButton('Yükle', self)
        self.btn_upload.setFont(font)
        self.btn_upload.move(250, 320)
        self.btn_upload.resize(100, 30)
        self.btn_upload.clicked.connect(self.upload)

        self.btn_logout = QPushButton('Çıkış Yap', self)
        self.btn_logout.setFont(font)
        self.btn_logout.move(400, 320)
        self.btn_logout.resize(100, 30)
        self.btn_logout.clicked.connect(self.logout)

    def upload(self):
        subject = self.cmb_subjects.currentText()
        material = self.txt_upload.toPlainText()
        self.materials[subject] = material
        QMessageBox.information(self, 'Başarılı', '{} konu anlatımı yüklendi!'.format(subject))

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
