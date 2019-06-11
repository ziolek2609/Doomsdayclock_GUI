from tkinter import *
import datetime
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import sys

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
        remained = Label(master,bg="#ff0000",font=("Times New Roman",20),foreground="white",text = "REMAINED:")
        remained.place(x=30,y=280)
        timer=Label(master,bg="lightcoral",font=("Verdana",12),text=("years:",years))
        timer.place(x=30,y=320)
        timer=Label(master,bg="lightcoral",font=("Verdana",12),text=("days:",days))
        timer.place(x=30,y=345)
        timer=Label(master,bg="lightcoral",font=("Verdana",12),text=("hours:",hours))
        timer.place(x=30,y=370)
        timer=Label(master,bg="lightcoral",font=("Verdana",12),text=("minutes:",minutes))
        timer.place(x=30,y=395)
        timer=Label(master,bg="lightcoral",font=("Verdana",12),text=("seconds:",seconds))
        timer.place(x=30,y=420)
        # po sekundzie funkcja wywołuje się od nowa, przez co czas spada na oczach użytkownika
        timer.after(1000, count)
        if sec ==(3600*24*365*5) :
            gif_window =Toplevel()
            gif_window.title("Memento mori")
            gif_window.geometry("650x400")
            panel = Label(gif_window, image=img)
            panel.pack(fill=BOTH, expand = 1)
            message = Label(gif_window,pady=10,font=("Verdana 20"),bg="black",foreground="white",text = "Five years left")
            message.pack(BOTTOM)

        elif sec ==(3600*24*365) :
            gif_window =Toplevel()
            gif_window.title("Memento mori")
            gif_window.geometry("650x400")
            panel = Label(gif_window, image=img2)
            panel.pack(fill=BOTH, expand = 1)
            message = Label(gif_window,pady=10,font=("Verdana 20"),bg="black",foreground="white",text = "One Year left")
            message.pack(side=BOTTOM)
        elif sec == (3600 * 24):
            gif_window =Toplevel()
            gif_window.title("Memento mori")
            gif_window.geometry("650x400")
            panel = Label(gif_window, image=img3)
            panel.pack(fill=BOTH, expand = 1)
            message = Label(gif_window,pady=10,font=("Verdana 20"),bg="black",foreground="white",text = "One day left")
            message.pack(side=BOTTOM)
        elif sec == 3600 :
            gif_window =Toplevel()
            gif_window.title("Memento mori")
            gif_window.geometry("650x400")
            panel = Label(gif_window, image=img4)
            panel.pack(fill=BOTH, expand = 1)
            message = Label(gif_window,pady=10,font=("Verdana 20"),bg="black",foreground="white",text = "One hour left")
            message.pack(side=BOTTOM)
        elif sec == 0:
            gif_window =Toplevel()
            gif_window.title("Memento mori")
            gif_window.geometry("650x400")
            panel = Label(gif_window, image=img5)
            panel.pack(fill=BOTH, expand = 1)
            message = Label(gif_window,pady=10,font=("Verdana 20"),bg="black",foreground="white",text = "This is the end!")
            message.pack(side=BOTTOM)
        else:
            pass
    # 'except' określa co ma się stać, gdy program napotka błąd, w naszym programie jest to źle wpisana data przez użytkownika
    except ValueError:
        error = Label(master, text = "incorrect data")
        error.place(x=0,y=180)

    text=Label(master,font=("Verdana 20 bold"),text=("There is\nNO\nTURNING\nBACK!"))
    text.place(x=580,y=300)

master = Tk()
master.title("Doomsdayclock")
master.geometry("800x500")
img_url = "https://media.giphy.com/media/3orif3VHjBeYBDTGlG/giphy.gif"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

img_url2= 'https://media.giphy.com/media/xT9IgIqup6NRcbVI8U/giphy.gif'
response2 = requests.get(img_url2)
img_data2 = response2.content
img2 = ImageTk.PhotoImage(Image.open(BytesIO(img_data2)))

img_url3 = 'https://media.giphy.com/media/y3e2P2Sdf8RUc/giphy.gif'
response3 = requests.get(img_url3)
img_data3 = response3.content
img3 = ImageTk.PhotoImage(Image.open(BytesIO(img_data3)))

img_url4 ='https://media.giphy.com/media/BpXmTsM9q9thS/giphy.gif'
response4 = requests.get(img_url4)
img_data4 = response4.content
img4 = ImageTk.PhotoImage(Image.open(BytesIO(img_data4)))

