from tkinter import *
from tkinter import messagebox

def count():
         end = datetime.datetime(int(yearbox.get()),int(monthbox.get()),int(daybox.get()),int(hourbox.get()),int(minutebox.get()),int(secondbox.get()))
         now = datetime.datetime.now()
         delta = end - now
         sec = round(delta.total_seconds())
         years = sec//(365*24*60*60)
         days = (sec%(365*24*60*60))//(24*60*60)
         hours = (sec%(24*60*60))//(60*60)
         minutes = (sec%(60*60))//60
         seconds = (sec%60)
         endwillcome = Label(master, text =(years,"years",days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")).place(x=0,y=200)

master = Tk()
master.title("Doomsdayclock")
master.geometry("600x300")

title = Label(master, text = "DOOMSDAYCLOCK").place(x=0,y=0)
text = Label(master, text = "BLA BLA BLA").place(x=0,y=20)

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

button = Button(master, text = "zatwierdź", command = count).place(x=0,y=160)

glowneOkno.mainloop()
