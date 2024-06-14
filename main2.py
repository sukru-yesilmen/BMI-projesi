import tkinter

def on_window_resize(event):
    mylabel.place(relx=0.5, rely=0.1, anchor="center")

def on_entry_click(event):
    myentry.delete(0, tkinter.END)  # Entry içindeki tüm metni sil
# Bu, silme işleminin başlangıç indeksini belirtir. 0, metnin en başından itibaren başlamak anlamına gelir.
# Bu, silme işleminin bitiş indeksini belirtir. tkinter.END, metnin sonunu ifade eder.bu sayede de daha dinamik bir yapıya sahip olmuş
# oldu.
def on_entry_click2(event):
    myentry2.delete(0, tkinter.END)

def clickButton():
    try:
        kilo = float(myentry.get())
        boy = float(myentry2.get())
        BMI = kilo / (boy * boy)
        if BMI<18.5:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen zayıfsın")
        elif BMI>=18.5 and BMI<24.9:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen normal Kilolusun")
        elif BMI>=25 and BMI<29.4:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen hafif kilolusun")
        elif BMI>=30 and BMI<34.9:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen şişman (obez) sınıf-1")
        elif BMI>=18.5 and BMI<24.9:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen şişman (obez) sınıf-2")
        else:
            print(f"Vücut Kitle İndeksin:{BMI} ve sen Şişman(Obez)-Sınıf III")
    except ValueError:
        print("Lütfen geçerli sayısal değerler girin.")

mywindow = tkinter.Tk()                                 # burada ben penceremi tanımladım
mywindow.title("BMI Hesaplayıcı")


                        # burada mywindow yazmamın sebebi o pencereye ait olduğunu göstermek bu okunaklığı artırır önemlidir.
mylabel = tkinter.Label(mywindow, text="!!Vücüt İndeks Hesaplamak için Doğru Yerdesin!!", font=("Helvetica", 20))
mylabel.place(relx=0.5, rely=0.1, anchor="center")
# ben normalde x ve y değerlerini kullanırdım onlar oldukça sitatik bir yapıya sahipler relx ve rely ise böyle değil
# çünkü ben relx = 0.5 derken ekranın yani x ekseninin yarısı demek istiyorum.sağını 1 solunu 0 olarak algılıyo.
# aynı olgu y ekseni içinde geçerli kardeşş.
# peki anchor ne işe yarar burada o da şu ;
# anchor parametresi, place yöntemi ile bir widget'ı yerleştirirken, widget'ın kendisini referans alarak konumlandırılacağı noktayı
# belirler. Bu parametre, widget'ın hangi noktasının belirtilen koordinatlara yerleştirileceğini kontrol eder.oldukça kullanışlı bir
# yapısı vardır.

mywindow.bind("<Configure>", on_window_resize)  # Ekran boyutu değiştiğinde tetiklenecek fonksiyon
# buradaki .bing şu işe yarar;
# Tkinter'daki bind fonksiyonu, bir olaya (event) bir fonksiyon bağlamak için kullanılır. İlk parametre, bağlanacak olayı belirtir
# "<Configure>" olayı, pencerenin boyutunun, konumunun veya başka bir yapılandırma özelliğinin değiştiği anlamına gelir.
# Yani, pencereniz boyutlandırıldığında, bu olay tetiklenir.ben bunu aynı şekilde farklı yapılara da bağlayabilirim.


myentry = tkinter.Entry(mywindow)                 # aynı şekilde mywindow'a bağlı olduğunu gösterdim.
myentry.place(relx=0.5,rely=0.2, anchor="center")
myentry.config(width=20)
myentry.insert(0, "Kilo(kg)") # index eklenecek metnin hangi indeksten başlayarak eklenmesi gerektiğini belirtir.
myentry.bind("<Button-1>", on_entry_click)


myentry2 = tkinter.Entry(mywindow)
myentry2.place(relx=0.5,rely=0.3, anchor="center")
myentry2.config(width=20)
myentry2.insert(0, "Boy(m)")
myentry2.bind("<Button-1>", on_entry_click2)


mybutton = tkinter.Button(text="Hesapla",command=clickButton)
mybutton.place(relx=0.5, rely=0.4, anchor="center")




mywindow.mainloop()                   # ben eğer penceremin ayakta durmasını istiyorsam mainloop() kullanmak zorundayım
                                      # done() dan kullanabilirsin fakat done() genellikle turtle kütüphanesinde kullanılır.ayrıca
                                      # basit uygulamalarda.