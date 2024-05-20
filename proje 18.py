import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox, QTextEdit, QMessageBox, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap

# Örnek tarihi olaylar ve hikayeleri
tarihi_olaylar = {
    "Apollo 11 Ay Görevi": {"Hikaye": "Apollo 11, 16-24 Temmuz 1969 tarihleri arasında gerçekleşen uzay göreviydi. "
                                    "Neil Armstrong, Buzz Aldrin ve Michael Collins, Ay'a gitmek üzere görevlendirilen "
                                    "astronotlardı. 20 Temmuz 1969'da Apollo 11, Ay'a inen ilk insanlı uzay aracı oldu.",
                             "Kişiler": ["Neil Armstrong - İlk insanlı ay yürüyüşünün kumandanı",
                                         "Buzz Aldrin - Apollo 11 astronotu",
                                         "Michael Collins - Apollo 11 komuta modülü pilotu"]},
    "Fransız Devrimi": {"Hikaye": "Fransız Devrimi, 1789'da Fransa'da başlayan siyasi ve toplumsal bir dönüşümdü. "
                                   "Devrim, mutlakiyetçilik ve soyluların ayrıcalıklarına karşı halkın öfkesi sonucu patlak verdi. "
                                   "Fransız Devrimi, halkın eşitlik, özgürlük ve kardeşlik talepleriyle ortaya çıktı.",
                        "Kişiler": ["Napolyon Bonaparte - Fransa'nın imparatoru",
                                    "Jean-Jacques Rousseau - Aydınlanma Çağı filozofu",
                                    "Marie Antoinette - Fransa kraliçesi"]},
    "İkinci Dünya Savaşı": {"Hikaye": "İkinci Dünya Savaşı, 1939-1945 yılları arasında dünyanın dört bir yanındaki "
                                       "ülkeler arasında gerçekleşen büyük ölçekli bir savaştı. Milyonlarca asker ve sivil öldü, "
                                       "büyük ekonomik hasarlar meydana geldi ve tarih boyunca en yıkıcı çatışmalardan biri oldu.",
                             "Kişiler": ["Winston Churchill - Birleşik Krallık başbakanı",
                                         "Adolf Hitler - Nazi Almanyası lideri",
                                         "Franklin D. Roosevelt - ABD başkanı"]}
}

class TarihOlaylariUygulamasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarihi Olaylar ve Hikayeler")
        self.setGeometry(100, 100, 600, 500)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.event_combo = QComboBox()
        self.event_combo.addItems(tarihi_olaylar.keys())
        self.layout.addWidget(self.event_combo)

        self.show_story_button = QPushButton("Hikayeyi Görüntüle")
        self.show_story_button.clicked.connect(self.show_story)
        self.layout.addWidget(self.show_story_button)

        self.story_text = QTextEdit()
        self.layout.addWidget(self.story_text)

        self.person_combo = QComboBox()
        self.person_combo.addItem("Kişi Seçin")
        self.person_combo.currentIndexChanged.connect(self.show_person)
        self.layout.addWidget(self.person_combo)

        self.person_info_text = QTextEdit()
        self.layout.addWidget(self.person_info_text)

        self.extra_info_text = QTextEdit()
        self.layout.addWidget(self.extra_info_text)

        self.add_event_button = QPushButton("Olay Ekle")
        self.add_event_button.clicked.connect(self.add_event)
        self.layout.addWidget(self.add_event_button)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def show_story(self):
        selected_event = self.event_combo.currentText()
        story = tarihi_olaylar[selected_event]["Hikaye"]
        self.story_text.setText(story)
        self.load_people(selected_event)
        self.show_extra_info(selected_event)  # Ek bilgileri göster

    def load_people(self, selected_event):
        people = tarihi_olaylar[selected_event]["Kişiler"]
        self.person_combo.clear()
        self.person_combo.addItem("Kişi Seçin")
        self.person_combo.addItems(people)

    def show_person(self):
        selected_person = self.person_combo.currentText()
        if selected_person == "Kişi Seçin":
            return
        selected_event = self.event_combo.currentText()
        people_info = tarihi_olaylar[selected_event]["Kişiler"]
        for info in people_info:
            if selected_person.split(' - ')[0] in info:
                self.person_info_text.setText(info)
                break

    def show_extra_info(self, selected_event):
        extra_info = tarihi_olaylar[selected_event]
        formatted_info = "\n".join(["{}: {}".format(key, value) for key, value in extra_info.items()])
        self.extra_info_text.setText(formatted_info)

    def add_event(self):
        self.add_event_window = AddEventWindow()
        self.add_event_window.show()

class AddEventWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Olay Ekle")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.event_name_input = QLineEdit()
        layout.addWidget(self.event_name_input)

        self.event_desc_input = QTextEdit()
        layout.addWidget(self.event_desc_input)

        add_button = QPushButton("Olay Ekle")
        add_button.clicked.connect(self.add_event)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_event(self):
        event_name = self.event_name_input.text()
        event_desc = self.event_desc_input.toPlainText()
        if event_name and event_desc:
            tarihi_olaylar[event_name] = {"Hikaye": event_desc, "Kişiler": []}
            window.event_combo.addItem(event_name)
            self.close()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen olay adı ve açıklaması girin.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TarihOlaylariUygulamasi()
    window.show()
    sys.exit(app.exec_())
