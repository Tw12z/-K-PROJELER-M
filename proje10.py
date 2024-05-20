import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QPlainTextEdit, QTabWidget

class Musteri:
    def __init__(self, adi, soyadi, tc, telno, urun_id):
        self.adi = adi
        self.soyadi = soyadi
        self.tc = tc
        self.telno = telno
        self.urunler = []
        self.urun_id = urun_id

    def urun_ekle(self, urun):
        self.urunler.append(urun)

    def urunleri_listele(self):
        return self.urunler

class MusteriYonetimi(QWidget):
    def __init__(self):
        super().__init__()

        self.musteri_listesi = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Müşteri İlişkileri Yönetimi")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.tab_musteri = QWidget()
        self.tab_widget.addTab(self.tab_musteri, "Müşteri Ekle")

        self.layout_musteri = QVBoxLayout()
        self.tab_musteri.setLayout(self.layout_musteri)

        self.label_adi = QLabel("Müşteri Adı:")
        self.lineedit_adi = QLineEdit()
        self.layout_musteri.addWidget(self.label_adi)
        self.layout_musteri.addWidget(self.lineedit_adi)

        self.label_soyadi = QLabel("Müşteri Soyadı:")
        self.lineedit_soyadi = QLineEdit()
        self.layout_musteri.addWidget(self.label_soyadi)
        self.layout_musteri.addWidget(self.lineedit_soyadi)

        self.label_tc = QLabel("Müşteri TcNo:")
        self.lineedit_tc = QLineEdit()
        self.layout_musteri.addWidget(self.label_tc)
        self.layout_musteri.addWidget(self.lineedit_tc)

        self.label_telno = QLabel("Müşteri TelNo:")
        self.lineedit_telno = QLineEdit()
        self.layout_musteri.addWidget(self.label_telno)
        self.layout_musteri.addWidget(self.lineedit_telno)

        self.label_urun_id = QLabel("Ürün ID:")
        self.lineedit_urun_id = QLineEdit()
        self.layout_musteri.addWidget(self.label_urun_id)
        self.layout_musteri.addWidget(self.lineedit_urun_id)

        self.label_urunler = QLabel("Ürünler:")
        self.plaintext_urunler = QPlainTextEdit()
        self.layout_musteri.addWidget(self.label_urunler)
        self.layout_musteri.addWidget(self.plaintext_urunler)

        self.button_ekle = QPushButton("Müşteri Ekle")
        self.button_ekle.clicked.connect(self.musteri_ekle)
        self.layout_musteri.addWidget(self.button_ekle)

        self.tab_liste = QWidget()
        self.tab_widget.addTab(self.tab_liste, "Müşteri Listesi")

        self.layout_liste = QVBoxLayout()
        self.tab_liste.setLayout(self.layout_liste)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)  # 6 sütun, biri daha eklendi
        self.table_widget.setHorizontalHeaderLabels(["Adı", "Soyadı", "TcNo", "TelNo", "Ürün ID", "Ürünler"])
        self.layout_liste.addWidget(self.table_widget)

        self.table_widget.cellClicked.connect(self.musteri_detay_goster)

    def musteri_ekle(self):
        adi = self.lineedit_adi.text()
        soyadi = self.lineedit_soyadi.text()
        tc = self.lineedit_tc.text()
        telno = self.lineedit_telno.text()
        urun_id = self.lineedit_urun_id.text()
        urunler = self.plaintext_urunler.toPlainText().split(", ")

        musteri = Musteri(adi, soyadi, tc, telno, urun_id)
        for urun in urunler:
            musteri.urun_ekle(urun)

        self.musteri_listesi.append(musteri)

        self.update_table()

    def update_table(self):
        self.table_widget.setRowCount(len(self.musteri_listesi))
        for i, musteri in enumerate(self.musteri_listesi):
            self.table_widget.setItem(i, 0, QTableWidgetItem(musteri.adi))
            self.table_widget.setItem(i, 1, QTableWidgetItem(musteri.soyadi))
            self.table_widget.setItem(i, 2, QTableWidgetItem(musteri.tc))
            self.table_widget.setItem(i, 3, QTableWidgetItem(musteri.telno))
            self.table_widget.setItem(i, 4, QTableWidgetItem(musteri.urun_id))
            self.table_widget.setItem(i, 5, QTableWidgetItem("\n".join(musteri.urunleri_listele())))

    def musteri_detay_goster(self, row, column):
        musteri = self.musteri_listesi[row]
        detay = f"Müşteri Adı: {musteri.adi}\nMüşteri Soyadı: {musteri.soyadi}\nMüşteri TcNo: {musteri.tc}\nMüşteri TelNo: {musteri.telno}\nÜrün ID: {musteri.urun_id}\nÜrünler: {', '.join(musteri.urunleri_listele())}"
        QMessageBox.information(self, "Müşteri Detayı", detay)

