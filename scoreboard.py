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

        self.create_team_frame(main_frame, "ao", "#00449f", "blue_flag.png", "Team 1", "Gankaku")
        self.create_team_frame(main_frame, "aka", "#b60000", "red_flag.png", "Team 2", "Kosokun (Kushanku)")

        bottom_frame = tk.Frame(root, bg="black")
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text="Reset", font=("Arial", 16), bg="gray", fg="white", width=12,
                  command=self.reset_all).pack(side="left", padx=10)
        tk.Button(bottom_frame, text="Close", font=("Arial", 16), bg="orange", fg="white", width=12,
                  command=root.quit).pack(side="left", padx=10)

    def create_team_frame(self, parent, team, color, flag_filename, team_name, kata_style):
        frame = tk.Frame(parent, bg=color)
        frame.pack(side="left", expand=True, fill="both")

        tk.Label(frame, text="Ao" if team == "ao" else "Aka", font=("Arial", 28, 'bold'), bg=color, fg="white").pack(anchor="nw", padx=20, pady=5)
        tk.Label(frame, text=team_name, font=("Arial", 20), bg=color, fg="white").pack(anchor="nw", padx=20)

        style_var = tk.StringVar(value=kata_style)
        tk.OptionMenu(frame, style_var, kata_style, "Other").pack(anchor="nw", padx=20, pady=5)

        top_info = tk.Frame(frame, bg=color)
        top_info.pack(expand=True, fill="both", pady=10)

        score_frame = tk.Frame(top_info, bg=color)
        score_frame.pack(side="left", expand=True, fill="both", padx=20, anchor="n")

        score_top = tk.Frame(score_frame, bg=color)
        score_top.pack(pady=10, anchor="n")

        score_label = tk.Label(score_top, text="0", font=("Digital-7", 200), bg=color, fg="white")
        score_label.pack()

        btn_frame = tk.Frame(score_top, bg=color)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="+1", font=("Arial", 20), bg="green", fg="white", width=4,
                  command=lambda: self.change_score(team, 1)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="-1", font=("Arial", 20), bg="red", fg="white", width=4,
                  command=lambda: self.change_score(team, -1)).pack(side="left", padx=5)

        note_label = tk.Label(score_frame, text="", font=("Arial", 26, "bold"), bg=color, fg="yellow")
        note_label.pack(pady=(10, 0)) 

flag_frame = tk.Frame(top_info, bg=color)
        flag_frame.pack(side="left", expand=True, fill="both", padx=20)

        try:
            img_path = os.path.join("gambar", flag_filename)
            flag_img = Image.open(img_path).resize((250, 250))
            flag_photo = ImageTk.PhotoImage(flag_img)
            flag_label = tk.Label(flag_frame, image=flag_photo, bg=color)
            flag_label.image = flag_photo
        except:
            flag_label = tk.Label(flag_frame, text="Flag", font=("Arial", 18), bg=color, fg="white")
        flag_label.pack()

        timer_box = tk.Frame(flag_frame, bg="#2e2e2e", bd=3, relief="solid")
        timer_box.pack(pady=20)
        timer_label = tk.Label(timer_box, text="0.00", font=("Digital-7", 80), bg="#2e2e2e", fg="white")
        timer_label.pack(padx=20, pady=10)

        if team == "ao":
            self.ao_score_label = score_label
            self.ao_timer_label = timer_label
            self.ao_note_label = note_label
            self.ao_timer_box = timer_box
        else:
            self.aka_score_label = score_label
            self.aka_timer_label = timer_label
            self.aka_note_label = note_label
            self.aka_timer_box = timer_box

        control_frame = tk.Frame(frame, bg=color)
        control_frame.pack(side="bottom", pady=10)

        start_stop_btn = tk.Button(control_frame, text="Start", font=("Arial", 18), bg="green", fg="white", width=10)
        start_stop_btn.pack(side="left", padx=5)
        start_stop_btn.config(command=lambda btn=start_stop_btn: self.toggle_timer(team, btn))

        tk.Button(control_frame, text="Show/Hide Timer", font=("Arial", 14), bg="blue", fg="white", width=14,
                  command=lambda: self.toggle_timer_visibility(team)).pack(side="left", padx=5)
        tk.Button(control_frame, text="Shikkaku", font=("Arial", 18), bg="gray", fg="black", width=10,
                  command=lambda: self.shikkaku(team)).pack(side="left", padx=5)
        tk.Button(control_frame, text="Kikken", font=("Arial", 18), bg="gray", fg="black", width=10,
                  command=lambda: self.kikken(team)).pack(side="left", padx=5)