img_url5 = 'https://media.giphy.com/media/fImh4xthZV5lK/giphy.gif'
response5 = requests.get(img_url5)
img_data5 = response5.content
img5 = ImageTk.PhotoImage(Image.open(BytesIO(img_data5)))

title = Label(master,text ="DOOMSDAYCLOCK",font=("Times New Roman",40),foreground="white",bg="#ff0000",borderwidth=9,width=26).place(x=0,y=0)
# tu trzeba będzie dodać te ładne opisy:
textbox=Text(master,width=600,height=200)
textbox.pack()
textbox.place(x=0,y=80)
textbox.insert(END,"                                 \"We all have two lifes.\nThe second one starts when you realize, that you only have one.\"\n",("h1"))
textbox.insert(END,"                                                   Since you've realized it, end your first life.\n",("h2"))
textbox.insert(END,"           Thanks to our great DoomsdayClock you'll be able to know how much time you have on this world.\n"
                "                           The most incredible thing is that it's you who choose THE HOUR.\n"
                "                                                  Choose wisely.\n",("h3"))
textbox.insert(END,"                              Our best specialists took care your sense of humor is fine while waiting for the end of the world.                                ",("h4"))
textbox.tag_add("h1","1.0","1.0")
textbox.tag_config("h1",font=("Helvetica",20,"italic"),spacing3=10)
textbox.tag_add("h2","1.0","1.0")
textbox.tag_config("h2",font=("Verdana",10),spacing3=10)
textbox.tag_add("h3","1.0","1.0")
textbox.tag_config("h3",font=("Courier",8),background="#d9d9d9")
textbox.tag_add("h4","1.0","1.0")
textbox.tag_config("h4",font=("Ariel",10),spacing1=10,background="lightcoral")
# użytkownik wprowadza datę i czas końca świata
# problem z wpisywaniem daty rozwiązany, w prawdzie na piechotę ale działa:)
# oczywiście potrzebne opisy wszędzie
xboxposition=370
yboxposition=300
xtextposition=305
ytextposition=300
yearbox = Spinbox(master, from_ = 2019, to = 9999999999)
yearbox.place(x=xboxposition,y=yboxposition)
text = Label(master,text = "year:").place(x=xtextposition,y=ytextposition)
monthbox = Spinbox(master, from_ = 1, to = 12)
monthbox.place(x=xboxposition,y=yboxposition+20)
text = Label(master,bg="#ffb3b3",text = "month:").place(x=xtextposition,y=ytextposition+20)
#tu określam ile dni mają poszczególne miesiące
if int(monthbox.get())==2 and int(yearbox.get())%4==0:
    daybox = Spinbox(master, from_ = 1, to = 29)
    daybox.place(x=xboxposition,y=yboxposition+40)
elif int(monthbox.get())==2 and int(yearbox.get())%4!=0:
    daybox = Spinbox(master, from_ = 1, to = 28)
    daybox.place(x=xboxposition,y=yboxposition+40)
elif int(monthbox.get())==4 or int(monthbox.get())==6 or int(monthbox.get())==9 or int(monthbox.get())==11:
    daybox = Spinbox(master, from_ = 1, to = 30)
    daybox.place(x=xboxposition,y=yboxposition+40)
else:
    daybox = Spinbox(master, from_ = 1, to = 31)
    daybox.place(x=xboxposition,y=yboxposition+40)
text = Label(master,text = "day:").place(x=xtextposition,y=ytextposition+40)
hourbox = Spinbox(master, from_ = 0, to = 23)
hourbox.place(x=xboxposition,y=yboxposition+60)
text = Label(master,bg="#ffb3b3",text = "hour:").place(x=xtextposition,y=ytextposition+60)
minutebox = Spinbox(master, from_ = 0, to = 59)
minutebox.place(x=xboxposition,y=yboxposition+80)
text = Label(master, text = "minute:").place(x=xtextposition,y=ytextposition+80)
secondbox = Spinbox(master, from_ = 0, to = 59)
secondbox.place(x=xboxposition,y=yboxposition+100)
text = Label(master,bg="#ffb3b3",text = "second:").place(x=xtextposition,y=ytextposition+100)

# przycisk rozpoczynający odliczanie
button=Button(master,font=("Verdana 15 bold"),text="COUNT DOWN",command=count,activebackground="red",
bg="#e6e6e6",foreground="red",height="2",width="13",overrelief="groove"
).place(x=310,y=420)


master.mainloop()