class Satis(QWidget):
    def __init__(self, musteri_yonetimi):
        super().__init__()
        self.musteri_yonetimi = musteri_yonetimi
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Satış Yönetimi")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.tab_ekle = QWidget()
        self.tab_widget.addTab(self.tab_ekle, "Ürün Ekle")

        self.layout_ekle = QVBoxLayout()
        self.tab_ekle.setLayout(self.layout_ekle)

        self.label_urun_kodu = QLabel("Ürün Kodu:")
        self.lineedit_urun_kodu = QLineEdit()
        self.layout_ekle.addWidget(self.label_urun_kodu)
        self.layout_ekle.addWidget(self.lineedit_urun_kodu)

        self.label_urun_adi = QLabel("Ürün Adı:")
        self.lineedit_urun_adi = QLineEdit()
        self.layout_ekle.addWidget(self.label_urun_adi)
        self.layout_ekle.addWidget(self.lineedit_urun_adi)

        self.label_urun_marka = QLabel("Ürün Marka:")
        self.lineedit_urun_marka = QLineEdit()
        self.layout_ekle.addWidget(self.label_urun_marka)
        self.layout_ekle.addWidget(self.lineedit_urun_marka)

        self.label_urun_adet = QLabel("Ürün Adet:")
        self.lineedit_urun_adet = QLineEdit()
        self.layout_ekle.addWidget(self.label_urun_adet)
        self.layout_ekle.addWidget(self.lineedit_urun_adet)

        self.label_urun_tarihi = QLabel("Ürün Tarihi:")
        self.lineedit_urun_tarihi = QLineEdit()
        self.layout_ekle.addWidget(self.label_urun_tarihi)
        self.layout_ekle.addWidget(self.lineedit_urun_tarihi)

        self.button_urun_ekle = QPushButton("Ürün Ekle")
        self.button_urun_ekle.clicked.connect(self.urun_ekle)
        self.layout_ekle.addWidget(self.button_urun_ekle)

        self.tab_liste = QWidget()
        self.tab_widget.addTab(self.tab_liste, "Ürün Listesi")

        self.layout_liste = QVBoxLayout()
        self.tab_liste.setLayout(self.layout_liste)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["Ürün Kodu", "Ürün Adı", "Ürün Marka", "Ürün Adet", "Ürün Tarihi"])
        self.layout_liste.addWidget(self.table_widget)

    def urun_ekle(self):
        urun_kodu = self.lineedit_urun_kodu.text()
        urun_adi = self.lineedit_urun_adi.text()
        urun_marka = self.lineedit_urun_marka.text()
        urun_adet = self.lineedit_urun_adet.text()
        urun_tarihi = self.lineedit_urun_tarihi.text()

        # Burada veritabanına ürün ekleme veya tabloya ekleme işlemleri yapılabilir

        self.guncelle_tablo(urun_kodu, urun_adi, urun_marka, urun_adet, urun_tarihi)

    def guncelle_tablo(self, urun_kodu, urun_adi, urun_marka, urun_adet, urun_tarihi):
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        self.table_widget.setItem(row_count, 0, QTableWidgetItem(urun_kodu))
        self.table_widget.setItem(row_count, 1, QTableWidgetItem(urun_adi))
        self.table_widget.setItem(row_count, 2, QTableWidgetItem(urun_marka))
        self.table_widget.setItem(row_count, 3, QTableWidgetItem(urun_adet))
        self.table_widget.setItem(row_count, 4, QTableWidgetItem(urun_tarihi))

    def urun_id_alan_musterileri_goster (self, urun_id):
        musteri_listesi = self.musteri_yonetimi.musteri_listesi
        urun_id_alan_musteriler = []

        for musteri in musteri_listesi:
            if urun_id in musteri.urunler:
                urun_id_alan_musteriler.append (musteri)

        if urun_id_alan_musteriler:
            QMessageBox.information (self, "Ürünü Alan Müşteriler", "\n\n".join ([f"Müşteri Adı: {musteri.adi}\nMüşteri Soyadı: {musteri.soyadi}\nMüşteri TcNo: {musteri.tc}\nMüşteri TelNo: {musteri.telno}\nÜrünler: {', '.join (musteri.urunleri_listele ())}"
                                                                                     for musteri in
                                                                                     urun_id_alan_musteriler]))
        else:
            QMessageBox.information (self, "Ürünü Alan Müşteriler", "Bu ürünü alan müşteri bulunamadı.")

class Destek(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Destek")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_talep_sahibi_adi = QLabel("Talep Sahibi Adı:")
        self.lineedit_talep_sahibi_adi = QLineEdit()
        self.layout.addWidget(self.label_talep_sahibi_adi)
        self.layout.addWidget(self.lineedit_talep_sahibi_adi)

        self.label_eposta = QLabel("E-Posta:")
        self.lineedit_eposta = QLineEdit()
        self.layout.addWidget(self.label_eposta)
        self.layout.addWidget(self.lineedit_eposta)

        self.label_destek_hatti = QLabel("Destek Hattı:")
        self.label_destek_hatti_auto = QLabel("212 88782")
        self.layout.addWidget(self.label_destek_hatti)
        self.layout.addWidget(self.label_destek_hatti_auto)

        self.label_talep = QLabel("Destek Talep Sebebi:")
        self.lineedit_talep = QLineEdit()
        self.layout.addWidget(self.label_talep)
        self.layout.addWidget(self.lineedit_talep)

        self.button_gonder = QPushButton("Gönder")
        self.button_gonder.clicked.connect(self.gonder)
        self.layout.addWidget(self.button_gonder)
        self.label_talep_sonuc = QLabel("")
        self.layout.addWidget(self.label_talep_sonuc)

    def gonder(self):
        self.label_talep_sonuc.setText("Talep gönderildi")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    musteri_yonetimi = MusteriYonetimi()
    musteri_yonetimi.show()
    satis_sinifi = Satis(musteri_yonetimi)
    satis_sinifi.show()
    destek_sinifi = Destek()
    destek_sinifi.show()

    sys.exit(app.exec_())
