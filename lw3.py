import tkinter as tk
import random
from pygame import mixer


#generating key
def rn_num():
    return chr(random.randint(ord('A'), ord('Z')))

def generate():
    nums = user_entry.get()
    if not nums.isdigit() or len(nums) != 6:
        key_label.config(text="введите 6-значное число")
        return

    nums1 = "".join(random.sample(nums[-3:], 3))
    nums2 = "".join(random.sample(nums[:3], 3))
    p1 = nums1 + rn_num() + rn_num()
    p2 = nums2 + rn_num() + rn_num()
    p3 = (f'0{int(nums1) + int(nums2)}' if len(str(int(nums1) + int(nums2))) == 3 else int(nums1) + int(nums2))

    key = f"{p1}-{p2}-{p3}"
    key_label.config(text=key)

#user interface
window = tk.Tk()
window.title("lab 3")
window.geometry("650x500")


bg_photo = tk.PhotoImage(file="phazmaa (1).png")
background_label = tk.Label(window, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


label_text = tk.Label(window,
                      text="KEY GENERATOR",
                      font="roman 30",
                      bg="black",
                      fg="blue")
label_text.place(relx=0.33, rely=0.1)


key_label = tk.Label(window,
                      text="",
                      font="roman 20",
                      bg="black",
                      fg="yellow")
key_label.place(relx=0.3, rely=0.7)


button = tk.Button(window, text="GENERATE", command=generate, width=20, height=3, font="roman 10")
button.place(relx=0.42, rely=0.3)
button.size()

user_entry = tk.Entry(window,
                      width=20,
                      font=("roman", 16))
user_entry.place(relx=0.36, rely=0.5)

#музыка
mixer.init()
mixer.music.load('Music Box to Phasmophobia.mp3')

mixer.music.play()



window.mainloop()