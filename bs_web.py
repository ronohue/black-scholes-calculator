import customtkinter as ctk
import math
from scipy.stats import norm

def calculate():
    try:
        S = float(entry_S.get())
        K = float(entry_K.get())
        r = float(entry_r.get()) / 100
        V = float(entry_V.get()) / 100
        t = float(entry_t.get()) / 365
        V = V * math.sqrt(252/365)
        CorP = option_type.get()

        d1 = (math.log(S/K) + (r + (0.5 * V**2)) * t) / (V * math.sqrt(t))
        d2 = d1 - (V * math.sqrt(t))

        if CorP == "Call":
            price = S * norm.cdf(d1) - K * math.exp(-r * t) * norm.cdf(d2)
        else:
            price = K * math.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)

        result_label.configure(text=f"Option Price: {round(price, 2)}")
    except Exception as e:
        result_label.configure(text="Invalid input!")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Black-Scholes Option Pricing Calculator")
app.geometry("600x600")  # Bigger window

# Center the window
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry(f"{width}x{height}+{x}+{y}")

frame = ctk.CTkFrame(app, corner_radius=15, width=400, height=400)
frame.place(relx=0.5, rely=0.5, anchor="center")

entry_S = ctk.CTkEntry(frame, placeholder_text="Underlying Price (S)", font=("Times New Roman", 18), width=350)
entry_K = ctk.CTkEntry(frame, placeholder_text="Strike Price (K)", font=("Times New Roman", 18), width=350)
entry_r = ctk.CTkEntry(frame, placeholder_text="Risk-Free Rate (%)", font=("Times New Roman", 18), width=350)
entry_V = ctk.CTkEntry(frame, placeholder_text="Volatility (%)", font=("Times New Roman", 18), width=350)
entry_t = ctk.CTkEntry(frame, placeholder_text="Days to Expiry", font=("Times New Roman", 18), width=350)

for widget in [entry_S, entry_K, entry_r, entry_V, entry_t]:
    widget.pack(pady=8, padx=20)

option_type = ctk.CTkOptionMenu(frame, values=["Call", "Put"], font=("Times New Roman", 18))
option_type.pack(pady=8, padx=20)

calc_button = ctk.CTkButton(frame, text="Calculate", command=calculate, font=("Times New Roman", 18))
calc_button.pack(pady=12)

result_label = ctk.CTkLabel(frame, text="", font=("Times New Roman", 24))
result_label.pack(pady=15)

app.mainloop()
