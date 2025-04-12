import tkinter as tk
import numpy as np
import pygame

SAMPLE_RATE = 44100
DURATION = 1
VOLUME = 0.00028  # 거의 무음, 블루투스 연결 유지만을 위한 최소치

samples = (np.random.uniform(-1, 1, int(SAMPLE_RATE * DURATION)) * 32767 * VOLUME).astype(np.int16)
sound_array = np.stack([samples, samples], axis=1)

pygame.mixer.init(frequency=SAMPLE_RATE, channels=2)
sound = pygame.sndarray.make_sound(sound_array)

is_playing = False

def start():
    global is_playing
    if not is_playing:
        is_playing = True
        sound.play(loops=-1)
        status_label.config(text="🟢 작동 중")

def stop():
    global is_playing
    if is_playing:
        is_playing = False
        sound.stop()
        status_label.config(text="🔴 중지됨")

root = tk.Tk()
root.title("Bluetooth 끊김 방지기")
root.geometry("280x150+100+100")
root.attributes("-topmost", True)

status_label = tk.Label(root, text="🔴 중지됨", font=("Arial", 12))
status_label.pack(pady=10)

start_btn = tk.Button(root, text="▶ ON (노이즈 재생)", command=start, width=30)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="⏹ OFF (정지)", command=stop, width=30)
stop_btn.pack(pady=5)

root.mainloop()


#나의 첫 코딩
