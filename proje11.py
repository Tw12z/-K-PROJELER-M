import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot

class Enstruman():
    def __init__(self, adi, fiyat, stok):
        self.adi = adi
        self.fiyat = fiyat
        self.stok = stok

class Satis():
    def __init__(self, siparis_no, siparis_tarih, satilan_enstruman, teslimat_adresi):
        self.siparis_no = siparis_no
        self.siparis_tarih = siparis_tarih
        self.satilan_enstruman = satilan_enstruman
        self.teslimat_adresi = teslimat_adresi

class SatisEkleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Satış Ekle')
        self.layout = QVBoxLayout()

        self.label_siparis_no = QLabel('Sipariş No:')
        self.edit_siparis_no = QLineEdit()
        self.layout.addWidget(self.label_siparis_no)
        self.layout.addWidget(self.edit_siparis_no)

        self.label_siparis_tarih = QLabel('Sipariş Tarihi:')
        self.edit_siparis_tarih = QLineEdit()
        self.layout.addWidget(self.label_siparis_tarih)
        self.layout.addWidget(self.edit_siparis_tarih)

        self.label_satilan_enstruman = QLabel('Satılan Enstrüman:')
        self.edit_satilan_enstruman = QLineEdit()
        self.layout.addWidget(self.label_satilan_enstruman)
        self.layout.addWidget(self.edit_satilan_enstruman)

        self.label_teslimat_adresi = QLabel('Teslimat Adresi:')
        self.edit_teslimat_adresi = QLineEdit()
        self.layout.addWidget(self.label_teslimat_adresi)
        self.layout.addWidget(self.edit_teslimat_adresi)

        self.button_ekle = QPushButton('EKLE')
        self.button_ekle.clicked.connect(self.ekle)
        self.layout.addWidget(self.button_ekle)

        self.setLayout(self.layout)

    def ekle(self):
        self.parent().satis_ekle(self.edit_siparis_no.text(), self.edit_siparis_tarih.text(),
                                  self.edit_satilan_enstruman.text(), self.edit_teslimat_adresi.text())
        self.close()

