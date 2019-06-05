from tkinter import *
from tkinter import messagebox
import datetime

# funkcja licząca ile czasu pozostało do końca świata i wyświetlająca pozostały czas w odpoweidnich jednostkach
def count():
    # jako 'end' ustawiam date wprowadzoną przez użytkownika
    end = datetime.datetime(int(yearbox.get()),int(monthbox.get()),int(daybox.get()),int(hourbox.get()),int(minutebox.get()),int(secondbox.get()))
    # 'now' to dzisiejsza data
    now = datetime.datetime.now()
    delta = end - now
    # obliczenia w celu uzyskania odpowiednich jednostek czasowych
    sec = round(delta.total_seconds())
    years = sec//(365*24*60*60)
    days = (sec%(365*24*60*60))//(24*60*60)
    hours = (sec%(24*60*60))//(60*60)
    minutes = (sec%(60*60))//60
    seconds = (sec%60)
    # 'remained' oraz 'timer' pokazują ile czasu pozostało
    remained = Label(master, text = "REMAINED:")
    remained.place(x=0,y=180)
    timer = Label(master, text =(years,"years",days,"days",hours,"hours",minutes,"minutes",seconds,"seconds"))
    timer.place(x=0,y=200)
    # po sekundzie funkcja wywołuje się od nowa, przez co czas spada na oczach użytkownika
    timer.after(1000, count)


master = Tk()
master.title("Doomsdayclock")
master.geometry("600x300")


title = Label(master, text = "DOOMSDAYCLOCK").place(x=0,y=0)
# tu trzeba będzie dodać te ładne opisy:
text = Label(master, text = "BLA BLA BLA").place(x=0,y=20)

# użytkownik wprowadza datę i czas końca świata
# POTRZEBA ZNALEŹĆ INNY SPOSÓB NIŻ TE SPINBOXY, BO TU MOŻEMY WPROWADZIĆ NP: 31 LUTY
# oczywiście potrzebne opisy wszędzie
yearbox = Spinbox(master, from_ = 2019, to = 3000)
yearbox.place(x=0,y=40)
monthbox = Spinbox(master, from_ = 1, to = 12)
monthbox.place(x=0,y=60)
daybox = Spinbox(master, from_ = 1, to = 31)
daybox.place(x=0,y=80)
hourbox = Spinbox(master, from_ = 0, to = 23)
hourbox.place(x=0,y=100)
minutebox = Spinbox(master, from_ = 0, to = 59)
minutebox.place(x=0,y=120)
secondbox = Spinbox(master, from_ = 0, to = 59)
secondbox.place(x=0,y=140)

# przycisk rozpoczynający odliczanie
button = Button(master, text = "count down", command = count).place(x=0,y=160)


master.mainloop()
