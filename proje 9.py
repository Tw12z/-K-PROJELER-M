import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QLabel, QTabWidget


class SeyahatPlanlamaUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Seyahat Planlama Uygulaması')

        self.tur_incele = []
        self.tur_sec = []
        self.tur_iptal = []

        self.layout = QVBoxLayout()

        self.tab_widget = QTabWidget()

        self.tab_seyahat = QWidget()
        self.init_seyahat_tab_ui()

        self.tab_rota = QWidget()
        self.init_rota_tab_ui()

        self.tab_widget.addTab(self.tab_seyahat, 'Seyahat Planlama')
        self.tab_widget.addTab(self.tab_rota, 'Rota Planlama')

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        self.show()

    def init_seyahat_tab_ui(self):
        layout_seyahat = QVBoxLayout()

        self.checkbox_mavi_tur = QCheckBox('Mavi Tur', self)
        self.checkbox_mavi_tur.stateChanged.connect(self.tur_secildi)
        layout_seyahat.addWidget(self.checkbox_mavi_tur)

        self.checkbox_avrupa_turu = QCheckBox('Avrupa Turu', self)
        self.checkbox_avrupa_turu.stateChanged.connect(self.tur_secildi)
        layout_seyahat.addWidget(self.checkbox_avrupa_turu)

        self.checkbox_asya_turu = QCheckBox('Asya Turu', self)
        self.checkbox_asya_turu.stateChanged.connect(self.tur_secildi)
        layout_seyahat.addWidget(self.checkbox_asya_turu)

        self.button_tur_incele = QPushButton('Tur İncele', self)
        self.button_tur_incele.clicked.connect(self.tur_incele_clicked)
        layout_seyahat.addWidget(self.button_tur_incele)

        self.button_tur_sec = QPushButton('Tur Seç', self)
        self.button_tur_sec.clicked.connect(self.tur_sec_clicked)
        layout_seyahat.addWidget(self.button_tur_sec)

        self.button_tur_iptal = QPushButton('Tur İptal', self)
        self.button_tur_iptal.clicked.connect(self.tur_iptal_clicked)
        layout_seyahat.addWidget(self.button_tur_iptal)

        self.label_tur_secildi = QLabel(self)
        layout_seyahat.addWidget(self.label_tur_secildi)

        self.tab_seyahat.setLayout(layout_seyahat)

    def init_rota_tab_ui(self):
        layout_rota = QVBoxLayout()

        self.arac_incele = []
        self.arac_sec = []
        self.arac_degistir = []

        self.checkbox_araclar = []
        araclar = ['Uçak', 'Tren', 'Otomobil', 'Otobüs']

        for arac in araclar:
            checkbox_arac = QCheckBox(arac, self)
            checkbox_arac.stateChanged.connect(self.arac_secildi)
            layout_rota.addWidget(checkbox_arac)
            self.checkbox_araclar.append(checkbox_arac)

        self.button_arac_sec = QPushButton('Araç Seç', self)
        self.button_arac_sec.clicked.connect(self.arac_sec_clicked)
        layout_rota.addWidget(self.button_arac_sec)

        self.button_arac_incele = QPushButton('Araç İncele', self)
        self.button_arac_incele.clicked.connect(self.arac_incele_clicked)
        layout_rota.addWidget(self.button_arac_incele)

        self.button_arac_degistir = QPushButton('Araç Değiştir', self)
        self.button_arac_degistir.clicked.connect(self.arac_degistir_clicked)
        layout_rota.addWidget(self.button_arac_degistir)

        self.label_arac_secildi = QLabel(self)
        layout_rota.addWidget(self.label_arac_secildi)

        self.tab_rota.setLayout(layout_rota)

    def tur_secildi(self, state):
        sender = self.sender()
        if state == 2:  # 2: Qt.Checked
            self.tur_sec.append(sender.text())
        else:
            self.tur_sec.remove(sender.text())

    def tur_incele_clicked(self):
        if self.tur_sec:
            message = "Seçilen turlar: " + ", ".join(self.tur_sec)
            self.label_tur_secildi.setText(message)
        else:
            self.label_tur_secildi.setText('Lütfen bir tur seçin!')

    def tur_sec_clicked(self):
        if self.tur_sec:
            message = "Seçilen turlar: " + ", ".join(self.tur_sec)
            self.label_tur_secildi.setText(message)
        else:
            self.label_tur_secildi.setText('Lütfen bir tur seçin!')

    def tur_iptal_clicked(self):
        if self.tur_sec:
            self.tur_iptal.extend(self.tur_sec)
            self.tur_sec.clear()
            self.label_tur_secildi.setText('Seçilen turlar iptal edildi.')
        else:
            self.label_tur_secildi.setText('İptal edilecek tur bulunamadı!')

    def arac_secildi(self, state):
        sender = self.sender()
        if state == 2:  # 2: Qt.Checked
            self.arac_sec.append(sender.text())
        else:
            self.arac_sec.remove(sender.text())

    def arac_incele_clicked(self):
        if self.arac_sec:
            message = "Seçilen araçlar: " + ", ".join(self.arac_sec)
            self.label_arac_secildi.setText(message)
        else:
            self.label_arac_secildi.setText('Lütfen bir araç seçin!')

    def arac_sec_clicked(self):
        if self.arac_sec:
            message = "Seçilen araçlar: " + ", ".join(self.arac_sec)
            self.label_arac_secildi.setText(message)
        else:
            self.label_arac_secildi.setText('Lütfen bir araç seçin!')

    def arac_degistir_clicked(self):
        if self.arac_sec:
            self.arac_degistir.extend(self.arac_sec)
            self.arac_sec.clear()
            self.label_arac_secildi.setText('Seçilen araçlar değiştirildi.')
        else:
            self.label_arac_secildi.setText('Değiştirilecek araç bulunamadı!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SeyahatPlanlamaUygulamasi()
    sys.exit(app.exec_())
