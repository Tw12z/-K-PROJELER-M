import tkinter as tk
from tkinter import messagebox, simpledialog

class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Müsait"

    def durum_guncelle(self, durum):
        self.durum = durum

class Uye:
    def __init__(self, uye_id, ad, soyad):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad
        self.odunc_alinan_kitaplar = []

    def odunc_al(self, kitap):
        if kitap.durum == "Müsait":
            kitap.durum_guncelle("Ödünç Alındı")
            self.odunc_alinan_kitaplar.append(kitap)
            print(f"{kitap.ad} adlı kitap {self.ad} tarafından ödünç alındı.")
        else:
            print("Bu kitap şu anda müsait değil.")

    def iade_et(self, kitap):
        if kitap in self.odunc_alinan_kitaplar:
            self.odunc_alinan_kitaplar.remove(kitap)
            kitap.durum_guncelle("Müsait")
            print(f"{kitap.ad} adlı kitap {self.ad} tarafından iade edildi.")
        else:
            print("Bu kitap bu üye tarafından ödünç alınmamış.")

# Kitaplar ve üyeler listesi
kitaplar = [Kitap(1, "1984", "George Orwell"), Kitap(2, "Fareler ve İnsanlar", "John Steinbeck")]
uyeler = [Uye(1, "Ali", "Veli"), Uye(2, "Ayşe", "Fatma")]

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Kütüphane Yönetim Sistemi")
root.geometry("500x400")

label = tk.Label(root, text="Kütüphane Yönetim Sistemi'ne Hoş Geldiniz!")
label.pack()

def uye_ekle():
    uye_id = simpledialog.askinteger("Üye ID", "Lütfen üye ID'nizi girin:")
    uye_ad = simpledialog.askstring("Üye Adı", "Lütfen adınızı girin:")
    uye_soyad = simpledialog.askstring("Üye Soyadı", "Lütfen soyadınızı girin:")
    uye = Uye(uye_id, uye_ad, uye_soyad)
    uyeler.append(uye)
    uye_listesi_goster()  # Üye listesini güncelle

def kitap_ekle():
    kitap_id = simpledialog.askinteger("Kitap ID", "Eklemek istediğiniz kitabın ID'sini girin:")
    kitap_ad = simpledialog.askstring("Kitap Adı", "Eklemek istediğiniz kitabın adını girin:")
    kitap_yazar = simpledialog.askstring("Kitap Yazarı", "Eklemek istediğiniz kitabın yazarını girin:")
    kitap = Kitap(kitap_id, kitap_ad, kitap_yazar)
    kitaplar.append(kitap)
    kitap_listesi_goster()  # Kitap listesini güncelle

def uye_listesi_goster():
    listbox.delete(0, tk.END)  # Listbox'ı temizle
    for uye in uyeler:
        listbox.insert(tk.END, f"Üye ID: {uye.uye_id}, Ad: {uye.ad}, Soyad: {uye.soyad}")

def kitap_listesi_goster():
    listbox1.delete(0, tk.END)  # Listbox1'i temizle
    for kitap in kitaplar:
        listbox1.insert(tk.END, f"Kitap ID: {kitap.kitap_id}, Ad: {kitap.ad}, Yazar: {kitap.yazar}, Durum: {kitap.durum}")

def odunc_al():
    uye_id = simpledialog.askinteger("Üye ID", "Lütfen üye ID'nizi girin:")
    for uye in uyeler:
        if uye.uye_id == uye_id:
            kitap_id = simpledialog.askinteger("Kitap ID", "Ödünç almak istediğiniz kitabın ID'sini girin:")
            for kitap in kitaplar:
                if kitap.kitap_id == kitap_id:
                    uye.odunc_al(kitap)
                    kitap_listesi_goster()  # Kitap listesini güncelle
                    return
            messagebox.showerror("Hata", "Kitap bulunamadı!")
            return
    messagebox.showerror("Hata", "Üye bulunamadı!")

def iade_et():
    uye_id = simpledialog.askinteger("Üye ID", "Lütfen üye ID'nizi girin:")
    for uye in uyeler:
        if uye.uye_id == uye_id:
            kitap_id = simpledialog.askinteger("Kitap ID", "İade etmek istediğiniz kitabın ID'sini girin:")
            for kitap in kitaplar:
                if kitap.kitap_id == kitap_id:
                    uye.iade_et(kitap)
                    kitap_listesi_goster()  # Kitap listesini güncelle
                    return
            messagebox.showerror("Hata", "Kitap bulunamadı!")
            return
    messagebox.showerror("Hata", "Üye bulunamadı!")

uye_ekle_button = tk.Button(root, text="Üye Ekle", command=uye_ekle)
uye_ekle_button.pack()

kitap_ekle_button = tk.Button(root, text="Kitap Ekle", command=kitap_ekle)
kitap_ekle_button.pack()

odunc_al_button = tk.Button(root, text="Ödünç Al", command=odunc_al)
odunc_al_button.pack()

iade_et_button = tk.Button(root, text="İade Et", command=iade_et)
iade_et_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

listbox1 = tk.Listbox(root, width=50)
listbox1.pack()

uye_listesi_goster()  # İlk üye listesini göster
kitap_listesi_goster()  # İlk kitap listesini göster

root.mainloop()
