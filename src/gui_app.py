# 🧠 OJD Stock Chatbot — GUI Interface
import tkinter as tk
from tkinter import scrolledtext
import threading
import time
from src.chatbot import respond_to_query
from src.voice_utils import listen, speak


def insert_message(role, message):
    """Tampilkan pesan di chatbox dengan gaya berbeda."""
    chat_box.insert(tk.END, f"{role}: {message}\n\n", role)
    chat_box.see(tk.END)


def send_message():
    """Kirim pesan dari input teks."""
    query = user_input.get().strip()
    if not query:
        return

    insert_message("user", query)
    user_input.delete(0, tk.END)

    response = respond_to_query(query)
    insert_message("bot", response)


def voice_input():
    """Mode input suara (dijalankan di thread agar GUI tidak freeze)."""
    def process_voice():
        insert_message("system", "🎙️ Mendengarkan...")
        query = listen()

        insert_message("user", query)
        response = respond_to_query(query)
        time.sleep(0.3)  # jeda natural
        insert_message("bot", response)

        threading.Thread(target=lambda: speak(response), daemon=True).start()

    threading.Thread(target=process_voice, daemon=True).start()


# --- GUI Setup ---
root = tk.Tk()
root.title("📦 OJD Stock Chatbot")
root.geometry("520x630")
root.config(bg="#f7f7f7")

tk.Label(
    root,
    text="🤖 OJD Stock Chatbot (Text + Voice)",
    font=("Segoe UI", 14, "bold"),
    bg="#f7f7f7",
    fg="#333"
).pack(pady=10)

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=58, height=25, bg="white", fg="#222", font=("Consolas", 10))
chat_box.tag_config("user", foreground="#1976D2", font=("Segoe UI", 10, "bold"))
chat_box.tag_config("bot", foreground="#388E3C", font=("Segoe UI", 10))
chat_box.tag_config("system", foreground="#999999", font=("Segoe UI", 9, "italic"))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root, bg="#f7f7f7")
frame.pack(pady=5)

user_input = tk.Entry(frame, width=40, font=("Segoe UI", 10))
user_input.grid(row=0, column=0, padx=5, ipady=4)

send_btn = tk.Button(frame, text="💬 Send", command=send_message, bg="#4CAF50", fg="white", font=("Segoe UI", 9, "bold"))
send_btn.grid(row=0, column=1, padx=5)

voice_btn = tk.Button(frame, text="🎙️ Voice", command=voice_input, bg="#2196F3", fg="white", font=("Segoe UI", 9, "bold"))
voice_btn.grid(row=0, column=2)

chat_box.insert(tk.END, "👋 Halo! Saya siap membantu kamu cek informasi part dan stok.\n\n", "bot")

root.mainloop()