class EnstrumanDukkani(QWidget):
    def __init__(self):
        super().__init__()

        self.enstrumanlar = []
        self.satislar = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Müzik Enstrümanları Dükkanı Yönetim Programı')

        # Enstrümanlar tablosu
        self.table_enstrumanlar = QTableWidget()
        self.table_enstrumanlar.setColumnCount(3)  # Üç sütun
        self.table_enstrumanlar.setHorizontalHeaderLabels(["Enstrüman Adı", "Fiyat", "Stok Miktarı"])

        # Satışlar tablosu
        self.table_satislar = QTableWidget()
        self.table_satislar.setColumnCount(4)  # Dört sütun
        self.table_satislar.setHorizontalHeaderLabels(["Sipariş No", "Sipariş Tarihi", "Satılan Enstrüman", "Teslimat Adresi"])

        # Ekleme bileşenleri
        self.label_adi = QLabel('Enstrüman Adı:')
        self.edit_adi = QLineEdit()

        self.label_fiyat = QLabel('Enstrüman Fiyatı:')
        self.edit_fiyat = QLineEdit()

        self.label_stok = QLabel('Stok Miktarı:')
        self.edit_stok = QLineEdit()

        self.button_ekle_enstruman = QPushButton('ENSTRÜMAN EKLE')
        self.button_ekle_enstruman.clicked.connect(self.enstruman_ekle)

        self.button_ekle_satis = QPushButton('SATIŞ EKLE')
        self.button_ekle_satis.clicked.connect(self.ac_satis_ekle_dialog)

        # Layout
        vbox = QVBoxLayout()

        hbox_enstrumanlar = QHBoxLayout()
        hbox_enstrumanlar.addWidget(self.table_enstrumanlar)

        hbox_satislar = QHBoxLayout()
        hbox_satislar.addWidget(self.table_satislar)

        hbox_adi = QHBoxLayout()
        hbox_adi.addWidget(self.label_adi)
        hbox_adi.addWidget(self.edit_adi)

        hbox_fiyat = QHBoxLayout()
        hbox_fiyat.addWidget(self.label_fiyat)
        hbox_fiyat.addWidget(self.edit_fiyat)

        hbox_stok = QHBoxLayout()
        hbox_stok.addWidget(self.label_stok)
        hbox_stok.addWidget(self.edit_stok)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.button_ekle_enstruman)
        hbox_buttons.addWidget(self.button_ekle_satis)

        vbox.addLayout(hbox_adi)
        vbox.addLayout(hbox_fiyat)
        vbox.addLayout(hbox_stok)
        vbox.addLayout(hbox_buttons)
        vbox.addLayout(hbox_enstrumanlar)
        vbox.addLayout(hbox_satislar)

        self.setLayout(vbox)

        # Sinyal-slot bağlantıları
        self.table_enstrumanlar.cellClicked.connect(self.enstruman_bilgisi_goster)
        self.table_satislar.cellClicked.connect(self.satis_bilgisi_goster)

    def enstruman_ekle(self):
        adi = self.edit_adi.text()
        fiyat = self.edit_fiyat.text()
        stok = self.edit_stok.text()

        enstruman = Enstruman(adi, fiyat, stok)
        self.enstrumanlar.append(enstruman)

        row_count = self.table_enstrumanlar.rowCount()
        self.table_enstrumanlar.insertRow(row_count)
        self.table_enstrumanlar.setItem(row_count, 0, QTableWidgetItem(adi))
        self.table_enstrumanlar.setItem(row_count, 1, QTableWidgetItem(fiyat))
        self.table_enstrumanlar.setItem(row_count, 2, QTableWidgetItem(stok))

    def ac_satis_ekle_dialog(self):
        dialog = SatisEkleDialog(self)
        dialog.exec_()

    def satis_ekle(self, siparis_no, siparis_tarih, satilan_enstruman, teslimat_adresi):
        satis = Satis(siparis_no, siparis_tarih, satilan_enstruman, teslimat_adresi)
        self.satislar.append(satis)

        row_count = self.table_satislar.rowCount()
        self.table_satislar.insertRow(row_count)
        self.table_satislar.setItem(row_count, 0, QTableWidgetItem(siparis_no))
        self.table_satislar.setItem(row_count, 1, QTableWidgetItem(siparis_tarih))
        self.table_satislar.setItem(row_count, 2, QTableWidgetItem(satilan_enstruman))
        self.table_satislar.setItem(row_count, 3, QTableWidgetItem(teslimat_adresi))

    @pyqtSlot(int, int)
    def enstruman_bilgisi_goster(self, row, column):
        if column == 0:  # Eğer Enstrüman Adı sütununda bir hücreye tıklanırsa
            enstruman_adi = self.table_enstrumanlar.item(row, column).text()
            for enstruman in self.enstrumanlar:
                if enstruman.adi == enstruman_adi:
                    bilgi = f"Enstrüman Adı: {enstruman.adi}\nFiyat: {enstruman.fiyat}\nStok Miktarı: {enstruman.stok}"
                    QMessageBox.information(self, "Enstrüman Bilgisi", bilgi)

    @pyqtSlot(int, int)
    def satis_bilgisi_goster(self, row, column):
        if column == 0:  # Eğer Sipariş No sütununda bir hücreye tıklanırsa
            siparis_no = self.table_satislar.item(row, column).text()
            for satis in self.satislar:
                if satis.siparis_no == siparis_no:
                    bilgi = f"Sipariş No: {satis.siparis_no}\nSipariş Tarihi: {satis.siparis_tarih}\nSatılan Enstrüman: {satis.satilan_enstruman}\nTeslimat Adresi: {satis.teslimat_adresi}"
                    QMessageBox.information(self, "Satış Bilgisi", bilgi)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EnstrumanDukkani()
    window.show()
    sys.exit(app.exec_())
