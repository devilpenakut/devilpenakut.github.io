---
layout: post
title: 'Membuat FM26 Berbahasa Indonesia: Menerjemahkan Skin UI dan Merapikan File Bahasa'
date: '2026-09-29 07:16:09'
---

Kabar baik untuk manajer Indonesia: **Football Manager 27 akan hadir dengan bahasa Indonesia resmi**, untuk pertama kalinya sepanjang sejarah seri ini. SEGA mengumumkannya bersamaan dengan dibukanya halaman toko FM27 di Steam dan Epic Games Store, dan bahasa Indonesia sudah tercantum di daftar bahasa antarmuka yang didukung.

<blockquote class="twitter-tweet"><a href="https://twitter.com/id_fm/status/2103637904102937050">https://x.com/id_fm/status/2103637904102937050</a></blockquote>

Tapi FM27 belum rilis. Sambil menunggu, kenapa tidak membuat FM26 terasa "Indonesia" dari sekarang?

Momennya juga pas. Belakangan muncul skin baru dari komunitas Korea, **UICHANGE** karya fmkorea/Gigliati, yang membuat tampilan FM26 terasa seperti FM24. Buat banyak pemain yang kurang cocok dengan antarmuka baru FM26 sejak pindah ke engine Unity, skin ini merubah tata letak yang familier, navigasi yang lebih akrab, tapi tetap dengan mesin permainan FM26.

<blockquote class="twitter-tweet"><a href="https://twitter.com/id_fm/status/2103368850742055114">https://x.com/id_fm/status/2103368850742055114</a></blockquote>

Masalahnya, begitu skin ini dipasang , menu masih menggunakan Bahasa Inggris.

Itulah titik awal project kecil ini: membuat FM26 dengan skin **UICHANGE** dan mod **Bahasa Indonesia** terasa satu kesatuan, sebagai "jembatan" yang nyaman sampai FM27 datang.

## Kenapa Teks Skin Tidak Ikut Diterjemahkan?

FM26 sudah memakai engine Unity. Teks di layar sebenarnya datang dari dua sumber yang berbeda:

- **File bahasa (**`.ltc`**)** menyimpan ratusan ribu teks: menu, berita, inbox, konferensi pers, dan dialog pemain. Setiap teks dipanggil game lewat ID, bukan lewat kalimat bahasa Inggrisnya.

- **Bundle layout UI (**`.bundle`**)** menyimpan susunan panel. Sebagian label di sini ditulis langsung di layout oleh pembuat skin.

Mod bahasa hanya mengubah sumber pertama. Label yang ditulis langsung di layout skin tidak pernah melewati file bahasa, jadi tetap tampil dalam bahasa Inggris. Masalahnya bukan pada mod bahasanya, tapi memang dua jalur yang terpisah.

## Langkah 1: Membongkar Bundle Skin

File yang jadi target adalah `ui-panelids-uxml_assets_all.bundle`. Setelah dibuka, isinya **1.473 aset UI** dari **737 panel**, mulai dari halaman klub, keuangan, taktik, transfer, sampai layar pembuatan game.

Dari semua itu, hanya ada **146 teks** (123 unik) yang ditulis langsung di layout. Tidak semuanya layak diterjemahkan:

- **Aman diterjemahkan:** label yang tampil saat bermain, seperti halaman profil klub, menu navigasi, portal berita, dialog pengaturan shortcut, dan beberapa judul panel lain.

- **Dibiarkan:** semua panel *debug* milik developer (isinya placeholder dengan typo seperti "Calasendar" dan nama internal seperti `ClubVisionObjectives`), serta kredit pembuat skin.

Prinsipnya sederhana: **ubah hanya teks yang tampil, jangan sentuh apa pun yang mungkin terhubung ke logika game.** Nama elemen, class, binding, dan ID dibiarkan persis seperti aslinya.

## Langkah 2: Menyeragamkan Istilah dengan File Bahasa

Setelah label skin diterjemahkan, muncul masalah baru: **istilah yang berbeda untuk hal yang sama.** Skin menulis "Riwayat Liga", sementara file bahasa menulis "Sejarah Liga". Skin menulis "Bola Mati", file bahasa sebagian besar masih "Set Pieces".

Pilihannya: ikuti istilah file bahasa, atau ubah file bahasa supaya mengikuti istilah skin. Saya memilih yang kedua, supaya satu istilah dipakai konsisten di seluruh game.

Untuk itu, format file `.ltc` perlu dipahami dulu. Strukturnya ternyata cukup rapi:

- sebuah header,

- blok berisi semua teks (setiap entri bisa punya beberapa varian, misalnya versi pemain putra dan putri),

- tabel indeks yang memetakan setiap ID teks ke posisinya di file.

Karena panjang teks berubah, posisi semua teks sesudahnya ikut bergeser. Jadi seluruh **192.024 penunjuk** di tabel indeks dihitung ulang. Uji yang sama dilakukan di sini: file dibongkar lalu disusun ulang tanpa perubahan, dan hasilnya identik dengan aslinya.

**65 teks** diseragamkan, misalnya:

Sebelumnya
Sesudahnya

Tahun Didirikan
Tahun Berdiri

Kepribadian Skuad
Karakter Skuad

Kepercayaan Petinggi Klub
Kepercayaan Dewan

Pengembangan Pemain Muda
Pembinaan Pemain Muda

Pertandingan Berikutnya
Laga Berikutnya

Set Pieces
Bola Mati

Hanya teks yang **persis sama** yang diganti. Nama jabatan seperti "Kepala Pengembangan Pemain Muda" sengaja tidak disentuh, begitu juga semua tag game seperti `[%male#1-hidden]`.

