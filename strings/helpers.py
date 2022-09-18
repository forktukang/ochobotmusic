HELP_1 = """👨‍⚖️ **<u>Perintah Admin :</u>**

1️⃣ **Perintah Dasar**

`/pin loud/notify` - Sematkan pesan senyap atau beritahu anggota.
`/antich on/off` - Mode anti Channel.
`/ban` - Blokir pengguna.
`/unban` - Buka blokir pengguna.
`/sban` - Blokir pengguna secara diam-diam.
`/mute username/reply` - Bisukan pengguna.
`/unmute username/reply` - Batal bisukan pengguna.
`/warn` - Peringati pengguna.
`/dwarn` - Peringati pengguna dan menghapus pesan.
`/restart` - Mulai ulang Bot untuk grup Anda.
`/connect ID/link` - Menghubungkan Bot ke Grup.

2️⃣ **Modul Filter**

`/filter` (kata kunci) (Isi pesan balasan) - Tambahkan filter ke obrolan dan Bot akan membalas pesan setiap kata kunci disebutkan.
`/stop` (kata kunci) - Menghapus kata kunci tertentu.
`/removeallfilters` - Menghapus semua kata kunci.
`/filters` - Mendapatkan kata kunci yang ditambahkan ke grup.

**Contoh :**

`/filter "owner"
Owner lagi tidur 😴. 
%%%
Hai ada yang bisa saya bantu? 
%%%
Owner akan segera mambalas pesan anda.`

3️⃣ **Setwelcome**

`/welcome on/off` - Hidupkan atau matikan Pesan sambutan.
`/setwelcome` (Pesan) - Atur pesan sambutan anggota masuk.
`/setgoodbye` (Pesan) - Atur pesan perpisahan anggota keluar.
`/welcomehelp` - Dapatkan format lengkap untuk setwelcome dan setgoodbye.
**Contoh :** `/setwelcome Hai selamat bergabung di Grup ini.`

4️⃣ ** Force Subscribe

`/fsub` (channel username) - Paksa anggota Grup berlangganan ke Channel.
`/fsub disable` - Menghentikan Force Subscibe.
`/fsub clear` - Membatalkan bisu untuk semua anggota yang dibisukan."""

HELP_2 = """⚡ <u>**Perintah Streaming :**</u>

1️⃣ *c* Untuk streaming di Channel. *v* Untuk streaming video.

`/play` `/vplay` `/cplay` (query) - Bot akan mulai memainkan query yang Anda berikan di obrolan suara atau streaming tautan langsung di obrolan suara.

`/channelplay linked` - Sambungkan Grub ke Channel dan mulai streaming di obrolan suara channel dari grup Anda.

2️⃣ Daftar Putar

`/playlist`  - Periksa Daftar Putar tersimpan Anda di server.
`/deleteplaylist` - Hapus semua yang disimpan di daftar putar Anda.
`/play` - Mainkan Daftar Putar tersimpan Anda.
`/queue` or `/cqueue` - Periksa Daftar Antrian Streaming.

3️⃣ Admin dan Pengguna Auth

`/pause` or `/cpause` - Jeda streaming yang diputar.
`/resume` or `/cresume` - Lanjutkan streaming yang dijeda.
`/mute` or `/cmute` - Bisukan musik yang diputar.
`/unmute` or `/cunmute` - Suarakan musik yang dibisukan.
`/skip` or `/cskip` - Lompati musik yang sedang diputar.
`/stop` or `/cstop` - Hentikan pemutaran musik.
`/shuffle` or `/cshuffle` - Secara acak mengacak daftar putar yang antri.
`/seek` or `/cseek` - Teruskan mencari musik sesuai durasi.
`/seekback` or `/cseekback` - Kembali mencari musik sesuai durasi.
`/skip` or `/cskip` (nomor) - Lompat ke nomor antrian yang ditentukan.

4️⃣ Loop

`/loop` or `/cloop` (Angka 1-10) - contoh : `/loop 3`. Bot mengulagi trek yang sedang diputar menjadi 3 kali pada obrolan suara."""

HELP_3 = """🤖 <u>**Perintah Bot :**</u>

1️⃣ Informasi

`/info` - Dapatkan informasi tentang pengguna.
`/admins` - Daftar Admin atau Staf Grup.
`/report` - Laporkan ke Admin.
`/id` - Dapatkan ID Grup <balas ke pengguna untuk mendapatkan ID pengguna>.
`/sg` - Dapatkan riwayat nama pengguna.
`/ping` - Periksa statistik Ram, Cpu, dll dari Bot.
`/stats` - Dapatkan statistik Bot.
`/speedtest` - Periksa kecepatan Bot di server.
`/sudolist` - Periksa Pengguna Sudo.

2️⃣ Tools

`/all` (pesan atau balas pesan) - Menandai semua Anggota Grup.
`/cancel` - Berhenti menandai anggota Grup.
`/tl id` - Terjemahkan kalimat ke bahasa Indonesia.
`/tl en` - Terjemahkan kalimat ke bahasa Inggris.
`/tl kode bahasa` - Tejemahkan ke bahasa lainya.

3️⃣ Download

`/lyrics` (Nama Lagu) - Mencari Lirik untuk lagu tertentu di web.
`/song` (Nama Trek atau YT Link) - Unduh apa pun dari youtube dalam format mp3 atau mp4.
`/player` - Dapatkan Panel Mainkan interaktif."""

