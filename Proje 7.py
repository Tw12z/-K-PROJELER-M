import tkinter as tk
from tkinter import messagebox, simpledialog

class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.program = []
        self.ilerleme = []

class Antrenman:
    def __init__(self, ad, detaylar):
        self.ad = ad
        self.detaylar = detaylar

class Takip:
    def __init__(self, sporcu, antrenman, ilerleme):
        self.sporcu = sporcu
        self.antrenman = antrenman
        self.ilerleme = ilerleme

# Sporcular, antrenmanlar ve takip verileri listesi
sporcular = []
antrenmanlar = []
takipler = []

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Spor Takip Uygulaması")
root.geometry("500x400")

label = tk.Label(root, text="Spor Takip Uygulaması'na Hoş Geldiniz!")
label.pack()

def sporcu_ekle():
    ad = simpledialog.askstring("Sporcu Adı", "Lütfen sporcu adını girin:")
    spor_dali = simpledialog.askstring("Spor Dalı", "Lütfen spor dalını girin:")
    sporcu = Sporcu(ad, spor_dali)
    sporcular.append(sporcu)

def antrenman_ekle():
    ad = simpledialog.askstring("Antrenman Adı", "Lütfen antrenman adını girin:")
    detaylar = simpledialog.askstring("Antrenman Detayları", "Lütfen antrenman detaylarını girin:")
    antrenman = Antrenman(ad, detaylar)
    antrenmanlar.append(antrenman)

def program_olustur():
    sporcu_ad = simpledialog.askstring("Sporcu Adı", "Lütfen program oluşturmak istediğiniz sporcu adını girin:")
    antrenman_ad = simpledialog.askstring("Antrenman Adı", "Lütfen programına eklemek istediğiniz antrenman adını girin:")
    for sporcu in sporcular:
        if sporcu.ad == sporcu_ad:
            for antrenman in antrenmanlar:
                if antrenman.ad == antrenman_ad:
                    sporcu.program.append(antrenman)
                    messagebox.showinfo("Başarılı", "Antrenman programı başarıyla oluşturuldu!")
                    return
    messagebox.showerror("Hata", "Sporcu veya antrenman bulunamadı!")

def ilerleme_kaydet():
    sporcu_ad = simpledialog.askstring("Sporcu Adı", "Lütfen ilerlemeyi kaydetmek istediğiniz sporcu adını girin:")
    antrenman_ad = simpledialog.askstring("Antrenman Adı", "Lütfen ilerlemeyi kaydetmek istediğiniz antrenman adını girin:")
    ilerleme = simpledialog.askstring("İlerleme", "Lütfen ilerlemeyi girin:")
    for sporcu in sporcular:
        if sporcu.ad == sporcu_ad:
            for antrenman in antrenmanlar:
                if antrenman.ad == antrenman_ad:
                    takip = Takip(sporcu, antrenman, ilerleme)
                    takipler.append(takip)
                    messagebox.showinfo("Başarılı", "İlerleme başarıyla kaydedildi!")
                    return
    messagebox.showerror("Hata", "Sporcu veya antrenman bulunamadı!")

def rapor_al():
    sporcu_ad = simpledialog.askstring("Sporcu Adı", "Lütfen rapor almak istediğiniz sporcu adını girin:")
    for sporcu in sporcular:
        if sporcu.ad == sporcu_ad:
            for takip in takipler:
                if takip.sporcu == sporcu:
                    print(f"Sporcu: {takip.sporcu.ad}, Antrenman: {takip.antrenman.ad}, İlerleme: {takip.ilerleme}")
            return
    messagebox.showerror("Hata", "Sporcu bulunamadı!")

sporcu_ekle_button = tk.Button(root, text="Sporcu Ekle", command=sporcu_ekle)
sporcu_ekle_button.pack()

antrenman_ekle_button = tk.Button(root, text="Antrenman Ekle", command=antrenman_ekle)
antrenman_ekle_button.pack()

program_olustur_button = tk.Button(root, text="Program Oluştur", command=program_olustur)
program_olustur_button.pack()

ilerleme_kaydet_button = tk.Button(root, text="İlerleme Kaydet", command=ilerleme_kaydet)
ilerleme_kaydet_button.pack()

rapor_al_button = tk.Button(root, text="Rapor Al", command=rapor_al)
rapor_al_button.pack()

root.mainloop()
