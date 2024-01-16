import numpy as np
import cv2
file_path = "kipas.jpg"
def ambil_gambar_kalibrasi(file_path):
    # Baca gambar
    gambar = cv2.imread(file_path)

    # Check if the image is loaded successfully
    if gambar is None:
        print(f"Error: Unable to load image from {file_path}")
        return None, None

    # Print the shape of the image
    print("Shape of the image:", gambar.shape)

    # Konversi ke citra abu-abu
    citra_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    return gambar, citra_abu

# Rest of your code...
'''
# Mengambil gambar untuk kalibrasi
def ambil_gambar_kalibrasi(file_path):
    # Baca gambar
    gambar = cv2.imread(file_path)
    # Konversi ke citra abu-abu
    citra_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    return gambar, citra_abu
'''
# Menentukan kotak kalibrasi pada objek fisik (mis. papan catur)
def kotak_kalibrasi():
    # Masukkan ukuran kotak kalibrasi dalam grid (mis. 7x7)
    baris = 7
    kolom = 7
    ukuran_kotak = 25  # Ukuran kotak dalam milimeter
    kotak_koordinat = np.zeros((baris * kolom, 3), np.float32)
    kotak_koordinat[:, :2] = np.mgrid[0:baris, 0:kolom].T.reshape(-1, 2)
    kotak_koordinat[:, :2] *= ukuran_kotak
    return kotak_koordinat

# Kalibrasi kamera
def kalibrasi_kamera(gambar, citra_abu, kotak_koordinat):
    baris, kolom = citra_abu.shape[:2]
    ret, matriks_kalibrasi, distorsi_koefisien, sudut_rotasi, translasi_vektor = cv2.calibrateCamera([kotak_koordinat],
                                                                                                      [citra_abu.shape[::-1]],
                                                                                                      None, None)
    return matriks_kalibrasi, distorsi_koefisien

# Transformasi kollineasi
def transformasi_kollineasi(matriks_kalibrasi, distorsi_koefisien, sudut_rotasi, translasi_vektor):
    # Menghitung matriks ekstrinsik
    rotasi_vektor, _ = cv2.Rodrigues(sudut_rotasi)
    matriks_ekstrinsik = np.hstack((rotasi_vektor, translasi_vektor))
    
    # Menghitung matriks proyeksi kollineasi
    matriks_proyeksi = np.dot(matriks_kalibrasi, matriks_ekstrinsik)
    
    return matriks_ekstrinsik, matriks_proyeksi

# Contoh penggunaan
if __name__ == "__main__":
    # Ganti dengan lokasi gambar Anda
    file_path = 'lokasi_gambar_kalibrasi.jpg'
    
    gambar, citra_abu = ambil_gambar_kalibrasi(file_path)
    kotak_koordinat = kotak_kalibrasi()
    
    matriks_kalibrasi, distorsi_koefisien = kalibrasi_kamera(gambar, citra_abu, kotak_koordinat)
    matriks_ekstrinsik, matriks_proyeksi = transformasi_kollineasi(matriks_kalibrasi, distorsi_koefisien, sudut_rotasi, translasi_vektor)
    
    print("Matriks Kalibrasi:")
    print(matriks_kalibrasi)
    
    print("Distorsi Koefisien:")
    print(distorsi_koefisien)
    
    print("Matriks Ekstrinsik:")
    print(matriks_ekstrinsik)
    
    print("Matriks Proyeksi Kollineasi:")
    print(matriks_proyeksi)