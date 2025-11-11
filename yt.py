import yt_dlp
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress

def main():
    console = Console()
    console.print("\n[bold blue]🚀 Aplikasi YouTube Downloader CLI[/bold blue]")
    
    # 1. Akses URL
    video_url = Prompt.ask("Masukkan URL Video YouTube")
    
    try:
        # 2. Parsing/Ekstraksi Info menggunakan yt-dlp
        ydl_opts = {'quiet': True, 'format': 'bestvideo+bestaudio/best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])
            video_title = info_dict.get('title', 'video')

        # Siapkan Pilihan
        download_options = {}
        option_id = 1

        # A. Format Video (Gabungan Terbaik / Resolusi Tinggi)
        # yt-dlp secara otomatis akan memilih format terbaik dan menggabungkannya jika FFmpeg tersedia
        download_options[option_id] = {'type': 'Video', 'description': 'Video Terbaik (Resolusi Tertinggi, Otomatis Gabung Audio+Video)', 'format': 'bestvideo+bestaudio/best'}
        option_id += 1
        
        # B. Format Audio (Opsi Konversi ke MP3)
        # Pilihan untuk mengunduh audio terbaik dan konversi ke MP3/M4A
        download_options[option_id] = {'type': 'Audio', 'description': 'Audio MP3 Terbaik', 'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}
        option_id += 1
        
        # C. Contoh Pilihan Format Khusus (Misalnya 720p progresif, cepat)
        # Cari format progresif (video dan audio tergabung) hingga 720p
        for f in formats:
            if f.get('ext') == 'mp4' and f.get('height') == 720 and f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                download_options[option_id] = {'type': 'Video', 'description': 'Video MP4 (720p Progresif, Cepat)', 'format': f['format_id']}
                option_id += 1
                break

        # 3. Menu Pilihan Interaktif menggunakan rich.table
        table = Table(title=f"Pilih Format untuk: [bold yellow]{video_title}[/bold yellow]", style="magenta", header_style="bold cyan")
        table.add_column("ID", style="dim", width=4)
        table.add_column("Tipe Konten", style="green")
        table.add_column("Deskripsi Format", style="white")

        for key, val in download_options.items():
            table.add_row(str(key), val['type'], val['description'])

        console.print(table)
        
        # 4. Menerima Input Pilihan
        choice_id = Prompt.ask("Masukkan ID Pilihan Anda", choices=[str(i) for i in download_options.keys()])
        selected_option = download_options[int(choice_id)]

        # 5. Path Penyimpanan
        download_path = Prompt.ask("Masukkan Path Penyimpanan (Kosongkan untuk direktori saat ini)", default=os.getcwd())
        
        # 6. Memulai Unduhan
        console.print(f"\n[bold green]⬇️ Memulai Unduhan...[/bold green] (Menggunakan yt-dlp dan FFmpeg jika diperlukan)")

        # Konfigurasi yt-dlp untuk unduhan
        dl_opts = {
            'format': selected_option['format'],
            'outtmpl': os.path.join(download_path, f'{video_title}.%(ext)s'),
            'merge_output_format': 'mp4', # Format untuk hasil gabungan
            'noplaylist': True,
            # Handler untuk menampilkan progress bar
            'progress_hooks': [lambda d: progress_hook(d, console)], 
            'postprocessors': selected_option.get('postprocessors', []),
            # Menjamin FFmpeg digunakan untuk muxing/audio extraction
            'external_downloader': 'ffmpeg',
            'external_downloader_args': ['-loglevel', 'error']
        }

        with yt_dlp.YoutubeDL(dl_opts) as ydl:
            ydl.download([video_url])
        
        console.print("\n[bold green]✅ Unduhan Selesai![/bold green]")
        console.print(f"File tersimpan di: [bold yellow]{download_path}[/bold yellow]")


    except yt_dlp.utils.DownloadError as e:
        console.print(f"\n[bold red]❌ Terjadi Kesalahan Download:[/bold red] {e}")
    except Exception as e:
        console.print(f"\n[bold red]❌ Terjadi Kesalahan Umum:[/bold red] {e}")

# Fungsi Progress Hook untuk yt-dlp dan rich
def progress_hook(d, console):
    if d['status'] == 'downloading':
        # yt-dlp secara default sudah cukup baik dalam menampilkan progress
        pass

if __name__ == "__main__":
    main()