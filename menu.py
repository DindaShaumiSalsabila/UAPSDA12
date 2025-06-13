import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import subprocess
import os

BG = "#FFFFFF"
ACCENT = "#e9258e"
WHITE = "#ffffff"
TEXT = "#000000"

class WelcomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome & Perkenalan Kelompok")
        self.root.state("zoomed")
        self.root.configure(bg=BG)

        self.hfont = font.Font(family="Helvetica", size=36, weight="bold")
        self.sfont = font.Font(family="Helvetica", size=16)
        self.bfont = font.Font(family="Helvetica", size=14, weight="bold")

        self.photos = {}
        self.load_photos()

        self.show_login()

    def load_photos(self):
        filenames = {
            "Faqih": "fotofaqih.png",
            "Herdi": "fotoherdi.png",
            "Dinda": "fotodinda.png",
            "Nisa": "fotonisa.png"
        }
        for key, file in filenames.items():
            try:
                img_path = os.path.join("gambar", file)
                img = Image.open(img_path).resize((330, 180))
                self.photos[key] = ImageTk.PhotoImage(img)
            except:
                self.photos[key] = None

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear()
        container = tk.Frame(self.root, bg=BG)
        container.pack(expand=True, fill="both")

        left_frame = tk.Frame(container, bg=BG)
        left_frame.pack(side="left", fill="both", expand=True)
        left_frame.pack_propagate(False)

