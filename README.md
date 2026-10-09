# devilpenakut.github.io

Blog pribadi berbahasa Indonesia. Dapat dilihat di https://devilpenakut.github.io

## Tentang

Blog ini berisi 101 tulisan yang terbit dari tahun 2008 sampai 2023. Topiknya meliputi gadget dan iPhone, Linux dan modem (tulisan era 2008), konsol game (PlayStation, Xbox, Steam Deck), ulasan, dan tulisan opini.

Situs dibangun dengan Jekyll dan di-host di GitHub Pages. Setiap push ke branch `master` memicu build otomatis. Plugin yang dipakai:

- `jekyll-feed` - feed Atom di `/feed.xml`
- `jekyll-sitemap` - sitemap situs

## Menulis tulisan baru

Buat file baru di `_posts/` dengan nama `YYYY-MM-DD-judul.markdown`, lalu isi front matter seperti berikut:

```
---
layout: post
title: 'Judul Tulisan'
date: '2024-01-01 10:00:00'
tags:
- review
---
```

Isi tulisan ditulis dalam Markdown setelah blok front matter.

Tag yang diawali `hash-` disembunyikan. Tag tersebut merupakan sisa dari proses impor.

Tulisan yang hanya berisi front matter (tanpa isi) otomatis diberi tanda "Judul saja" di arsip dan di halaman tulisannya.

## Preview lokal

```
gem install jekyll jekyll-feed jekyll-sitemap
jekyll serve
```

Lalu buka http://127.0.0.1:4000

## Struktur

- `_posts/` - tulisan blog
- `_layouts/` - template: `default`, `post`, `page`
- `_includes/` - potongan template: `meta`, `tanggal` (format tanggal Indonesia), `analytics`, `disqus`
- `index.html` - beranda: tulisan pilihan (tulisan terbaru yang ada isinya) dan arsip per tahun
- `about.md` - halaman tentang
- `404.md` - halaman 404
- `_config.yml` - konfigurasi situs. Permalink `/:title` (tanpa garis miring akhir), sama dengan format URL Hashnode
- `_redirects` - aturan redirect untuk Cloudflare Pages (URL lama Hashnode/Ghost)
- `tools/cek_url.py` - cek bahwa setiap URL di sitemap Hashnode punya halaman atau redirect: `jekyll build` lalu `python tools/cek_url.py`
- `style.scss` - seluruh gaya situs. Warna dan font didefinisikan sebagai custom property di `:root` pada bagian atas file

## Desain

Tampilan bergaya "broadsheet" (seperti lembaran koran):

- latar belakang parchment hangat dan teks hitam tinta
- judul display besar dengan Bodoni Moda
- isi tulisan dengan Source Serif 4
- masthead dengan Pirata One
- satu aksen warna oranye bara

## Lisensi

MIT. Lihat berkas [LICENSE](LICENSE). Tema ini awalnya berbasis Jekyll Now oleh Barry Clark.
