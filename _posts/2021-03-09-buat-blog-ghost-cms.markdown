---
layout: post
title: 'Buat Blog di Amazon Web Server dengan Ghost CMS'
date: '2021-03-09 12:17:07'
---

Ada beberapa cara untuk memulai membuat blog, mulai dari beberapa layanan
gratis seperti Wordpress, Blogger dan Medium. Nah di pembahasan kali ini saya
bahas cara buat blog di Amazon Web Server dengan Ghost CMS.

## Apa itu Ghost CMS

[Ghost](https://ghost.org/) adalah salah satu CMS (Content Management System)
yang berfungsi sebagai *blogging platform*. Seperti halnya WordPress, Ghost
dirancang khusus dengan tampilan elegan cocok untuk para blogger di seluruh
dunia. Kamu bisa berbagi ide, berbagi cerita dan berbagi tutorial layaknya
blog biasa. Ghost sendiri terdiri dari beberapa *theme* yang bisa digunakan
sebagai tempat menampung tulisan kamu.

## **Apa itu AWS**

[Amazon Web Services](https://aws.amazon.com/id/) adalah sekumpulan layanan-
layanan berbasis *Cloud Computing* yang di sediakan oleh Amazon sejak tahun
2002.

Amazon Elastic Compute Cloud (Amazon EC2) adalah layanan web yang memberikan
kapasitas komputasi yang aman dan berukuran fleksibel di *cloud*. Amazon EC2
dirancang untuk membuat komputasi *cloud* berskala web lebih mudah bagi
pengembang.

### Tingkatan gratis

AWS menyediakan tingkatan gratis dengan ketentuan meliputi 750 jam instans
t2.micro Linux dan Windows. Nah untuk tetap berada di Tingkat Gratis, **hanya
gunakan instans Mikro EC2 saja**.

## Install Ghost di AWS

Nah disini kita akan membuat Instans Mikro EC2 agar kita bisa menikmati
pembuatan blog gratis di AWS.

Pertama buat akun AWS. Bila dibutuhkan masukkan detail pembayaran seperti
kartu debit atau kredit. Tapi tenang, jika langkah-langkah berikut diikuti
dengan seksama bisa menikmati tingkatan gratis selama 12 bulan. Bila nanti
setelah 12 bulan, anggaran yang dibutuhkan sekitar 60-80 ribu per bulan.
Seperti langganan Netflix dan Spotify saja kan?

Masuk ke [AWS Marketplace
(amazon.com)](https://console.aws.amazon.com/marketplace/home?region=ap-southeast-1#/landing), bisa menggunakan *search* di bagian atas.

Cari `Ghost Certified by Bitnami` lalu klik pilihan `Launch New Instance`
dengan pilihan server ap-southeast-1 (Singapura) karena region Indonesia belum
ada.

Pada langkah selanjutnya untuk tipe dari instans menggunakan `t2.micro`,
jangan yang lain agar bisa menikmati tingkatan gratis.

Langsung pilih tombol `Review and launch` yang berwarna biru. Bila ada pilihan
untuk buat `key pairs` bisa beri nama dan disimpan key-nya, karena akan
berguna untuk akses SSH nanti.

Selanjutnya akan masuk ke EC2 Dashboard. Sampai disini sebetulnya blog Ghost
kamu sudah jalan.

Namun perlu pengaturan lebih lanjut karena posisi saat ini masih menggunakan
*username* dan *password* bawaan dan menggunakan alamat IP Publik dari
instans.

### Membuka Ghost di web browser

Langkah selanjutnya adalah untuk mengetahui *username* dan *password* bawaan
dari Bitnami-nya untuk bisa masuk ke admin Ghost.

Pilih `Instances`,

Lalu *checklist* Instance kamu,

Pilih `Actions` dibagian atas > `Monitor and troubleshoot` > `Get system log`,

Cari tulisan seperti ini, copy seluruhnya atau bagian username dan password
nya saja,

Kembali ke halaman Instances klik bagian `Instances ID` buka atau *copy*
`Public IPv4 address` di browser kamu,

Jika tertampil halaman awal Ghost seperti ini berarti instalasi kamu sudah
berhasil.

## Ghost Setting

### Mengganti IP address menjadi domain yang kita punya

Saat ini blog Ghost kamu bisa diakses menggunakan IP publik yang diberikan
oleh AWS.

Nah untuk *setting* menjadi domain yang kamu punya, arahkan A Record domain
kamu ke IP publik yang tadi.

Lalu rubah kita rubah *setting* di Ghostnya.

Kita menggunakan CLI (Command Line Interface), apa itu CLI bisa akses
penjelasan singkat [disini](https://www.w3schools.com/whatis/whatis_cli.asp).
Dengan menggunakan [Ghost CLI](https://ghost.org/docs/ghost-cli/) maka kita
bisa menyambungkan dengan menggunakan fitur `Connect` di EC2.

Masuk ke direktori Ghost

    cd /opt/bitnami/apps/ghost/htdocs/

*Update setting domain* Ghost kamu dengan menggunakan perintah `ghost config`
dalam direktori Ghost:

    ghost config url https://my-domain.com

Bila fitur perintah `ghost config` tidak mau muncul mungkin Ghost CLI belum
terinstal. Karenanya perlu *install* dengan perintah, lewati perintah ini bila
`ghost config` sudah jalan normal.

    sudo npm install -g ghost-cli@latest

Lalu pastikan SSL berjalan jika kamu pakai SSL

    ghost setup nginx ssl

Selanjutnya *restart* Ghost agar bisa mengadopsi menggunakan domain yang sudah
di *setting*

    ghost restart

Disini seharusnya untuk membuka dengan domain yang kamu punya sudah bisa.

*Login* menggunakan alamat: [domain]/ghost menggunakan *username* dan
*password* yang tadi sudah di catat.

Kalau kamu sudah bisa *login* di dalam admin-nya Ghost sebelum mulai apa pun
segera masuk ke akun *`staff`*.

Rubah detail di akun `owner`, termasuk *email* dan *password-* nya agar tidak
menggunakan *email* dan *password default*.

Di bagian desain kamu bisa mengubah tampilan blog Ghost dengan pilihan yang
sudah ada atau masuk ke `marketplace`.

Untuk memulai *postingan* bisa masuk ke `Posts` lalu `New Post` atau langsung
pilih tanda `+` disebelah `Posts`

Blog Ghost kamu sudah aktif dan bisa diakses melalui Web. Sebenarnya masih
banyak lagi yang bisa di-kostumasi dari Ghost, namun kita bahas dilain waktu.

Bila ada pertanyaan bisa sampaikan ke Twitter saya
[@devilpenakut](**GHOST_URL**/2021/03/buat-blog-ghost-cms/twitter.com/devilpenakut). Terima kasih.
