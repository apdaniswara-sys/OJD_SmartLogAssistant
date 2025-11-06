# OJD_SmartLogAssistant
**NLP + Voice + GUI System for Real-Time Stock Inquiry**

This project provides an intelligent chatbot that helps users check part information and stock levels interactively — through text or voice.  
It integrates **Natural Language Processing (NLP)**, **speech recognition**, and a **simple GUI (Tkinter)**.  

---

## ✨ Features

- 🔍 Query any part using its **Part No** (e.g. `stock 105D`)  
- 🧠 Smart NLP engine — responds only to what the user asks  
- 💬 Support for **text** and **voice** interaction  
- 🖥️ Simple, modern **GUI interface**  
- 🗃️ Reads data directly from local **CSV database** (or future API)

---

## 🗂️ Project Structure

```bash
OJD_SmartLogAssistant/
│
├── data/
│   └── master_parts.csv                  # Parts data (CSV)
│
├── src/
│   ├── config.py                  # Configuration (paths & API)
│   ├── chatbot.py                 # NLP logic + CSV lookup
│   ├── voice_utils.py             # Voice input/output functions
│   └── gui_app.py                 # Main GUI app (Tkinter)
│
├── requirements.txt
└── README.md
```
