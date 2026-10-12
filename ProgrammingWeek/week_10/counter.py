import tkinter as tk

# --- ฟังก์ชันคำนวณ ---
def count_char():
    t = e1.get()
    c = e2.get()
    
    if not t or not c:
        lbl.config(text="เตือน: กรุณากรอกข้อมูลให้ครบ")
        return
        
    num = t.count(c)
    lbl.config(text=f"ผลลัพธ์: '{c}' มี {num} ตัว")

def count_vow():
    t = e1.get()
    if not t:
        lbl.config(text="เตือน: กรุณากรอกข้อความก่อน")
        return
        
    vowels = "aeiouAEIOU"
    num = sum(1 for x in t if x in vowels)
    lbl.config(text=f"ผลลัพธ์: มีสระ {num} ตัว")

def check_palin():
    t = e1.get()
    if not t:
        lbl.config(text="เตือน: กรุณากรอกข้อความก่อน")
        return
        
    clean = t.replace(" ", "").lower()
    if clean == clean[::-1]:
        lbl.config(text="ผลลัพธ์: เป็น Palindrome ")
    else:
        lbl.config(text="ผลลัพธ์: ไม่ใช่ Palindrome")

# --- สร้างหน้าต่างหลัก ---
root = tk.Tk()
root.title("Text Analyzer")
root.geometry("400x300")

# --- ส่วนกรอกข้อมูล ---
f1 = tk.Frame(root)
f1.pack(pady=20)

tk.Label(f1, text="ข้อความหลัก:").grid(row=0, column=0, sticky="w", pady=5)
e1 = tk.Entry(f1, width=20)
e1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(f1, text="ตัวอักษรค้นหา:").grid(row=1, column=0, sticky="w", pady=5)
e2 = tk.Entry(f1, width=10)
e2.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# --- ส่วนปุ่มกด ---
f2 = tk.Frame(root)
f2.pack(pady=10)

tk.Button(f2, text="Count Char", command=count_char).pack(side="left", padx=3)
tk.Button(f2, text="Count Vowels", command=count_vow).pack(side="left", padx=3)
tk.Button(f2, text="Palindrome", command=check_palin).pack(side="left", padx=3)

# --- ส่วนแสดงผล ---
lbl = tk.Label(root, text="ผลลัพธ์จะแสดงตรงนี้", font=("Arial", 11))
lbl.pack(pady=20)

root.mainloop()