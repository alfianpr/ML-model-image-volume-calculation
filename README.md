# Sistem perhitungan volume objek simetri pada citra menggunakan metode regresi linier
Objek yang diamati dalam program ini adalah beras. Metode ini dipilih karena karakteristik data yang linier dan memiliki dua variabel bebas, yaitu jumlah pixel dari citra objek dan jarak antara objek ke kamera serta satu variabel terikat yaitu volume objek.

Model pertama dalam penelitian ini menggunakan 100 citra beras dan 80 citra telur yang memiliki variasi jumlah pixel dan jarak objek ke kamera. Datasheet citra obkel ini nantinya akan dibersihkan dari outlier-outliernya supaya menghasilkan model machine learning memiliki tingkat akurasi yang tinggi. Setelah dibersihkan, data dibagi menjadi data latih dan data uji dengan perbandingan 80% : 20%. Model machine learning ini menghasilkan nilai akurasi sebesar 91% untuk objek telur dan 96% untuk objek beras.

Setelah model pertama dibuat, model tersebut akan dilatih terus untuk menghasilkan tingkat akurasi yang tinggi dengan range jarak yang panjang.

Credit : 

1. https://medium.com/@adiptamartulandi
2. https://medium.com/@kaushikvarma.katari
