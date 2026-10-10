---
layout: post
title: 'devilpenakut.com versi 9: pindah ke Jekyll dan Cloudflare Pages'
date: '2026-10-10 09:00:00'
tags:
- opini
- blog
---

Di [versi 6](/devilpenakut-com-versi-6) saya menulis kalau saya belum puas dengan performanya. Masalahnya waktu itu ada di sisi kode WordPress, bukan di hosting. Karena itu saya mulai mencoba platform lain.

Perjalanannya ternyata cukup panjang. Versi 7 pindah ke Ghost CMS yang saya pasang sendiri di AWS (Amazon Web Services), seperti yang sudah saya tulis di [Buat Blog di Amazon Web Server dengan Ghost CMS](/buat-blog-ghost-cms), bahkan sempat pindah ke server lain yang lebih murah. Versi 8 sempat menetap di Hashnode. Dan sekarang sudah masuk versi 9.

## Kenapa pindah lagi

Hashnode sebenarnya nyaman. Menulis tinggal fokus di editor, urusan server tidak perlu dipikirkan. Tapi ada beberapa hal yang bikin saya tidak tenang.

Pertama, semua tulisan tinggal di platform orang lain. Kalau aturan platform berubah, saya harus mulai lagi dari nol. Jadi kali ini saya ingin sesuatu yang benar-benar milik sendiri, dan itu terjadi dengan perubahan akhir-akhir ini yang Hashnode mengeluarkan layanan “pro”-nya yang banyak pembatasan. Bahkan saya ngga bisa ekspor tulisan saya.

Kedua, saya mau blog yang cepat, ringan, gratis, dan bisa saya kontrol sepenuhnya.

## Kenapa Jekyll dan Cloudflare Pages

Jekyll itu *static site generator*. Artinya blog ini tidak punya server yang harus dijaga dan tidak ada database yang harus di-backup. Setiap tulisan adalah file Markdown biasa yang disimpan di repository GitHub. Ketika saya push perubahan, situsnya otomatis dibangun ulang dan di-deploy dalam kurang lebih 2 sampai 3 menit.

Hasilnya disajikan dari jaringan CDN Cloudflare, termasuk node di Jakarta. Jadi pembaca dari Indonesia seharusnya bisa mendapat respons yang lebih cepat.

Sebelumnya sebenarnya blog dengan Jekyll ini sudah jalan lama dan saya taruh di GitHub Pages. Setelah itu hosting-nya saya pindah ke Cloudflare Pages. Alasannya sederhana: DNS domain ini memang sudah di Cloudflare, dan Cloudflare Pages memudahkan pengaturan redirect.

## Mengumpulkan tulisan yang tercecer

Selama bertahun-tahun tulisan saya tersebar di banyak tempat. Sebagian ada di WordPress lama, sebagian di Hashnode, dan sebagian lagi di Medium. Pindahan ini sekalian untuk merapikan semuanya.

Hasilnya ada 236 tulisan dari tahun 2008 sampai 2026 dalam satu tempat. Dari Medium, ada 73 artikel berbahasa Indonesia yang saya ambil dari file ekspor. Versi bahasa Inggris dari tulisan yang sudah ada saya lewati supaya tidak dobel. Ada juga 11 tulisan yang dulu hanya tersisa judulnya. Isinya sempat hilang, dan sekarang semuanya sudah kembali.

## Alamat lama tidak boleh rusak

Ini bagian yang paling saya khawatirkan. Link yang sudah dibagikan orang di mana-mana tidak boleh berubah jadi halaman error karena itu akan berpengaruh ke mana-mana terutama untuk tampilan di Google Search.

Semua 166 alamat lama dari Hashnode tetap membuka artikel yang sama. Formatnya saya buat sama, dan tidak ada tanda garis miring di akhir. Alamat format lama dari era Ghost seperti `/2021/03/judul/`, juga alamat feed lama `/rss.xml`, diarahkan (redirect) ke alamat yang baru.

