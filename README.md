# 🔽 YouTube CLI Downloader 💻

Aplikasi *YouTube CLI Downloader* adalah aplikasi berbasis *Command Line Interface* (CLI) yang berfungsi untuk mengunduh konten YouTube. Aplikasi ini memungkinkan pengguna untuk memilih antara mengunduh **video** atau **audio**, menentukan **resolusi**, dan memilih **path penyimpanan** file, sehingga cara kerjanya mirip dengan aplikasi *downloader* populer.

Proyek ini bertujuan untuk menyediakan *tool* pengunduhan yang **cepat dan efisien** melalui terminal.

## ✨ Fitur Utama

  * ✅ **Pilihan Konten Fleksibel:** Pengguna dapat memilih untuk mengunduh konten sebagai **Video** (MP4/WebM) atau hanya **Audio** (MP3/M4A).
  * ⚙️ **Kualitas Tertinggi:** Mendukung pengunduhan resolusi **4K, 1080p, dan 720p**. Untuk resolusi tinggi, sistem akan secara otomatis menggabungkan (*muxing*) *stream* video dan audio terpisah.
  * 🧭 **Antarmuka Interaktif:** Menu pilihan resolusi dan format disajikan secara terstruktur dan interaktif menggunakan *library* **`rich`**.
  * ⏳ **Indikator Kemajuan *Real-time***: Menampilkan *progress bar* yang responsif saat pengunduhan berjalan, memberikan *feedback* langsung kepada pengguna.
  * 📂 **Kustomisasi *Path* Penyimpanan:** Pengguna dapat menentukan folder tujuan penyimpanan file yang diunduh.

## 🛠️ Persyaratan Sistem

Aplikasi ini bergantung pada **Python** dan *tool* pihak ketiga untuk operasi penggabungan (*muxing*) dan konversi audio (*extraction*).

| Persyaratan | Deskripsi |
| :--- | :--- |
| **Python** | Versi **3.6** atau yang lebih baru. |
| **Git** | Diperlukan untuk *cloning* repositori (opsional, jika tidak mengunduh ZIP). |
| **FFmpeg** | **Wajib** untuk pengunduhan video di atas 720p dan konversi ke MP3. Harus terinstal dan berada di **PATH** sistem. |

### Instalasi FFmpeg (Wajib)

FFmpeg digunakan oleh `yt-dlp` untuk menggabungkan *stream* video dan audio terpisah, serta mengkonversi audio.

| Sistem Operasi | Perintah Instalasi (Disarankan) |
| :--- | :--- |
| **Linux (Debian/Ubuntu)** | `sudo apt update && sudo apt install ffmpeg` |
| **macOS** | `brew install ffmpeg` (Membutuhkan [Homebrew](https://brew.sh/)) |
| **Windows** | Unduh dan ekstrak dari [situs resmi FFmpeg](https://ffmpeg.org/download.html), lalu tambahkan folder `/bin` ke **Variabel Lingkungan PATH** Anda. |

-----

## 🚀 Instalasi dan Penggunaan

### Langkah 1: *Clone* Repositori

Buka terminal dan *clone* repositori ini:

```bash
git clone https://github.com/NamaUserAnda/youtube-cli-downloader.git
cd youtube-cli-downloader
```

### Langkah 2: Instalasi Library Python

Instal *library* yang diperlukan (`yt-dlp` dan `rich`) menggunakan `pip`:

```bash
pip install yt-dlp rich
```

### Langkah 3: Menjalankan Aplikasi

Jalankan *script* utama di terminal:

```bash
python yt_downloader.py
```

### Alur Kerja

Aplikasi akan memandu Anda secara otomatis:

1.  **Input URL:** Masukkan *link* video YouTube.
2.  **Pilih ID:** Pilih ID format yang diinginkan dari tabel yang muncul (misalnya: *Video Terbaik* atau *Audio MP3*).
3.  **Path Penyimpanan:** Tentukan folder penyimpanan file.
4.  **Download:** Proses unduhan akan dimulai dengan *progress bar* yang informatif.

-----

## 🛑 Penanganan Error

Jika Anda mengalami masalah, terutama pada resolusi tinggi atau konversi MP3, pesan *error* biasanya mengindikasikan bahwa **FFmpeg tidak ditemukan** di sistem Anda. Pastikan instalasi dan konfigurasi **PATH** untuk FFmpeg sudah benar.
