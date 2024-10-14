import tkinter as tk
from tkinter import messagebox
def bmi_hesapla():
    try:

        if not kilo_entry.get() or not boy_entry.get():
            raise ValueError("Lütfen tüm alanları doldurun.")

        kilo=float(kilo_entry.get())
        boy=float(boy_entry.get()) / 100
        bmi=kilo / (boy **2)

        if bmi<18.5:
            sonuc= f"BMI : {bmi:.2f} (Underweight)"
        elif 18.5<=bmi<=25:
            sonuc=f"BMI : {bmi:.2f} (Normal weight)"
        elif 25<=bmi<=30:
            sonuc=f"BMI : {bmi:.2f} (Overweight)"
        else:
            sonuc=f"BMI : {bmi:.2f} (Obesity)"

        messagebox.showinfo("BMI Sonucu:", sonuc)
    except ValueError as e:
        # Hata mesajına göre uygun uyarıyı göster
        if str(e) == "Lütfen tüm alanları doldurun.":
            messagebox.showerror("Hatalı giriş", str(e))
        else:
            messagebox.showerror("Hatalı giriş", "Lütfen geçerli bir sayı girin.")


windoww=tk.Tk()
windoww.title("bmi hesaplıyom")
windoww.geometry("300x200")

#kilo
tk.Label(windoww,text="Kilonuzu girin(kg):").pack(pady=5)
kilo_entry=tk.Entry(windoww)
kilo_entry.pack()

#boy
tk.Label(windoww,text="Boyunuzu girin:").pack(pady=5)
boy_entry=tk.Entry(windoww)
boy_entry.pack()

hesaplama_butonu=tk.Button(windoww,text="Hesapla",command=bmi_hesapla)
hesaplama_butonu.pack()
windoww.mainloop()