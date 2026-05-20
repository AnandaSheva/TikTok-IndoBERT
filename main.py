# ==========================================
# CONTOH KODE PYTHON: ALGORITMA MANUAL
# ==========================================

# ==========================================
# 1. PENCARIAN BILANGAN (LINEAR SEARCH)
# ==========================================
print("=" * 50)
print("1. LINEAR SEARCH - Mencari elemen dalam list")
print("=" * 50)

def linear_search(list_angka, target):
    """
    Mencari target dalam list dengan cara pergi satu per satu
    Logika: Loop dari awal, bandingkan setiap elemen, jika ketemu return index
    """
    for i in range(len(list_angka)):
        if list_angka[i] == target:
            return i  # Ketemu! Return posisinya
    return -1  # Tidak ketemu

angka = [10, 25, 30, 45, 50, 65, 80]
cari = 45
hasil = linear_search(angka, cari)
print(f"Mencari {cari} dalam {angka}")
if hasil != -1:
    print(f"✓ Ketemu! Posisi index: {hasil}")
else:
    print(f"✗ Tidak ketemu")


# ==========================================
# 2. PENGURUTAN BILANGAN (BUBBLE SORT)
# ==========================================
print("\n" + "=" * 50)
print("2. BUBBLE SORT - Mengurutkan dari kecil ke besar")
print("=" * 50)

def bubble_sort(list_angka):
    """
    Bubble Sort: Membandingkan pasangan elemen bersebelahan
    Logika: Jika elemen kiri > kanan, tukar posisi. Ulangi sampai urut.
    """
    n = len(list_angka)
    
    # Loop untuk setiap 'pass'
    for i in range(n):
        sudah_berubah = False
        
        # Loop untuk membandingkan pasangan elemen
        for j in range(0, n - i - 1):
            if list_angka[j] > list_angka[j + 1]:
                # Tukar posisi
                temp = list_angka[j]
                list_angka[j] = list_angka[j + 1]
                list_angka[j + 1] = temp
                sudah_berubah = True
        
        # Jika tidak ada perubahan, list sudah urut
        if not sudah_berubah:
            break
    
    return list_angka

angka_acak = [64, 34, 25, 12, 22, 11, 90]
print(f"Sebelum: {angka_acak}")
angka_urut = bubble_sort(angka_acak.copy())
print(f"Sesudah: {angka_urut}")


# ==========================================
# 3. PENCARIAN BINER (BINARY SEARCH)
# ==========================================
print("\n" + "=" * 50)
print("3. BINARY SEARCH - Pencarian cepat (list harus urut)")
print("=" * 50)

def binary_search(list_angka, target):
    """
    Binary Search: Membagi list menjadi 2 bagian terus-menerus
    Logika: Cek tengah, jika target > tengah, cari kanan, jika target < tengah, cari kiri
    """
    kiri = 0
    kanan = len(list_angka) - 1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2  # Cari posisi tengah
        nilai_tengah = list_angka[tengah]
        
        if nilai_tengah == target:
            return tengah  # Ketemu!
        elif nilai_tengah < target:
            kiri = tengah + 1  # Target di sebelah kanan
        else:
            kanan = tengah - 1  # Target di sebelah kiri
    
    return -1  # Tidak ketemu

angka_urut = [10, 20, 30, 40, 50, 60, 70, 80, 90]
cari = 60
hasil = binary_search(angka_urut, cari)
print(f"Mencari {cari} dalam {angka_urut}")
if hasil != -1:
    print(f"✓ Ketemu! Posisi index: {hasil}")
else:
    print(f"✗ Tidak ketemu")


# ==========================================
# 4. HITUNG JUMLAH DAN RATA-RATA
# ==========================================
print("\n" + "=" * 50)
print("4. HITUNG JUMLAH DAN RATA-RATA")
print("=" * 50)

def hitung_jumlah(list_angka):
    """
    Logika: Mulai dari 0, terus tambahkan setiap elemen
    """
    jumlah = 0
    for angka in list_angka:
        jumlah = jumlah + angka
    return jumlah

def hitung_rata_rata(list_angka):
    """
    Logika: Jumlah semua elemen dibagi banyak elemen
    """
    jumlah = hitung_jumlah(list_angka)
    banyak = len(list_angka)
    return jumlah / banyak

