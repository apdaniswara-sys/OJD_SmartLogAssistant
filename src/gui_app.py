import tkinter as tk
from tkinter import scrolledtext
from src.chatbot import respond_to_query
from src.voice_utils import listen, speak

def send_message():
    query = user_input.get()
    if not query.strip():
        return
    chat_box.insert(tk.END, f"You: {query}\n", "user")
    response = respond_to_query(query)
    chat_box.insert(tk.END, f"Bot: {response}\n\n", "bot")
    user_input.delete(0, tk.END)

def voice_input():
    query = listen()
    chat_box.insert(tk.END, f"You (voice): {query}\n", "user")
    response = respond_to_query(query)
    chat_box.insert(tk.END, f"Bot: {response}\n\n", "bot")
    speak(response)

root = tk.Tk()
root.title("📦 OJD Stock Chatbot")
root.geometry("500x600")
root.config(bg="#f2f2f2")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=58, height=25, bg="white", fg="black")
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")
chat_box.pack(padx=10, pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

user_input = tk.Entry(frame, width=40)
user_input.grid(row=0, column=0, padx=5)

send_btn = tk.Button(frame, text="Send", command=send_message, bg="#4CAF50", fg="white")
send_btn.grid(row=0, column=1)

voice_btn = tk.Button(frame, text="🎙️ Voice", command=voice_input, bg="#2196F3", fg="white")
voice_btn.grid(row=0, column=2)

root.mainloop()
