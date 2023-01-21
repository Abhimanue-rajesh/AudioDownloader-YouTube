from tkinter import *
from tkinter import  filedialog 
import customtkinter
from customtkinter import *
from pytube import YouTube
import os

#theme and apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#main_window_managment
root = customtkinter.CTk()
root.title('Youtube Audio Downloader')
root.minsize(1330,690)
window_width = 1330
window_height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
center_y_n = center_y - 35
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y_n}')
#icon
photo = PhotoImage(file = "youtube1.png")
root.iconphoto(False, photo)
    
#funtions
def destination():
    global save_directory
    global label
    save_directory = filedialog.askdirectory(title = "Select A Folder To Save Your File")
    label.configure(text="Destination : \n "+ save_directory,font=('Century Gothic',20))
    if len(save_directory) == 0:
        label.configure(text='No Location Found, Click On The Destination Button To Select The Destination',text_color='Red')
    else :
        switchButtonState()
    return
        
def switchButtonState():
    global download_button
    state = download_button.cget("state")
    if state == "disabled":
        download_button.configure(state=NORMAL)
    elif state =="normal":
        download_button.configure(state=DISABLED)

def progressbar_start():
    progressbar.start()
    
def url_download():
    global url_entry
    global progressbar
    url_string = url_entry.get()
    partioned_string = url_string.partition('youtube')
    if 'youtube' in partioned_string:
        label.configure(text="Downloading Your File to "+save_directory)
        progressbar_start()
        yt = YouTube( str(url_string))
        audio_file = yt.streams.filter(only_audio=True).first()
        out_file = audio_file.download(output_path=save_directory)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        progressbar.stop()
        label.configure(text=yt.title + " has been successfully downloaded.")
    elif not url_string:
        label.configure(text='No Valid URL Found, Enter The URL And Retry')

def switch_event():
    state = switch_1.get()
    print(state)
    switch_1.configure(text= 'Switch To Dark Theme')
    if state == 'on':
        customtkinter.set_appearance_mode("light")
    elif state == 'off':
        switch_1.configure(text='Switch To Light Theme')
        customtkinter.set_appearance_mode("dark")
        
    
#widgets
#buttons_w
#download_button
download_button = customtkinter.CTkButton(master=root, text = "Download",command=url_download,
                                          width=300,
                                          height=60,corner_radius=20,
                                          font=('Century Gothic',30))
download_button.place(relx=0.68, rely= 0.53, anchor= CENTER)
download_button.configure(state=DISABLED)
#destination_button
destination_button = customtkinter.CTkButton(master=root, text="Choose Destination",command=destination,
                                             width=300,
                                             height=60,corner_radius=20,
                                             font=('Century Gothic',28))
destination_button.place(relx=0.32, rely=0.53, anchor= CENTER)
#exit_button
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,
                                      width=300,
                                      height=60,corner_radius=20,
                                      hover_color='Red4')
exit_button.place(relx=0.5,rely=0.8,anchor=CENTER)
#entry_w
url_entry = customtkinter.CTkEntry(master=root,
                               placeholder_text="Enter the Video URL",
                               width=1000,
                               height=50,
                               border_width=2,
                               corner_radius=25)
url_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
#label_w
label = customtkinter.CTkLabel(master=root,
                               text="Choose The Destination To Save Your File",
                               width=500,
                               height=50,
                               fg_color=("transparent"),
                               font = ('Century Gothic', 28),
                               text_color='Green',
                               corner_radius=10)
label.place(relx=0.5, rely=0.3, anchor=CENTER)
#progressbar_w
progressbar = customtkinter.CTkProgressBar(master=root,
                                           corner_radius=10,
                                           width=500,
                                           height=15,mode = 'indeterminate')
progressbar.pack(padx=20, pady=310)
#switch_w
switch_1 = customtkinter.CTkSwitch(master=root, text="Switch Appearance",command = switch_event,
                                   onvalue="on", offvalue="off")
switch_1.pack(padx=20, pady=10)

root.mainloop()
