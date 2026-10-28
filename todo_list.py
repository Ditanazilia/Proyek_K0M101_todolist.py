# 1. Variabel List kosong untuk menyimpan tugas
daftar_tugas = []

# 2. Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== APLIKASI PENCATAT TUGAS ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

# 3. Fungsi Tambah Tugas (Fika)
def tambah_tugas():
    print("\n--- TAMBAH TUGAS ---")
    tugas_baru = input("Masukkan nama tugas baru: ")
    daftar_tugas.append(tugas_baru) # Memasukkan data ke List
    print(f'[Berhasil!] Tugas "{tugas_baru}" telah ditambahkan.')

# 4. Fungsi Lihat Tugas (Fika)
def lihat_tugas():
    print("\n--- DAFTAR TUGAS ANDA ---")
    if len(daftar_tugas) == 0:
        print("(Belum ada tugas yang dicatat)")
    else:
        for i in range(len(daftar_tugas)):
            print(f"{i + 1}. {daftar_tugas[i]}")

# 5. Fungsi Hapus Tugas (Ismi)
def hapus_tugas():
    lihat_tugas() 
    if len(daftar_tugas) > 0:
        print("\n--- HAPUS TUGAS ---")
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(daftar_tugas):
                tugas_dihapus = daftar_tugas.pop(nomor - 1) # Menghapus dari List
                print(f'[Berhasil!] Tugas "{tugas_dihapus}" telah dihapus.')
            else:
                print("[Error] Nomor tugas tidak ditemukan.")
        except ValueError:
            print("[Error] Harap masukkan angka!")

# 6. PROGRAM UTAMA (Dita)
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        tambah_tugas()
    elif pilihan == '2':
        lihat_tugas()
    elif pilihan == '3':
        hapus_tugas()
    elif pilihan == '4':
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("\n[Error] Pilihan tidak valid. Silakan pilih 1-4.")