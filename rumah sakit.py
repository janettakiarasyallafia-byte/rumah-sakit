
print("========================================")
print("          RUMAH SAKIT SEHAT")
print("       SISTEM DATA PASIEN")
print("========================================")

nama = input("NAMA PASIEN : ")

print("\nDAFTAR PENYAKIT PASIEN")
penyakit_list = [
    ("Influenza", 100000, "Pemeriksaan dokter dan obat"),
    ("Demam Berdarah", 200000, "Pemeriksaan darah dan pemantauan dokter"),
    ("Tifus", 175000, "Pemeriksaan laboratorium dan obat"),
    ("Diabetes", 225000, "Pemeriksaan gula darah dan konsultasi dokter"),
    ("Hipertensi", 125000, "Pemeriksaan tekanan darah dan konsultasi dokter"),
    ("Tipes", 150000, "Pemeriksaan laboratorium dan obat"),
    ("Diare", 100000, "Pemeriksaan dokter dan cairan rehidrasi"),
    ("Pneumonia", 250000, "Pemeriksaan pernapasan dan pemantauan dokter"),
    ("Infeksi Saluran Kemih", 125000, "Pemeriksaan urine dan konsultasi dokter"),
    ("Radang Tenggorokan", 100000, "Pemeriksaan dokter dan obat")
]

for i, data in enumerate(penyakit_list, 1):
    print(i, ".", data[0])

pilihan = int(input("Pilih penyakit (1-10): "))
lama = int(input("Lama opname (hari): "))

print("\nDAFTAR KELAS RUANG RAWAT INAP")
ruang_list = [
    ("Kelas III", 100000, "Tempat tidur dan fasilitas dasar"),
    ("Kelas II", 150000, "Tempat tidur, lemari, dan kamar mandi bersama"),
    ("Kelas I", 200000, "Tempat tidur, lemari, TV, dan kamar mandi"),
    ("VIP", 350000, "Tempat tidur eksklusif, TV, AC, sofa, dan kamar mandi pribadi")
]

for i, data in enumerate(ruang_list, 1):
    print(i, ".", data[0], ": Rp", format(data[1], ",").replace(",", "."), "/hari")

ruang = int(input("Pilih kelas ruang inap (1-4): "))

if 1 <= pilihan <= 10 and 1 <= ruang <= 4 and lama >= 1:

    penyakit, harga, fasilitas = penyakit_list[pilihan - 1]
    jenis_ruang, biaya_ruang, fasilitas_kamar = ruang_list[ruang - 1]

    total_penyakit = harga * lama
    total_ruang = biaya_ruang * lama
    total = total_penyakit + total_ruang

    rupiah = lambda angka: format(angka, ",").replace(",", ".")

    print("\n========================================")
    print("             DATA PASIEN")
    print("========================================")
    print("Nama Pasien       :", nama)
    print("Jenis Penyakit    :", penyakit)
    print("Lama Opname       :", lama, "hari")
    print("Kelas Ruangan     :", jenis_ruang)
    print("Biaya Penyakit    : Rp", rupiah(total_penyakit))
    print("Biaya Ruangan     : Rp", rupiah(total_ruang))
    print("Total Biaya       : Rp", rupiah(total))

    print("\n========================================")
    print("         FASILITAS RUMAH SAKIT")
    print("========================================")
    print("Ruang Rawat Inap, " + fasilitas)
    print("Fasilitas Kamar   :", fasilitas_kamar)

    print("\n========================================")
    print("             MENU MAKANAN")
    print("========================================")

    if lama > 3:
        print("Pasien mendapatkan makanan khusus:")
        print("- Bubur atau nasi lunak\n- Sayuran\n- Buah-buahan\n- Susu sesuai kebutuhan pasien")
    else:
        print("Pasien mendapatkan makanan reguler:")
        print("- Nasi\n- Sayuran\n- Lauk pauk")

    print("\n========================================")
    print("           JADWAL KUNJUNGAN")
    print("========================================")

    if lama > 7:
        print("Kunjungan: Setiap hari")
        print("Waktu: 10.00 - 12.00 dan 16.00 - 18.00")
        print("Maksimal 2 pengunjung secara bergantian")
    elif lama > 3:
        print("Kunjungan: Setiap hari")
        print("Waktu: 16.00 - 18.00")
        print("Maksimal 2 pengunjung secara bergantian")
    else:
        print("Kunjungan: Sesuai jadwal rumah sakit")
        print("Waktu: 16.00 - 17.00")
        print("Maksimal 1 pengunjung")

    print("\n========================================")
    print("           STATUS PASIEN")
    print("========================================")

    if lama > 7:
        print("Status: Opname jangka panjang")
    elif lama > 3:
        print("Status: Opname menengah")
    else:
        print("Status: Opname singkat")

    print("\n========================================")
    print("          METODE PEMBAYARAN")
    print("========================================")
    print("1. BPJS Kesehatan")
    print("2. Pembayaran Mandiri")

    bayar = int(input("Pilih pembayaran (1-2): "))

    print("\n========================================")
    print("          RINCIAN PEMBAYARAN")
    print("========================================")

    if bayar == 1:
        print("Metode Pembayaran : BPJS Kesehatan")
        print("Total Biaya       : Rp", rupiah(total))
        print("Ditanggung BPJS   : Rp", rupiah(total))
        print("Total Dibayar     : Rp 0")
        print("Keterangan        : Simulasi biaya dijamin BPJS")
    elif bayar == 2:
        print("Metode Pembayaran : Mandiri")
        print("Total Biaya       : Rp", rupiah(total))
        print("Total Dibayar     : Rp", rupiah(total))
        print("Keterangan        : Pembayaran pribadi")
    else:
        print("Pilihan pembayaran tidak valid")

    print("\n========================================")
    print("       SEMOGA CEPAT SEMBUH!")
    print("          RUMAH SAKIT SEHAT")
    print("========================================")

else:
    print("\nData tidak valid!")
    print("Silakan periksa pilihan penyakit, kelas ruangan, dan lama opname.")