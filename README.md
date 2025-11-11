🔽 YouTube CLI Downloader
Aplikasi berbasis Command Line Interface (CLI) untuk mengunduh konten YouTube (Video atau Audio) dengan pilihan resolusi dan path penyimpanan, mirip dengan fungsionalitas aplikasi seperti VidMate, namun efisien dan cepat berkat library yt-dlp.

✨ Fitur Utama
Pilihan Konten Fleksibel: Unduh sebagai Video (MP4) atau Audio (MP3/M4A).

Kualitas Terbaik: Mendukung pengunduhan resolusi tertinggi (1080p, 4K) dengan penggabungan otomatis stream audio dan video.

Antarmuka Bersih: Menggunakan library rich untuk tampilan menu yang interaktif dan mudah dibaca di terminal.

Indikator Kemajuan Real-time: Menampilkan progress bar saat proses pengunduhan berjalan.

Kustomisasi Path: Memungkinkan user menentukan folder penyimpanan file.

🛠️ Persyaratan Sistem
Aplikasi ini dibangun menggunakan Python dan bergantung pada tool pihak ketiga untuk operasi penggabungan (muxing) dan konversi audio (extraction).

1. Python 3
Pastikan Anda telah menginstal Python 3.6 atau versi yang lebih baru. Anda dapat memeriksanya di terminal:

Bash

python --version
# atau
python3 --version
2. FFmpeg (Wajib untuk Kualitas Tinggi)
FFmpeg adalah tool penting yang digunakan oleh yt-dlp untuk:

Menggabungkan stream video resolusi tinggi (misalnya 1080p ke atas) dan stream audio terpisah menjadi satu file MP4/WebM.

Mengkonversi stream audio terbaik menjadi format seperti MP3.

Cara Instalasi FFmpeg:

Sistem Operasi	Perintah Instalasi (Disarankan)
Linux (Debian/Ubuntu)	sudo apt update && sudo apt install ffmpeg
macOS	brew install ffmpeg (Membutuhkan Homebrew)
Windows	Unduh langsung dari situs resmi FFmpeg, ekstrak, dan pastikan folder /bin ditambahkan ke Variabel Lingkungan PATH Anda.
Pastikan Anda dapat menjalankan perintah ffmpeg -version di terminal setelah instalasi.

🚀 Instalasi dan Penggunaan
Langkah 1: Instalasi Library Python
Setelah Python 3 dan FFmpeg terinstal, instal library Python yang diperlukan (yt-dlp dan rich):

Bash

pip install yt-dlp rich
Langkah 2: Menjalankan Aplikasi
Asumsikan Anda telah menyimpan kode program di file bernama yt_downloader.py.

Jalankan aplikasi melalui terminal:

Bash

python yt_downloader.py
Langkah 3: Alur Kerja Aplikasi
Aplikasi akan memandu Anda melalui langkah-langkah berikut:

Masukkan URL: Anda akan diminta memasukkan URL video YouTube.

Pilih Format: Aplikasi akan menampilkan menu yang berisi opsi Video Terbaik (Resolusi Tinggi), Audio MP3, atau format spesifik lainnya. Masukkan ID pilihan Anda.

Tentukan Path: Masukkan path folder tempat Anda ingin menyimpan file (kosongkan untuk menyimpan di folder saat ini).

Proses Download: Aplikasi akan memulai pengunduhan dan menampilkan progress bar hingga selesai.

⚠️ Catatan Penting
Jika Anda memilih resolusi tinggi (misalnya, Video Terbaik), proses akan mencakup pengunduhan dua stream terpisah dan proses penggabungan (muxing) oleh FFmpeg. Proses ini mungkin memakan waktu lebih lama daripada pengunduhan satu stream progresif 720p.

Jika FFmpeg tidak ditemukan di sistem Anda, pengunduhan resolusi 1080p ke atas dan konversi audio MP3 akan gagal. Pastikan instalasi FFmpeg sudah benar!
