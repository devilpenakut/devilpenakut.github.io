# devilpenakut

Blog pribadi berbahasa Indonesia: catatan gadget, game, dan opini. Tayang di https://devilpenakut.com

## Tentang

163 tulisan dari 2008 sampai 2026. Topiknya gadget dan iPhone, Linux dan modem (era 2008), konsol game, ulasan produk, dan opini.

Situs dibangun dengan Jekyll dan di-host di **Cloudflare Pages**. Setiap push ke branch `master` otomatis memicu build dan deploy (sekitar 2–3 menit). Pindah dari Hashnode pada Oktober 2026; semua URL lama tetap sama.

## Menulis tulisan baru

**Lewat Pages CMS (paling mudah):** buka https://app.pagescms.org, login dengan GitHub, pilih repo ini, lalu **Tulisan → Add an entry**. Menyimpan di CMS sama dengan commit ke `master`. Pengaturannya ada di `.pages.yml`.

**Lewat GitHub atau editor biasa:** buat file `_posts/YYYY-MM-DD-judul.markdown`. Bagian setelah tanggal menjadi URL (`devilpenakut.com/judul`).

```
---
layout: post
title: 'Judul Tulisan'
date: '2026-10-10 09:00:00'
tags:
- review
- iphone
---

Paragraf pembuka...

## Subjudul pertama
```

Pedoman singkat:

- **Subjudul pakai `##`.** Judul tulisan sudah menjadi H1. Subjudul `##` otomatis masuk daftar isi (muncul kalau ada minimal dua).
- **Tag:** satu kategori (`review`, `opini`, `tips`, `berita`, `panduan`) ditambah satu sampai tiga topik (mis. `iphone`, `game`, `netflix`, `operator`). Pakai ejaan yang sudah ada.
- **Gambar:** unggah ke Cloudinary folder `devilpenakut`, lalu pakai
  `https://res.cloudinary.com/setanwedinan/image/upload/f_auto,q_auto,c_limit,w_1400/devilpenakut/<nama-file>`.
  Gambar yang diunggah lewat Pages CMS tersimpan di `images/posts/`.
- **Tweet:** tempel sebagai `<blockquote class="twitter-tweet"><a href="https://twitter.com/akun/status/ID"></a></blockquote>`. Script X hanya dimuat di halaman yang memakainya.
- **Postingan Instagram:** tempel sebagai `<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/ID/" data-instgrm-version="14"><a href="https://www.instagram.com/p/ID/">Lihat postingan ini di Instagram</a></blockquote>`.
- **List bernomor yang tidak mulai dari 1:** tambahkan `{: start="N"}` tepat di bawah list (kramdown selalu mulai dari 1).

## Preview lokal

```
bundle install
bundle exec jekyll serve
```

Lalu buka http://127.0.0.1:4000

## Struktur

- `_posts/` - tulisan
- `_layouts/` - `default`, `post` (daftar isi, link ke X/Threads, tulisan sebelum/sesudah), `page`
- `_includes/` - `meta` (SEO dan kartu share), `analytics` (GA4 dan AdSense), `tanggal` (format tanggal Indonesia), `disqus`
- `index.html` - beranda: tulisan pilihan dan arsip per tahun
- `about.md`, `privasi.md`, `404.md` - halaman statis
- `style.scss` - seluruh gaya situs; warna dan font ada di `:root`
- `_config.yml` - konfigurasi; permalink `/:title` (tanpa garis miring akhir, sama dengan format URL Hashnode)
- `_redirects` - redirect Cloudflare Pages untuk URL lama Hashnode/Ghost dan `/rss.xml`
- `ads.txt` - verifikasi AdSense
- `favicon.ico`, `icon-192.png`, `apple-touch-icon.png`, `images/` - ikon, maskot, kartu share
- `.pages.yml` - pengaturan Pages CMS
- `tools/cek_url.py` - cek bahwa setiap URL di sitemap Hashnode masih tertangani: `jekyll build` lalu `python tools/cek_url.py`
- `DESIGN.md`, `PRODUCT.md` - catatan desain dan produk (tidak ikut di-build)

## Integrasi

- Google Analytics 4 dan Google AdSense (Auto ads), diatur di `_config.yml`
- `jekyll-feed` (feed di `/feed.xml`) dan `jekyll-sitemap` (`/sitemap.xml`)
- Gambar di Cloudinary, dengan `f_auto,q_auto,c_limit,w_1400` dan lazy loading

## Desain

Gaya "broadsheet" (lembaran koran): latar parchment, teks hitam tinta, judul display besar Bodoni Moda, isi Source Serif 4, nameplate blackletter Pirata One dengan maskot "dp", dan satu aksen oranye bara. Detail lengkap di `DESIGN.md`.

## Lisensi

MIT. Lihat [LICENSE](LICENSE). Awalnya berbasis tema Jekyll Now oleh Barry Clark.
