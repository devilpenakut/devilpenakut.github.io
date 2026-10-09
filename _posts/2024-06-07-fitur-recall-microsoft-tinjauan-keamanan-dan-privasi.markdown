---
layout: post
title: 'Fitur Recall Microsoft: Tinjauan Keamanan dan Privasi'
date: '2024-06-07 11:12:29'
tags:
- review
- keamanan
- windows
---

Fitur Recall Windows dari Microsoft, yang dirancang untuk membantu pengguna melacak aktivitas masa lalu di PC mereka, telah **menimbulkan kekhawatiran signifikan tentang potensi risiko keamanan dan privasi yang ditimbulkannya**. Fitur ini, yang akan diluncurkan pada PC Copilot+ Windows 11 pada 18 Juni, mengambil tangkapan layar desktop setiap lima detik dan menyimpannya bersama log aktivitas pengguna dalam database SQLite lokal.

### **Masalah Keamanan Inti**

Masalah utama terletak pada cara Recall menyimpan data ini. Meskipun Microsoft mengklaim bahwa enkripsi seluruh hard drive aktif saat pengguna tidak masuk, drive tersebut didekripsi setelah pengguna masuk. Kerentanan ini diperparah oleh temuan bahwa akses administrator, yang awalnya dianggap sebagai perlindungan, tidak diperlukan untuk mengakses data Recall. **James Forshaw, seorang peneliti di tim riset kerentanan Project Zero Google, menemukan metode untuk melewati persyaratan hak istimewa administrator dengan mengeksploitasi kelemahan dalam daftar kontrol akses Windows, yang mengatur izin untuk mengakses dan memodifikasi file dan folder.**

### **Mengeksploitasi Recall dengan TotalRecall**

Meningkatkan kekhawatiran ini, Alex Hagenah, seorang *ethical hacker*, mengembangkan alat bernama **TotalRecall yang secara efektif menunjukkan betapa mudahnya mengeksploitasi kerentanan Recall**. Alat ini dapat mengekstrak riwayat lengkap yang direkam oleh Recall dari mesin target, termasuk tangkapan layar dan data interaksi pengguna, yang semuanya disimpan tanpa enkripsi. Hagenah menekankan kesederhanaan proses ekstraksi ini, dengan menyatakan bahwa *“* ***There is no rocket science behind all this****”*.

### **Implikasi yang Mengkhawatirkan untuk Privasi dan Keamanan**

**Para ahli khawatir bahwa aktor jahat, termasuk peretas dan bahkan pelaku kekerasan dalam rumah tangga, dapat memanfaatkan kerentanan Recall untuk mencuri informasi sensitif.** Karena Recall menyimpan riwayat aktivitas pengguna yang komprehensif, database-nya dapat berisi berbagai macam data pribadi, mulai dari pesan dan email hingga informasi kesehatan dan situs web yang dikunjungi. Malware seperti virus pencuri info juga dapat dirancang untuk mengeksploitasi kelemahan ini, secara diam-diam mengekstrak data sensitif dari mesin yang terinfeksi tanpa sepengetahuan pengguna.

### **Tanggapan Microsoft dan Ketidakpastian yang Akan Datang**

Meskipun peneliti keamanan telah memberi tahu Microsoft tentang potensi masalah ini, tetap tidak jelas bagaimana, atau apakah, perusahaan berencana untuk mengatasinya sebelum peluncuran resmi Recall. Meskipun terdapat opsi untuk menonaktifkan Recall dalam pengaturan Windows, **fitur ini diaktifkan secara default pada PC Copilot+**. Kurangnya tindakan nyata dari Microsoft, dikombinasikan dengan risiko keamanan dan privasi yang melekat pada Recall, menimbulkan pertanyaan serius tentang apakah manfaat fitur ini lebih besar daripada potensi kerugiannya.

Hingga Microsoft mengatasi masalah ini secara memadai, pengguna tetap rentan, dan banyak yang menyerukan agar perusahaan mempertimbangkan kembali peluncuran Recall sepenuhnya.
