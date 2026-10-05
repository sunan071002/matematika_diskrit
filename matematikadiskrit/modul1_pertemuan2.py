# B. modul 1 mtk diskrit pertemuan 2

# Generator Tabel Kebenaran
nilai = [True, False]

print("P     Q        P and Q  P or Q   not P")
for p in nilai:
 for q in nilai:
  print(f"{p!s:<5} {q!s:<8} {p and q!s:<8} {p or q!s:<8} {not p!s}")

# Seleksi Praktikum 
def memenuhi_syarat(formulir, nilai, kehadiran, sanksi):
 return formulir and nilai >= 60 and kehadiran >= 75 and not sanksi

data = (True, 72, 80, False)
print("Dapat mengikuti praktikum:", memenuhi_syarat(*data))