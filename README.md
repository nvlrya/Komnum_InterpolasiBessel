# Komnum_InterpolasiBessel C04


# Interpolasi Bessel dengan Python

Dokumen ini menjelaskan implementasi metode interpolasi Bessel menggunakan Python, terutama untuk menghitung nilai fungsi di sekitar titik tengah dua data yang diketahui. Metode ini cocok dipakai ketika data diskrit memiliki jarak yang sama dan kita ingin memperkirakan nilai antara dua titik.


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
Fungsi __init__() akan menerima data berisi pasangan x: f(x) lalu akan disimpan, diurutkan berdasarkan x, menghitung jarak antar titik, dan membentuk tabel delta(selisih).

#### b. Fungsi `_calculate_delta()`

```python
def _calculate_delta(self):
        n = len(self.x_values)
        delta = {}

        for i in range(n):
            delta[(i, 0)] = self.data[self.x_values[i]]
        
        for j in range(1, n):
            for i in range(n - j):
                delta[(i, j)] = delta[(i+1, j-1)] - delta[(i, j-1)]
        
        return delta
```

Membentuk tabel delta menggunakan rumus rekursif hingga Δ⁴.

#### c. Fungsi `Tabel_data()`

```python
def Tabel_data(self):
        n = len(self.x_values)
        print("Tabel data & delta:")
        print("i\tx\tf(x)\t\tΔf(x)\t\tΔ²f(x)\t\tΔ³f(x)\t\tΔ⁴f(x)")
        print("-" * 85)
        
        for i in range(n):
            row = f"{i}\t{self.x_values[i]}\t{self.delta[(i, 0)]}"
            for j in range(1, min(5, n-i)):
                if (i, j) in self.delta:
                    row += f"\t\t{self.delta[(i, j)]}"
                else:
                    row += "\t\t-"
            print(row)
```

Mencetak tabel berisi nilai x, f(x), Δf, Δ²f, Δ³f, dan Δ⁴f.

#### d. Fungsi `Bessel_Delta(x0)`

```python
def Bessel_Delta(self, x0):
        idx = self.x_values.index(x0)
        
        # Δf₀
        delta_f0 = self.delta.get((idx, 1), 0)
        
        # Δ²f
        delta2_f = self.delta.get((idx, 2), 0)
        delta2_f_minus1 = self.delta.get((idx-1, 2), 0)
        avg_delta2_f = (delta2_f_minus1 + delta2_f) / 2
        
        # Δ³f₋₁
        delta3_f_minus1 = self.delta.get((idx-1, 3), 0)
        
        # Δ⁴f
        delta4_f_minus2 = self.delta.get((idx-2, 4), 0)
        delta4_f_minus1 = self.delta.get((idx-1, 4), 0)
        avg_delta4_f = (delta4_f_minus2 + delta4_f_minus1) / 2
        
        return delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f
```

Mengambil nilai delta yang dibutuhkan untuk rumus Bessel, termasuk rata-rata Δ² dan Δ⁴.

---

### 3. Fungsi `bessel_terms()`

```python
def bessel_terms(x, x0, h, f0, delta_f0, delta2_f, delta3_f_minus1, delta4_f0, f_actual):
    s = (x - x0) / h
    
    term1 = f0
    term2 = s * delta_f0
    term3 = (s * (s - 1) / 2) * delta2_f
    term4 = (1/3) * ((s * (s - 1)) / 2) * (x - 0.5) * delta3_f_minus1
    term5 = (s * (s - 1) * (s - 2) * (s - 3) / 24) * delta4_f0  # 4! = 24
    
    f_interp = term1 + term2 + term3 + term4 + term5
    E_t = abs(f_actual - f_interp) / f_actual * 100
    
    return term1, term2, term3, term4, term5, f_interp, E_t
```

Menghitung nilai interpolasi Bessel dengan rumus:

- f(x) = f₀ + sΔf₀ + [(s(s-1))/2]Δ²f_avg + (1/3) * [(s(s - 1)/2)] *(x-0.5)Δ³f₋₁ + [s(s-1)(s-2)(s-3)/4!)Δ⁴f_avg
- Program sudah menghitung semua bagian rumus sehingga hanya perlu ditambahkan saja semua terms.

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
print(f"ET= {error:.4f}%")
```

---

## Output

- Tabel selisih (dari Δ hingga Δ⁴)
- Hasil pendekatan interpolasi f(x)
- Error true (ET)

![image](https://github.com/user-attachments/assets/c3aee582-471c-4db4-a3de-0d8fcc8bf571)


---


