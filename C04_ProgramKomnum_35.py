def bessel_terms_corrected(x, x0, h, f0, delta_f0, delta2_f0, delta3_f_minus1, delta4_f0, f_actual):
    s = (x - x0) / h
    
    term1 = f0
    term2 = s * delta_f0
    term3 = (s * (s - 1) / 2) * delta2_f0
    term4 = (1/3) * ((s * (s - 1)) / 2) * (x - 0.5) * delta3_f_minus1
    term5 = (s * (s - 1) * (s - 2) * (s - 3) / 24) * delta4_f0  # 4! = 24
    
    f_interp = term1 + term2 + term3 + term4 + term5
    E_t = abs(f_actual - f_interp) / f_actual * 100
    
    return term1, term2, term3, term4, term5, f_interp, E_t


# Data input
x = 11
x0 = 10
h = 2
f0 = 74020
delta_f0 = 205940
delta2_f0 = 188496
delta3_f_minus1 = 111072
delta4_f0 = 42240

f_actual = 154418

t1, t2, t3, t4, t5, result, error = bessel_terms_corrected(x, x0, h, f0, delta_f0, delta2_f0, delta3_f_minus1, delta4_f0, f_actual)

print(f"Term 1 (f0): {t1}")
print(f"Term 2 (s * Δf0): {t2}")
print(f"Term 3 (s(s-1)/2 * Δ²f0): {t3}")
print(f"Term 4 (1/3 * s(s-1)/2 * (x - 1/2) * Δ³f-1): {t4}")
print(f"Term 5 (s(s-1)(s-2)(s-3)/24 * Δ⁴f0): {t5}")
print(f"\nHasil interpolasi Bessel untuk f({x}) dengan x0={x0}: {int(result)}")
print(f"Nilai sebenarnya: {f_actual}")
print(f"Galat ET: {error:.2f}%")
