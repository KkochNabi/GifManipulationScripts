import sys
import os
from apng import APNG

# Check if a file was dropped
file_valid = False
try:
    inp = sys.argv[1]
    original = APNG.open(inp)

    # Check if the input is actually animated
    if len(original.frames) >= 2:
        file_valid = True
except:
    pass

if not file_valid:
    input("Please execute this script by dragging and dropping an animated .png file")
    sys.exit()

# Set delay to 11ms (lowest Firefox/Chromium allows?)
for i in range(len(original.frames)):
    original.frames[i][1].delay = 11
    original.frames[i][1].delay_den = 1000

# Save new apng
original.save(f"{os.path.dirname(os.path.realpath(inp))}\\{os.path.basename(inp)[:-4]}_delay11ms.png")