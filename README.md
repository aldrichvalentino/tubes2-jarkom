# tubes2-jarkom
Tugas Besar Distance Vector Routing

## Petunjuk Penggunaan Program
### Windows
* Compile file main.cpp, lalu jalankan

### Linux
* Compile file cpp dengan mengetikkan "make all" di cmd
* Run program dengan mengetikkan "make run" di cmd, lalu mengetikkan testcasenya secara manual
* Atau run program dengan dengan mengetikkan "make test" di cmd untuk menjalankan program dengan testcase yang sudah ada di file txt

## Penjelasan
### Implementasi node
Node diimplementasi menggunakan struktur data list dengan dua parameter dan bertipe data integer, dua parameter ini berisikan nomer dari nodes. Nilai akan diinisialisasi terlebih dahulu sesuai dengan spesifikasi pada soal. Setelah node dibentuk, akan dihubungkan dengan dua parameter lainnya pada list yaitu source dan destination yang merupakan nomer dari nodes. Karena koneksi bisa dilakukan sebaliknya (dari 1 ke 2, dan 2 ke 1) maka node sebaliknya pun dihubungkan.

### Proses pengiriman pesan
Dari beberapa testcase skenario yang telah dibuat, nilai source dan destination akan disimpan. Lalu akan ada 3 jenis kasus yang akan ditangani yaitu
* Jika kedua nodes belum terhubung (Distance dari destination = -1, distance dari source <> -1) : Jarak destination akan bernilai -1 karena belum terhubung, lalu nilai distance akan di update dengan info jarak yang diketahui dari node source dan menambahkannya dengan 1
* Jika kedua nodes sudah terhubung tetapi destination dan source tidak bersebelahan (Distance dari destination > Distance dari Source + 1; distance dari source <> -1; nextHop dari destination <> source) : Mengupdate informasi pada destination dari informasi yang terdapat pada source
* Jika kedua nodes sudah terhubung, destination dan source bersebelahan (Distance destination = distance source + 1; distance dari destination <> -1; nextHop dari destination > source) : Mengupdate informasi pada destination  dengan mengambil informasi pada source


## Pembagian Tugas
* Ega Rifqi Saputra : Membuat Readme, debugging TLE
* Girvandi Ilyas	: Membuat struktur data, debugging TLE
* Aldrich V. Halim	: Membuat perhitungan update jarak, debugging TLE

## Pertanyaan
* Apakah perbedaan dari routing protocol distance-vector dan link state? Manakah yang lebih baik untuk digunakan?
* Jawaban : Distance-vector seperti namanya menggunakan dua nilai untuk memilih jalur terbaik, yaitu menggunakan jarak(distance) dan menggunakan arah(vector). Sedangkan link state akan melakukan tracking ke semua node dan status dari tiap node seperti jenis dan tipe koneksi, kecepatan dll akan disimpan menjadi sebuah informasi. Jika diliat dari kedua jenis routing protocol, terlihat bahwa link state memiliki data yang lebih lengkap tidak hanya jarak dan arah saja, walaupun akan lebih rumit, link state akan lebih baik karena memiliki informasi spesifik.
* Pada implementasinya saat ini manakah yang lebih banyak digunakan, distance-vector atau link state? Kenapa?
* Jawaban : Dalam persoalan ini, informasi yang perlu dicari dari tiap node hanya jarak dan statusnya saja, oleh karena itu akan lebih mudah jika menggunakan distance-vector, karena tidak akan rumit dan dengan distance-vector pun persoalan bisa terjawab.

## Anggota Kelompok
* Ega Rifqi Saputra			: 13515015
* Girvandi Ilyas			: 13515051
* Aldrich Valentino Halim	: 13515081