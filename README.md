NAMA: Delvi nur ropiq sitepu
NPM: G1A022005
KELAS: INFROMATIKA (A)
<<<<<<<<(PERBEDAAN ANTARA OOP DAN FP)>>>>>>>
   Functional programming (FP) dan Object-Oriented Programming (OOP) adalah dua paradigma pemrograman yang berbeda dalam hal pendekatan dan gaya pemrograman. Berikut adalah perbedaan antara FP dan OOP dalam bahasa pemrograman Python:
  1.	Pendekatan Pemrograman FP adalah pendekatan pemrograman di mana Anda menulis fungsi-fungsi terpisah dan menyusunnya untuk mencapai tujuan tertentu. Sedangkan pada OOP, Anda membuat objek yang memiliki properti dan metode yang saling berinteraksi satu sama lain untuk mencapai tujuan tertentu.
  2.	Immutability FP mengutamakan nilai-nilai yang tidak berubah (immutable) dan menggunakan fungsi-fungsi murni (pure functions) untuk menghasilkan nilai-nilai baru dari nilai-nilai yang ada. Sedangkan pada OOP, Anda dapat mengubah properti dari objek yang dibuat.
  3.	Inheritance dan Polymorphism OOP memiliki konsep inheritance dan polymorphism yang memungkinkan Anda untuk membuat kelas baru yang mewarisi sifat-sifat dari kelas induk dan memiliki metode yang berbeda-beda dengan cara yang sama. Sedangkan pada FP, konsep inheritance dan polymorphism tidak diterapkan.
  4.	Penggunaan variabel Pada FP, variabel hanya dapat diisi satu kali dan tidak dapat diubah setelahnya. Sedangkan pada OOP, Anda dapat mengubah nilai variabel dalam objek.
  5.	Asynchronous programming FP dapat menggunakan fitur asynchronous programming menggunakan konsep Future dan Promise. Sedangkan pada OOP, asynchronous programming juga dapat dilakukan namun perlu diimplementasikan menggunakan library atau framework tertentu.
  6.	Fokus FP lebih fokus pada apa yang harus dilakukan (what to do), sedangkan OOP lebih fokus pada bagaimana melakukannya (how to do it).
  Kesimpulannya, FP dan OOP adalah paradigma pemrograman yang berbeda dan memiliki keunggulan dan kelemahan masing-masing. Pemilihan paradigma yang tepat akan tergantung pada kebutuhan aplikasi dan preferensi programmer.
 
 ( PENJELASAN CODE PROGRAM  FP dan OOP  )
   Kode pertama adalah contoh program dalam gaya pemrograman fungsional (FP), yang menggunakan fungsi-fungsi tingkat tinggi seperti filter dan reduce untuk memanipulasi data. Sedangkan, kode kedua adalah contoh program dalam gaya pemrograman berorientasi objek (OOP), yang menggunakan kelas dan objek untuk mengorganisasi data dan perilaku.
   Perbedaan mendasar antara gaya pemrograman FP dan OOP adalah pendekatan yang digunakan untuk memecahkan masalah. Pada gaya pemrograman FP, fokus utama adalah pada fungsi yang memetakan masukan ke keluaran, tanpa perlu mempertimbangkan keadaan yang disimpan di variabel. Sementara pada gaya pemrograman OOP, fokus utama adalah pada objek yang memiliki sifat (atribut) dan perilaku (metode), dan berinteraksi dengan objek lainnya untuk memecahkan masalah.
Dalam kode pertama, fungsi filter dan reduce digunakan untuk memanipulasi data dalam list dan menghasilkan hasil akhir dengan cara yang deklaratif dan singkat. Sedangkan pada kode kedua, kelas Person digunakan untuk mengorganisasi data tentang seseorang dan metode say_hello digunakan untuk menampilkan informasi tentang orang tersebut.
Kedua pendekatan tersebut memiliki kelebihan dan kekurangan masing-masing, tergantung pada jenis masalah yang dihadapi dan preferensi pribadi pengembang perangkat lunak.

   { 2. berikan apa saja contoh pengimplementasian dari oop }
Jawaban:
   OOP atau Object-Oriented Programming adalah paradigma pemrograman yang sangat umum digunakan dalam pengembangan perangkat lunak modern. Berikut adalah beberapa contoh pengimplementasian dari OOP dalam kehidupan sehari-hari:
 >>> 1.	Pengembangan Game: OOP sangat umum digunakan dalam pengembangan game, di mana setiap karakter atau objek dalam game diwakili sebagai objek dalam program. Misalnya, karakter pemain, musuh, senjata, dan item lainnya semuanya diwakili sebagai objek dalam game. contoh program oop terdapat di atas
(Penjelasan program:)
	Program ini memiliki dua kelas yaitu Character dan Enemy. Kelas Enemy merupakan subclass dari Character. Setiap karakter dalam game memiliki atribut name, health, dan attack. Fungsi take_damage() digunakan untuk mengurangi nilai health saat karakter menerima serangan, sedangkan fungsi attack_enemy() digunakan untuk menyerang musuh.
	Dalam program ini, objek player dan enemy diinisialisasi dengan nilai awal yang telah ditentukan. Pada saat objek player menyerang objek enemy, fungsi attack_enemy() pada player akan dipanggil dan parameter yang diteruskan adalah objek enemy. Selanjutnya, fungsi take_damage() pada enemy akan dipanggil dengan parameter attack dari player sebagai argumen.
	Proses yang sama terjadi saat objek enemy menyerang objek player. Program akan terus berjalan sampai salah satu karakter memiliki health yang bernilai kurang atau sama dengan 0.
	Contoh program ini hanya merupakan gambaran sederhana dari implementasi OOP dalam pengembangan game dan masih banyak lagi konsep-konsep yang bisa diterapkan seperti inheritance, polymorphism, dan abstraction untuk membuat game yang lebih kompleks.


