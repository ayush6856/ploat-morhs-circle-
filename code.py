import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# FUNCTION TO COMPUTE AND PLOT MOHR’S CIRCLE
def plot_mohrs_circle():
    try:
        σx = float(entry_sigma_x.get())
        σy = float(entry_sigma_y.get())
        τxy = float(entry_tau_xy.get())
    except ValueError:
        result_label.config(text="PLEASE ENTER VALID NUMERIC VALUES!", fg="red")
        return

    # CALCULATIONS
    center = (σx + σy) / 2
    radius = np.sqrt(((σx - σy) / 2) ** 2 + τxy ** 2)
    σ1 = center + radius
    σ2 = center - radius
    θp = 0.5 * np.arctan2(2 * τxy, σx - σy) * 180 / np.pi

    # CLEAR THE PLOT
    ax.clear()

    # PLOT MOHR'S CIRCLE
    circle = plt.Circle((center, 0), radius, fill=False, color='orange', lw=2)
    ax.add_artist(circle)
    ax.set_xlabel('NORMAL STRESS (σ)')
    ax.set_ylabel('SHEAR STRESS (τ)')
    ax.set_title("MOHR’S CIRCLE REPRESENTATION", color="black")
    ax.axhline(0, color='gray', linestyle='--')
    ax.axvline(center, color='gray', linestyle='--')

    # PLOT KEY POINTS IN BLACK COLOR
    ax.plot([σx, σy], [τxy, -τxy], 'ko')  # 'k' means black
    ax.text(σx, τxy, f"A ({σx}, {τxy})", fontsize=9, color='black')
    ax.text(σy, -τxy, f"B ({σy}, {-τxy})", fontsize=9, color='black')

    ax.set_aspect('equal', adjustable='datalim')
    canvas.draw()

    result_label.config(
        text=f"CENTER = {center:.2f}, RADIUS = {radius:.2f}\n"
             f"σ₁ = {σ1:.2f}, σ₂ = {σ2:.2f}, θp = {θp:.2f}°",
        fg="green"
    )

# TKINTER WINDOW
root = tk.Tk()
root.title("2D STRESS ANALYSIS WITH MOHR’S CIRCLE")
root.geometry("800x700")
root.configure(bg="#f5f5f5")

# TITLE
title_label = tk.Label(root, text="2D STRESS ANALYSIS WITH MOHR’S CIRCLE",
                       font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#000000")
title_label.pack(pady=10)

# INPUT FRAME
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=10)

tk.Label(input_frame, text="σx:", font=("Arial", 12), bg="#f5f5f5", fg="black").grid(row=0, column=0, padx=5, pady=5)
entry_sigma_x = ttk.Entry(input_frame, width=10)
entry_sigma_x.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="σy:", font=("Arial", 12), bg="#f5f5f5", fg="black").grid(row=0, column=2, padx=5, pady=5)
entry_sigma_y = ttk.Entry(input_frame, width=10)
entry_sigma_y.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="τxy:", font=("Arial", 12), bg="#f5f5f5", fg="black").grid(row=0, column=4, padx=5, pady=5)
entry_tau_xy = ttk.Entry(input_frame, width=10)
entry_tau_xy.grid(row=0, column=5, padx=5, pady=5)

# BUTTON
plot_button = ttk.Button(root, text="PLOT MOHR’S CIRCLE", command=plot_mohrs_circle)
plot_button.pack(pady=10)

# RESULT LABEL
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5", fg="black")
result_label.pack(pady=5)

# MATPLOTLIB FIGURE
fig, ax = plt.subplots(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()