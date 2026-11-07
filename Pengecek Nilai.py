def cek_nilai(nama, nilai):
    if nilai < 0 or nilai > 100:
        return "Nilai tidak valid"
    elif nilai >= 85:
        grade = "A"
        status = "Sangat Baik"
    elif nilai >= 75:
        grade = "B"
        status = "Baik"
    elif nilai >= 65:
        grade = "C"
        status = "Cukup"
    elif nilai >= 50:
        grade = "D"
        status = "Kurang"
    elif nilai >= 0:
        grade = "E"
        status = "Tidak Lulus"

    return f"""
Nama: {nama}
Nilai: {nilai}
Grade: {grade}
Status: {status}
"""


print("=== SISTEM PENILAIAN MAHASISWA ===")
nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai "))

hasil = cek_nilai(nama, nilai)

print(hasil)