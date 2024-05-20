import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QTextEdit, \
    QListWidget, QCalendarWidget, QFormLayout, QMessageBox
from PyQt5.QtGui import QColor, QPalette


class Etkinlik:
    def __init__(self, etkinlik_adi, tarih, mekan, bilet_sayisi):
        self.etkinlik_adi = etkinlik_adi
        self.tarih = tarih
        self.mekan = mekan
        self.bilet_sayisi = bilet_sayisi
        self.biletler = []

    def etkinlik_ekle(self, etkinlik):
        # Etkinlik ekleme işlemleri
        pass

    def bilet_sat(self, bilet_miktari):
        # Bilet satışı işlemleri
        if self.bilet_sayisi >= bilet_miktari:
            bilet_numaralari = self.bilet_numarasi_uret(bilet_miktari)
            for bilet_numarasi in bilet_numaralari:
                bilet = Bilet(bilet_numarasi, self)
                self.biletler.append(bilet)
            self.bilet_sayisi -= bilet_miktari
            return True, bilet_numaralari
        else:
            return False, []

    def bilet_numarasi_uret(self, miktar):
        bilet_numaralari = []
        for _ in range(miktar):
            bilet_numarasi = ''.join(random.choices('0123456789', k=6))
            bilet_numaralari.append(bilet_numarasi)
        return bilet_numaralari


class Bilet:
    def __init__(self, bilet_numarasi, etkinlik):
        self.bilet_numarasi = bilet_numarasi
        self.etkinlik = etkinlik


class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.kalan_hak = 3

    def sifre_kontrol(self, girilen_sifre):
        if self.kalan_hak > 0:
            if girilen_sifre == self.sifre:
                return True
            else:
                self.kalan_hak -= 1
                QMessageBox.warning(None, "Uyarı", f"Yanlış şifre! {self.kalan_hak} adet hakkınız kaldı.")
                return False
        else:
            self.kilitlenme_baslat()
            return False

    def kilitlenme_baslat(self):
        QMessageBox.warning(None, "Kilitlendi", "Hesabınız geçici olarak kitlendi.")


class GirisSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('KültürBilet')
        self.setGeometry(100, 100, 300, 200)

        self.kullanici_adi_label = QLabel('Kullanıcı Adı:')
        self.kullanici_adi_input = QLineEdit()

        self.sifre_label = QLabel('Şifre:')
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.Password)

        self.giris_button = QPushButton('Giriş Yap')
        self.giris_button.clicked.connect(self.giris_kontrol)

        layout = QVBoxLayout()
        layout.addWidget(self.kullanici_adi_label)
        layout.addWidget(self.kullanici_adi_input)
        layout.addWidget(self.sifre_label)
        layout.addWidget(self.sifre_input)
        layout.addWidget(self.giris_button)

        self.setLayout(layout)

        # Arka plan rengini ayarla
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 204))
        self.setPalette(palette)

    def giris_kontrol(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()

        # Kullanıcı adı ve şifre kontrolü
        if kullanici_adi == "öğretmen":
            kullanici = Kullanici(kullanici_adi, "123")
            if kullanici.sifre_kontrol(sifre):
                etkinlikler = []
                self.etkinlik_arayuzu = EtkinlikArayuzu(etkinlikler)
                self.etkinlik_arayuzu.show()
                self.close()
        else:
            QMessageBox.warning(None, "Hata", "Böyle bir kullanıcı bulunamadı.")


class BiletIslemleriSayfasi(QWidget):
    def __init__(self, etkinlikler, ana_ekran):
        super().__init__()
        self.etkinlikler = etkinlikler
        self.ana_ekran = ana_ekran
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bilet İşlemleri')
        self.setGeometry(100, 100, 500, 300)

        self.etkinlikler_label = QLabel('Etkinlikler:')
        self.etkinlikler_listwidget = QListWidget()

        for etkinlik in self.etkinlikler:
            self.etkinlikler_listwidget.addItem(f"{etkinlik.etkinlik_adi} - {etkinlik.tarih} - {etkinlik.mekan}")

        self.bilet_miktari_label = QLabel('Bilet Miktarı:')
        self.bilet_miktari_input = QLineEdit()

        self.bilet_sat_button = QPushButton('Bilet Satın Al')
        self.bilet_sat_button.clicked.connect(self.bilet_sat)

        layout = QVBoxLayout()
        layout.addWidget(self.etkinlikler_label)
        layout.addWidget(self.etkinlikler_listwidget)
        layout.addWidget(self.bilet_miktari_label)
        layout.addWidget(self.bilet_miktari_input)
        layout.addWidget(self.bilet_sat_button)

        self.setLayout(layout)

        # Arka plan rengini ayarla
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(204, 255, 229))
        self.setPalette(palette)

    def bilet_sat(self):
        secilen_etkinlik_index = self.etkinlikler_listwidget.currentRow()
        if secilen_etkinlik_index != -1:
            secilen_etkinlik = self.etkinlikler[secilen_etkinlik_index]
            bilet_miktari = int(self.bilet_miktari_input.text())
            basarili, bilet_numaralari = secilen_etkinlik.bilet_sat(bilet_miktari)
            if basarili:
                QMessageBox.information(None, "Başarılı", "Bilet satın alma işlemi başarıyla tamamlandı.")
                self.ana_ekran.guncelle_bilet_listesi(secilen_etkinlik, bilet_numaralari)
            else:
                QMessageBox.warning(None, "Geçersiz", "Seçilen etkinlik için yeterli bilet yok.")
        else:
            QMessageBox.warning(None, "Hata", "Lütfen bir etkinlik seçin.")


