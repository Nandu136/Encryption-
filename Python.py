import tkinter as tk
from tkinter import messagebox

PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "cdefghijklmnopqrstuvwxyzab"  

def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch in PLAIN:
            index = PLAIN.index(ch)
            result += CIPHER[index]
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text.lower():
        if ch in CIPHER:
            index = CIPHER.index(ch)
            result += PLAIN[index]
        else:
            result += ch
    return result

# GUI Application
def create_app():
    def on_encrypt():
        text = input_text.get("1.0", tk.END).strip()
        if text:
            result = encrypt(text)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)
        else:
            messagebox.showwarning("Warning", "Please enter text to encrypt.")

    def on_decrypt():
        text = input_text.get("1.0", tk.END).strip()
        if text:
            result = decrypt(text)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)
        else:
            messagebox.showwarning("Warning", "Please enter text to decrypt.")

    app = tk.Tk()
    app.title("Encryption-Decryption Tool")
    app.geometry("400x300")
    app.resizable(False, False)

    tk.Label(app, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
    input_text = tk.Text(app, height=4, width=40)
    input_text.pack(pady=5)

    button_frame = tk.Frame(app)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Encrypt", command=on_encrypt, width=15, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Decrypt", command=on_decrypt, width=15, bg="#2196F3", fg="white").pack(side=tk.RIGHT, padx=10)

    tk.Label(app, text="Result:", font=("Arial", 12)).pack(pady=5)
    output_text = tk.Text(app, height=4, width=40)
    output_text.pack(pady=5)

    app.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_app()
