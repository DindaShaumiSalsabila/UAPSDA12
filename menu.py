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


def animate(self, label, text, button_frame):
        def run(i=0):
            if i <= len(text):
                label.config(text=text[:i])
                self.root.after(40, lambda: run(i+1))
            else:
                style = ttk.Style()
                style.configure("Huge.TButton",
                    font=("Helvetica", 28, "bold"),
                    padding=(30, 20),
                    background=ACCENT,
                    foreground=TEXT)
                style.map("Huge.TButton",
                    background=[('active', "#c71d7b")],
                    foreground=[('active', TEXT)])
                
                ttk.Button(button_frame, text="Selanjutnya", command=self.show_team, style="Huge.TButton").pack(
                    pady=30, fill="x", padx=100
                )
        run()

    def show_welcome(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        lbl_title = tk.Label(frame, text="", font=self.hfont, fg=ACCENT, bg=BG)
        lbl_title.pack(pady=15)

        self.animate(lbl_title, "Selamat datang di Program Kami", frame)

        try:
            screen_width = self.root.winfo_screenwidth()
            img_path = os.path.join("gambar", "gambarkelompok.png")
            img_kel = Image.open(img_path).resize((screen_width - 100, 380))
            self.img_kelompok = ImageTk.PhotoImage(img_kel)
            lbl_img = tk.Label(frame, image=self.img_kelompok, bg=BG)
            lbl_img.pack(pady=(30, 20))
        except:
            tk.Label(frame, text="[Gambar Kelompok Tidak Ditemukan]", font=self.sfont, fg="red", bg=BG).pack(pady=20)

    def show_team(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(frame, text="Developer", font=self.hfont, fg=ACCENT, bg=BG).pack(pady=20)

  grid = tk.Frame(frame, bg=BG)
        grid.pack(expand=True, fill="both")
        grid.grid_columnconfigure((0, 1), weight=1)

        members = [
            {"name": "Faqih Lakaisha .P.", "role": "2417051037", "key": "Faqih"},
            {"name": "Herdi Irawan", "role": "2417051040", "key": "Herdi"},
            {"name": "Dinda Shaumi .S.", "role": "2417051033", "key": "Dinda"},
            {"name": "Annisa Syifa .H.", "role": "2417051019", "key": "Nisa"}
        ]

        for i, m in enumerate(members):
            row = i // 2
            col = i % 2
            card = tk.Frame(grid, bg=ACCENT, bd=2, relief="raised", height=180)
            card.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
            card.grid_propagate(False)

            left_info = tk.Frame(card, bg=ACCENT)
            left_info.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=10)

            tk.Label(left_info, text=m["name"], font=("Helvetica", 14, "bold"), fg=WHITE, bg=ACCENT, anchor="w").pack(anchor="w", pady=(10, 0))
            tk.Label(left_info, text=m["role"], font=("Helvetica", 12), fg="#bfdbfe", bg=ACCENT, anchor="w").pack(anchor="w", pady=(5, 0))

            right_photo = tk.Frame(card, bg=ACCENT, width=150)
            right_photo.pack(side="right", fill="both", pady=0)

            photo = self.photos.get(m["key"])
            if photo:
                tk.Label(right_photo, image=photo, bg=ACCENT).pack(expand=True, fill="both")
            else:
                tk.Label(right_photo, text="[Foto]", bg=ACCENT, fg=WHITE, font=("Helvetica", 16)).pack(expand=True, fill="both")

        style = ttk.Style()
        style.configure("Big.TButton",
            font=("Helvetica", 20, "bold"),
            padding=15,
            background=ACCENT,
            foreground=TEXT)
        style.map("Big.TButton",
            foreground=[('active', TEXT)],
            background=[('active', "#c71d7b")])

        ttk.Button(frame, text="Selanjutnya", command=self.show_menu, style="Big.TButton").pack(pady=30, fill="x", padx=50)

    def show_menu(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(frame, text="Pilih Program", font=self.hfont, fg=ACCENT, bg=BG).pack(pady=20)
        tk.Label(frame, text="Silakan pilih salah satu program untuk melanjutkan:", font=self.sfont, fg=ACCENT, bg=BG).pack(pady=10)

        style = ttk.Style()
        style.configure("Big2.TButton",
            font=("Helvetica", 20, "bold"),
            padding=15,
            background=ACCENT,
            foreground=TEXT)
        style.map("Big2.TButton",
            foreground=[('active', TEXT)],
            background=[('active', "#f3acd2")])

        ttk.Button(frame, text="Timer Pertandingan", command=lambda: self.run_script("scoreboard.py"), style="Big2.TButton").pack(pady=10, fill="x")
        ttk.Button(frame, text="Data Rank Peserta", command=lambda: self.run_script("protambah.py"), style="Big2.TButton").pack(pady=10, fill="x")
        ttk.Button(frame, text="Kembali", command=self.root.quit, style="Big2.TButton").pack(pady=30, fill="x")

    def run_script(self, script):
        try:
            subprocess.Popen(["python", script])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeApp(root)
    root.mainloop()
