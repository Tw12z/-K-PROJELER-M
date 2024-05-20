import tkinter as tk
from tkinter import messagebox, simpledialog

class Etkinlik:
    def __init__(self, etkinlik_id, ad, tarih):
        self.etkinlik_id = etkinlik_id
        self.ad = ad
        self.tarih = tarih
        self.katilimcilar = []

class Katilimci:
    def __init__(self, katilimci_id, ad, soyad):
        self.katilimci_id = katilimci_id
        self.ad = ad
        self.soyad = soyad
        self.etkinlikler = []

class Bilet:
    def __init__(self, bilet_id, etkinlik, katilimci):
        self.bilet_id = bilet_id
        self.etkinlik = etkinlik
        self.katilimci = katilimci

    def bilet_al(self):
        if self.etkinlik not in self.katilimci.etkinlikler:
            self.katilimci.etkinlikler.append(self.etkinlik)
            self.etkinlik.katilimcilar.append(self.katilimci)
            print(f"{self.katilimci.ad} adlı katılımcı {self.etkinlik.ad} adlı etkinliğe kaydoldu.")
        else:
            print("Bu katılımcı zaten bu etkinliğe kaydolmuş.")

# Etkinlikler ve katılımcılar listesi
etkinlikler = [Etkinlik(1, "Konser", "01.01.2023"), Etkinlik(2, "Tiyatro", "02.02.2023")]
katilimcilar = [Katilimci(1, "Ali", "Veli"), Katilimci(2, "Ayşe", "Fatma")]
biletler = []

# Bilet işlemleri
bilet1 = Bilet(1, etkinlikler[0], katilimcilar[0])
bilet1.bilet_al()
biletler.append(bilet1)

bilet2 = Bilet(2, etkinlikler[1], katilimcilar[1])
bilet2.bilet_al()
biletler.append(bilet2)

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Etkinlik Yönetim Sistemi")
root.geometry("500x400")

label = tk.Label(root, text="Etkinlik Yönetim Sistemi'ne Hoş Geldiniz!")
label.pack()

def katilimci_ekle():
    katilimci_id = simpledialog.askinteger("Katılımcı ID", "Lütfen katılımcı ID'nizi girin:")
    katilimci_ad = simpledialog.askstring("Katılımcı Adı", "Lütfen adınızı girin:")
    katilimci_soyad = simpledialog.askstring("Katılımcı Soyadı", "Lütfen soyadınızı girin:")
    katilimci = Katilimci(katilimci_id, katilimci_ad, katilimci_soyad)
    katilimcilar.append(katilimci)
    katilimci_listesi_goster()  # Katılımcı listesini güncelle

def etkinlik_ekle():
    etkinlik_id = simpledialog.askinteger("Etkinlik ID", "Eklemek istediğiniz etkinliğin ID'sini girin:")
    etkinlik_ad = simpledialog.askstring("Etkinlik Adı", "Eklemek istediğiniz etkinliğin adını girin:")
    etkinlik_tarih = simpledialog.askstring("Etkinlik Tarihi", "Eklemek istediğiniz etkinliğin tarihini girin:")
    etkinlik = Etkinlik(etkinlik_id, etkinlik_ad, etkinlik_tarih)
    etkinlikler.append(etkinlik)
    etkinlik_listesi_goster()  # Etkinlik listesini güncelle

def bilet_al():
    katilimci_id = simpledialog.askinteger("Katılımcı ID", "Lütfen katılımcı ID'nizi girin:")
    for katilimci in katilimcilar:
        if katilimci.katilimci_id == katilimci_id:
            etkinlik_id = simpledialog.askinteger("Etkinlik ID", "Bilet almak istediğiniz etkinliğin ID'sini girin:")
            for etkinlik in etkinlikler:
                if etkinlik.etkinlik_id == etkinlik_id:
                    bilet_id = simpledialog.askinteger("Bilet ID", "Almak istediğiniz biletin ID'sini girin:")
                    bilet = Bilet(bilet_id, etkinlik, katilimci)
                    bilet.bilet_al()
                    biletler.append(bilet)
                    bilet_listesi_goster()  # Bilet listesini güncelle
                    return
            messagebox.showerror("Hata", "Etkinlik bulunamadı!")
            return
    messagebox.showerror("Hata", "Katılımcı bulunamadı!")

def katilimci_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for katilimci in katilimcilar:
        listbox.insert(tk.END, f"Katılımcı ID: {katilimci.katilimci_id}, Ad: {katilimci.ad}, Soyad: {katilimci.soyad}")

def etkinlik_listesi_goster():
    listbox1.delete(0, tk.END)  # Listbox1'i temizle
    for etkinlik in etkinlikler:
        listbox1.insert(tk.END, f"Etkinlik ID: {etkinlik.etkinlik_id}, Ad: {etkinlik.ad}, Tarih: {etkinlik.tarih}")

def bilet_listesi_goster():
    listbox2.delete(0, tk.END)  # Listbox2'yi temizle
    for bilet in biletler:
        listbox2.insert(tk.END, f"Bilet ID: {bilet.bilet_id}, Etkinlik: {bilet.etkinlik.ad}, Katılımcı: {bilet.katilimci.ad}")

katilimci_ekle_button = tk.Button(root, text="Katılımcı Ekle", command=katilimci_ekle)
katilimci_ekle_button.pack()

etkinlik_ekle_button = tk.Button(root, text="Etkinlik Ekle", command=etkinlik_ekle)
etkinlik_ekle_button.pack()

bilet_al_button = tk.Button(root, text="Bilet Al", command=bilet_al)
bilet_al_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox1 = tk.Listbox(root, width=50)
listbox1.pack()

listbox2 = tk.Listbox(root, width=50)
listbox2.pack()

katilimci_listesi_goster()  # İlk katılımcı listesini göster
etkinlik_listesi_goster()  # İlk etkinlik listesini göster
bilet_listesi_goster()  # İlk bilet listesini göster

root.mainloop()
