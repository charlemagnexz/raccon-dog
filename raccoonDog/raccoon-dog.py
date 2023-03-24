import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image


def downloadFile():

    # grabs youtube link from input
    youTubeLink = video_entry.get()

    # grabs the link
    myVid = YouTube(youTubeLink)

    # prints info on linked video onto the terminal
    print("Title: ", myVid.title)
    print("Author: ", myVid.author)
    print("Description: ", myVid.description)

    # selects the highest video resolution for download
    dv = myVid.streams.get_highest_resolution()

    # downloads video // creates folder if none exists
    dv.download("/raccoon-dog-videos")

    messagebox.showinfo(title="Theft Success",
                        message="You have successfully stolen this video :)")

    video_entry.delete(0, 'end')


root = tk.Tk()
root.geometry("1000x800")
root.title("Raccoon Dog")
root.configure(bg="#fff")

ico = Image.open('raccoon-dog3.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

frame = tk.Frame(root, width=900, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("raccoon-dog2.jpg"))

# Create a Label Widget to display the text or Image
label = tk.Label(frame, image=img, bg="#fff")
label.pack()

title_label = tk.Label(root, text="Raccoon Dog",
                       bg="#fff", font=("Bodoni MT Poster Compressed", 50))
input_label = tk.Label(
    root, text="Please present your trash", bg="#fff", font=("Arial", 15))
video_entry = tk.Entry(root, width=60)
openfile_button = tk.Button(
    root, text="Download", bg="#fff", command=downloadFile)

title_label.pack(padx=10, pady=10)
input_label.pack(padx=10, pady=10)
video_entry.pack(padx=10, pady=10)
openfile_button.pack(padx=10, pady=10)


root.mainloop()
