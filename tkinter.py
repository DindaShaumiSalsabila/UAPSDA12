import tkinter as tk
from tkinter import ttk, font
import time

class WelcomeApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Welcome & Perkenalan Kelompok")
        self.root.geometry("800x600") 
        self.root.configure(bg="#FFFFFF")
self.header_font = font.Font(family="Helvetica", size=36, weight="bold")
        self.subheader_font = font.Font(family="Helvetica", size=16)
        self.card_font = font.Font(family="Helvetica", size=16)
        self.name_font = font.Font(family="Helvetica", size=14)
        self.button_font = font.Font(family="Helvetica", size=12)
        
        style = ttk.Style()
        style.configure("TButton", font=self.button_font, padding=10, background="")
        style.map("TButton",
                  background=[('active', "#FF75DC"), ('!active', '#FF75DC')],
                  foreground=[('active', '#000000'), ('!active', '#000000')])
        
        self.show_welcome_page()

    def show_welcome_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
 self.welcome_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.welcome_frame.pack(expand=True, fill="both")
        
        self.welcome_label = tk.Label(self.welcome_frame, text="", font=self.header_font,
                                      fg="#FF75DC", bg="#FFFFFF")
        self.welcome_label.pack(pady=50)
        
        tk.Label(self.welcome_frame, text="Selamat datang di presentasi kami!",
                 font=self.subheader_font, fg="#FF75DC", bg="#FFFFFF").pack(pady=20)
        
        welcome_text = "Welcome!"
        self.animate_text(self.welcome_label, welcome_text)

 def animate_text(self, widget, text):
        for i in range(len(text) + 1):
            widget.configure(text=text[:i])
            self.root.update()
            time.sleep(0.1)
        
        ttk.Button(self.welcome_frame, text="Lanjutkan", command=self.show_team_page, style="TButton").pack(pady=20)
def show_team_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        team_frame = tk.Frame(self.root, bg="#FFFFFF")
        team_frame.pack(expand=True, fill="both")
        
        tk.Label(team_frame, text="Perkenalan Kelompok", font=self.header_font,
                 fg="#FF75DC", bg="#FFFFFF").pack(pady=20)
        
        members_frame = tk.Frame(team_frame, bg="#FFFFFF")
        members_frame.pack(expand=True, fill="both", padx=20, pady=0)
        
        members_frame.grid_columnconfigure(0, weight=1)
        members_frame.grid_columnconfigure(1, weight=1)
        
        members = [
            {"name": "Faqih Lakaisha .P.", "role": "2417051037"},
            {"name": "Herdi Irawan", "role": "2417051040"},
            {"name": "Dinda Shaumi .S.", "role": "2417051033"},
            {"name": "Annisa Syifa .H.", "role": "2417051019"}
        ]
        
        for i, member in enumerate(members):
            row = i // 2
            col = i % 2
            self.create_member_card(members_frame, member["name"], member["role"], row, col)
        
        ttk.Button(team_frame, text="Lanjutkan ke Projek", command=self.show_project_selection, style="TButton").pack(pady=20)

