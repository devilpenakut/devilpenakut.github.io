---
layout: post
title: 'Windows Package Manager, menyuruh Windows melakukan install atau delete aplikasi'
date: '2021-08-10 08:57:45'
---

## "Windows, install Firefox!" dan Windows akan otomatis mencari dan install

Firefox.

Pernah kamu ingin install aplikasi tapi bingung cari tempat downloadnya di
browser? atau malas buat buka browser atau Microsoft Store. Kamu bisa pakai
layanan bernama **Windows Package Manager**.

Windows Package Manager dikenal sebagai `winget`. Misal kamu tinggal ketik
`winget install firefox` untuk mengunduh dan menginstal browser Firefox secara
otomatis.

Winget ini tersedia di Windows 10, versi 1809 dan yang lebih baru.

## Cara Menggunakan Winget untuk Mengunduh Aplikasi dengan Cepat

Buka aplikasi Windows **PowerShell** , juga bisa memakai **Command Prompt**.
Ketik `winget` untuk melihat daftar perintah yang bisa kamu pakai.

```bash
winget
```

Apa yang hebat tentang perintah `winget` adalah ia terhubung ke repositori
aplikasi paket yang ada, sehingga Anda dapat dengan cepat menemukan apa yang
Anda cari jika Anda sudah mengetahui nama aplikasinya.

Pengecualian adalah jika ada lebih dari satu versi aplikasi dengan nama yang
hampir mirip; mengetik `winget install opera`, misalnya, akan keluar pilihan
untuk browser game Opera GX atau browser Opera biasa.

```bash
winget install opera
```

`winget search` diikuti dengan nama paket adalah cara mencari aplikasi yang
ingin kamu install.

```bash
winget search brave
```

Kalau mau lihat aplikasi apa yang terinstall di PC kita tinggal ketik `winget list`
. Di perintah ini juga akan keliatan apakah ada aplikasi di PC kita yang
butuh untuk di upgrade.

```bash
winget list
```

Perintah `winget upgrade` bisa digunakan untuk upgrade versi aplikasi.
Walaupun ini mungkin tidak diperlukan, karena banyak aplikasi hanya akan
memutakhirkan sendiri secara otomatis atau meminta Anda melakukannya saat
berikutnya Anda memulai ulang.

```bash
winget upgrade
```

```bash
winget upgrade spotify
winget upgrade epicgames
```

## Cara Menggunakan Winget untuk Menghapus Aplikasi

Untuk melakukan *uninstall* aplikasi maka bisa memakai perintah: `winget uninstall`
 dan secara otomatis winget akan melakukan proses *uninstall* tanpa
kita harus membuka *add/remove program.*

Kompleksitas aplikasi Microsoft Store dan keterbatasan isinya telah menjadi
masalah bagi pengguna Windows.

Microsoft diperkirakan akan merombak Microsoft Store bersamaan dengan Windows

- Winget adalah alternatif yang bagus sementara menunggu.

Ada komentar atau masukan? silahkan lewat [Discord
devilpenakut](https://discord.gg/694HsdDGzy) atau lewat
[Twitter](https://x.com/devilpenakut).
