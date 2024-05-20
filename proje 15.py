import sys
from PyQt5.QtCore import Qt  # Qt modülünü içe aktar

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QListWidget, QDialog, QLineEdit, QHBoxLayout, QTextEdit, QMessageBox, QInputDialog, QProgressBar, QFrame
from PyQt5.QtGui import QFont, QColor

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.comments = []
        self.rating = None
        self.progress = 0

    def add_comment(self, comment):
        self.comments.append(comment)

class BookReadingPlatform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çevrimiçi Kitap Okuma ve Paylaşım Platformu")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Kitap Listesi")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.label)

        self.book_list = QListWidget()
        self.book_list.itemClicked.connect(self.show_book_details)
        self.layout.addWidget(self.book_list)

        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.books = []
        self.users = [User("öğretmen", "123"), User("öğrenci", "123")]

        self.current_user = None

    def login(self):
        username, ok = QInputDialog.getText(self, "Giriş", "Kullanıcı Adı:")
        if ok and username:
            password, ok = QInputDialog.getText(self, "Giriş", "Şifre:", QLineEdit.Password)
            if ok and password:
                for user in self.users:
                    if user.username == username and user.password == password:
                        self.current_user = user
                        QMessageBox.information(self, "Giriş Başarılı", "Hoş geldiniz, {}!".format(username))
                        self.show_add_book_button()
                        return
                QMessageBox.warning(self, "Giriş Başarısız", "Kullanıcı adı veya şifre yanlış.")

    def show_add_book_button(self):
        if self.current_user:
            self.add_book_button = QPushButton("Kitap Ekle")
            self.add_book_button.clicked.connect(self.add_book_dialog)
            self.layout.addWidget(self.add_book_button)

    def add_book_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Kitap Ekle")
        dialog.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        title_label = QLabel("Kitap Adı:")
        layout.addWidget(title_label)

        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        author_label = QLabel("Yazarı:")
        layout.addWidget(author_label)

        self.author_input = QLineEdit()
        layout.addWidget(self.author_input)

        publisher_label = QLabel("Yayınevi:")
        layout.addWidget(publisher_label)

        self.publisher_input = QLineEdit()
        layout.addWidget(self.publisher_input)

        add_button = QPushButton("Ekle")
        add_button.clicked.connect(lambda: self.add_book(dialog))
        layout.addWidget(add_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def add_book(self, dialog):
        title = self.title_input.text()
        author = self.author_input.text()
        publisher = self.publisher_input.text()

        if title and author and publisher:
            book = Book(title, author, publisher)
            self.books.append(book)
            self.update_book_list()
            dialog.close()

    def update_book_list(self):
        self.book_list.clear()
        for book in self.books:
            item = "{} - {}".format(book.title, "Puan: {}".format(book.rating) if book.rating else "Puan: -")
            self.book_list.addItem(item)

    def show_book_details(self, item):
        if not self.current_user:
            QMessageBox.warning(self, "Uyarı", "Giriş yapmadınız. Lütfen giriş yapın.")
            return

        selected_book_title = item.text().split(" - ")[0]
        for book in self.books:
            if book.title == selected_book_title:
                dialog = QDialog(self)
                dialog.setWindowTitle(book.title)
                dialog.setGeometry(300, 300, 400, 300)

                layout = QVBoxLayout()

                author_label = QLabel("Yazarı: " + book.author)
                layout.addWidget(author_label)

                publisher_label = QLabel("Yayınevi: " + book.publisher)
                layout.addWidget(publisher_label)

                comments_label = QLabel("Yorumlar:")
                layout.addWidget(comments_label)

                self.comments_list = QListWidget()
                for comment in book.comments:
                    self.comments_list.addItem(comment)
                layout.addWidget(self.comments_list)

                self.comment_input = QTextEdit()
                layout.addWidget(self.comment_input)

                add_comment_button = QPushButton("Yorum Yap")
                add_comment_button.clicked.connect(lambda: self.add_comment(book))
                layout.addWidget(add_comment_button)

                remove_comment_button = QPushButton("Yorumları Sil")
                remove_comment_button.clicked.connect(lambda: self.remove_comment(book))
                layout.addWidget(remove_comment_button)

                rate_button = QPushButton("Kitaba Puan Ver")
                rate_button.clicked.connect(lambda: self.rate_book(book))
                layout.addWidget(rate_button)

                read_button = QPushButton("Kitabı Oku")
                read_button.clicked.connect(lambda: self.read_book(book))
                layout.addWidget(read_button)

                self.progress_bar = QProgressBar()
                layout.addWidget(self.progress_bar)

                dialog.setLayout(layout)
                dialog.exec_()

    def add_comment(self, book):
        comment = self.comment_input.toPlainText()
        if comment:
            book.add_comment(comment)
            self.comments_list.addItem(comment)
            self.comment_input.clear()

    def remove_comment(self, book):
        selected_comment = self.comments_list.currentItem()
        if selected_comment:
            index = self.comments_list.row(selected_comment)
            del book.comments[index]
            self.comments_list.takeItem(index)

    def rate_book(self, book):
        if book.progress == 100:
            rating, ok = QInputDialog.getInt(self, "Kitaba Puan Ver", "Puan (1-5):", 1, 1, 5)
            if ok:
                book.rating = rating
                self.update_book_list()
                QMessageBox.information(self, "Bilgi", "Kitaba {} puan verildi.".format(rating))
        else:
            QMessageBox.warning(self, "Uyarı", "Kitabı okumadan puan veremezsiniz.")

    def read_book(self, book):
        progress, ok = QInputDialog.getInt(self, "Kitabı Oku", "Okuma İlerlemesi (%):", 0, 0, 100)
        if ok:
            book.progress = progress
            self.progress_bar.setValue(progress)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookReadingPlatform()
    window.show()
    sys.exit(app.exec_())
