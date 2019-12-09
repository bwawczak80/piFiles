from tkinter import *
from PIL import Image, ImageTk
import requests as req


def go():
    
    qry = {"q" : entry.get()}
    filename = entry.get()
    r = req.get("https://www.discogs.com/search/",params=qry)
    hold_string = r.text
    start_url = hold_string.find("https://img")
    stop_url = hold_string.find(".jpeg.jpg" )
    image_url = hold_string[start_url:stop_url + 9]
    r = req.get(image_url)
    if r.status_code == 200:
        print('Successful request!')
        download_file = open(filename+".jpg","wb" )
        for chunk in r.iter_content(chunk_size=256):
            if chunk:
                download_file.write(chunk)
        download_file.close()
        image = Image.open(filename+".jpg")
        photo2 = ImageTk.PhotoImage(image)
        label.configure(image=photo2)
        label.image = photo2    
        print("done")
        return
    else:
        print('An error has occurred.')


main = Tk()
frame = Frame(main)
text_label = Label(main, text="Album")
text_label.pack()
entry = Entry(main)
entry.pack()
btn_go = Button(main, text="Go", command = go)
btn_go.pack()
image = Image.open("placeholder.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(main, height=350, width=350, image=photo)
label.pack()

main.mainloop()