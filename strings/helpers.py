HELP_1 = """✅ **<u>Perintah Admin :</u>**

**Hanya Admin**.

/pin [loud or notify] - Menyematkan pesan senyap atau beritahu anggota.
/antich [on or off] - Mode anti Channel.
/ban - Blokir pengguna.
/unban - Buka blokir pengguna.
/sban - Blokir pengguna secara diam-diam.
/mute [username/balas pesan] - Bisukan pengguna.
/unmute [username/balas pesan] - Batal bisukan pengguna.
/all [Isi pesan] - Tandai semua anggota
/cancel - Berhenti menandai anggota
/warn - Memperingati pengguna
/dwarn - Memperingati pengguna dan menghapus pesan
/restart - Mulai ulang Bot untuk grup Anda.
/filter "kata kunci" [Isi pesan balasan] - Tambahkan filter ke obrolan dan Bot akan membalas pesan setiap kata kunci disebutkan.
/stop "kata kunci" - Menghapus kata kunci tertentu.
/removeallfilters - Menghapus semua kata kunci.
/filters - Mendapatkan kata kunci yang ditambahkan ke grup.
/welcome on/off - Hidupkan atau matikan Pesan sambutan.
/setwelcome [Pesan] - Mengatur pesan sambutan anggota masuk.
/setgoodbye [Pesan] - Mengatur pesan perpisahan anggota keluar.
/welcomehelp - Dapatkan format lengkap untuk setwelcome dan setgoodbye.
/auth [Username] - Tambahkan pengguna ke daftar AUTH grup.
/unauth [Username] - Hapus pengguna dari daftar AUTH grup.
/authusers - Periksa daftar AUTH grup."""





HELP_2 = """✅ <u>**Perintah Streaming :**</u>
Perintah yang tersedia = play , vplay , cplay
Perintah ForcePlay = playforce , vplayforce , cplayforce
/play or /vplay or /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.
/playforce or /vplayforce or /cplayforce -  **Force Play** menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrean.
/channelplay [Chat username or id] or [Disable] - Hubungkan channel ke grup dan streaming musik di obrolan suara channel dari grup Anda.
/channelplay linked - Menghubungkan ke Channel yang terhubung ke Grup. Sama seperti perintah diatas.
/playlist  - Periksa Daftar Putar tersimpan Anda di server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda.
/play  - Mulai mainkan Daftar Putar tersimpan Anda dari Server.
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
/loop or /cloop [enable/disable] or [Angka antara 1-10] : Bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara."""

HELP_3 = """✅ <u>**Perintah Bot :**</u>

/admins - Daftar admin atau staf Grup.
/id - Dapatkan ID Grup [balas ke pengguna untuk mendapatkan ID pengguna].
info - Dapatkan informasi tentang pengguna.
/sg - Dapatkan riwayat nama pengguna.
/tl "kode bahasa" - Menerjemahkan kalimat [/tl id Hello guys] atau balas ke pengguna.
/stats - Dapatkan 10 Trek Teratas.
/sudolist - Periksa Pengguna Sudo.
/lyrics [Nama Lagu] - Mencari Lirik untuk lagu tertentu di web.
/song [Nama Trek] or [YT Link] - Unduh apa pun dari youtube dalam format mp3 atau mp4.
/player - Dapatkan Panel Mainkan interaktif.
**c** singkatan dari pemutaran di Channel.
/queue or /cqueue - Periksa Daftar Antrian Streaming."""


HELP_4 = """✅ <u>**Perintah Ekstra :**</u>
/start - Memulai Bot.
/help  - Dapatkan Menu  Perintah dengan penjelasan rinci tentang perintah.
/setting - Dapatkan pengaturan grup lengkap dengan tombol sebaris.
/ping - Ping Bot dan periksa statistik Ram, Cpu, dll dari Bot.
/quote - Mendapatkan kutipan secara acak.
/image "kata kunci" - Cari gambar di google.
/tgm - Balas ke media untuk dapatkan link Telegraph.
/tgt - Balas ke teks untuk dapatkan link Telegraph.
/json - Dapatkan info detail pengguna.
/report, @admin - Balas pesan untuk melaporkan ke Admin
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
