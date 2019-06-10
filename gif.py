from tkinter import *
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

root = Tk()
img_url = "https://media.giphy.com/media/3orif3VHjBeYBDTGlG/giphy.gif"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
