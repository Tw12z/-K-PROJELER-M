import tkinter as tk
from tkinter import messagebox, simpledialog

class Urun:
    def __init__(self, ad, stok_miktari):
        self.ad = ad
        self.stok_miktari = stok_miktari

class Siparis:
    def __init__(self, numara, detaylar):
        self.numara = numara
        self.detaylar = detaylar

# Ürünler ve siparişler listesi
urunler = []
siparisler = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Stok Takip Sistemi")
root.geometry("500x400")

label = tk.Label(root, text="Stok Takip Sistemine Hoş Geldiniz!")
label.pack()

def urun_ekle():
    ad = simpledialog.askstring("Ürün Adı", "Lütfen ürün adını girin:")
    stok_miktari = simpledialog.askinteger("Stok Miktarı", "Lütfen stok miktarını girin:")
    urun = Urun(ad, stok_miktari)
    urunler.append(urun)

def siparis_olustur():
    numara = simpledialog.askinteger("Sipariş Numarası", "Lütfen sipariş numarasını girin:")
    detaylar = simpledialog.askstring("Sipariş Detayları", "Lütfen sipariş detaylarını girin:")
    siparis = Siparis(numara, detaylar)
    siparisler.append(siparis)

def stok_guncelle():
    ad = simpledialog.askstring("Ürün Adı", "Lütfen stok miktarını güncellemek istediğiniz ürün adını girin:")
    for urun in urunler:
        if urun.ad == ad:
            yeni_miktar = simpledialog.askinteger("Yeni Stok Miktarı", "Lütfen yeni stok miktarını girin:")
            urun.stok_miktari = yeni_miktar
            messagebox.showinfo("Başarılı", "Stok miktarı başarıyla güncellendi!")
            return
    messagebox.showerror("Hata", "Ürün bulunamadı!")

def urun_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for urun in urunler:
        listbox.insert(tk.END, f"Ürün Adı: {urun.ad}, Stok Miktarı: {urun.stok_miktari}")

def siparis_listesi_goster():
    listbox1.delete(0, tk.END)  # Listbox1'i temizle
    for siparis in siparisler:
        listbox1.insert(tk.END, f"Sipariş Numarası: {siparis.numara}, Detaylar: {siparis.detaylar}")

urun_ekle_button = tk.Button(root, text="Ürün Ekle", command=urun_ekle)
urun_ekle_button.pack()

siparis_olustur_button = tk.Button(root, text="Sipariş Oluştur", command=siparis_olustur)
siparis_olustur_button.pack()

stok_guncelle_button = tk.Button(root, text="Stok Güncelle", command=stok_guncelle)
stok_guncelle_button.pack()

urun_listesi_goster_button = tk.Button(root, text="Ürün Listesi Göster", command=urun_listesi_goster)
urun_listesi_goster_button.pack()

siparis_listesi_goster_button = tk.Button(root, text="Sipariş Listesi Göster", command=siparis_listesi_goster)
siparis_listesi_goster_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox1 = tk.Listbox(root, width=50)
listbox1.pack()

root.mainloop()