HELP_4 = """🗒 <u>**Perintah Ekstra :**</u>

`/start` - Memulai Bot.
`/help`  - Dapatkan Menu  Perintah dengan penjelasan rinci tentang perintah.
`/setting` - Dapatkan pengaturan grup lengkap dengan tombol sebaris.
`/quote` - Mendapatkan kutipan secara acak.
`/image` "kata kunci" - Cari gambar di google.
`/tgm` - Balas ke media untuk dapatkan link Telegraph.
`/tgt` - Balas ke teks untuk dapatkan link Telegraph.
`/json` - Dapatkan info detail pengguna.
`/logo` (teks/nama) - Membuat logo secara acak.
`/wlogo` (teks/nama) - Membuat logo keren.
`/edit` (balas ke media) - Edit foto"""


HELP_5 = """🔰 **<u>Tambah & Hapus Pengguna Sudo :</u>**
`/addsudo` <Nama Pengguna atau Balas ke Pengguna>
`/delsudo` <Nama Pengguna atau Balas ke Pengguna>

🛃 **<u>Heroku :</u>**
`/usage` - Penggunaan Dynos.

🌐 **<u>Config Vars :</u>**
`/get_var` - Dapatkan var konfigurasi dari Heroku atau .env.
`/del_var` - Hapus semua var di Heroku atau .env.
`/set_var` (Nama Var) (Value) - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Value dengan spasi.

🤖 **<u>Perintah Bot :</u>**
`/reboot` - Nyalakan ulang Bot. 
`/update` - Perbarui Bot.
`/speedtest` - Periksa kecepatan server.
`/maintenance enable/disable`
`/logger enable/disable` - Bot mencatat kueri yang dicari di grup logger.
`/get_log` (Number of Lines) - Dapatkan log bot Anda dari heroku atau vps. Bisa untuk keduanya.
`/autoend enable/disable` - Aktifkan Auto end setelah 3 menit jika tidak ada yang mendengarkan.

📈 **<u>Perintah Statistik :</u>**
`/activevoice` - Periksa obrolan suara aktif di Bot.
`/activevideo` - Periksa panggilan video aktif di Bot.
`/stats` - Periksa Statistik Bot.

⚠️ **<u>Perintah Blacklist :</u>**
`/blacklistchat` (CHAT_ID) - Daftar hitam obrolan Grup.
`/whitelistchat` (CHAT_ID) - Mengubah daftar hitam ke daftar putih obrolan Grup.
`/blacklistedchat` - Cek semua daftar hitam.

👤 **<u>Perintah Blokir :</u>**
`/block` (Username atau Balas ke Pengguna) - Mencegah pengguna menggunakan perintah Bot.
`/unblock` (Username atau Balas ke Pengguna) - Hapus pengguna dari Daftar Blokir Bot.
`/blockedusers` - Periksa Daftar Pengguna yang diblokir.

👤 **<u>Global Ban :</u>**
`/gban` (Username atau Balas ke Pengguna) - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan Bot.
`/ungban` (Username atau Balas ke Pengguna) - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan Bot.
`/gbannedusers` - Periksa Daftar Pengguna Gbanned.

🎥 **<u>Fungsi Videocall :</u>**
`/set_video_limit` (Number atau Chats) - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
`/videomode download/m3u8` - Jika mode download diaktifkan, Bot akan mengunduh video. Bot Secara default ke M3u8. Anda dapat menggunakan mode unduhan ketika kueri apa pun tidak diputar dalam mode m3u8.

⚡️ **<u>Perintah Bot Pribadi :</u>**
`/authorize` (CHAT_ID) - Izinkan obrolan untuk menggunakan Bot.
`/unauthorize` (CHAT_ID) - Larang obrolan menggunakan Bot.
`/authorized` - Periksa semua obrolan Bot yang dizinkan.

🌐 **<u>Perintah Penyiaran:</u>**
`/broadcast` (Message atau balas ke pesan) - Siarkan pesan apa pun ke Grup yang Dilayani Bot.

<u>options for broadcast :</u>
**-pin** : Menyematkan pesan Anda.
**-pinloud** : Menyematkan pesan Anda dengan pemberitahuan keras.
**-user** : Menyiarkan pesan Anda ke pengguna yang telah memulai Bot.
**-assistant** : Menyiarkan pesan Anda dari akun asisten Bot.
**-nobot** : Memaksa Bot untuk tidak menyiarkan pesan.

**Contoh :** `/broadcast -user -assistant -pin Hello guys`

"""
