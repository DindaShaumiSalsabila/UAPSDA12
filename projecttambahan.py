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

