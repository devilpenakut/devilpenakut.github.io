---
layout: post
title: 'VoiceStudio: lima detik suara saya bikin penasaran'
date: '2026-10-13 09:00:00 +0700'
tags:
- panduan
- ai
- aplikasi
---

Saya baru menginstal VoiceStudio, dan yang bikin kagum justru hal kecil: sampel suara saya yang cuma lima detik.

Dari potongan sesingkat itu, saya bisa bikin narasi dengan suara saya sendiri, gratis. Kalau kamu pernah penasaran bagaimana suara sendiri bisa dipakai untuk membaca teks baru, ini menarik buat dicoba.

<figure>
<svg viewBox="0 0 640 340" role="img" aria-labelledby="voicestudio-t" style="display:block;inline-size:100%;block-size:auto;background:var(--paper)">
  <title id="voicestudio-t">Potongan gelombang suara pendek berstempel 5 DETIK, berpanah ke gelombang suara yang jauh lebih panjang</title>
  <path d="M0 40H640M0 300H640" style="stroke:var(--ink);stroke-width:1"/>
  <g style="fill:none;stroke:var(--ink);stroke-linecap:round">
    <rect x="60" y="110" width="170" height="120" style="fill:var(--parchment);stroke-width:2.5"/>
    <path d="M80 165V175M90 158V182M100 150V190M110 161V179M120 144V196M130 155V185M140 140V200M150 159V181M160 148V192M170 162V178M180 153V187M190 164V176M200 157V183M210 166V174" style="stroke-width:4"/>
    <path d="M246 170H286M278 162L286 170L278 178" style="stroke-width:2.5;stroke-linejoin:round"/>
    <path d="M300 163V177M308 154V186M316 149V191M324 152V188M332 159V181M340 159V181M348 155V185M356 154V186M364 157V183M372 163V177M380 155V185M388 150V190M396 151V189M404 159V181M412 158V182M420 151V189M428 150V190M436 155V185M444 163V177M452 156V184M460 154V186M468 155V185M476 160V180M484 159V181M492 152V188M500 150V190M508 155V185M516 163V177M524 153V187M532 149V191M540 152V188M548 160V180M556 159V181M564 154V186M572 155V185M580 157V183M588 163V177M596 155V185" style="stroke-width:3"/>
  </g>
  <g transform="translate(150 238) rotate(-10)" style="fill:none;stroke:var(--ember)">
    <rect x="-68" y="-22" width="136" height="44" rx="2.88" style="fill:var(--paper);stroke-width:2.5"/>
    <text text-anchor="middle" dominant-baseline="central" style="fill:var(--ember);stroke:none;font:800 20px var(--display);letter-spacing:.16em">5 DETIK</text>
  </g>
</svg>
<figcaption>Lima detik rekaman di kiri, narasi baru di kanan.</figcaption>
</figure>

Tapi rasa kagum itu juga membawa satu pertanyaan: kalau aplikasi bisa meniru suara saya, ke mana rekaman saya pergi? Apakah diproses di PC sendiri, atau dikirim ke server orang lain? Bisakah suara saya dipakai orang lain?

Masalahnya, kata “lokal” belum menjawab semua pertanyaan soal privasi. Sebelum kamu ikut mencoba, saya ingin tahu dulu apa yang diproses di PC dan kapan aplikasinya tetap memakai internet.

