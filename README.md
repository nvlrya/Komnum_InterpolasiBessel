
# Interpolasi Bessel dengan Python

Dokumen ini menjelaskan implementasi metode interpolasi Bessel menggunakan Python, terutama untuk menghitung nilai fungsi di sekitar titik tengah dua data yang diketahui. Metode ini cocok dipakai ketika data diskrit memiliki jarak yang sama dan kita ingin memperkirakan nilai antara dua titik.

---

## Tujuan Program

- Menghitung nilai pendekatan f(x) berdasarkan tabel data diskrit menggunakan metode Bessel.
- Menyusun tabel selisih (Δ) hingga derajat ke-4.
- Menghitung nilai interpolasi dan galat relatif terhadap nilai aktual (jika diketahui).

---

## Struktur Program

### 1. Import Library

```python
import math
```

Modul `math` disiapkan jika nantinya dibutuhkan fungsi matematika seperti akar atau faktorial.

---

### 2. Kelas `InterpolationSolver`

Kelas ini menangani pembentukan tabel selisih dan menyediakan komponen-komponen delta yang dibutuhkan untuk rumus Bessel.

#### a. Konstruktor

```python
class InterpolationSolver:
    def __init__(self, data):
        self.data = data
        self.x_values = sorted(data.keys())
        self.h = self.x_values[1] - self.x_values[0]
        self.delta = self._calculate_delta()
```

#### b. Fungsi `_calculate_delta()`

```python
def _calculate_delta(self):
    ...
```

Membentuk tabel delta menggunakan rumus rekursif hingga Δ⁴.

#### c. Fungsi `Tabel_data()`

```python
def Tabel_data(self):
    ...
```

Mencetak tabel berisi nilai x, f(x), Δf, Δ²f, Δ³f, dan Δ⁴f.

#### d. Fungsi `Bessel_Delta(x0)`

```python
def Bessel_Delta(self, x0):
    ...
```

Mengambil nilai delta yang dibutuhkan untuk rumus Bessel, termasuk rata-rata Δ² dan Δ⁴.

---

### 3. Fungsi `bessel_terms()`

```python
def bessel_terms(x, x0, h, f0, delta_f0, delta2_f, delta3_f_minus1, delta4_f0, f_actual):
    ...
```

Menghitung nilai interpolasi Bessel dengan rumus:

- f(x) = f₀ + sΔf₀ + [(s(s-1))/2]Δ²f_avg + ...
- Termasuk galat relatif jika nilai sebenarnya (`f_actual`) diketahui.

---

## Contoh Penggunaan Program

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

solver = InterpolationSolver(data)
solver.Tabel_data()

x = 11
x0 = 10
h = 2
f0 = 74020
f_actual = 154418

delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f = solver.Bessel_Delta(x0)

t1, t2, t3, t4, t5, result, error = bessel_terms(
    x, x0, h, f0, delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f, f_actual
)

print(f"Interpolasi f({x}) = {result}")
print(f"Galat relatif = {error:.4f}%")
```

---

## Output

- Tabel selisih (dari Δ hingga Δ⁴)
- Hasil pendekatan interpolasi f(x)
- Galat relatif dibandingkan dengan nilai aktual

---



