# main.py
# Program utama yang memanggil fungsi dari utils.py

import utils  # import modul

def main():
    data_mahasiswa = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))

    # Input mahasiswa
    for i in range(jumlah):
        print(f"\nData mahasiswa ke-{i+1}")
        mhs = utils.input_mahasiswa()
        
        # Hitung rata & status
        rata = utils.hitung_rata(mhs["nilai"])
        status = utils.tentukan_status(rata)

        # Simpan ke data
        mhs["rata"] = rata
        mhs["status"] = status
        data_mahasiswa.append(mhs)

    # Tampilkan hasil akhir
    utils.tampilkan_hasil(data_mahasiswa)

# Jalankan program
if __name__ == "__main__":
    main()
