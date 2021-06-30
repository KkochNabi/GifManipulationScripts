import sys
import os
from wand.image import Image
import math

# Check if a file was dropped
try:
    input = sys.argv[1]
except:
    input("Please open this script by dragging and dropping a gif.")
    sys.exit() 
    
# Prepare vars
original = Image(filename=input)
frame_count = len(original.sequence)

# Extract every other frame
frames = Image()
for i in range(math.floor(frame_count/2)):
    try: 
        frames.sequence.append(original.sequence[1 + (i*2)])
    except:
        pass

# Save new gif
frames.save(filename=f"{os.path.dirname(os.path.realpath(input))}\\{os.path.basename(input)[:-4]}_frameSkipped.gif")