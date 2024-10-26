---
layout: post
title: Permission yang aneh dari aplikasi BookMyShow
date: '2016-11-24 09:30:00'
tags:
- android
- bookmyshow
- permission
- play-store
- hash-import-2024-05-05-07-58
---

Saya suka melakukan _update_ aplikasi untuk mendapatkan versi app yang paling baru. Buka _Play Store — My aplikasi & games — update all_. Biasanya kalau misal ada _permission_ baru dari _update_ aplikasi, _Play Store_ akan memberi tahu.

Itu yang terjadi ketika aplikasi [BookMyShow](https://id.bookmyshow.com/jakarta)meminta _update permission_. Oh iya, BookMyShow adalah aplikasi pemesanan tiket event dan bioskop yang saat ini sedang banyak promo. Saya suka menggunakan aplikasi ini karena bisa melihat persediaan tiket di beberapa jaringan bioskop dan langsung bisa memesannya. Selain itu banyak promo diskon yang sangat menguntungkan untuk yang sering nonton seperti saya.

Oke, kembali ke _permission_ yang diminta oleh BookMyShow.

<figure id="3ca7" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"></div>
<div class="progressiveMedia js-progressiveMedia graf-image is-imageLoaded is-canvasLoaded" data-image-id="1*F8pwzQQlucYdj7U1NHDaHw.png" data-width="1440" data-height="2560" data-action="zoom" data-action-value="1*F8pwzQQlucYdj7U1NHDaHw.png" data-scroll="native">
<canvas class="progressiveMedia-canvas js-progressiveMedia-canvas" width="42" height="75"></canvas><img class="progressiveMedia-image js-progressiveMedia-image" src="https://i2.wp.com/cdn-images-1.medium.com/max/800/1*F8pwzQQlucYdj7U1NHDaHw.png?w=1200&amp;ssl=1" data-src="https://i2.wp.com/cdn-images-1.medium.com/max/800/1*F8pwzQQlucYdj7U1NHDaHw.png?w=1200&amp;ssl=1" data-recalc-dims="1">
</div>
</div>
</figure>

_Permission_ yang aneh dari aplikasi pesan _event_ dan tiket. Kenapa perlu _Device & app history_?

Dari bantuan Google menyebutkan bahwa _permission_ itu adalah untuk:

> An app can do one or more of the following:

> -Read sensitive log data  
> -Retrieve system internal state  
> -Read your web bookmarks and history  
> -Retrieve running apps

Wow. Aplikasi itu bisa melihat sampai sedalam itu kalau _permission_ nya diberikan.

Dari penjelasan _permission_ itu berkata, _one of_. Berarti bisa cuma salah satu. Berarti yang dipakai sama BookMyShow bisa dicari halaman _Play Store_-nya di bagian paling bawah. Ternyata dipakai satu, _retrieve running app._

<figure id="f3bf" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"></div>
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*AWWh8PemUcJTNyJXBjkYRw.jpeg" data-width="1080" data-height="2344" data-action="zoom" data-action-value="1*AWWh8PemUcJTNyJXBjkYRw.jpeg" data-scroll="native">
<canvas class="progressiveMedia-canvas js-progressiveMedia-canvas" width="34" height="75"></canvas><img class="progressiveMedia-image js-progressiveMedia-image" src="https://i0.wp.com/cdn-images-1.medium.com/max/800/1*AWWh8PemUcJTNyJXBjkYRw.jpeg?w=1200&amp;ssl=1" data-src="https://i0.wp.com/cdn-images-1.medium.com/max/800/1*AWWh8PemUcJTNyJXBjkYRw.jpeg?w=1200&amp;ssl=1" data-recalc-dims="1">
</div>
</div>
</figure>

Namun ini terlalu banyak. Aplikasi serupa tidak sebanyak yang diminta oleh BookMyShow.

Ini contoh untuk Cinemaxx.

<figure id="2b3f" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"></div>
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*SDBBrSII8XN8Db55fZo-hQ.jpeg" data-width="1080" data-height="2070" data-action="zoom" data-action-value="1*SDBBrSII8XN8Db55fZo-hQ.jpeg" data-scroll="native">
<canvas class="progressiveMedia-canvas js-progressiveMedia-canvas" width="39" height="75"></canvas><img class="progressiveMedia-image js-progressiveMedia-image" src="https://i1.wp.com/cdn-images-1.medium.com/max/800/1*SDBBrSII8XN8Db55fZo-hQ.jpeg?w=1200&amp;ssl=1" data-src="https://i1.wp.com/cdn-images-1.medium.com/max/800/1*SDBBrSII8XN8Db55fZo-hQ.jpeg?w=1200&amp;ssl=1" data-recalc-dims="1">
</div>
</div>
</figure>

Ini CGV Blitz.

<figure id="76ac" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"></div>
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*oEKFwr_BDu1g8SW8uiGlkg.png" data-width="1440" data-height="2560" data-action="zoom" data-action-value="1*oEKFwr_BDu1g8SW8uiGlkg.png" data-scroll="native">
<canvas class="progressiveMedia-canvas js-progressiveMedia-canvas" width="42" height="75"></canvas><img class="progressiveMedia-image js-progressiveMedia-image" src="https://i1.wp.com/cdn-images-1.medium.com/max/800/1*oEKFwr_BDu1g8SW8uiGlkg.png?w=1200&amp;ssl=1" data-src="https://i1.wp.com/cdn-images-1.medium.com/max/800/1*oEKFwr_BDu1g8SW8uiGlkg.png?w=1200&amp;ssl=1" data-recalc-dims="1">
</div>
</div>
</figure>

Kita mengesampingkan dulu _permission_ yang terlalu banyak dari aplikasi BookMyShow, kita lihat permintaan _permission_ yang baru, _retrieve running app_.

Penjelasan yang saya dapat dari [androidforum.com](http://androidforums.com/threads/android-permissions-explained-security-tips-and-avoiding-malware.36936/)

> **Retrieve running applications**  
> Hardware controls  
> URI: **android.permission.GET\_TASKS**  
> Risk: **MEDIUM-HIGH**  
> Protection level: **DANGEROUS**

> **Official Description**  
> Allows an application to get information about the currently or recently running tasks: a thumbnail representation of the tasks, what activities are running in it, etc.

> **Details**  
> This permission is of moderate importance. It will allow an application to find out what other applications are running on your phone. While not a danger in and of itself, it would be a useful tool for someone trying to steal your data. Typical legitimate applications that require this permission include: task killers and battery history widgets. Other than that however, **most apps should not need this permission.**

Jadi aplikasi ini mempunyai permission untuk mendapatkan informasi aplikasi lain yang berjalan, aktivitas yang dilakukan aplikasi lain tersebut. Biasanya itu diperlukan di aplikasi _task killer_ atau aplikasi untuk melihat penggunaan baterai.

Untuk apa aplikasi BookMyShow membutuhkan itu?

Saya juga meneruskan hal ini ke kontak BookMyShow. Bila ada update akan saya sampaikan disini. Bagaimana menurut kamu?

<!--kg-card-end: html-->