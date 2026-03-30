import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Inisialisasi engine suara
engine = pyttsx3.init()

class QueueNode:
    def __init__(self, nomor, nama):
        self.nomor = nomor
        self.nama = nama
        self.next = None

class BankQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, nama):
        self.count += 1
        new_node = QueueNode(self.count, nama)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return self.count

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp

    def get_all(self):
        curr = self.front
        data = []
        while curr:
            data.append(f"{curr.nomor}. {curr.nama}")
            curr = curr.next
        return data

# --- GUI Setup ---
class App:
    def __init__(self, root):
        self.queue = BankQueue()
        self.root = root
        self.root.title("Simulasi Antrian Bank")
        self.root.geometry("400x500")

        tk.Label(root, text="Nama Nasabah:").pack(pady=5)
        self.entry_nama = tk.Entry(root)
        self.entry_nama.pack(pady=5)

        tk.Button(root, text="Ambil Antrian", command=self.tambah, bg="#8FAF9B").pack(pady=5)
        tk.Button(root, text="Panggil Antrian", command=self.panggil, bg="#C9A646").pack(pady=5)
        
        tk.Label(root, text="Daftar Antrian:").pack(pady=10)
        self.listbox = tk.Listbox(root, width=40, height=15)
        self.listbox.pack(pady=5)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.queue.get_all():
            self.listbox.insert(tk.END, item)

    def tambah(self):
        nama = self.entry_nama.get()
        if nama:
            no = self.queue.enqueue(nama)
            messagebox.showinfo("Sukses", f"Nomor Antrian: {no}\nNama: {nama}")
            self.entry_nama.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Input Kosong", "Masukkan nama nasabah!")

    def panggil(self):
        nasabah = self.queue.dequeue()
        if nasabah:
            teks = f"Nomor antrian {nasabah.nomor}, atas nama {nasabah.nama}, silahkan ke loket"
            self.refresh_list()
            messagebox.showinfo("Memanggil", teks)
            engine.say(teks)
            engine.runAndWait()
        else:
            messagebox.showwarning("Kosong", "Tidak ada antrian!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()