Untuk memastikan tidak ada yang terlewat, dengan bantuan Claude, saya bikin skrip kecil yang membandingkan sitemap lama dengan hasil build yang baru. Kalau ada yang hilang, skrip itu akan memberi tahu saya. Link di dalam tulisan yang mengarah ke alamat WordPress atau Medium juga sudah saya ganti, sekarang menunjuk ke tulisan yang ada di sini.

## Menyelamatkan gambar

Dulu gambar di blog ini sering di-hotlink dari banyak tempat: CDN WordPress, CDN Hashnode, Google Photos, Dropbox, dan entah dari mana lagi. Begitu satu layanan berubah, gambar di tulisan lama ikut rusak.

Gambar yang masih hidup saya pindahkan ke layanan gambar Cloudinary. Beberapa yang sudah tidak ada di sumber aslinya saya coba ambil lagi dari Internet Archive lewat Wayback Machine. Sisanya, sekitar 260 gambar, sudah hilang untuk selamanya. Daripada menyisakan ikon gambar rusak di mana-mana, gambar-gambar itu saya hapus dari tulisan.

Ironisnya, screenshot di tulisan versi 6 juga termasuk yang hilang. Tulisan tentang perjalanan blog ini justru kehilangan gambarnya sendiri. Saya ngga tahu taruh dimana backupnya, tapi ya sudahlah.

Sekarang gambar otomatis diubah ukurannya dan dikompres oleh Cloudinary, lalu dimuat *lazy* ketika sudah mendekati layar.

## Merapikan isi

Selain pindahan, isi tulisannya juga saya rapikan satu per satu.

- Heading diperbaiki. Sub-heading sekarang otomatis masuk ke daftar isi.
- Perintah di panduan Linux dan modem yang lama sekarang jadi *code block* yang layak, tidak lagi bercampur dengan teks biasa.
- Tweet dan postingan Instagram yang dulu tidak tampil sudah di-embed lagi.
- Setiap tulisan punya satu kategori (review, opini, tips, berita, atau panduan) ditambah beberapa topik.

## Tampilan baru

Desainnya sekarang bergaya *broadsheet*, seperti koran zaman dulu. Latar belakangnya warna kertas krem, judulnya memakai huruf Bodoni yang tebal, dan nama situs di bagian atas memakai huruf blackletter dengan maskot devil "dp" kecil. Arsip dikelompokkan per tahun. Di desktop, daftar isi ada di sebelah kiri, dan ada link "Kembali ke atas" di bagian bawah.

Kolom komentar tidak saya pasang lagi. Sebagai gantinya, diskusi saya ajak lewat X dan Threads. Mungkin nanti komentar akan kembali, tapi belum sekarang.

## Di balik layar

Bagian ini memang tidak terlihat, tapi kerjaannya lumayan banyak:

- Meta tag dan gambar untuk share dirapikan supaya tampil bagus ketika link dibagikan.
- Favicon dipasang lagi, analytics dan iklan disambungkan ulang.
- Halaman privasi ditambahkan.
- DNS dibersihkan. Ada beberapa subdomain lama yang sudah tidak dipakai, dan salah satunya ternyata menampilkan website milik orang lain.

Untuk menulis tulisan baru, sekarang saya pakai editor web sederhana bernama Pages CMS. Tulisan yang disimpan langsung masuk ke repository, jadi tidak perlu ekspor impor lagi.

## Yang hilang

Tidak semuanya bisa ikut pindah. Komentar dari era Disqus dan Ghost tidak terbawa. Sebagian gambar juga hilang, seperti yang sudah saya ceritakan di atas.

## Penutup

Akhirnya performanya terasa sesuai harapan. Tapi saya masih belajar, dan dengan bantuan Claude masih banyak yang bisa diperbaiki. Mungkin nanti saya tambahkan fitur pencarian, kalau sudah ada waktunya.

Kalau kamu sudah mengikuti blog ini dari dulu, atau baru mampir hari ini, halo!

