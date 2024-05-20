import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget, QFormLayout, QCheckBox, QComboBox, QMessageBox, QTextEdit
from PyQt5.QtGui import QIntValidator

class Kullanici:
    def __init__(self, adi, soyadi, yas, cinsiyet, telefon_no):
        self.adi = adi
        self.soyadi = soyadi
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.telefon_no = telefon_no
        self.sikayet = ""  # Yeni eklenen özellik

class SaglikBilgileri:
    def __init__(self, boy, kilo, kan_grubu, seker_durumu, tansiyon_durumu):
        self.boy = boy
        self.kilo = kilo
        self.kan_grubu = kan_grubu
        self.seker_durumu = seker_durumu
        self.tansiyon_durumu = tansiyon_durumu

class Egzersiz:
    def __init__(self, seviye1, seviye2, seviye3):
        self.seviye1 = seviye1
        self.seviye2 = seviye2
        self.seviye3 = seviye3


class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.setGeometry(200, 200, 400, 300)

        self.tab_widget = QTabWidget()

        self.kullanici_tab = QWidget()
        self.saglik_tab = QWidget()
        self.egzersiz_tab = QWidget()

        self.tab_widget.addTab(self.kullanici_tab, "Kullanıcı")
        self.tab_widget.addTab(self.saglik_tab, "Sağlık Bilgileri")
        self.tab_widget.addTab(self.egzersiz_tab, "Egzersiz")

        self.kullanici_arayuz_olustur()
        self.saglik_arayuz_olustur()
        self.egzersiz_arayuz_olustur()

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def kullanici_arayuz_olustur(self):
        layout = QFormLayout()

        self.adi_input = QLineEdit()
        self.soyadi_input = QLineEdit()
        self.yas_input = QLineEdit()
        self.cinsiyet_combo = QComboBox()  # Cinsiyet seçenekleri için combo box
        self.cinsiyet_combo.addItem("Kadın")
        self.cinsiyet_combo.addItem("Erkek")
        self.sikayet_combo = QComboBox ()  # Şikayet seçenekleri için combo box
        self.sikayet_combo.addItem ("Baş Bölgesi")
        self.sikayet_combo.addItem ("Boyun Bölgesi")
        self.sikayet_combo.addItem ("Kol Bölgesi")
        self.sikayet_combo.addItem ("Göğüs Bölgesi")
        self.sikayet_combo.addItem ("Bacak Bölgesi")
        self.telefon_no_input = QLineEdit()

        layout.addRow(QLabel("Kullanıcı Adı:"), self.adi_input)
        layout.addRow(QLabel("Kullanıcı Soyadı:"), self.soyadi_input)
        layout.addRow(QLabel("Yaş:"), self.yas_input)
        layout.addRow(QLabel("Cinsiyet:"), self.cinsiyet_combo)
        layout.addRow(QLabel("Telefon No:"), self.telefon_no_input)
        layout.addRow(QLabel("Şikayet:"), self.sikayet_combo)

        self.kullanici_tab.setLayout(layout)

        # Ekle butonunu ekle
        ekle_button = QPushButton("Ekle")
        ekle_button.clicked.connect(self.kullanici_ekle)
        layout.addRow(ekle_button)

    def saglik_arayuz_olustur (self):
        layout = QFormLayout ()

        self.boy_input = QLineEdit ()
        self.boy_input.setMaxLength (3)  # Maksimum 3 karakter uzunluğunda olacak şekilde sınırla
        self.kilo_input = QLineEdit ()
        self.kilo_input.setMaxLength (3)  # Maksimum 3 karakter uzunluğunda olacak şekilde sınırla

        # Boy ve kilo için değer sınırlarını belirle
        boy_validator = QIntValidator (0, 300)  # En küçük değer 0 (0 cm), en büyük değer 300 (3 metre)
        kilo_validator = QIntValidator (0, 300)  # En küçük değer 0, en büyük değer 300

        self.boy_input.setValidator (boy_validator)
        self.kilo_input.setValidator (kilo_validator)

        self.kan_grubu_input = QLineEdit ()
        self.seker_durumu_input = QLineEdit ()
        self.tansiyon_durumu_input = QLineEdit ()

        layout.addRow (QLabel ("Boy (cm):"), self.boy_input)
        layout.addRow (QLabel ("Kilo (kg):"), self.kilo_input)
        layout.addRow (QLabel ("Kan Grubu:"), self.kan_grubu_input)
        layout.addRow (QLabel ("Şeker Durumu:"), self.seker_durumu_input)
        layout.addRow (QLabel ("Tansiyon Durumu:"), self.tansiyon_durumu_input)

        self.saglik_tab.setLayout (layout)

        # Güncelle butonunu ekle
        guncelle_button = QPushButton ("Güncelle")
        guncelle_button.clicked.connect (self.egzersiz_sekmeye_git)
        layout.addRow (guncelle_button)

    def egzersiz_arayuz_olustur(self):
        layout = QVBoxLayout()

        self.seviye1_checkbox = QCheckBox("Seviye 1")
        self.seviye2_checkbox = QCheckBox("Seviye 2")
        self.seviye3_checkbox = QCheckBox("Seviye 3")

        layout.addWidget(self.seviye1_checkbox)
        layout.addWidget(self.seviye2_checkbox)
        layout.addWidget(self.seviye3_checkbox)

        self.egzersiz_tab.setLayout(layout)

        # Başla butonunu ekle
        basla_button = QPushButton("Başla")
        basla_button.clicked.connect(self.egzersiz_basla)
        layout.addWidget(basla_button)

    def kullanici_ekle(self):
        # Kullanıcı ekleme işlemi burada yapılacak
        self.tab_widget.setCurrentIndex(1)  # Sağlık sekmesine geçiş
        # Kullanıcının girdiği şikayeti al ve sakla
        self.kullanici = Kullanici(
            self.adi_input.text(),
            self.soyadi_input.text(),
            self.yas_input.text(),
            self.cinsiyet_combo.currentText(),
            self.telefon_no_input.text(),
        )
        self.kullanici.sikayet = self.sikayet_combo.currentText()

    def egzersiz_sekmeye_git(self):
        self.tab_widget.setCurrentIndex(2)

    def egzersiz_basla (self):
        # Kullanıcının girdiği şikayeti analiz et
        sikayet = self.kullanici.sikayet
        egzersiz_onerisi = ""

        # Şikayete göre egzersiz önerisi yap
        if "Baş Bölgesi" in sikayet:
            egzersiz_onerisi = "Baş ağrıları için şakaklara yuvarlak çizerek masaj yapabilirsiniz.."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)
        elif "Boyun Bölgesi" in sikayet:
            egzersiz_onerisi = "Kafanızı öne arkaya sağa sola yavaşça çevirerek hafif bir egzersiz yapabilirsiniz.. Sonrasında sıcak bir bezle boyun bölgesini sararak ağrıyı azaltabilirsiniz."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)
        elif "Kol Bölgesi" in sikayet:
            egzersiz_onerisi = "Kollarınızı 2 kgluk Dumbell kullanarak güçlendirebilirsiniz. Plates lastiği kullanarak kollarınızı esnetebilirsiniz."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)
        elif "Göğüs Bölgesi" in sikayet:
            egzersiz_onerisi = "Göğüs ağrısı veya daralması için: Kobra gerinmesi yapabilirsiniz. Bu göğüs bölgesindeki kasları gerecek ve ciğerlerinize daha fazla oksijen gitmesine sebep olacaktır."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)
        elif "Bacak Bölgesi" in sikayet:
            egzersiz_onerisi = "Bacak ağrıları için, bacak esnetme yapabilirsiniz. Bir bacağınız önde, diğeri arkadayken, öndeki bacağınızı oturur şekilde kırarken arkadaki bacağı dümdüz tutarak diz arkası kaslarını esnetirsiniz.."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)
        else:
            egzersiz_onerisi = "Genel olarak vücudu güçlendirecek egzersizler yapabilirsiniz."
            QMessageBox.information (self, "Egzersiz Önerisi", egzersiz_onerisi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
