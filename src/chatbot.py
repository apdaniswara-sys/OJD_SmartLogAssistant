import pandas as pd
from src.config import DATA_PATH

# Load data once
df = pd.read_csv(DATA_PATH)

def get_part_info(part_no):
    """Return dict of part info by part number"""
    row = df.loc[df["Part No"].astype(str).str.lower() == str(part_no).lower()]
    if row.empty:
        return None
    return row.iloc[0].to_dict()

def respond_to_query(query):
    """Analyze query and return smart response"""
    words = query.lower().split()

    # Cari part number (kode unik)
    for w in words:
        if df["Part No"].astype(str).str.lower().eq(w).any():
            part_no = w.upper()
            part = get_part_info(part_no)
            if not part:
                return "❌ Sorry, that part number is not found."

            # Analisa konteks pertanyaan
            if "stock" in query or "available" in query:
                return f"📦 Stock for {part_no} is {part['Stock Available']} pcs."
            elif "supplier" in query:
                return f"🏢 Supplier for {part_no} is {part['Supplier Name']}."
            elif "line" in query:
                return f"📍 Line address for {part_no} is {part['Line Address']}."
            elif "qty" in query or "box" in query:
                return f"📦 Each box of {part_no} contains {part['Qty/Box']} units."
            elif "all" in query or "info" in query:
                return (
                    f"📋 Part Info for {part_no}\n"
                    f"1. Part Name     : {part['Part Name']}\n"
                    f"2. Part No       : {part['Part No']}\n"
                    f"3. Supplier Name : {part['Supplier Name']}\n"
                    f"4. Qty/Box       : {part['Qty/Box']}\n"
                    f"5. Line Address  : {part['Line Address']}\n"
                    f"6. Stock Avail.  : {part['Stock Available']} pcs"
                )
            else:
                return f"🔍 What do you want to know about part {part_no}? (stock, supplier, qty, etc.)"

    return "🤔 Please specify the part number (e.g., 'stock 105D')."