angka = [10, 20, 30, 40, 50]
print(f"Daftar angka: {angka}")
print(f"Jumlah: {hitung_jumlah(angka)}")
print(f"Rata-rata: {hitung_rata_rata(angka)}")


# ==========================================
# 5. CARI NILAI MAX DAN MIN
# ==========================================
print("\n" + "=" * 50)
print("5. CARI NILAI TERBESAR DAN TERKECIL")
print("=" * 50)

def cari_max(list_angka):
    """
    Logika: Anggap elemen pertama sebagai max, 
    bandingkan dengan elemen lain, jika lebih besar ganti max
    """
    if len(list_angka) == 0:
        return None
    
    max_nilai = list_angka[0]
    for angka in list_angka:
        if angka > max_nilai:
            max_nilai = angka
    return max_nilai

def cari_min(list_angka):
    """
    Logika: Anggap elemen pertama sebagai min,
    bandingkan dengan elemen lain, jika lebih kecil ganti min
    """
    if len(list_angka) == 0:
        return None
    
    min_nilai = list_angka[0]
    for angka in list_angka:
        if angka < min_nilai:
            min_nilai = angka
    return min_nilai

angka = [45, 23, 67, 12, 89, 34, 56]
print(f"Daftar angka: {angka}")
print(f"Nilai terbesar: {cari_max(angka)}")
print(f"Nilai terkecil: {cari_min(angka)}")


# ==========================================
# 6. HITUNG FAKTORIAL
# ==========================================
print("\n" + "=" * 50)
print("6. HITUNG FAKTORIAL")
print("=" * 50)

def faktorial(n):
    """
    Logika: 5! = 5 × 4 × 3 × 2 × 1
    Gunakan loop untuk perkalian berulang
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil = hasil * i
    return hasil

angka = 5
print(f"{angka}! = {faktorial(angka)}")
angka = 6
print(f"{angka}! = {faktorial(angka)}")


# ==========================================
# 7. CEK BILANGAN PRIMA
# ==========================================
print("\n" + "=" * 50)
print("7. CEK BILANGAN PRIMA")
print("=" * 50)

def cek_prima(n):
    """
    Logika: Bilangan prima hanya bisa dibagi 1 dan dirinya sendiri
    Periksa sisa bagi dari 2 hingga n-1. Jika ada yang habis dibagi, bukan prima
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:  # Jika habis dibagi
            return False
    return True

print("Bilangan 1-20 yang prima:")
bilangan_prima = []
for num in range(1, 21):
    if cek_prima(num):
        bilangan_prima.append(num)
print(bilangan_prima)


# ==========================================
# 8. BALIK URUTAN (REVERSE STRING/LIST)
# ==========================================
print("\n" + "=" * 50)
print("8. BALIK URUTAN")
print("=" * 50)

def balik_string(s):
    """
    Logika: Loop dari akhir ke awal, tambahkan ke hasil
    """
    hasil = ""
    for i in range(len(s) - 1, -1, -1):
        hasil = hasil + s[i]
    return hasil

def balik_list(list_data):
    """
    Logika: Loop dari akhir ke awal
    """
    hasil = []
    for i in range(len(list_data) - 1, -1, -1):
        hasil.append(list_data[i])
    return hasil

kata = "PYTHON"
print(f"Kata: {kata}")
print(f"Dibalik: {balik_string(kata)}")

angka = [1, 2, 3, 4, 5]
print(f"\nList: {angka}")
print(f"Dibalik: {balik_list(angka)}")


# ==========================================
# 9. HITUNG FIBONACCI
# ==========================================
print("\n" + "=" * 50)
print("9. DERET FIBONACCI")
print("=" * 50)

