import csv
import tkinter as tk
from tkinter import messagebox, filedialog

class PesertaKarate:
    def __init__(self, id: str, nama: str):
        self.id = id
        self.nama = nama
        self.skor = 0

    def tambah_skor(self, nilai: int):
        self.skor += nilai

    def skor_tertinggi(self) -> int:
        return self.skor

    def rata_skor(self) -> float:
        return self.skor

class SistemScoringKarate:
    def __init__(self):
        self.peserta = {}

    def daftar_peserta(self, id: str, nama: str):
        id = id.strip().lower()
        if id not in self.peserta:
            self.peserta[id] = PesertaKarate(id, nama)
            return f"✓ Peserta {nama} (ID: {id}) terdaftar"
        else:
            return f"× ID {id} sudah ada"

    def tambah_skor(self, id: str, skor: int):
        id = id.strip().lower()
        if id in self.peserta:
            self.peserta[id].tambah_skor(skor)
            return f"✓ Skor {skor} ditambahkan untuk {self.peserta[id].nama}, total: {self.peserta[id].skor}"
        else:
            return f"× ID {id} tidak ditemukan"
            
    def import_csv(self, filepath):
        results = []
        try:
            with open(filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                for row in reader:
                    if len(row) >= 2:
                        id, nama = row[0].strip().lower(), row[1].strip()
                        result = self.daftar_peserta(id, nama)
                        results.append(result)
                        if len(row) > 4 and row[4]:
                            scores = row[4].split(',')
                            for score in scores:
                                try:
                                    score = int(score.strip())
                                    result = self.tambah_skor(id, score)
                                    results.append(result)
                                except ValueError:
                                    results.append(f"× Skor tidak valid untuk {nama}: {score}")
                    else:
                        results.append("× Baris tidak lengkap")
                        return results
        except Exception as e:
            return [f"× Gagal mengimpor CSV: {str(e)}"]

    def urutkan_skor_tertinggi(self):
        peserta_dengan_skor = [(peserta.skor, peserta) for peserta in self.peserta.values()]
        return sorted(peserta_dengan_skor, key=lambda x: x[0], reverse=True)

    def urutkan_id(self):
        return sorted(self.peserta.values(), key=lambda x: x.id)

    def ekspor_csv(self, filepath):
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Skor Total"])
            for peserta in self.peserta.values():
                writer.writerow([
                    peserta.id,
                    peserta.nama,
                    peserta.skor
                ]) 

class AplikasiKarate(tk.Tk):
    def _init_(self):
        super()._init_()
        self.sistem = SistemScoringKarate()
        self.title("Sistem Scoring Karate - GUI Fullscreen")
        self.state('zoomed')
        self.configure(bg="#2e003e")

        self.warna_utama = "#FF75DC"
        self.warna_bg_list = "#FFB3E6"

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="SISTEM SCORING KARATE", font=("Arial", 24, "bold"), bg="#2e003e", fg=self.warna_utama)
        header.pack(pady=20)

        btn_style = {"width": 30, "height": 2, "font": ("Arial", 14, "bold"), "bg": self.warna_utama, "fg": "white", "activebackground": "#cc61bf"}

        frame_main = tk.Frame(self, bg="#2e003e")
        frame_main.pack(fill=tk.BOTH, expand=True)

        frame_kiri = tk.Frame(frame_main, bg="#2e003e", width=self.winfo_screenwidth()//2)
        frame_kiri.pack(side=tk.LEFT, fill=tk.Y, padx=(20,10), pady=10)
        frame_kiri.pack_propagate(False)

        tk.Button(frame_kiri, text="1. Daftarkan Peserta", command=self.daftar_peserta_gui, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="2. Tambahkan Skor", command=self.tambah_skor_gui, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="3. Impor Data dari CSV", command=self.import_csv_gui, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="4. Ekspor Data ke CSV", command=self.ekspor_csv_gui, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="Urutkan Peserta Berdasarkan Skor", command=self.urutkan_skor, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="Urutkan Peserta Berdasarkan ID", command=self.urutkan_id, **btn_style).pack(pady=10)
        tk.Button(frame_kiri, text="Keluar Program", command=self.destroy, *{*btn_style, "bg": "#d3004e", "activebackground": "#9a0038"}).pack(pady=10)

        self.frame_kanan = tk.Frame(frame_main, bg="#ffb3e6", width=self.winfo_screenwidth()//2)
        self.frame_kanan.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10,20), pady=10)
        self.frame_kanan.pack_propagate(False)

        self.canvas = tk.Canvas(self.frame_kanan, bg="#ffb3e6", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.frame_kanan, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ffb3e6")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.update_list_peserta()

