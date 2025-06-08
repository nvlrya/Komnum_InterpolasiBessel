import math

class InterpolationSolver:
    def __init__(self, data):
        self.data = data
        self.x_values = sorted(data.keys())
        self.h = self.x_values[1] - self.x_values[0]
        self.delta = self._calculate_delta()
    
    def _calculate_delta(self):
        n = len(self.x_values)
        delta = {}

        for i in range(n):
            delta[(i, 0)] = self.data[self.x_values[i]]
        
        for j in range(1, n):
            for i in range(n - j):
                delta[(i, j)] = delta[(i+1, j-1)] - delta[(i, j-1)]
        
        return delta
    
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
    
    def Bessel_Delta(self, x0):
        idx = self.x_values.index(x0)

        delta_f0 = self.delta.get((idx, 1), 0)

        delta2_f = self.delta.get((idx, 2), 0)
        delta2_f_minus1 = self.delta.get((idx-1, 2), 0)
        avg_delta2_f = (delta2_f_minus1 + delta2_f) / 2

        delta3_f_minus1 = self.delta.get((idx-1, 3), 0)

        delta4_f_minus2 = self.delta.get((idx-2, 4), 0)
        delta4_f_minus1 = self.delta.get((idx-1, 4), 0)
        avg_delta4_f = (delta4_f_minus2 + delta4_f_minus1) / 2
        
        return delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f

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

print("=== SOAL 3 - Bessel INTERPOLATION ===")
print("f(x):")
for x, y in data.items():
    print(f"f({x}) = {y}")
print()

solver = InterpolationSolver(data)

solver.Tabel_data()
print()

x = 11
x0 = 10
h = 2
f0 = 74020
f_actual = 154418

delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f = solver.Bessel_Delta(x0)

t1, t2, t3, t4, t5, result, error = bessel_terms(
    x, x0, h, f0, delta_f0, avg_delta2_f, delta3_f_minus1, avg_delta4_f, f_actual
)

print("=== HASIL INTERPOLASI BESSEL ===")
print(f"Term 1 (f0): {t1}")
print(f"Term 2 (s * Δf0): {t2}")
print(f"Term 3 (s(s-1)/2 * Δ²f0_avg): {t3}")
print(f"Term 4 (1/3 * s(s-1)/2 * (x - 1/2) * Δ³f-1): {t4}")
print(f"Term 5 (s(s-1)(s-2)(s-1/2)/24 * Δ⁴f0_avg): {t5}")
print(f"\nHasil interpolasi Bessel untuk f({x}) dengan x0={x0}: {int(result)}")
print(f"Nilai sebenarnya: {f_actual}")
print(f"ET: {error:.2f}%")

print("\n=== DETAIL PERHITUNGAN ===")
s = (x - x0) / h
print(f"s = (x - x0) / h = ({x} - {x0}) / {h} = {s}")
print(f"Δf₀ = {delta_f0}")
print(f"Δ²f = {avg_delta2_f}")
print(f"Δ³f₋₁ = {delta3_f_minus1}")
print(f"Δ⁴f = {avg_delta4_f}")
