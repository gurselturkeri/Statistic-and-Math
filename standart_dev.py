import csv
import statistics

# verilerin olduğu csv dosyası ile
# python dosyası aynı klasörde olmali

dosya_adi = "iris.csv"
kolon = "sepal.length"
veriler = []

# csv dosyasında istediğimiz kolondaki degerleri
# verileri adlı listede sakladik
with open(dosya_adi, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        veriler.append(float(row[kolon]))

standart_sapma = statistics.stdev(veriler)
varyans = statistics.variance(veriler)
ortalama = statistics.mean(veriler)
degisim_araligi = max(veriler) - min(veriler)
degisim_katsayisi = standart_sapma / ortalama


print("Standard sapma:", standart_sapma)
print("Varyans:", varyans)
print("Degisim araligi:, ", degisim_araligi)
print("Degisim katsayisi: ", degisim_katsayisi)
