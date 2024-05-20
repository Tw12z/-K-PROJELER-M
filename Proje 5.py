import tkinter as tk
from tkinter import messagebox, simpledialog

class Kurs:
    def __init__(self, kurs_id, ad, egitmen, icerik):
        self.kurs_id = kurs_id
        self.ad = ad
        self.egitmen = egitmen
        self.icerik = icerik
        self.ogrenciler = []

class Egitmen:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik

class Ogrenci:
    def __init__(self, ogrenci_id, isim, email):
        self.ogrenci_id = ogrenci_id
        self.isim = isim
        self.email = email
        self.kurslar = []

# Kurslar ve öğrenciler listesi
kurslar = []
ogrenciler = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Online Eğitim Platformu")
root.geometry("500x400")

label = tk.Label(root, text="Online Eğitim Platformu'na Hoş Geldiniz!")
label.pack()

def kurs_ekle():
    kurs_id = simpledialog.askinteger("Kurs ID", "Lütfen kurs ID'nizi girin:")
    kurs_ad = simpledialog.askstring("Kurs Adı", "Lütfen kurs adını girin:")
    egitmen_isim = simpledialog.askstring("Eğitmen İsmi", "Lütfen eğitmen ismini girin:")
    egitmen_uzmanlik = simpledialog.askstring("Eğitmen Uzmanlık", "Lütfen eğitmenin uzmanlık alanını girin:")
    kurs_icerik = simpledialog.askstring("Kurs İçeriği", "Lütfen kurs içeriğini girin:")
    kurs = Kurs(kurs_id, kurs_ad, Egitmen(egitmen_isim, egitmen_uzmanlik), kurs_icerik)
    kurslar.append(kurs)
    kurs_listesi_goster()  # Kurs listesini güncelle

def ogrenci_ekle():
    ogrenci_id = simpledialog.askinteger("Öğrenci ID", "Lütfen öğrenci ID'nizi girin:")
    ogrenci_isim = simpledialog.askstring("Öğrenci İsmi", "Lütfen isminizi girin:")
    ogrenci_email = simpledialog.askstring("Öğrenci Email", "Lütfen email adresinizi girin:")
    ogrenci = Ogrenci(ogrenci_id, ogrenci_isim, ogrenci_email)
    ogrenciler.append(ogrenci)
    ogrenci_listesi_goster()  # Öğrenci listesini güncelle

def kursa_kaydol():
    ogrenci_id = simpledialog.askinteger("Öğrenci ID", "Lütfen öğrenci ID'nizi girin:")
    for ogrenci in ogrenciler:
        if ogrenci.ogrenci_id == ogrenci_id:
            kurs_id = simpledialog.askinteger("Kurs ID", "Kaydolmak istediğiniz kursun ID'sini girin:")
            for kurs in kurslar:
                if kurs.kurs_id == kurs_id:
                    kurs.ogrenciler.append(ogrenci)
                    ogrenci.kurslar.append(kurs)
                    messagebox.showinfo("Başarılı", "Kursa başarıyla kaydoldunuz!")
                    kurs_listesi_goster()  # Kurs listesini güncelle
                    return
            messagebox.showerror("Hata", "Kurs bulunamadı!")
            return
    messagebox.showerror("Hata", "Öğrenci bulunamadı!")

def ogrenci_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for ogrenci in ogrenciler:
        listbox.insert(tk.END, f"Öğrenci ID: {ogrenci.ogrenci_id}, İsim: {ogrenci.isim}, Email: {ogrenci.email}")

def kurs_listesi_goster():
    listbox1.delete(0, tk.END)  # Listbox1'i temizle
    for kurs in kurslar:
        listbox1.insert(tk.END, f"Kurs ID: {kurs.kurs_id}, Ad: {kurs.ad}, Eğitmen: {kurs.egitmen.isim}, İçerik: {kurs.icerik}")

kurs_ekle_button = tk.Button(root, text="Kurs Ekle", command=kurs_ekle)
kurs_ekle_button.pack()

ogrenci_ekle_button = tk.Button(root, text="Öğrenci Ekle", command=ogrenci_ekle)
ogrenci_ekle_button.pack()

kursa_kaydol_button = tk.Button(root, text="Kursa Kaydol", command=kursa_kaydol)
kursa_kaydol_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox1 = tk.Listbox(root, width=50)
listbox1.pack()

ogrenci_listesi_goster()  # İlk öğrenci listesini göster
kurs_listesi_goster()  # İlk kurs listesini göster

root.mainloop()
