HELP_1 = """👨‍⚖️ **<u>Perintah Admin :</u>**

1️⃣ **Perintah Dasar**

/pin [loud or notify] - Menyematkan pesan senyap atau beritahu anggota.
/antich [on or off] - Mode anti Channel.
/ban - Blokir pengguna.
/unban - Buka blokir pengguna.
/sban - Blokir pengguna secara diam-diam.
/mute [username/balas pesan] - Bisukan pengguna.
/unmute [username/balas pesan] - Batal bisukan pengguna.
/cancel - Berhenti menandai anggota
/warn - Memperingati pengguna
/dwarn - Memperingati pengguna dan menghapus pesan
/restart - Mulai ulang Bot untuk grup Anda.

2️⃣ **Modul Filter**

/filter "kata kunci" [Isi pesan balasan] - Tambahkan filter ke obrolan dan Bot akan membalas pesan setiap kata kunci disebutkan.
/stop "kata kunci" - Menghapus kata kunci tertentu.
/removeallfilters - Menghapus semua kata kunci.
/filters - Mendapatkan kata kunci yang ditambahkan ke grup.

3️⃣ **Setwelcome**

/welcome on/off - Hidupkan atau matikan Pesan sambutan.
/setwelcome [Pesan] - Mengatur pesan sambutan anggota masuk.
/setgoodbye [Pesan] - Mengatur pesan perpisahan anggota keluar.
/welcomehelp - Dapatkan format lengkap untuk setwelcome dan setgoodbye."""

HELP_2 = """⚡ <u>**Perintah Streaming :**</u>

1️⃣ Play (audio) , vplay (video) , cplay, cvplay (channel)

/play or /vplay or /cplay (kata kunci) - Bot akan mulai memainkan kata kunci yang Anda berikan di obrolan suara atau streaming tautan langsung di obrolan suara.

/channelplay linked - Hubungkan channel ke grup dan streaming di obrolan suara channel dari grup Anda.

2️⃣ Daftar Putar

/playlist  - Periksa Daftar Putar tersimpan Anda di server.
/deleteplaylist - Hapus semua yang disimpan di daftar putar Anda.
/play - Mulai mainkan Daftar Putar tersimpan Anda dari Server.
/queue or /cqueue - Periksa Daftar Antrian Streaming.

3️⃣ Admin dan Pengguna Auth

/pause or /cpause - Jeda streaming yang diputar.
/resume or /cresume - Lanjutkan streaming yang dijeda.
/mute or /cmute - Bisukan musik yang diputar.
/unmute or /cunmute - Suarakan musik yang dibisukan.
/skip or /cskip - Lewati musik yang sedang diputar.
/stop or /cstop - Hentikan pemutaran musik.
/shuffle or /cshuffle - Secara acak mengacak daftar putar yang antri.
/seek or /cseek - Teruskan mencari musik sesuai durasi.
/seekback or /cseekback - Kembali mencari musik sesuai durasi.
/skip or /cskip [Nomor (contoh : 3)] : Melewati musik ke nomor antrian yang ditentukan.

4️⃣ Loop

/loop or /cloop [Angka antara 1-10] : Bot mengulagi lagu yang sedang diputar menjadi 1-10 kali pada obrolan suara. contoh : '/loop 3' bot akan mengulang lagu sebanyak 3 kali"""

HELP_3 = """🤖 <u>**Perintah Bot :**</u>

1️⃣ Informasi

/info - Dapatkan informasi tentang pengguna.
/admins - Daftar admin atau Staf Grup.
/report - Laporkan ke Admin
/id - Dapatkan ID Grup [balas ke pengguna untuk mendapatkan ID pengguna].
/sg - Dapatkan riwayat nama pengguna.
/ping - Ping Bot dan periksa statistik Ram, Cpu, dll dari Bot.
/stats - Dapatkan statistik Bot.
/speedtest - periksa kecepatan Bot di server.
/sudolist - Periksa Pengguna Sudo.

2️⃣ Tools

/all 'pesan' atau 'balas pesan' - Menandai semua Anggota Grup.
/tl 'kode bahasa' - Menerjemahkan kalimat contoh : '/tl id Hello guys' atau 'balas pesan'.

3️⃣ Download

/lyrics [Nama Lagu] - Mencari Lirik untuk lagu tertentu di web.
/song [Nama Trek] or [YT Link] - Unduh apa pun dari youtube dalam format mp3 atau mp4.
/player - Dapatkan Panel Mainkan interaktif."""

