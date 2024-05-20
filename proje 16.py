import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QInputDialog, QMessageBox, QComboBox, QDialog, QDateEdit, QGroupBox, QFormLayout, QLineEdit, QListView, QProgressBar
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Film:
    def __init__(self, ad, yonetmen, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.tur = tur
        self.izleme_durumu = 0

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.izleme_gecmisi = []

class FilmServisi(QWidget):
    def __init__(self):
        super().__init__()

        self.film_listesi = []
        self.kullanici = Kullanici("kullanici", "sifre")

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Film ve Dizi İzleme Servisi")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label_baslik = QLabel("Film ve Dizi İzleme Servisi")
        self.label_baslik.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.label_baslik)

        self.button_film_ekle = QPushButton("Film Ekle")
        self.button_film_ekle.clicked.connect(self.film_ekle_dialog_ac)
        layout.addWidget(self.button_film_ekle)

        self.button_filmleri_listele = QPushButton("Filmleri Listele")
        self.button_filmleri_listele.clicked.connect(self.filmleri_listele)
        layout.addWidget(self.button_filmleri_listele)

        self.button_izleme_listesi_olustur = QPushButton("İzleme Listesi Oluştur")
        self.button_izleme_listesi_olustur.clicked.connect(self.izleme_listesi_olustur)
        layout.addWidget(self.button_izleme_listesi_olustur)

        self.button_izleme_gecmisi = QPushButton("İzleme Geçmişi")
        self.button_izleme_gecmisi.clicked.connect(self.izleme_gecmisi_goster)
        layout.addWidget(self.button_izleme_gecmisi)

        self.setLayout(layout)

    def film_ekle_dialog_ac(self):
        dialog = QDialog()
        dialog.setWindowTitle("Film Ekle")

        layout = QFormLayout()

        self.line_edit_film_ad = QLineEdit()
        layout.addRow("Film Adı:", self.line_edit_film_ad)

        self.line_edit_yonetmen = QLineEdit()
        layout.addRow("Yönetmen:", self.line_edit_yonetmen)

        self.combo_box_tur = QComboBox()
        self.combo_box_tur.addItems(["Aksiyon", "Komedi", "Fantezi", "Korku", "Aşk", "Bilim Kurgu", "Western", "Müzikal"])
        layout.addRow("Tür:", self.combo_box_tur)

        button_kaydet = QPushButton("Kaydet")
        button_kaydet.clicked.connect(self.film_ekle)
        layout.addRow(button_kaydet)

        dialog.setLayout(layout)
        dialog.exec_()

    def film_ekle(self):
        film_ad = self.line_edit_film_ad.text()
        yonetmen = self.line_edit_yonetmen.text()
        tur = self.combo_box_tur.currentText()

        film = Film(film_ad, yonetmen, tur)
        self.film_listesi.append(film)

        QMessageBox.information(self, "Başarılı", "Film başarıyla eklendi.")

    def filmleri_listele(self):
        dialog = QDialog()
        dialog.setWindowTitle("Filmleri Listele")

        layout = QVBoxLayout()

        list_widget_filmler = QListWidget()
        for film in self.film_listesi:
            list_widget_filmler.addItem(film.ad + " - " + film.yonetmen + " - " + film.tur)
        list_widget_filmler.itemClicked.connect(self.izlemeye_basla)
        layout.addWidget(list_widget_filmler)

        dialog.setLayout(layout)
        dialog.exec_()

    def izlemeye_basla(self, item):
        film_ad = item.text().split(" - ")[0]
        for film in self.film_listesi:
            if film.ad == film_ad:
                progress = QInputDialog.getInt(self, "İlerleme Durumu", "İzleme Durumu:", 0, 0, 100)
                film.izleme_durumu = progress[0]
                QMessageBox.information(self, "Başarılı", "İzleme durumu kaydedildi.")

    def izleme_listesi_olustur(self):
        dialog = QDialog()
        dialog.setWindowTitle("İzleme Listesi Oluştur")

        layout = QVBoxLayout()

        list_view_filmler = QListView()
        model = QStandardItemModel()
        for film in self.film_listesi:
            item = QStandardItem(film.ad + " - " + film.yonetmen + " - " + film.tur)
            item.setCheckable(True)
            model.appendRow(item)
        list_view_filmler.setModel(model)

        button_olustur = QPushButton("Oluştur")
        button_olustur.clicked.connect(lambda: self.izleme_listesi_kaydet(model))
        layout.addWidget(list_view_filmler)
        layout.addWidget(button_olustur)

        dialog.setLayout(layout)
        dialog.exec_()

    def izleme_listesi_kaydet(self, model):
        for row in range(model.rowCount()):
            item = model.item(row)
            if item.checkState() == 2:
                film_ad = item.text().split(" - ")[0]
                for film in self.film_listesi:
                    if film.ad == film_ad:
                        self.kullanici.izleme_gecmisi.append(film)
        QMessageBox.information(self, "Başarılı", "İzleme listesi oluşturuldu.")

    def izleme_gecmisi_goster(self):
        dialog = QDialog()
        dialog.setWindowTitle("İzleme Geçmişi")

        layout = QVBoxLayout()

        list_widget_gecmis = QListWidget()
        for film in self.kullanici.izleme_gecmisi:
            list_widget_gecmis.addItem(film.ad + " - " + film.yonetmen + " - " + film.tur + " (%" + str(film.izleme_durumu) + " izlendi)")
        layout.addWidget(list_widget_gecmis)

        dialog.setLayout(layout)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    film_servisi = FilmServisi()
    film_servisi.show()
    sys.exit(app.exec_())

