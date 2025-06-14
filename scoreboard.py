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
        
btn_frame = tk.Frame(score_frame, bg=color)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="+1", font=("Arial", 16), bg="green", fg="white", width=4,
                  command=lambda: self.change_score(team, 1)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="-1", font=("Arial", 16), bg="red", fg="white", width=4,
                  command=lambda: self.change_score(team, -1)).pack(side="left", padx=5)

        flag_frame = tk.Frame(top_info, bg=color)
        flag_frame.pack(side="left", padx=20)
        try:
            img_path = os.path.join("gambar", flag_filename)
            flag_img = Image.open(img_path).resize((150, 150))
            flag_photo = ImageTk.PhotoImage(flag_img)
            flag_label = tk.Label(flag_frame, image=flag_photo, bg=color)
            flag_label.image = flag_photo
        except:
            flag_label = tk.Label(flag_frame, text="Flag", font=("Arial", 18), bg=color, fg="white")
        flag_label.pack()

        timer_label = tk.Label(flag_frame, text="0:00", font=("Digital-7", 50), bg=color, fg="white")
        timer_label.pack(pady=10)

        if team == "ao":
            self.ao_score_label = score_label
            self.ao_timer_label = timer_label
            self.ao_note_label = note_label
        else:
            self.aka_score_label = score_label
            self.aka_timer_label = timer_label
            self.aka_note_label = note_label


       control_frame = tk.Frame(frame, bg=color)
        control_frame.pack(side="bottom", pady=10)
        tk.Button(control_frame, text="Start", font=("Arial", 16), bg="green", fg="white", width=10,
                  command=lambda: self.start_timer(team)).pack(side="left", padx=5)
        tk.Button(control_frame, text="Stop", font=("Arial", 16), bg="orange", fg="white", width=10,
                  command=lambda: self.stop_timer(team)).pack(side="left", padx=5)
        tk.Button(control_frame, text="Shikkaku", font=("Arial", 16), bg="gray", fg="black", width=10,
                  command=lambda: self.shikkaku(team)).pack(side="left", padx=5)
        tk.Button(control_frame, text="Kikken", font=("Arial", 16), bg="gray", fg="black", width=10,
                  command=lambda: self.kikken(team)).pack(side="left", padx=5)

    def change_score(self, team, delta):
        if team == "ao":
            self.ao_score = max(0, self.ao_score + delta)
            self.ao_score_label.config(text=str(self.ao_score))
        else:
            self.aka_score = max(0, self.aka_score + delta)
            self.aka_score_label.config(text=str(self.aka_score))

    def start_timer(self, team):
        if team == "ao" and not self.running_ao:
            self.running_ao = True
            self.update_timer('ao')
        elif team == "aka" and not self.running_aka:
            self.running_aka = True
            self.update_timer('aka')

    def stop_timer(self, team):
        if team == "ao":
            self.running_ao = False
        else:
            self.running_aka = False

    def update_timer(self, team):
        if team == "ao" and self.running_ao:
            self.ao_timer += 1
            mins, secs = divmod(self.ao_timer, 60)
            self.ao_timer_label.config(text=f"{mins}:{secs:02}")
            self.root.after(1000, lambda: self.update_timer('ao'))
        elif team == "aka" and self.running_aka:
            self.aka_timer += 1
            mins, secs = divmod(self.aka_timer, 60)
            self.aka_timer_label.config(text=f"{mins}:{secs:02}")
            self.root.after(1000, lambda: self.update_timer('aka'))

    def reset_all(self):
        self.ao_score = 0
        self.aka_score = 0
        self.ao_timer = 0
        self.aka_timer = 0
        self.running_ao = False
        self.running_aka = False
        self.ao_score_label.config(text="0")
        self.aka_score_label.config(text="0")
        self.ao_timer_label.config(text="0:00")
        self.aka_timer_label.config(text="0:00")
        self.ao_note_label.config(text="")
        self.aka_note_label.config(text="")

    def shikkaku(self, team):
        self.stop_timer(team)
        if team == "ao":
            self.ao_note_label.config(text="DISQ")
        else:
            self.aka_note_label.config(text="DISQ")

    def kikken(self, team):
        self.stop_timer(team)
        if team == "ao":
            self.ao_note_label.config(text="FORF")
        else:
            self.aka_note_label.config(text="FORF")

if __name__ == "__main__":
    root = tk.Tk()
    app = KarateScoreboard(root)
    root.mainloop()
