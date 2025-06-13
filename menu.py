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
        
        try:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            img_path = os.path.join("gambar", "gambarlogin.png")
            img_login = Image.open(img_path).resize((screen_width // 2, screen_height))
            self.img_login = ImageTk.PhotoImage(img_login)
            lbl_img = tk.Label(left_frame, image=self.img_login)
            lbl_img.pack(fill="both", expand=True)
        except:
            tk.Label(left_frame, text="[Gambar Login Tidak Ditemukan]", font=self.sfont, fg="red", bg=BG).pack(expand=True)
            
            right_frame = tk.Frame(container, bg=BG)
            right_frame.pack(side="right", fill="both", expand=True)
            right_frame.pack_propagate(False)
            
            form_frame = tk.Frame(right_frame, bg=BG)
            form_frame.place(relx=0.5, rely=0.5, anchor="center")
            
            tk.Label(form_frame, text="Login Dulu Yuk!", font=self.hfont, fg=ACCENT, bg=BG).pack(pady=(0, 30))
            
            username_var = tk.StringVar()
            password_var = tk.StringVar()
            
            tk.Label(form_frame, text="Username", font=self.sfont, fg=TEXT, bg=BG).pack(anchor="w")
            ttk.Entry(form_frame, textvariable=username_var, font=self.sfont, width=30).pack(pady=(0, 20))
            tk.Label(form_frame, text="Password", font=self.sfont, fg=TEXT, bg=BG).pack(anchor="w")
            ttk.Entry(form_frame, textvariable=password_var, font=self.sfont, show="*", width=30).pack(pady=(0, 30))
            
            error_label = tk.Label(form_frame, text="", font=("Helvetica", 10), fg="red", bg=BG)
            error_label.pack()

    def check_login():
        if username_var.get() == "admin" and password_var.get() == "123":
            self.show_welcome()
        else:
            error_label.config(text="Username atau password salah.")
            
            style = ttk.Style()
            style.configure("Login.TButton", font=("Helvetica", 12, "bold"), padding=(10, 5), foreground=ACCENT, background=WHITE, borderwidth=0) style.map("Login.TButton", background=[('active', "#fcd7e8")], foreground=[('active', ACCENT)])
            ttk.Button(form_frame, text="Login", command=check_login, style="Login.TButton").pack(pady=10)

