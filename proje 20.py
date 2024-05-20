import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QInputDialog, QTextEdit, QDialog, QDialogButtonBox, QHBoxLayout, QSlider, QTextBrowser
from PyQt5.QtCore import Qt

class Oyun:
    def __init__(self, adi, turu, platformu):
        self.adi = adi
        self.turu = turu
        self.platformu = platformu
        self.yorum = ""
        self.yildiz = 0

class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

    def oyun_listele(self):
        for oyun in self.oyunlar:
            print("{} ({}) - {} - Yıldız: {}".format(oyun.adi, oyun.turu, oyun.platformu, oyun.yildiz))

class Oyuncu:
    def __init__(self, adi):
        self.adi = adi
        self.koleksiyon = Koleksiyon()
        self.favori_oyunlar = []

    def oyun_ekle(self, oyun):
        self.koleksiyon.oyun_ekle(oyun)

    def yildiz_ver(self, oyun, yildiz):
        oyun.yildiz = yildiz
        self.sirala_favori_oyunlar()

    def sirala_favori_oyunlar(self):
        self.favori_oyunlar = sorted(self.koleksiyon.oyunlar, key=lambda oyun: oyun.yildiz, reverse=True)

class YorumEkleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Yorum Ekle")
        self.layout = QVBoxLayout()

        self.yorum_edit = QTextEdit()
        self.yorum_edit.setPlaceholderText("Yorumunuzu buraya yazınız...")
        self.layout.addWidget(self.yorum_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

        self.setLayout(self.layout)

    def get_yorum(self):
        return self.yorum_edit.toPlainText()

class FavoriOyunlarDialog(QDialog):
    def __init__(self, oyuncu, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Favori Oyunlar")
        self.layout = QVBoxLayout()

        self.browser = QTextBrowser()
        self.browser.setPlainText("\n".join("{} ({}) - {} - Yıldız: {}".format(oyun.adi, oyun.turu, oyun.platformu, oyun.yildiz) for oyun in oyuncu.favori_oyunlar))
        self.layout.addWidget(self.browser)

        self.setLayout(self.layout)

class YorumlarDialog(QDialog):
    def __init__(self, oyuncu, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oyun Yorumları")
        self.layout = QVBoxLayout()

        self.browser = QTextBrowser()
        self.browser.setPlainText("\n\n".join("{}\nYorum: {}\n".format(oyun.adi, oyun.yorum) for oyun in oyuncu.koleksiyon.oyunlar if oyun.yorum))
        self.layout.addWidget(self.browser)

        self.setLayout(self.layout)

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Oyun Koleksiyonu Yönetimi")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.label = QLabel("Oyun Koleksiyonu Yönetimi")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Oyun Ekle")
        self.button.clicked.connect(self.oyun_ekle)
        self.layout.addWidget(self.button)

        self.favori_button = QPushButton("Favori Oyunlarım")
        self.favori_button.clicked.connect(self.show_favori_oyunlar)
        self.layout.addWidget(self.favori_button)

        self.yorumlar_button = QPushButton("Oyun Yorumları")
        self.yorumlar_button.clicked.connect(self.show_yorumlar)
        self.layout.addWidget(self.yorumlar_button)

        self.game_widgets = []

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.oyuncu = Oyuncu("Ahmet")
        self.oyuncu.oyun_ekle(Oyun("The Witcher 3", "RPG", "PC"))
        self.oyuncu.oyun_ekle(Oyun("Super Mario Odyssey", "Platform", "Nintendo Switch"))

        # Rastgele 6 oyun ekle
        oyunlar = [("Red Dead Redemption 2", "Aksiyon", "PC"), 
                   ("FIFA 21", "Spor", "PlayStation 4"), 
                   ("The Legend of Zelda: Breath of the Wild", "Aksiyon", "Nintendo Switch"),
                   ("Minecraft", "Sandbox", "PC"), 
                   ("Cyberpunk 2077", "RPG", "PC"), 
                   ("Grand Theft Auto V", "Aksiyon", "PC")]
        for oyun in oyunlar:
            self.oyuncu.oyun_ekle(Oyun(*oyun))

        self.update_game_widgets()

    def update_game_widgets(self):
        for widget in self.game_widgets:
            self.layout.removeWidget(widget)
            widget.deleteLater()
        self.game_widgets = []

        for oyun in self.oyuncu.koleksiyon.oyunlar:
            label = QLabel("{} ({}) - {} - Yıldız: {}".format(oyun.adi, oyun.turu, oyun.platformu, oyun.yildiz))
            self.layout.addWidget(label)
            self.game_widgets.append(label)

            yildiz_slider = QSlider(Qt.Horizontal)
            yildiz_slider.setMinimum(0)
            yildiz_slider.setMaximum(5)
            yildiz_slider.setValue(oyun.yildiz)
            yildiz_slider.valueChanged.connect(lambda value, oyun=oyun: self.yildiz_ver(oyun, value))
            self.layout.addWidget(yildiz_slider)
            self.game_widgets.append(yildiz_slider)

            yorum_button = QPushButton("Yorum Ekle")
            yorum_button.clicked.connect(lambda checked, oyun=oyun: self.yorum_ekle(oyun))
            self.layout.addWidget(yorum_button)
            self.game_widgets.append(yorum_button)

    def oyun_ekle(self):
        oyun_adi, ok = QInputDialog.getText(self, "Oyun Ekle", "Oyun adı:")
        if ok:
            oyun_turu, ok = QInputDialog.getText(self, "Oyun Ekle", "Oyun türü:")
            if ok:
                oyun_platformu, ok = QInputDialog.getText(self, "Oyun Ekle", "Oyun platformu:")
                if ok:
                    oyun = Oyun(oyun_adi, oyun_turu, oyun_platformu)
                    self.oyuncu.oyun_ekle(oyun)
                    self.update_game_widgets()

    def yildiz_ver(self, oyun, yildiz):
        self.oyuncu.yildiz_ver(oyun, yildiz)
        self.update_game_widgets()

    def yorum_ekle(self, oyun):
        dialog = YorumEkleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            yorum = dialog.get_yorum()
            oyun.yorum = yorum
            self.update_game_widgets()

    def show_favori_oyunlar(self):
        dialog = FavoriOyunlarDialog(self.oyuncu, self)
        dialog.exec_()

    def show_yorumlar(self):
        dialog = YorumlarDialog(self.oyuncu, self)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec_())
