# Sistem perhitungan volume objek simetri pada citra menggunakan metode regresi linier

Project ini memiliki tiga tahap dan menggunakan telur dan beras sebagai objek pengamatan. Tahap pertama yaitu akuisisi data, pada tahap ini dilakukan pengambilan citra menggunakan kamera handphone Samsung A20S. Citra yang diambil nantinya akan digunakan untuk dijadikan data latih dan data uji. Data latih dan data uji masing-masing memiliki rasio 80% : 20%, data latih nantinya digunakan untuk melatih machine learning dan data uji digunakan untuk menguji akurasi dari machine learning. 

Tahap kedua yaitu ekstraksi ciri dari citra telur untuk mendapatkan informasi. Proses ekstraksi ciri dilakukan di notebook google colab dengan bahasa pemrograman python. Hasil dari proses ekstraksi ciri sendiri berupa jumlah pixel dengan nilai 255 (citra berwarna putih) yang merupakan objek telur. Sebelum diambil jumlah pixel, citra yang awalnya berwarna RGB (Red, Green, Blue) dikonversi menjadi citra grayscale (hitam dan putih) untuk memudahkan segmentasi berdasarkan bentuk objek. Proses segmentasi sendiri menggunakan algoritma thresholding yang akan membuat citra menjadi citra binner yang hanya memiliki dua nilai pixel, yaitu 0 untuk warna hitam (background) dan 255 untuk warna putih (objek). Setelah proses thresholding, dilakukan proses morfologi menggunakan algoritma open untuk menghilangkan noise dan dilanjut perhitungan jumlah pixel yang bernilai 255.

Tahap ketiga adalah dengan memprediksi volume dengan machine learning yang telah dilatih dan diuji dengan data latih dan data uji. Algoritma machine learning yang digunakan adalah multiple linear regression. Jumlah pixel yang didapat dari proses ekstraksi ciri dan jarak dari kamera ke objek diproses untuk didapat nilai volume.

Credit : 

1. https://medium.com/@adiptamartulandi
2. https://medium.com/@kaushikvarma.katari
