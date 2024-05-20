import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QDialog, QGridLayout, QLabel, QLineEdit, QMessageBox, QDialogButtonBox,
    QComboBox
)
from PyQt5.QtCore import Qt

class RestaurantApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KÜLTÜRSEPETİ.COM")
        self.setGeometry(100, 100, 800, 600)

        self.menu_items = {
            "Hamburger": {"fiyat": 120, "stok": 15},
            "Pizza": {"fiyat": 200, "stok": 20},
            "Sosisli": {"fiyat": 75, "stok": 12},
            "Köfte": {"fiyat": 90, "stok": 18},
            "Makarna": {"fiyat": 50, "stok": 25},
            "Tavuk Şiş": {"fiyat": 150, "stok": 10},
            "Çıtır Tavuk": {"fiyat": 80, "stok": 14},
            "Salata": {"fiyat": 30, "stok": 30},
            "Pilav": {"fiyat": 40, "stok": 22},
            "Kumpir": {"fiyat": 70, "stok": 16},
        }

        self.drink_items = {
            "Kola": {"fiyat": 5, "stok": 20},
            "Limonata": {"fiyat": 4, "stok": 25},
            "Meyve Suyu": {"fiyat": 6, "stok": 18},
            "Çay": {"fiyat": 3, "stok": 30},
            "Kahve": {"fiyat": 7, "stok": 15},
        }

        self.selected_items = {}
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel("KÜLTÜRSEPETİ.COM'un İNANILMAZ FIRSATLARINA HOŞGELDİNİZ!")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.welcome_label)
        
        self.welcome_label = QLabel("MAYIS AYINA ÖZEL ÜCRETSİZ KARGO!")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.welcome_label)


        self.food_button = QPushButton("Yemekler")
        self.food_button.setStyleSheet("background-color: #FFC107; color: black;")
        self.food_button.setMinimumHeight(50)
        self.food_button.clicked.connect(self.show_foods)
        self.layout.addWidget(self.food_button)

        self.drink_button = QPushButton("İçecekler")
        self.drink_button.setStyleSheet("background-color: #2196F3; color: white;")
        self.drink_button.setMinimumHeight(50)
        self.drink_button.clicked.connect(self.show_drinks)
        self.layout.addWidget(self.drink_button)

        self.order_button = QPushButton("Sipariş Ver")
        self.order_button.setStyleSheet("background-color: #f44336; color: white;")
        self.order_button.setMinimumHeight(50)
        self.order_button.clicked.connect(self.place_order)
        self.layout.addWidget(self.order_button)

        self.central_widget.setLayout(self.layout)

    def populate_menu(self, items, layout):
        row = 0
        col = 0
        for item in items:
            button = QPushButton(item)
            button.clicked.connect(lambda checked, item=item: self.add_item(item))
            layout.addWidget(button, row, col)

            quantity_label = QLabel("Stok: {}".format(items[item]["stok"]))
            layout.addWidget(quantity_label, row, col + 1)

            col += 2
            if col >= 4:
                col = 0
                row += 1

    def add_item(self, item):
        dialog = QDialog(self)
        dialog.setWindowTitle("Adet Seçin")

        layout = QVBoxLayout(dialog)
        label = QLabel("Kaç adet {} istiyorsunuz?".format(item))
        layout.addWidget(label)

        line_edit = QLineEdit()
        layout.addWidget(line_edit)

        add_button = QPushButton("Ekle", dialog)
        add_button.clicked.connect(lambda: self.add_to_selected(item, line_edit.text(), dialog))
        layout.addWidget(add_button)

        remove_button = QPushButton("Çıkar", dialog)
        remove_button.clicked.connect(lambda: self.remove_from_selected(item, line_edit.text(), dialog))
        layout.addWidget(remove_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def add_to_selected(self, item, quantity, dialog):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
            if item in self.menu_items:
                if self.menu_items[item]["stok"] >= quantity:
                    if item in self.selected_items:
                        self.selected_items[item]["adet"] += quantity
                    else:
                        self.selected_items[item] = {"fiyat": self.menu_items[item]["fiyat"], "adet": quantity}
                    self.menu_items[item]["stok"] -= quantity
                    QMessageBox.information(self, "Başarılı", "{} adet {} seçildi.".format(quantity, item))
                else:
                    QMessageBox.warning(self, "Uyarı", "Stokta yeterli {} yok.".format(item))
            elif item in self.drink_items:
                if self.drink_items[item]["stok"] >= quantity:
                    if item in self.selected_items:
                        self.selected_items[item]["adet"] += quantity
                    else:
                        self.selected_items[item] = {"fiyat": self.drink_items[item]["fiyat"], "adet": quantity}
                    self.drink_items[item]["stok"] -= quantity
                    QMessageBox.information(self, "Başarılı", "{} adet {} seçildi.".format(quantity, item))
                else:
                    QMessageBox.warning(self, "Uyarı", "Stokta yeterli {} yok.".format(item))
            dialog.close()
        except ValueError:
            QMessageBox.warning(self, "Hata", "Geçerli bir sayı girin.")

    def remove_from_selected(self, item, quantity, dialog):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
            if item in self.selected_items:
                if self.selected_items[item]["adet"] >= quantity:
                    self.selected_items[item]["adet"] -= quantity
                    if item in self.menu_items:
                        self.menu_items[item]["stok"] += quantity
                    elif item in self.drink_items:
                        self.drink_items[item]["stok"] += quantity
                    if self.selected_items[item]["adet"] == 0:
                        del self.selected_items[item]
                    QMessageBox.information(self, "Başarılı", "{} adet {} çıkartıldı.".format(quantity, item))
                else:
                    QMessageBox.warning(self, "Uyarı", "Seçili {} kadar ürün yok.".format(item))
            dialog.close()
        except ValueError:
            QMessageBox.warning(self, "Hata", "Geçerli bir sayı girin.")

    def place_order(self):
        total_price = sum(item["fiyat"] * item["adet"] for item in self.selected_items.values())
        order_text = "Siparişiniz:\n\n"
        for item, info in self.selected_items.items():
            order_text += "{} x{} - Toplam: {} TL\n".format(item, info['adet'], info['fiyat'] * info['adet'])
        order_text += "\nToplam Tutar: {} TL".format(total_price)

        # Siparişi onaylamak için bir iletişim kutusu aç
        confirmation = QMessageBox.question(self, "Sipariş Onayı", order_text,
                                             QMessageBox.Yes | QMessageBox.No)

        # Eğer kullanıcı onaylarsa, müşteri bilgilerini al
        if confirmation == QMessageBox.Yes:
            self.get_customer_info(total_price)

    def get_customer_info(self, total_price):
        # Müşteri bilgilerini girmesi için bir iletişim kutusu aç
        dialog = QDialog(self)
        dialog.setWindowTitle("Müşteri Bilgileri")

        layout = QVBoxLayout(dialog)

        name_label = QLabel("Ad:")
        name_input = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(name_input)

        surname_label = QLabel("Soyad:")
        surname_input = QLineEdit()
        layout.addWidget(surname_label)
        layout.addWidget(surname_input)

        phone_label = QLabel("Telefon Numarası:")
        phone_input = QLineEdit()
        layout.addWidget(phone_label)
        layout.addWidget(phone_input)

        address_label = QLabel("Adres:")
        address_input = QLineEdit()
        layout.addWidget(address_label)
        layout.addWidget(address_input)

        payment_label = QLabel("Ödeme Tipi:")
        payment_input = QComboBox()
        payment_input.addItems(["Nakit", "Kredi Kartı"])
        layout.addWidget(payment_label)
        layout.addWidget(payment_input)

        # Onay ve İptal düğmelerini ekle
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        if dialog.exec_() == QDialog.Accepted:
            # Eğer kullanıcı bilgileri onaylarsa, siparişi işle
            name = name_input.text()
            surname = surname_input.text()
            phone_number = phone_input.text()
            address = address_input.text()
            payment = payment_input.currentText()

            # Telefon numarasının doğruluğunu ve formatını kontrol et
            if len(phone_number) != 11 or not phone_number.startswith("05"):
                QMessageBox.warning(self, "Hata", "Geçerli bir telefon numarası girin.")
                return

            customer_info = {
                "name": name,
                "surname": surname,
                "phone": phone_number,
                "address": address,
                "payment": payment,
                "total_price": total_price
            }
            self.process_order(customer_info)

    def process_order(self, customer_info):
        # Burada siparişi işleyebilirsiniz
        # Örneğin, müşteri bilgilerini ve sipariş toplamını yazdırabiliriz:
        print("Müşteri Bilgileri:", customer_info)
        QMessageBox.information(self, "Sipariş Tamamlandı",
                                "Siparişiniz alınmıştır. Teşekkür ederiz!")

    def show_drinks(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("İçecekler")
        layout = QGridLayout(dialog)
        self.populate_menu(self.drink_items, layout)
        dialog.setLayout(layout)
        dialog.exec_()

    def show_foods(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Yemekler")
        layout = QGridLayout(dialog)
        self.populate_menu(self.menu_items, layout)
        dialog.setLayout(layout)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestaurantApp()
    window.show()
    sys.exit(app.exec_())