## Langkah 3: Mencari Teks Inggris yang Tersisa

Mod bahasa Indonesia yang dipakai sebenarnya sudah sangat lengkap. Dari sekitar 130 ribu kalimat panjang (berita, inbox, dialog), sebagian besar sudah berbahasa Indonesia.

Tapi masih ada yang terselip. Setelah dipindai, ada **93 teks** (45 kalimat unik beserta variannya) yang masih bahasa Inggris, antara lain:

- berita kekalahan tim yang terkena pengurangan poin,

- berita klub yang meraih trofi ketujuh dalam semusim,

- peringatan staf soal gaji yang melebihi anggaran,

- harapan dewan dan suporter jelang laga penentuan degradasi,

- komentar pemain soal cuaca dan kondisi lapangan,

- notifikasi instruksi taktik seperti arah umpan silang.

Semuanya diterjemahkan, dengan satu aturan ketat: **setiap kode game harus tetap ada.** Tag seperti `[%team#1-short]` (nama tim), `[%comp#1-short]` (nama kompetisi), dan `{upper}` (huruf kapital otomatis) dicek otomatis di setiap kalimat. Tidak ada satu pun yang hilang.

## Bagaimana dengan `catalog.bin`?

Skin UICHANGE juga menyertakan `catalog.bin`, yaitu katalog Addressables Unity yang berfungsi sebagai "daftar isi" aset. Skin memakai katalog ini untuk mendaftarkan 6 aset tambahan, seperti pengaturan tabel saat pertandingan dan tile *pass map*.

Katalog ini tidak perlu diubah. Katalog hanya merujuk bundle lewat nama dan lokasi, dan tidak menyimpan checksum per bundle. Jadi bundle yang sudah diterjemahkan tetap dikenali game.

## Yang Masih Tetap Bahasa Inggris

Supaya ekspektasinya jelas, ada beberapa hal yang memang di luar jangkauan file bahasa:

- **Nama kompetisi, klub, dan penghargaan** berasal dari database game.

- **Angka yang ditulis dengan huruf** (misalnya "three") dibuat oleh mesin game.

- **Teks baru dari patch** akan tampil dalam bahasa Inggris sampai file bahasanya diperbarui.

## Cara Install

Download dulu UICHANGE dari sini

<blockquote class="twitter-tweet"><a href="https://twitter.com/LICAA747/status/2103675685386543172">https://x.com/LICAA747/status/2103675685386543172</a></blockquote>

Copy semua isi folder Bundles ke `...\StreamingAssets\aa\StandaloneWindows64`.

Copy semua isi Addressables ke `...\StreamingAssets\aa\`

### Isi Paket Bahasa Indonesia

Download paket

[Paket Bahasa Indonesia](https://gofile.io/d/XlIjoHfp)

File
Fungsi

`Bahasa Indonesia.ltc`
File bahasa: menu, berita, inbox, dialog, konferensi pers

`ui-panelids-uxml_assets_all.bundle`
Layout UI skin UICHANGE dengan 82 label berbahasa Indonesia

### Sebelum Mulai

- Tutup FM26 sepenuhnya.

- **Backup** semua file asli yang akan ditimpa (copy ke folder lain).

- Pastikan skin UICHANGE sudah terpasang, karena bundle di paket ini adalah versi terjemahan dari file skin tersebut.

### Langkah 1: Pasang File Bahasa

- Buka folder `Documents\Sports Interactive\Football Manager 26\languages`. Buat folder `languages` jika belum ada.

- Copy `Bahasa Indonesia.ltc` ke folder tersebut. Jika sudah ada file dengan nama sama, timpa saja.

### Langkah 2: Pasang File UI (Bundle)

- Buka folder instalasi FM26. Di Steam: klik kanan FM26, lalu **Manage > Browse local files**.

- Masuk ke folder bundle aset UI: `...\StreamingAssets\aa\StandaloneWindows64`. Jika tidak ketemu, cari nama file `ui-panelids-uxml_assets_all.bundle` lewat kolom search Windows Explorer di folder instalasi game.

- Backup file `ui-panelids-uxml_assets_all.bundle` yang lama.

- Copy file bundle dari paket dan timpa file lama.

### Langkah 43 Aktifkan Bahasa di Game

- Jalankan FM26.

- Buka **Settings > Interface > Language**.

- Pilih **Bahasa Indonesia**.

- Restart game.

### Jika Ada Masalah

- **Game crash atau UI kosong setelah pasang bundle:** kembalikan `ui-panelids-uxml_assets_all.bundle` dari backup.

- **Bahasa tidak muncul di pilihan:** pastikan file `.ltc` ada di folder `languages` yang benar dan namanya `Bahasa Indonesia.ltc`.

- **Setelah FM26 update:** update game bisa menimpa file bundle dan catalog. Pasang ulang skin UICHANGE versi terbaru terlebih dahulu. Bundle terjemahan ini hanya cocok dengan versi skin yang dipakai saat dibuat.

## Kredit

- Mod Bahasa Indonesia: **Tupai Art** dan **Caramelio**, dengan bantuan **Kung @FMThai**.

- Skin UICHANGE: **fmkorea Gigliati**.

Project ini hanya melengkapi dan merapikan karya mereka. Tanpa fondasi itu, semua ini tidak akan mungkin.

## Sampai Jumpa di FM27

Begitu FM27 rilis dengan bahasa Indonesia resmi, sebagian besar pekerjaan seperti ini mungkin tidak diperlukan lagi. Tapi sampai hari itu tiba, FM26 dengan tampilan ala FM24 dan antarmuka berbahasa Indonesia adalah cara yang nyaman untuk tetap menikmati musim demi musim.

*Selamat bermain, manajer Indonesia!*