def fibonacci(n):
    """
    Logika: Deret Fibo = setiap angka adalah penjumlahan 2 angka sebelumnya
    0, 1, 1, 2, 3, 5, 8, 13, 21...
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    deret = [0, 1]
    for i in range(2, n):
        angka_baru = deret[i - 1] + deret[i - 2]
        deret.append(angka_baru)
    return deret

print(f"10 angka Fibonacci pertama: {fibonacci(10)}")


# ==========================================
# 10. MENGHITUNG PANGKAT
# ==========================================
print("\n" + "=" * 50)
print("10. MENGHITUNG PANGKAT (2^5)")
print("=" * 50)

def hitung_pangkat(basis, pangkat):
    """
    Logika: 2^5 = 2 × 2 × 2 × 2 × 2
    Kalikan basis dengan dirinya sendiri sebanyak pangkat kali
    """
    hasil = 1
    for i in range(pangkat):
        hasil = hasil * basis
    return hasil

print(f"2 pangkat 5 = {hitung_pangkat(2, 5)}")
print(f"3 pangkat 4 = {hitung_pangkat(3, 4)}")
print(f"10 pangkat 3 = {hitung_pangkat(10, 3)}")


# ==========================================
# 11. HITUNG DIGIT TERBESAR
# ==========================================
print("\n" + "=" * 50)
print("11. CARI DIGIT TERBESAR DALAM ANGKA")
print("=" * 50)

def digit_terbesar(n):
    """
    Logika: Ambil sisa bagi dengan 10 untuk dapat digit paling kanan
    Terus bagi angka dengan 10 sampai habis
    """
    n = abs(n)  # Pastikan positif
    digit_max = 0
    
    while n > 0:
        digit = n % 10  # Ambil digit paling kanan
        if digit > digit_max:
            digit_max = digit
        n = n // 10  # Hapus digit paling kanan
    
    return digit_max

angka = 4739
print(f"Angka: {angka}")
print(f"Digit terbesar: {digit_terbesar(angka)}")


# ==========================================
# 12. HITUNG JUMLAH DIGIT
# ==========================================
print("\n" + "=" * 50)
print("12. HITUNG JUMLAH DIGIT")
print("=" * 50)

def jumlah_digit(n):
    """
    Logika: Ambil sisa bagi dengan 10, tambahkan ke total
    Ulangi sampai angka habis
    """
    n = abs(n)
    total = 0
    
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    return total

angka = 12345
print(f"Angka: {angka}")
print(f"Jumlah semua digit: {jumlah_digit(angka)}")


# ==========================================
# 13. CEK PALINDROME
# ==========================================
print("\n" + "=" * 50)
print("13. CEK PALINDROME (Baca sama dari depan & belakang)")
print("=" * 50)

def cek_palindrome(s):
    """
    Logika: Bandingkan karakter dari depan dan belakang secara bersamaan
    Jika semua cocok, maka palindrome
    """
    s = s.lower()  # Ubah ke huruf kecil
    kiri = 0
    kanan = len(s) - 1
    
    while kiri < kanan:
        if s[kiri] != s[kanan]:
            return False
        kiri = kiri + 1
        kanan = kanan - 1
    
    return True

kata_list = ["radar", "hello", "madam", "racecar"]
for kata in kata_list:
    print(f"'{kata}' palindrome? {cek_palindrome(kata)}")


# ==========================================
# 14. HITUNG GCD (FAKTOR PERSEKUTUAN TERBESAR)
# ==========================================
print("\n" + "=" * 50)
print("14. GCD - FAKTOR PERSEKUTUAN TERBESAR")
print("=" * 50)

def gcd(a, b):
    """
    Logika (Euclidean Algorithm):
    GCD(a,b) = GCD(b, a mod b)
    Ulangi sampai b = 0
    """
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 75) = {gcd(100, 75)}")


# ==========================================
# 15. HITUNG SELISIH ANTARA 2 WAKTU
# ==========================================
print("\n" + "=" * 50)
print("15. HITUNG SELISIH WAKTU (Jam:Menit:Detik)")
print("=" * 50)

def hitung_selisih_waktu(jam1, menit1, detik1, jam2, menit2, detik2):
    """
    Logika: Konversi semua ke detik, hitung selisih, konversi balik
    """
    # Konversi ke detik
    total_detik1 = (jam1 * 3600) + (menit1 * 60) + detik1
    total_detik2 = (jam2 * 3600) + (menit2 * 60) + detik2
    
    selisih = abs(total_detik2 - total_detik1)
    
    # Konversi balik
    jam_hasil = selisih // 3600
    selisih = selisih % 3600
    menit_hasil = selisih // 60
    detik_hasil = selisih % 60
    
    return jam_hasil, menit_hasil, detik_hasil

jam, menit, detik = hitung_selisih_waktu(10, 30, 45, 14, 15, 20)
print(f"Selisih waktu: {jam} jam {menit} menit {detik} detik")

print("\n" + "=" * 50)
print("✓ SELESAI - SEMUA CONTOH ALGORITMA MANUAL")
print("=" * 50)