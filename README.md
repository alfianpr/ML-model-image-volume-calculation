# Sistem perhitungan volume objek simetri pada citra menggunakan metode regresi linier
Objek yang diamati dalam program ini adalah telur dan beras. Metode ini dipilih karena karakteristik data yang linier dan memiliki dua variabel bebas, yaitu jumlah pixel dari citra objek dan jarak antara objek ke kamera serta satu variabel terikat yaitu volume objek.

Penelitian ini menggunakan 100 citra telur dan 100 citra beras yang memiliki variasi jumlah pixel dan jarak objek ke kamera. Dataset 100 telur dan beras ini nantinya akan dibersihkan dari outlier-outliernya supaya menghasilkan model machine learning yang presisi. Setelah dibersihkan, data dibagi menjadi data latih dan data uji dengan perbandingan 80% : 20%. Model machine learning ini menghasilkan nilai akurasi sebesar 91% untuk telur dan beras.

Credit : 

1. https://medium.com/@adiptamartulandi
2. https://medium.com/@kaushikvarma.katari