HELP_4 = """🗒 <u>**Perintah Ekstra :**</u>

/start - Memulai Bot.
/help  - Dapatkan Menu  Perintah dengan penjelasan rinci tentang perintah.
/setting - Dapatkan pengaturan grup lengkap dengan tombol sebaris.
/quote - Mendapatkan kutipan secara acak.
/image "kata kunci" - Cari gambar di google.
/tgm - Balas ke media untuk dapatkan link Telegraph.
/tgt - Balas ke teks untuk dapatkan link Telegraph.
/json - Dapatkan info detail pengguna.
/logo [teks/nama] - Membuat logo secara acak
/wlogo [teks/nama] - Membuat logo keren
/edit [balas ke media] - Edit foto"""


HELP_5 = """🔰 **<u>Tambah & Hapus Pengguna Sudo :</u>**
/addsudo [Nama Pengguna atau Balas ke Pengguna]
/delsudo [Nama Pengguna atau Balas ke Pengguna]

🛃 **<u>Heroku :</u>**
/usage - Penggunaan Dynos.

🌐 **<u>Config Vars :</u>**
/get_var - Dapatkan var konfigurasi dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Nama Var] [Value] - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Value dengan spasi.

🤖 **<u>Perintah Bot :</u>**
/reboot - Nyalakan ulang Bot. 
/update - Perbarui Bot.
/speedtest - Periksa kecepatan server
/maintenance [enable / disable] 
/logger [enable / disable] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Number of Lines] - Dapatkan log bot Anda dari heroku atau vps. Bisa untuk keduanya.
/autoend [enable|disable] - Aktifkan Auto end setelah 3 menit jika tidak ada yang mendengarkan.

📈 **<u>Perintah Statistik :</u>**
/activevoice - Periksa obrolan suara aktif di Bot.
/activevideo - Periksa panggilan video aktif di Bot.
/stats - Periksa Statistik Bot.

⚠️ **<u>Perintah Blacklist :</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan Grup.
/whitelistchat [CHAT_ID] - Mengubah daftar hitam ke daftar putih obrolan grup
/blacklistedchat - Check all blacklisted chats.

👤 **<u>Perintah Blokir :</u>**
/block [Username atau Balas ke Pengguna] - Mencegah pengguna menggunakan perintah Bot.
/unblock [Username atau Balas ke Pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

👤 **<u>Global Ban :</u>**
/gban [Username atau Balas ke Pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan Bot.
/ungban [Username atau Balas ke Pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan Bot.
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥 **<u>Fungsi Videocall :</u>**
/set_video_limit [Number atau Chats] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode download diaktifkan, Bot akan mengunduh video. Bot Secara default ke M3u8. Anda dapat menggunakan mode unduhan ketika kueri apa pun tidak diputar dalam mode m3u8.

⚡️ **<u>Perintah Bot Pribadi :</u>**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan Bot.
/unauthorize [CHAT_ID] - Larang obrolan menggunakan Bot.
/authorized - Periksa semua obrolan Bot yang dizinkan.

🌐 **<u>Perintah Penyiaran:</u>**
/broadcast [Message atau balas ke pesan] - Siarkan pesan apa pun ke Grup yang Dilayani Bot.

<u>options for broadcast :</u>
**-pin** : Menyematkan pesan Anda
**-pinloud** : Menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Menyiarkan pesan Anda ke pengguna yang telah memulai Bot.
**-assistant** : Menyiarkan pesan Anda dari akun asisten Bot.
**-nobot** : Memaksa Bot untuk tidak menyiarkan pesan.

**Contoh :** `/broadcast -user -assistant -pin Hello guys`

"""
