import tkinter as tk
from tkinter import messagebox, simpledialog

class Tarif:
    def __init__(self, ad, malzemeler, icerik):
        self.ad = ad
        self.malzemeler = malzemeler
        self.icerik = icerik

class Malzeme:
    def __init__(self, ad, miktar):
        self.ad = ad
        self.miktar = miktar

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre

# Tarifler ve kullanıcılar listesi
tarifler = []
kullanicilar = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Yemek Tarifi Uygulaması")
root.geometry("500x400")

label = tk.Label(root, text="Yemek Tarifi Uygulaması'na Hoş Geldiniz!")
label.pack()

def tarif_ekle():
    ad = simpledialog.askstring("Tarif Adı", "Lütfen tarif adını girin:")
    malzeme_ad = simpledialog.askstring("Malzeme Adı", "Lütfen malzeme adını girin:")
    malzeme_miktar = simpledialog.askstring("Malzeme Miktarı", "Lütfen malzeme miktarını girin:")
    malzemeler = [Malzeme(malzeme_ad, malzeme_miktar)]
    icerik = simpledialog.askstring("Tarif İçeriği", "Lütfen tarif içeriğini girin:")
    tarif = Tarif(ad, malzemeler, icerik)
    tarifler.append(tarif)

def tarif_ara():
    ad = simpledialog.askstring("Tarif Adı", "Lütfen aramak istediğiniz tarif adını girin:")
    for tarif in tarifler:
        if tarif.ad == ad:
            messagebox.showinfo("Tarif Bulundu", f"Tarif Adı: {tarif.ad}\nMalzemeler: {', '.join([f'{malzeme.ad} ({malzeme.miktar})' for malzeme in tarif.malzemeler])}\nİçerik: {tarif.icerik}")
            return
    messagebox.showerror("Hata", "Tarif bulunamadı!")

def tarif_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for tarif in tarifler:
        listbox.insert(tk.END, f"Tarif Adı: {tarif.ad}, Malzemeler: {', '.join([f'{malzeme.ad} ({malzeme.miktar})' for malzeme in tarif.malzemeler])}, İçerik: {tarif.icerik}")

tarif_ekle_button = tk.Button(root, text="Tarif Ekle", command=tarif_ekle)
tarif_ekle_button.pack()

tarif_ara_button = tk.Button(root, text="Tarif Ara", command=tarif_ara)
tarif_ara_button.pack()

tarif_listesi_goster_button = tk.Button(root, text="Tarif Listesi Göster", command=tarif_listesi_goster)
tarif_listesi_goster_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()
