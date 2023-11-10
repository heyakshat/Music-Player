import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []

        self.track_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.track_label = tk.Label(root, textvariable=self.track_var, wraplength=300)
        self.track_label.pack(pady=10)

        self.status_label = tk.Label(root, textvariable=self.status_var)
        self.status_label.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.select_button = tk.Button(root, text="Select Music", command=self.select_music)
        self.select_button.pack(side=tk.RIGHT, padx=10)

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play()
            self.track_var.set("Now Playing: " + os.path.basename(self.playlist[0]))
            self.status_var.set("Status: Playing")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.status_var.set("Status: Paused")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.status_var.set("Status: Stopped")

    def select_music(self):
        file_paths = filedialog.askopenfilenames(title="Select Music", filetypes=[("MP3 Files", "*.mp3")])

        if file_paths:
            self.playlist = list(file_paths)
            self.status_var.set("Status: Playlist loaded")
            self.play_button["state"] = tk.NORMAL
            self.pause_button["state"] = tk.NORMAL
            self.stop_button["state"] = tk.NORMAL

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)

    # Initialize Pygame Mixer
    pygame.mixer.init()

    root.mainloop()
