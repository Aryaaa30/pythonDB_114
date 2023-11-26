import tkinter as tk
from tkinter import messagebox
import sqlite3

def prediksi_fakultas(biologi, fisika, inggris, matematika, kimia, sejarah, bahasa_indonesia, bahasa_jawa, seni_budaya, pendidikan_jasmani):
    nilai_mapel = {
        'Biologi': biologi,
        'Fisika': fisika,
        'Inggris': inggris,
        'Matematika': matematika,
        'Kimia': kimia,
        'Sejarah': sejarah,
        'Bahasa Indonesia': bahasa_indonesia,
        'Bahasa Jawa': bahasa_jawa,
        'Seni Budaya': seni_budaya,
        'Pendidikan Jasmani': pendidikan_jasmani
    }

    max_mapel = max(nilai_mapel, key=nilai_mapel.get)

    if max_mapel == 'Biologi':
        return "Kedokteran"
    elif max_mapel == 'Fisika':
        return "Teknik"
    elif max_mapel == 'Inggris':
        return "Bahasa"
    elif max_mapel == 'Matematika':
        return "Matematika"
    elif max_mapel == 'Kimia':
        return "Farmasi"
    elif max_mapel == 'Sejarah':
        return "Ilmu Sejarah"
    elif max_mapel == 'Bahasa Indonesia':
        return "Sastra Indonesia"
    elif max_mapel == 'Bahasa Jawa':
        return "Sastra Jawa"
    elif max_mapel == 'Seni Budaya':
        return "Seni Rupa"
    elif max_mapel == 'Pendidikan Jasmani':
        return "Olahraga"

def simpan_ke_database(nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, bahasa_indonesia, bahasa_jawa, seni_budaya, pendidikan_jasmani, prediksi_fakultas):
    connection = sqlite3.connect("nilai_siswaa.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            matematika INTEGER,
            kimia INTEGER,
            sejarah INTEGER,
            bahasa_indonesia INTEGER,
            bahasa_jawa INTEGER,
            seni_budaya INTEGER,
            pendidikan_jasmani INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, bahasa_indonesia, bahasa_jawa, seni_budaya, pendidikan_jasmani, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, bahasa_indonesia, bahasa_jawa, seni_budaya, pendidikan_jasmani, prediksi_fakultas))

    connection.commit()
    connection.close()

def submit_nilai():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())
    nilai_matematika = int(entry_matematika.get())
    nilai_kimia = int(entry_kimia.get())
    nilai_sejarah = int(entry_sejarah.get())
    nilai_bahasa_indonesia = int(entry_bahasa_indonesia.get())
    nilai_bahasa_jawa = int(entry_bahasa_jawa.get())
    nilai_seni_budaya = int(entry_seni_budaya.get())
    nilai_pendidikan_jasmani = int(entry_pendidikan_jasmani.get())

    prediksi = prediksi_fakultas(
        nilai_biologi, nilai_fisika, nilai_inggris,
        nilai_matematika, nilai_kimia, nilai_sejarah,
        nilai_bahasa_indonesia, nilai_bahasa_jawa,
        nilai_seni_budaya, nilai_pendidikan_jasmani
    )

    label_prediksi.config(text="Prediksi Fakultas: {}".format(prediksi))

    simpan_ke_database(
        nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris,
        nilai_matematika, nilai_kimia, nilai_sejarah,
        nilai_bahasa_indonesia, nilai_bahasa_jawa,
        nilai_seni_budaya, nilai_pendidikan_jasmani,
        prediksi
    )

    messagebox.showinfo("Info", "Data berhasil disimpan. Prediksi Fakultas: {}".format(prediksi))

root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1)

label_matematika = tk.Label(root, text="Nilai Matematika:")
label_matematika.grid(row=4, column=0)
entry_matematika = tk.Entry(root)
entry_matematika.grid(row=4, column=1)

label_kimia = tk.Label(root, text="Nilai Kimia:")
label_kimia.grid(row=5, column=0)
entry_kimia = tk.Entry(root)
entry_kimia.grid(row=5, column=1)

label_sejarah = tk.Label(root, text="Nilai Sejarah:")
label_sejarah.grid(row=6, column=0)
entry_sejarah = tk.Entry(root)
entry_sejarah.grid(row=6, column=1)

label_bahasa_indonesia = tk.Label(root, text="Nilai Bahasa Indonesia:")
label_bahasa_indonesia.grid(row=7, column=0)
entry_bahasa_indonesia = tk.Entry(root)
entry_bahasa_indonesia.grid(row=7, column=1)

label_bahasa_jawa = tk.Label(root, text="Nilai Bahasa Jawa:")
label_bahasa_jawa.grid(row=8, column=0)
entry_bahasa_jawa = tk.Entry(root)
entry_bahasa_jawa.grid(row=8, column=1)

label_seni_budaya = tk.Label(root, text="Nilai Seni Budaya:")
label_seni_budaya.grid(row=9, column=0)
entry_seni_budaya = tk.Entry(root)
entry_seni_budaya.grid(row=9, column=1)

label_pendidikan_jasmani = tk.Label(root, text="Nilai Pendidikan Jasmani:")
label_pendidikan_jasmani.grid(row=10, column=0)
entry_pendidikan_jasmani = tk.Entry(root)
entry_pendidikan_jasmani.grid(row=10, column=1)

button_submit = tk.Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=11, column=0, columnspan=2)

label_prediksi = tk.Label(root, text="Prediksi Fakultas:")
label_prediksi.grid(row=12, column=0, columnspan=2)

root.mainloop()
