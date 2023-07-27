
playlist = ['Alone.mp3','Darkside.mp3','Faded.mp3','Spectre.mp3']
import os
import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(playlist[2])
        pygame.mixer.music.play()

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()

def unpause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Alone.mp3")])
    if file_path:
        playlist.append("Alone.mp3")
        playlist_listbox.insert(tk.END, os.path.basename("Alone.mp3"))

def play_selected_song(event):
    global current_song_index
    selected_index = playlist_listbox.curselection()
    if selected_index:
        current_song_index = selected_index[0]
        play_music()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_music()

def set_volume(val):
    pygame.mixer.music.set_volume(float(val) / 100)

root = tk.Tk()
root.title("SB music player")
root.geometry("400x300")

pygame.mixer.init()

current_song_index = 0
playlist = []

playlist_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
playlist_listbox.pack(expand=True, fill=tk.BOTH)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(side=tk.LEFT)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(root, text="Next", command=next_song)
next_button.pack(side=tk.RIGHT, padx=10)

prev_button = tk.Button(root, text="Previous", command=prev_song)
prev_button.pack(side=tk.RIGHT)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.set(50)  # Set initial volume to 50%
volume_slider.pack(side=tk.BOTTOM, fill=tk.X)

choose_button = tk.Button(root, text="Add to Playlist", command=choose_file)
choose_button.pack(side=tk.BOTTOM, pady=10)

playlist_listbox.bind("<Double-Button-1>", play_selected_song)

root.mainloop()
