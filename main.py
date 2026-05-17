import tkinter as tk
from tkinter import ttk
import random

from data import *

EXTRA_WORDS = [
    "cinematic",
    "emotional",
    "futuristic",
    "dark neon",
    "melancholic",
    "epic atmosphere",
    "high energy",
]

def generate_prompt():

    genre = genre_var.get()
    mood = mood_var.get()
    vocal = vocal_var.get()
    instrument = instrument_var.get()
    bpm = bpm_var.get()

    theme = theme_text.get("1.0", tk.END).strip()

    random_words = random.sample(EXTRA_WORDS, 3)

    prompt = f"""
{genre} music,
{mood} atmosphere,
{vocal},
{instrument},
{random_words[0]},
{random_words[1]},
{random_words[2]},
professional production,
{bpm}.

Theme:
{theme}

Negative prompt:
low quality, muddy mix, weak drums
"""

    output.delete("1.0", tk.END)
    output.insert(tk.END, prompt)

def copy_prompt():

    text = output.get("1.0", tk.END)

    root.clipboard_clear()
    root.clipboard_append(text)

root = tk.Tk()

root.title("Suno Prompt Generator")
root.geometry("850x700")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")

title = tk.Label(
    root,
    text="Suno Prompt Generator",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 20)
)

title.pack(pady=15)

genre_var = tk.StringVar(value=GENRES[0])
mood_var = tk.StringVar(value=MOODS[0])
vocal_var = tk.StringVar(value=VOCALS[0])
instrument_var = tk.StringVar(value=INSTRUMENTS[0])
bpm_var = tk.StringVar(value=BPM[0])

fields = [
    ("Genre", genre_var, GENRES),
    ("Mood", mood_var, MOODS),
    ("Vocals", vocal_var, VOCALS),
    ("Instrument", instrument_var, INSTRUMENTS),
    ("BPM", bpm_var, BPM)
]

for label, variable, values in fields:

    tk.Label(
        root,
        text=label,
        bg="#1e1e1e",
        fg="white"
    ).pack()

    ttk.Combobox(
        root,
        textvariable=variable,
        values=values,
        state="readonly"
    ).pack(fill="x", padx=20, pady=5)

tk.Label(
    root,
    text="Theme / Idea",
    bg="#1e1e1e",
    fg="white"
).pack()

theme_text = tk.Text(
    root,
    height=8,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)

theme_text.pack(fill="both", padx=20, pady=10)

generate_btn = tk.Button(
    root,
    text="Generate Prompt",
    command=generate_prompt,
    bg="#00aa66",
    fg="white",
    height=2
)

generate_btn.pack(fill="x", padx=20, pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Prompt",
    command=copy_prompt,
    bg="#444",
    fg="white",
    height=2
)

copy_btn.pack(fill="x", padx=20)

output = tk.Text(
    root,
    height=14,
    bg="#2b2b2b",
    fg="#00ff99",
    insertbackground="white"
)

output.pack(fill="both", padx=20, pady=20)

root.mainloop()
