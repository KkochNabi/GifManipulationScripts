import sys
import os
from apng import APNG
import math

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

# Pop every other frame (in original)
for i in range(math.floor(len(original.frames)/2)):
    try:
        original.frames.pop(i+1)
    except:
        pass

# Save new apng
original.save(f"{os.path.dirname(os.path.realpath(inp))}\\{os.path.basename(inp)[:-4]}_frameSkipped.png")