# OCZYWIŚCIE NALEŻY WSZYSTKO ŁADNIE SFORMATOWAĆ BO NARAZIE WYGLĄDA JAK GÓWNO

from tkinter import *
from tkinter import messagebox
import datetime

# funkcja licząca ile czasu pozostało do końca świata i wyświetlająca pozostały czas w odpoweidnich jednostkach
def count():
    # 'try' daje możliwość tego, że dalsza część się wykona o ile nie napotka błędu wskazanego w 'except' (poniżej)
    try:
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
        if sec ==(3600*24*365*5) :
                    gif_window = Tk()
                    gif_window.title("Gif")
                    gif_window.geometry("300x150")
                    message = Label(gif_window,text = "Five years left")
                    message.pack()
        elif sec ==(3600*24*365) :
                    gif_window = Tk()
                    gif_window.title("Gif")
                    gif_window.geometry("300x150")
                    message = Label(gif_window,text = "One year left")
                    message.pack()
        elif sec == (3600 * 24):
                    gif_window = Tk()
                    gif_window.title("Gif")
                    gif_window.geometry("300x150")
                    message = Label(gif_window,text = "One day left")
                    message.pack()
        elif sec == 3600 :
                    gif_window = Tk()
                    gif_window.title("Gif")
                    gif_window.geometry("300x150")
                    message = Label(gif_window,text = "One hour left")
                    message.pack()
        elif sec == 0:
                    gif_window = Tk()
                    gif_window.title("Gif")
                    gif_window.geometry("300x150")
                    message = Label(gif_window,text = "Doomsday has come!")
                    message.pack()
        else:
            pass
    # 'except' określa co ma się stać, gdy program napotka błąd, w naszym programie jest to źle wpisana data przez użytkownika
    except ValueError:
        error = Label(master, text = "incorrect data")
        error.place(x=0,y=180)


master = Tk()
master.title("Doomsdayclock")
master.geometry("600x300")


title = Label(master, text = "DOOMSDAYCLOCK").place(x=240,y=0)
# tu trzeba będzie dodać te ładne opisy:

# użytkownik wprowadza datę i czas końca świata
# problem z wpisywaniem daty rozwiązany, w prawdzie na piechotę ale działa:)
# oczywiście potrzebne opisy wszędzie
yearbox = Spinbox(master, from_ = 2019, to = 9999999999)
yearbox.place(x=250,y=40)
text = Label(master, text = "year:").place(x=200,y=40)
monthbox = Spinbox(master, from_ = 1, to = 12)
monthbox.place(x=250,y=60)
text2 = Label(master, text = "month:").place(x=200,y=60)
#tu określam ile dni mają poszczególne miesiące
if int(monthbox.get())==2 and int(yearbox.get())%4==0:
    daybox = Spinbox(master, from_ = 1, to = 29)
    daybox.place(x=250,y=80)
elif int(monthbox.get())==2 and int(yearbox.get())%4!=0:
    daybox = Spinbox(master, from_ = 1, to = 28)
    daybox.place(x=250,y=80)
elif int(monthbox.get())==4 or int(monthbox.get())==6 or int(monthbox.get())==9 or int(monthbox.get())==11:
    daybox = Spinbox(master, from_ = 1, to = 30)
    daybox.place(x=250,y=80)
else:
    daybox = Spinbox(master, from_ = 1, to = 31)
    daybox.place(x=250,y=80)
text = Label(master, text = "day:").place(x=200,y=80)
hourbox = Spinbox(master, from_ = 0, to = 23)
hourbox.place(x=250,y=100)
text = Label(master, text = "hour:").place(x=200,y=100)
minutebox = Spinbox(master, from_ = 0, to = 59)
minutebox.place(x=250,y=120)
text = Label(master, text = "minute:").place(x=200,y=120)
secondbox = Spinbox(master, from_ = 0, to = 59)
secondbox.place(x=250,y=140)
text = Label(master, text = "second:").place(x=200,y=140)

# przycisk rozpoczynający odliczanie
button = Button(master, text = "count down", command = count).place(x=245,y=170)


master.mainloop()
