import tkinter as tk
from tkinter import messagebox, simpledialog

class Arac:
    def __init__(self, arac_id, model, fiyat, kiralama_durumu=False):
        self.arac_id = arac_id
        self.model = model
        self.fiyat = fiyat
        self.kiralama_durumu = kiralama_durumu
        self.musteri = None

    def arac_durumu_guncelle(self, durum, musteri=None):
        self.kiralama_durumu = durum
        self.musteri = musteri

class Musteri:
    def __init__(self, musteri_id, ad, soyad):
        self.musteri_id = musteri_id
        self.ad = ad
        self.soyad = soyad

# Araçlar ve müşteriler listesi
araclar = [Arac(1, "Toyota", 100), Arac(2, "Honda", 120), Arac(3, "Ford", 150)]
musteriler = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Araç Kiralama Sistemi")
root.geometry("500x400")

label = tk.Label(root, text="Araç Kiralama Sistemi'ne Hoş Geldiniz!")
label.pack()

def kiralama_yap():
    musteri_id = simpledialog.askstring("Müşteri ID", "Lütfen müşteri ID'nizi girin:")
    musteri_ad = simpledialog.askstring("Müşteri Adı", "Lütfen adınızı girin:")
    musteri_soyad = simpledialog.askstring("Müşteri Soyadı", "Lütfen soyadınızı girin:")
    musteri = Musteri(musteri_id, musteri_ad, musteri_soyad)
    musteriler.append(musteri)

    arac_id = simpledialog.askinteger("Araç ID", "Kiralamak istediğiniz aracın ID'sini girin:")
    for arac in araclar:
        if arac.arac_id == arac_id:
            if not arac.kiralama_durumu:
                arac.arac_durumu_guncelle(True, musteri)
                messagebox.showinfo("Başarılı", "Araç başarıyla kiralandı!")
                arac_listesi_goster()  # Araç listesini güncelle
                return
            else:
                messagebox.showerror("Hata", "Araç zaten kiralanmış!")
                return
    messagebox.showerror("Hata", "Araç bulunamadı!")

def arac_ekle():
    arac_id = simpledialog.askinteger("Araç ID", "Eklemek istediğiniz aracın ID'sini girin:")
    arac_model = simpledialog.askstring("Araç Modeli", "Eklemek istediğiniz aracın modelini girin:")
    arac_fiyat = simpledialog.askinteger("Araç Fiyatı", "Eklemek istediğiniz aracın fiyatını girin:")
    arac = Arac(arac_id, arac_model, arac_fiyat)
    araclar.append(arac)
    arac_listesi_goster()  # Araç listesini güncelle

def arac_cikar():
    arac_id = simpledialog.askinteger("Araç ID", "Çıkarmak istediğiniz aracın ID'sini girin:")
    for arac in araclar:
        if arac.arac_id == arac_id:
            araclar.remove(arac)
            arac_listesi_goster()  # Araç listesini güncelle
            return
    messagebox.showerror("Hata", "Araç bulunamadı!")

def arac_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    listbox2.delete(0, tk.END)  # Listbox2'yi temizle
    for arac in araclar:
        if arac.kiralama_durumu:
            listbox2.insert(tk.END, f"Araç ID: {arac.arac_id}, Model: {arac.model}, Fiyat: {arac.fiyat}, Kiralayan Müşteri ID: {arac.musteri.musteri_id}")
        else:
            listbox.insert(tk.END, f"Araç ID: {arac.arac_id}, Model: {arac.model}, Fiyat: {arac.fiyat}")

kiralama_button = tk.Button(root, text="Araç Kirala", command=kiralama_yap)
kiralama_button.pack()

ekle_button = tk.Button(root, text="Araç Ekle", command=arac_ekle)
ekle_button.pack()

cikar_button = tk.Button(root, text="Araç Çıkar", command=arac_cikar)
cikar_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox2 = tk.Listbox(root, width=50)
listbox2.pack()

arac_listesi_goster()  # İlk araç listesini göster

root.mainloop()
