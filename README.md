# Komnum_InterpolasiBessel

---

## 📌 Interpolasi Bessel dengan Python

Interpolasi Bessel adalah salah satu metode numerik untuk memperkirakan nilai fungsi pada titik-titik tertentu berdasarkan data yang diketahui. Metode ini sangat berguna ketika data disusun secara merata dan titik interpolasi berada di tengah dua titik data.

---

## 🎯 Tujuan

- Memberikan pemahaman praktis tentang cara kerja Interpolasi Bessel.
- Memfasilitasi perhitungan nilai fungsi di titik tengah data dengan akurasi tinggi.
- Menyediakan alat bantu untuk menghitung nilai pendekatan dan galat relatif menggunakan Python.
- Menampilkan proses perhitungan secara bertahap, mulai dari tabel selisih hingga hasil akhir.

---

## 📊 Dataset

Data berupa pasangan nilai `x` dan `f(x)`, disimpan dalam bentuk dictionary:

```python
data = {
    2: -940,
    4: -6008,
    6: -11652,
    8: 1040,
    10: 74020,
    12: 279960,
    14: 729932,
    16: 1581088,
    18: 3044340
}
```

---

## 🧠 Struktur Program

### 🔹 `InterpolationSolver` (Class)
Kelas utama yang menangani:
- Penyimpanan dan pengurutan data.
- Pembuatan tabel selisih hingga ordo ke-4 (Δ).
- Penghitungan nilai-nilai yang dibutuhkan dalam rumus Bessel.

### 🔹 Fungsi `bessel_terms(...)`
Fungsi untuk:
- Menghitung setiap suku dalam rumus Interpolasi Bessel.
- Menjumlahkan semua suku untuk menghasilkan nilai pendekatan.
- Menghitung galat relatif (jika nilai aktual tersedia).

---

## 🧮 Rumus Bessel

Interpolasi Bessel menggunakan rumus berikut:

```
f(x) ≈ f₀ + sΔf₀ + [s(s−1)/2!] Δ²f_avg
     + [s(s−1)(s−½)/3!] Δ³f_{−1}
     + [s(s−1)(s−2)(s−3)/4!] Δ⁴f_avg
```

dengan:

- `s = (x - x₀) / h`  
- `h` = jarak antar titik data (diasumsikan konstan)  
- `Δ` = operator selisih hingga  

---

## 💡 Contoh Output Program

Output yang ditampilkan mencakup:
- Tabel data dengan selisih Δ hingga ordo ke-4.
- Nilai `s` dan suku-suku interpolasi.
- Nilai hasil pendekatan.
- Galat relatif terhadap nilai aktual (jika diberikan).

---

## 🛠️ Ketergantungan

Program ini hanya menggunakan pustaka Python standar:

```python
import math
```

---
