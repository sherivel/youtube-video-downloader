import os
import tkinter as tk
from tkinter import messagebox, ttk
import yt_dlp

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please paste a YouTube URL first!")
        return

    status_label.config(text="📥 Downloading... Please wait...", foreground="#09cdc7")
    root.update()

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    ydl_opts = {
        'outtmpl': os.path.join(desktop, '%(title)s.%(ext)s'),
        'format': 'bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]',

    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="✅ Download Complete! Saved to Desktop.", foreground="#4ade80")
        messagebox.showinfo("Success", "Your video has been downloaded to your Desktop!")
    except Exception as e:
        status_label.config(text="❌ Download Failed!", foreground="#cf0000")
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

#GUI
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x250")
root.configure(bg="#0f172a")

style = ttk.Style()
style.configure("TLabel", background="#000000", foreground="#ffffff", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10, "bold"))

title_label = ttk.Label(root, text="🎥 YouTube Video Downloader", font=("Segoe UI", 20, "bold"), foreground="#cf6400")
title_label.pack(pady=20)

instruction_label = ttk.Label(root, text="Paste YouTube Link Below:", foreground="#000000")
instruction_label.pack(pady=5)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = ttk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=15)

status_label = ttk.Label(root, text="", font=("Segoe UI", 10, "italic"))
status_label.pack(pady=5)

#Application Loop
root.mainloop()