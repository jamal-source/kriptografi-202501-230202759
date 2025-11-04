# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama: Jamaludin
NIM: 230202759
Kelas: 5IKRB

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropi kunci adalah ukuran ketidakpastian atau kekuatan kunci dalam sistem kriptografi, dihitung sebagai logaritma basis 2 dari ukuran ruang kunci. Unicity distance adalah panjang minimum ciphertext yang diperlukan untuk menentukan kunci unik dengan probabilitas tinggi, dihitung berdasarkan entropi kunci, redundansi bahasa, dan ukuran alfabet. Brute force attack adalah metode mencoba semua kemungkinan kunci hingga menemukan yang benar, efektivitasnya tergantung pada ukuran ruang kunci dan kecepatan komputasi. Dalam kriptografi, entropi tinggi dan unicity distance panjang menunjukkan keamanan yang lebih baik terhadap serangan brute force.

---

## 3. Alat dan Bahan
- Python 3.11 atau lebih baru
- Visual Studio Code / editor lain
- Git dan akun GitHub
- Library tambahan: math (built-in Python)

---

## 4. Langkah Percobaan
1. Membuat folder praktikum/week4-entropy-unicity/src/ jika belum ada.
2. Membuat file entropy_unicity.py di folder src/.
3. Menyalin kode program dari panduan praktikum ke dalam file.
4. Menjalankan program dengan perintah `python entropy_unicity.py` di terminal.
5. Menyimpan output eksekusi ke file output.txt.
6. Mengambil screenshot hasil eksekusi dan menyimpannya di folder screenshots/.
7. Mengisi laporan.md dengan hasil percobaan.
8. Melakukan commit dengan pesan "week4-entropy-unicity".

---

## 5. Source Code
```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program menunjukkan perhitungan entropi, unicity distance, dan estimasi waktu brute force yang benar. Entropi Caesar Cipher adalah sekitar 4.7 bit, unicity distance sekitar 1.33, dan waktu brute force sangat singkat untuk Caesar tetapi astronomis untuk AES-128.

Hasil eksekusi program:

![Hasil Eksekusi](screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa arti dari nilai entropy dalam konteks kekuatan kunci?  
  Entropy mengukur ketidakpastian kunci, di mana nilai lebih tinggi menunjukkan ruang kunci yang lebih besar dan lebih sulit ditebak atau diserang brute force.

- Pertanyaan 2: Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?  
  Unicity distance menunjukkan panjang minimum ciphertext yang diperlukan untuk menentukan kunci unik, sehingga cipher dengan unicity distance panjang lebih aman karena memerlukan lebih banyak data untuk dipecahkan.

- Pertanyaan 3: Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?  
  Brute force tetap ancaman karena kemajuan teknologi komputasi seperti superkomputer atau quantum computing dapat mengurangi waktu yang diperlukan, terutama untuk algoritma dengan ruang kunci kecil.

---

## 8. Kesimpulan
Praktikum ini berhasil menghitung entropi kunci, unicity distance, dan estimasi brute force menggunakan Python. Hasil menunjukkan bahwa Caesar Cipher rentan terhadap brute force, sedangkan AES-128 sangat aman. Konsep ini penting untuk memahami evaluasi keamanan kriptografi.

---

## 9. Daftar Pustaka
- Stallings, W. *Cryptography and Network Security*.

---

## 10. Commit Log
```
commit [hash]
Author: Jamaludin <email>
Date: [Tanggal]

    week4-entropy-unicity: implementasi perhitungan entropi, unicity distance, dan brute force
