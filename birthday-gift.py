import tkinter as tk
import pygame
import time
import random
from threading import Thread

# Initialize pygame mixer
pygame.mixer.init()

# Load and play birthday song
pygame.mixer.music.load("birthday_song.wav")  # your MP3 file
pygame.mixer.music.play()

# Lyrics
lyrics = [
    "Happy Birthday to You 🎉",
    "Happy Birthday to You 🎉",
    "Happy Birthday Dear Brother 🥳",
    "Happy Birthday to You 🎂",
    "May all your dreams come true ✨",
    "Wishing you joy and laughter 💖",
    "You are the best brother ever! 🤗"
]

# Window
root = tk.Tk()
root.title("Happy Birthday 🎉")
root.geometry("800x600")
root.resizable(False, False)

# Canvas with gradient background
canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
canvas.pack()

# Create gradient
def draw_gradient():
    for i in range(600):
        r = int(255 - (i*0.15))
        g = int(182 + (i*0.1))
        b = int(193 + (i*0.05))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 800, i, fill=color)

draw_gradient()

# Confetti and hearts
particles = []
symbols = ["✨","🎉","💖","🎂","🎁","❤️"]
colors = ["#FF4C4C","#FFD700","#4CFF4C","#4C6EFF","#FF4CF2","#FF914C"]

def spawn_particles():
    x = random.randint(0, 780)
    y = -10
    symbol = random.choice(symbols)
    color = random.choice(colors)
    size = random.randint(20, 36)
    speed = random.uniform(2,6)
    particles.append({"x": x, "y": y, "symbol": symbol, "color": color, "size": size, "speed": speed})

def animate_particles():
    canvas.delete("particles")
    for p in particles:
        canvas.create_text(p["x"], p["y"], text=p["symbol"], fill=p["color"], font=("Arial", p["size"]), tag="particles")
        p["y"] += p["speed"]
        p["x"] += random.uniform(-1,1)
    particles[:] = [p for p in particles if p["y"] < 600]

# Lyrics animation
lyric_index = 0
lyric_text = canvas.create_text(400, 500, text="", fill="#FF1493", font=("Dancing Script", 36, "bold"))

def show_lyrics():
    global lyric_index
    lyric = lyrics[lyric_index % len(lyrics)]
    canvas.itemconfig(lyric_text, text=lyric)
    lyric_index += 1
    root.after(2500, show_lyrics)

# Animation loop
def animation_loop():
    spawn_particles()
    animate_particles()
    root.after(100, animation_loop)

# Personal message popup
def show_message():
    message_window = tk.Toplevel(root)
    message_window.title("A Special Message")
    message_window.geometry("500x300")
    message_window.configure(bg="#FFF0F5")
    tk.Label(message_window, text="Happy Birthday, Brother! 🎉🎂\nYou are amazing and loved 💖", 
             font=("Comic Sans MS", 20, "bold"), bg="#FFF0F5", fg="#FF1493", justify="center").pack(expand=True)
    tk.Button(message_window, text="Close", font=("Arial", 14), command=message_window.destroy).pack(pady=20)

# Show button after 10 seconds
root.after(10000, lambda: tk.Button(root, text="Show Personal Message 💌", font=("Arial", 14, "bold"), 
                                   bg="#FF69B4", fg="white", command=show_message).place(x=300, y=50))

# Run
show_lyrics()
animation_loop()
root.mainloop()