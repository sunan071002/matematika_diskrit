# C. modul 1 mtk diskrit pertemuan 3

# Himpunan/Python Set
from itertools import product

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
U = set(range(1, 9))

print(B|A)
print("Union          :", A | B)
print("Intersection   :", A & B)
print("Difference     :", A - B)
print("Complement     :", U - A)
print("Cardinalty     :", len(A))
print("Subset         :", A <= U)
print("A x B          :", set(product(A, B)))

# Referensi Teknologi Mahasiswa
python = {"Ani", "Budi", "Citra"} 
java = {"Budi", "Deni"}
sql = {"Ani", "Deni", "Eka"}
javascript = {"Fajar"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar", "maemunah"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
menyukai_dua_teknologi = (python & java) | (python & sql) | (python & javascript) | (java & sql) | (java & javascript) | (sql & javascript)
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("Python saja:", python_saja)
print("Python dan Java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu)
print("Tidak menyukai ketiganya:", tidak_menyukai_ketiganya)
print(menyukai_dua_teknologi)