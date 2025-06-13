import tkinter as tk
from PIL import Image, ImageTk
import os

class KarateScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Karate Scoreboard")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")

        self.ao_score = 0
        self.aka_score = 0
        self.ao_timer = 0
        self.aka_timer = 0
        self.running_ao = False
        self.running_aka = False

        tk.Label(root, text="Division: Team Kata Boy Beginners", font=("Arial", 24, 'bold'),
                 bg="black", fg="white").pack(pady=10)

        main_frame = tk.Frame(root, bg="black")
        main_frame.pack(expand=True, fill="both")

        self.create_team_frame(main_frame, "ao", "#007bff", "blue_flag.png", "Team 1", "Gankaku")
        self.create_team_frame(main_frame, "aka", "#ff4d4d", "red_flag.png", "Team 2", "Kosokun (Kushanku)")

        bottom_frame = tk.Frame(root, bg="black")
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text="Reset", font=("Arial", 16), bg="gray", fg="white", width=12,
                  command=self.reset_all).pack(side="left", padx=10)
        tk.Button(bottom_frame, text="Close", font=("Arial", 16), bg="orange", fg="white", width=12,
                  command=root.quit).pack(side="left", padx=10)
        
    def create_team_frame(self, parent, team, color, flag_filename, team_name, kata_style):
        frame = tk.Frame(parent, bg=color, padx=10, pady=10)
        frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        
        tk.Label(frame, text="Ao" if team == "ao" else "Aka", font=("Arial", 24, 'bold'), bg=color, fg="white").pack(anchor="nw")
        tk.Label(frame, text=team_name, font=("Arial", 16), bg=color, fg="white").pack(anchor="nw")

        style_var = tk.StringVar(value=kata_style)
        tk.OptionMenu(frame, style_var, kata_style, "Other").pack(anchor="nw", pady=10)

        top_info = tk.Frame(frame, bg=color)
        top_info.pack(pady=10)

        score_frame = tk.Frame(top_info, bg=color)
        score_frame.pack(side="left", padx=20)
        score_label = tk.Label(score_frame, text="0", font=("Digital-7", 120), bg=color, fg="white")
        score_label.pack()

        note_label = tk.Label(score_frame, text="", font=("Arial", 18, "bold"), bg=color, fg="yellow")
        note_label.pack()

