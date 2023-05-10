sıcaklık = int(input("Hava sıcaklığını giriniz: ")) #kullanıcıdan aldığımız değer sıcaklık değişkenine atandı

#sıcaklık değişkenini karşılaştırma bölümü

if sıcaklık > 30 :                    
    print("Sıcak bir gün")
    print("Bol bol su içmelisin")
elif sıcaklık > 20:
    print("İyi bir gün :)")
elif sıcaklık > 10:
    print("Birazcık soğuk olabilir")
else:
    print("Soğuk bir gün")
    
input("Çıkmak için ENTER'a basınız")  #bu kodun amacı komut sisteminde komutların tamamlandığı sırada sistemin kendini aniden kapatmamasını sağlar