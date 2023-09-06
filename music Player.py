from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

co1 = "#ffffff" #white
co2 = "#007500" #green
co3 = "#333333" #black

window = Tk()
window.title("Music Player")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE,height=FALSE)

#functions

def play_music():
    running = listbox.get(ACTIVE)
    running_song['text']= running
    mixer.music.load(running)
    mixer.music.play()

def pause():
    mixer.music.pause()

def next_music():
    playing= running_song['text']
    index= songs.index(playing)
    new_index = index +1
    playing= songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text']=playing

def prev_music():
    playing= running_song['text']
    index= songs.index(playing)
    new_index = index -1
    playing= songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text']=playing

#divs
left_frame = Frame(window, width=150, height=150,bg=co1)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame = Frame(window, width=250, height=150,bg=co3)
right_frame.grid(row=0,column=1,padx=0)

down_frame = Frame(window, width=400, height=100,bg=co2)
down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

#right division
listbox= Listbox(right_frame, selectmode=SINGLE,font=('Helvetica',10,"italic"),width=32,bg=co3,fg=co1)
listbox.grid(row=0,column=0)

w = Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

running_song= Label(down_frame, text="Choose a Song", anchor=NW, font=('Ivy 10'), width=44, height=1,padx=10, bg=co3, fg=co1)
running_song.place(x=0,y=1)

#images
img1= Image.open('icons/music.png')
img1= img1.resize((130,130))
img1= ImageTk.PhotoImage(img1)
app_img= Label(left_frame,height=125,image=img1,padx=10,bg=co1)
app_img.place(x=7,y=10)

img2= Image.open('icons/ico3.png')
img2= img2.resize((30,30))
img2= ImageTk.PhotoImage(img2)
prev_button= Button(down_frame,height=40,width=40,image=img2,padx=10,bg=co1, font=("Ivy 10"), command=prev_music)
prev_button.place(x=10+78,y=35)

img3= Image.open('icons/ico2.png')
img3= img3.resize((30,30))
img3= ImageTk.PhotoImage(img3)
next_button= Button(down_frame,height=40,width=40,image=img3,padx=10,bg=co1, font=("Ivy 10"), command=next_music)
next_button.place(x=130+78,y=35)

img4= Image.open('icons/ico1.png')
img4= img4.resize((30,30))
img4= ImageTk.PhotoImage(img4)
play_button= Button(down_frame, height=40, width=40, image=img4, padx=10, bg=co1, font=("Ivy 10"), command= play_music)
play_button.place(x=50+78,y=35)

img5= Image.open('icons/ico4.png')
img5= img5.resize((30,30))
img5= ImageTk.PhotoImage(img5)
pause_button= Button(down_frame,height=40,width=40,image=img5,padx=10,bg=co1, font=("Ivy 10"), command= pause)
pause_button.place(x=90+78,y=35)

os.chdir(r'C:\Users\shaik\Documents\GitHub\CodeClause\music')
songs= os.listdir()

def show():
    for i in songs:
        listbox.insert(END,i)

show()
mixer.init()
music_state= StringVar()
music_state.set('Choose one!')
window.mainloop()