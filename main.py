import win32gui
from PIL import ImageGrab
import time
from tqdm import tqdm
import os
import datetime

date = datetime.datetime.now().strftime("%m%d")

if not os.path.exists("img"):
    os.makedirs("img")

for i in tqdm(range(1,30+1)):
    time.sleep(10)
    x0, y0, x1, y1 = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    im = ImageGrab.grab((x0, y0, x1, y1), all_screens=True)
    im.save(f"img/{date}_{str(i).zfill(3)}.png")
