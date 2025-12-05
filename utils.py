# utils.py
# Berisi fungsi-fungsi pendukung (modular)

def input_mahasiswa():
    """
    Mengambil input data mahasiswa:
    - nama
    - 3 nilai
    Mengembalikan dictionary mahasiswa.
    """
    nama = input("Nama mahasiswa : ")
    n1 = float(input("Nilai 1: "))
    n2 = float(input("Nilai 2: "))
    n3 = float(input("Nilai 3: "))
    return {
        "nama": nama,
        "nilai": [n1, n2, n3]
    }

def hitung_rata(nilai):
    """
    Menghitung rata-rata dari list nilai.
    """
    return sum(nilai) / len(nilai)

def tentukan_status(rata):
    """
    Menentukan status kelulusan.
    Lulus = rata-rata >= 60
    Tidak Lulus = rata-rata < 60
    """
    return "Lulus" if rata >= 60 else "Tidak Lulus"

def tampilkan_hasil(data):
    """
    Menampilkan seluruh data mahasiswa beserta rata-rata & status.
    Juga menampilkan mahasiswa nilai tertinggi & terendah.
    """
    print("\n=== DATA MAHASISWA ===")
    for m in data:
        print(f"Nama : {m['nama']}")
        print(f"Nilai: {m['nilai']}")
        print(f"Rata-rata: {m['rata']:.2f}")
        print(f"Status: {m['status']}")
        print("-" * 30)

    # Cari mahasiswa nilai tertinggi & terendah
    tertinggi = max(data, key=lambda x: x["rata"])
    terendah = min(data, key=lambda x: x["rata"])

    print("\n=== HASIL TAMBAHAN ===")
    print(f"Nilai Tertinggi : {tertinggi['nama']} ({tertinggi['rata']:.2f})")
    print(f"Nilai Terendah  : {terendah['nama']} ({terendah['rata']:.2f})")
