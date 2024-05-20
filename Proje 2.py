import tkinter as tk
from tkinter import messagebox, simpledialog

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu_gecmisi = []

class Doktor:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik
        self.musaitlik = True

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta
        self.aktif = True

# Hastalar ve doktorlar listesi
hastalar = []
doktorlar = [Doktor("Dr. Ahmet", "Kardiyoloji"), Doktor("Dr. Fatma", "Nöroloji")]
randevular = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Hastane Randevu Sistemi")
root.geometry("500x400")

label = tk.Label(root, text="Hastane Randevu Sistemi'ne Hoş Geldiniz!")
label.pack()

def hasta_ekle():
    isim = simpledialog.askstring("İsim", "Lütfen isminizi girin:")
    tc = simpledialog.askstring("TC", "Lütfen TC'nizi girin:")
    hasta = Hasta(isim, tc)
    hastalar.append(hasta)
    hasta_listesi_goster()  # Hasta listesini güncelle

def randevu_al():
    tc = simpledialog.askstring("TC Kimlik No", "Lütfen TC kimlik numaranızı girin:")
    for hasta in hastalar:
        if hasta.tc == tc:
            doktor_isim = simpledialog.askstring("Doktor İsmi", "Randevu almak istediğiniz doktorun ismini girin:")
            for doktor in doktorlar:
                if doktor.isim == doktor_isim:
                    if doktor.musaitlik:
                        tarih = simpledialog.askstring("Tarih", "Randevu tarihi girin:")
                        randevu = Randevu(tarih, doktor, hasta)
                        hasta.randevu_gecmisi.append(randevu)
                        randevular.append(randevu)
                        doktor.musaitlik = False
                        messagebox.showinfo("Başarılı", "Randevunuz başarıyla oluşturuldu!")
                        randevu_listesi_goster()  # Randevu listesini güncelle
                        return
                    else:
                        messagebox.showerror("Hata", "Doktor müsait değil!")
                        return
            messagebox.showerror("Hata", "Doktor bulunamadı!")
            return
    messagebox.showerror("Hata", "Hasta bulunamadı!")

def randevu_iptal():
    tc = simpledialog.askstring("TC Kimlik No", "Lütfen TC kimlik numaranızı girin:")
    for hasta in hastalar:
        if hasta.tc == tc:
            doktor_isim = simpledialog.askstring("Doktor İsmi", "Randevuyu iptal etmek istediğiniz doktorun ismini girin:")
            for randevu in hasta.randevu_gecmisi:
                if randevu.doktor.isim == doktor_isim and randevu.aktif:
                    randevu.aktif = False
                    randevu.doktor.musaitlik = True
                    messagebox.showinfo("Başarılı", "Randevunuz başarıyla iptal edildi!")
                    randevu_listesi_goster()  # Randevu listesini güncelle
                    return
            messagebox.showerror("Hata", "Randevu bulunamadı!")
            return
    messagebox.showerror("Hata", "Hasta bulunamadı!")

def hasta_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for hasta in hastalar:
        listbox.insert(tk.END, f"Hasta: {hasta.isim}, TC: {hasta.tc}")

def doktor_listesi_goster():
    listbox1.delete(0, tk.END)  # Listbox1'i temizle
    for doktor in doktorlar:
        listbox1.insert(tk.END, f"Doktor: {doktor.isim}, Uzmanlık: {doktor.uzmanlik}")

def randevu_listesi_goster():
    listbox2.delete(0, tk.END)  # Listbox2'yi temizle
    for randevu in randevular:
        if randevu.aktif:
            listbox2.insert(tk.END, f"Hasta: {randevu.hasta.isim}, Doktor: {randevu.doktor.isim}, Tarih: {randevu.tarih}")
        else:
            listbox2.insert(tk.END, f"(İptal Edildi) Hasta: {randevu.hasta.isim}, Doktor: {randevu.doktor.isim}, Tarih: {randevu.tarih}")

hasta_ekle_button = tk.Button(root, text="Hasta Ekle", command=hasta_ekle)
hasta_ekle_button.pack()

randevu_al_button = tk.Button(root, text="Randevu Al", command=randevu_al)
randevu_al_button.pack()

randevu_iptal_button = tk.Button(root, text="Randevu İptal", command=randevu_iptal)
randevu_iptal_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox1 = tk.Listbox(root, width=50)
listbox1.pack()

listbox2 = tk.Listbox(root, width=50)
listbox2.pack()

hasta_listesi_goster()  # İlk hasta listesini göster
doktor_listesi_goster()  # İlk doktor listesini göster
randevu_listesi_goster()  # İlk randevu listesini göster

root.mainloop()
