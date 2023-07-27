import os
import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    if not pygame.mixer.music.get_busy():
        if current_song.get():
            pygame.mixer.music.load(current_song.get())
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
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        current_song.set('Spectre.mp3')

root = tk.Tk()
root.title("Simple Music Player")
root.geometry("300x150")

pygame.mixer.init()

current_song = tk.StringVar()

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(side=tk.LEFT)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(side=tk.LEFT, padx=10)

choose_button = tk.Button(root, text="Choose File", command=choose_file)
choose_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