[VoiceStudio](https://github.com/debpalash/VoiceStudio) adalah aplikasi open source untuk pekerjaan suara: voice cloning, pembuatan suara, dubbing video, transkripsi, sampai audiobook. Aplikasinya jadi tempat kamu memilih model AI dan menjalankan alur kerja, dan [kemampuan tiap model](https://github.com/debpalash/VoiceStudio/blob/main/docs/feature-catalog.md) bisa berbeda.

Tapi… ada tapinya. Lima detik tadi pengalaman saya, bukan janji bahwa semua rekaman lima detik akan menghasilkan kualitas yang sama. Model yang dipilih, kualitas sampel, dan teks yang dibaca tetap berpengaruh. Bahkan, ada model text-to-speech yang [ngga mendukung cloning sama sekali](https://github.com/debpalash/VoiceStudio/blob/main/docs/audio-quality.md).

## Sebelum mulai

[Panduan instalasi Windows](https://github.com/debpalash/VoiceStudio/blob/main/docs/install/windows.md) menyebut Windows 10/11 dan ruang kosong sekitar 10GB untuk aplikasi, lingkungan Python, dan bobot model. Kebutuhan akhirnya bergantung pada model yang kamu pasang, jadi siapkan juga koneksi untuk unduhan awal. Python dan FFmpeg disiapkan oleh aplikasi; kalau memakai installer, kamu ngga perlu menyiapkan alat pengembangan.

GPU NVIDIA bisa mempercepat engine berbasis PyTorch di Windows. Tanpa GPU yang didukung, pemrosesan tetap jalan di CPU, hanya lebih lama. Punya GPU AMD atau Intel juga [belum tentu dipakai](https://github.com/debpalash/VoiceStudio/blob/main/docs/install/windows.md#gpu-support-on-windows) oleh engine PyTorch.

Saya fokus ke Windows di sini; macOS dan Linux punya paket dan panduan sendiri di [repositori resmi](https://github.com/debpalash/VoiceStudio#get-started).

## Langkah 1: cara install di Windows

Kalau kamu ingin mencoba, jalur yang paling mudah diikuti adalah installer resmi:

1. Buka [halaman Releases VoiceStudio](https://github.com/debpalash/VoiceStudio/releases).
2. Untuk PC Intel atau AMD biasa, pilih installer Electron Windows x64 berformat `.exe`.
3. Cocokkan checksum installer dengan `SHA256SUMS.txt` yang ada di rilis. Di PowerShell, jalankan `Get-FileHash .\NamaInstaller.exe -Algorithm SHA256`, lalu bandingkan hasilnya dengan baris yang sesuai.
4. Jalankan installer, lalu buka aplikasinya.
5. Ikuti penyiapan awal untuk memasang lingkungan pemrosesan lokal dan model yang diperlukan.

Ada juga jalur PowerShell resmi:

```powershell
irm https://voicestudio.sh/install | iex
```

Perintah itu mengunduh dan langsung menjalankan skrip instalasi. Untuk percobaan pertama, saya sarankan jalur installer agar langkahnya mudah diperiksa.

## Langkah 2: pilih model sebelum download

Setelah aplikasi terpasang, jangan langsung download semua model. VoiceStudio hanya aplikasinya; model AI yang kamu pilih menentukan kemampuan yang bisa dipakai. Model untuk mengubah suara jadi teks beda tugasnya dengan model untuk membuat suara dari teks.

**Kalau tujuanmu meniru suara sendiri, pilih model yang mendukung voice cloning.** Bisa membaca teks belum tentu bisa meniru suara. Contohnya, KittenTTS memakai suara bawaan dan ngga mendukung cloning, sementara OmniVoice dan VoxCPM2 mendukungnya. Salah pilih model bisa bikin kamu sudah menunggu download, tapi fitur yang dicari ternyata ngga ada.

Sebelum menekan download di **Model Catalogue**, cek beberapa hal:

- **Fitur yang dibutuhkan:** voice cloning untuk suara sendiri, text-to-speech untuk membaca teks, atau transkripsi untuk mengubah rekaman menjadi tulisan.
- **Bahasa yang didukung:** cek dukungan bahasa Indonesia pada model tersebut. Banyaknya bahasa yang ditawarkan aplikasi ngga berarti setiap model punya dukungan yang sama.
- **Kebutuhan perangkat:** cocokkan kebutuhan RAM, VRAM, dan akselerasi dengan PC kamu. Model yang bisa dipasang belum tentu nyaman dijalankan di perangkatmu.
- **Ukuran unduhan dan penyimpanan:** mulai dari satu model yang sesuai, lalu tambah kalau ada kebutuhan lain. Ngga perlu menghabiskan ruang untuk model yang belum akan dipakai.

Untuk PC tanpa GPU NVIDIA, panduan Windows [menyarankan engine ringan](https://github.com/debpalash/VoiceStudio/blob/main/docs/install/windows.md#pcs-without-an-nvidia-gpu). Tapi ringan saja belum cukup kalau tujuanmu cloning; dukungan fiturnya tetap harus dicek.

Untuk percobaan pertama, kamu bisa mulai dari pilihan bawaan, OmniVoice, yang tercantum di [katalog resmi](https://github.com/debpalash/VoiceStudio/blob/main/docs/feature-catalog.md), setelah mengecek kecocokannya dengan perangkat dan bahasa yang kamu pakai. Pilihan bawaan bukan jaminan hasilnya paling cocok untuk semua orang. Coba satu paragraf dulu, lalu nilai kemiripan suara, pelafalan, dan waktu generate sebelum memutuskan perlu mencoba model lain.

## Langkah 3: coba suara sendiri dengan teks pendek

Setelah penyiapan selesai, buka **Voice cloning**, lalu pilih atau tambahkan rekaman referensi. Pilih engine yang mendukung cloning dan pasang modelnya kalau aplikasi meminta. Masukkan teks pendek, lalu jalankan generate.

Untuk rekaman referensi, pakai suara sendiri yang jelas, tanpa musik atau suara orang lain. Misalnya:

> “Halo, ini suara saya. Hari ini saya sedang mencoba membuat narasi dari teks.”

**Isi kolom Transcript pada profil suara dengan kalimat itu, persis seperti yang kamu ucapkan.** Kalau kolom ini kosong, aplikasi bisa menjalankan [transkripsi tambahan](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) dulu.

Lalu gunakan teks keluaran yang berbeda:

> “Selamat datang. Di video ini, saya akan membagikan satu alat yang baru saya coba.”

Dengarkan cara aplikasi mengucapkan kata, mengambil jeda, dan mempertahankan karakter suara. Dari beberapa kalimat, kekurangannya lebih mudah ketahuan sebelum kamu bikin narasi panjang.

Kalau hasilnya sudah cukup baik, simpan atau ekspor audionya untuk diedit. Format WAV tersedia, tapi presisi ekspor yang lebih tinggi [ngga otomatis bikin suaranya lebih mirip](https://github.com/debpalash/VoiceStudio/blob/main/docs/audio-quality.md).

## Langkah 4: periksa apakah suara keluar dari PC

Jawabannya bergantung pada konfigurasi yang dipakai. Menurut [penjelasan resmi proyek](https://github.com/debpalash/VoiceStudio), alur kerja lokal berjalan di perangkat pengguna, layanan remote bersifat opsional, dan analitik penggunaan perlu persetujuan. Artinya, voice cloning dengan engine lokal dan backend di PC sendiri memang dirancang untuk memproses suara di PC tersebut.

**Tapi aplikasi lokal tetap bisa memakai internet.** Instalasi dan unduhan model butuh koneksi. VoiceStudio juga menyediakan pilihan layanan atau server lain; [katalog engine](https://github.com/debpalash/VoiceStudio/blob/main/docs/feature-catalog.md), misalnya, mencantumkan transkripsi OpenAI-compatible yang memakai server yang kamu atur. Kalau server itu ada di luar PC, pemrosesannya juga ngga lagi sepenuhnya di PC kamu.

Aplikasi juga [terhubung ke internet](https://github.com/debpalash/VoiceStudio/blob/main/.github/CONTRIBUTING.md#quality-gates-your-pr-must-pass) untuk hal seperti pemeriksaan pembaruan dan galeri. [Kode analitiknya](https://github.com/debpalash/VoiceStudio/blob/main/backend/core/analytics.py) hanya mengirim metadata penggunaan ke PostHog setelah pengguna memilih ikut serta; isi rekaman dan isi teks ngga masuk daftar data yang diizinkan. Itu menjelaskan desain analitiknya, bukan hasil audit seluruh aplikasi.

Ada pula fitur [remote workers](https://github.com/debpalash/VoiceStudio/blob/main/docs/remote-workers.md) opsional. Kalau diaktifkan dan diizinkan untuk suatu worker, tugas bisa mengirim audio, suara referensi, dan teks ke komputer lain. Untuk memproses sepenuhnya di PC sendiri, pakai backend dan model lokal, biarkan fitur remote mati, dan tolak analitik kalau kamu ngga mau mengirim metadata penggunaan.

Setelah semua model yang dibutuhkan selesai diunduh, coba generate dengan internet dimatikan untuk memastikan alur yang kamu pakai bisa berjalan offline. Percobaan itu sendiri belum membuktikan bahwa aplikasi ngga pernah mengirim data saat online.

Bagian privasi ini saya susun dari dokumentasi dan kode sumber proyek, tanpa audit lalu lintas jaringan di PC saya. Jadi saya belum bisa menjanjikan “tidak ada satu pun data yang keluar” untuk setiap fitur dan konfigurasi.

## Jika ada masalah

Kalau generate terasa lambat, coba teks yang lebih pendek dan cek **Settings → Performance** untuk melihat apakah engine berjalan di GPU atau CPU. Generate pertama setelah aplikasi dinyalakan memang lebih lama karena model baru dimuat. Detailnya ada di [panduan performa](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md).

Kalau hasil suara kurang cocok, cek lagi kejernihan rekaman, kecocokan isi kolom **Transcript**, dan dukungan cloning pada engine yang dipilih. Untuk masalah penyiapan, ikuti [panduan troubleshooting resmi](https://github.com/debpalash/VoiceStudio/blob/main/docs/install/troubleshooting.md).

## Dari rasa kagum menjadi alat yang berguna

Bagi saya, daya tariknya ada pada kemungkinan memakai suara sendiri untuk membuat draft narasi, mencoba pembukaan video, atau mendengarkan tulisan sebelum merekam versi final. Kamu bisa mulai dari satu sampel dan satu paragraf, lalu menilai sendiri apakah hasilnya layak dipakai.

Gunakan suara sendiri atau suara orang yang memberi izin. Untuk pekerjaan komersial, cek juga ketentuan model yang dipilih: [lisensi aplikasi](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) ngga otomatis mencakup hak atas semua model, suara, dan keluaran.

Lima detik tadi cukup untuk membuat saya penasaran. Sekarang yang ingin saya lihat adalah seberapa konsisten hasilnya ketika dipakai untuk narasi yang benar-benar saya butuhkan.

Kalau kalian bisa membuat narasi dengan suara sendiri dari teks, mau dipakai untuk apa? Cerita lewat Threads atau X, saya penasaran.

*Selamat mencoba suara sendiri.*

## Kredit

VoiceStudio dikembangkan oleh [debpalash dan para kontributor](https://github.com/debpalash/VoiceStudio). Pengalaman lima detik berasal dari percobaan saya; bagian instalasi dan privasi dirangkum dari sumber resmi. Dokumentasi cabang `main` bisa lebih baru daripada yang disebutkan di sini.