class EtkinlikArayuzu(QWidget):
    def __init__(self, etkinlikler):
        super().__init__()
        self.etkinlikler = etkinlikler
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Etkinlik ve Bilet Satış Platformu')

        self.etkinlik_adi_label = QLabel('Etkinlik Adı:')
        self.etkinlik_adi_input = QLineEdit()

        self.tarih_label = QLabel('Tarih:')
        self.tarih_calendar = QCalendarWidget()

        self.mekan_label = QLabel('Mekan:')
        self.mekan_input = QLineEdit()

        self.bilet_sayisi_label = QLabel('Bilet Sayısı:')
        self.bilet_sayisi_input = QLineEdit()

        self.etkinlik_ekle_button = QPushButton('Etkinlik Ekle')
        self.etkinlik_ekle_button.clicked.connect(self.etkinlik_ekle)

        self.bilet_islemleri_button = QPushButton('Bilet İşlemleri')
        self.bilet_islemleri_button.clicked.connect(self.bilet_islemleri)

        self.etkinlikler_textbox = QTextEdit()
        self.etkinlikler_textbox.setReadOnly(True)

        self.etkinlikler_listwidget = QListWidget()

        layout = QFormLayout()
        layout.addRow(self.etkinlik_adi_label, self.etkinlik_adi_input)
        layout.addRow(self.tarih_label, self.tarih_calendar)
        layout.addRow(self.mekan_label, self.mekan_input)
        layout.addRow(self.bilet_sayisi_label, self.bilet_sayisi_input)
        layout.addWidget(self.etkinlik_ekle_button)
        layout.addWidget(self.bilet_islemleri_button)
        layout.addWidget(self.etkinlikler_textbox)
        layout.addWidget(self.etkinlikler_listwidget)

        self.setLayout(layout)

        # Arka plan rengini ayarla
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(204, 229, 255))
        self.setPalette(palette)

    def etkinlik_ekle(self):
        etkinlik_adi = self.etkinlik_adi_input.text()
        tarih = self.tarih_calendar.selectedDate().toString("dd.MM.yyyy")
        mekan = self.mekan_input.text()
        bilet_sayisi = self.bilet_sayisi_input.text()
        yeni_etkinlik = Etkinlik(etkinlik_adi, tarih, mekan, int(bilet_sayisi))
        self.etkinlikler.append(yeni_etkinlik)
        self.etkinlikler_textbox.append(
            f'Etkinlik Eklendi: {etkinlik_adi}, Tarih: {tarih}, Mekan: {mekan}, Bilet Sayısı: {bilet_sayisi}')

    def bilet_islemleri(self):
        self.bilet_islemleri_sayfasi = BiletIslemleriSayfasi(self.etkinlikler, self)
        self.bilet_islemleri_sayfasi.show()

    def guncelle_bilet_listesi(self, secilen_etkinlik, bilet_numaralari):
        self.etkinlikler_textbox.append(
            f'Bilet Satıldı: {secilen_etkinlik.etkinlik_adi}, Tarih: {secilen_etkinlik.tarih}, Mekan: {secilen_etkinlik.mekan}, Bilet Numaraları: {", ".join(bilet_numaralari)}'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = GirisSayfasi()
    giris_sayfasi.show()
    sys.exit(app.exec_())
