def ortalama_bul(n):
    # Eğer n negatif veya 0 ise hata mesajı yazdır
    if n <= 0:
        return "Geçerli bir pozitif sayı giriniz."

    # Çift sayıları bul ve topla
    toplam = 0
    adet = 0
    for i in range(2, n+1, 2):
        toplam += i
        adet += 1

    # Ortamı bul ve geri döndür
    if adet > 0:
        ortalama = toplam / adet
        return ortalama
    else:
        return "Çift sayı bulunamadı."

# Kullanıcıdan bir sayı al
try:
    N = int(input("Bir pozitif sayı giriniz: "))
    sonuc = ortalama_bul(N)
    print(f"1'den {N}'e kadar olan çift sayıların ortalaması: {sonuc}")
except ValueError:
    print("Geçerli bir sayı giriniz.")
