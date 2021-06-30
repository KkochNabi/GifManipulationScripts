import sys
import os
import requests
from bs4 import BeautifulSoup
import unicodedata

# Check if a file was dropped
file_valid = False
try:
    input = sys.argv[1]
    
    # Get link from the .url and check if it is tenor
    with open(input, "r") as file:
        url = file.read()[23:]
    if "tenor.com" in url:
        file_valid = True
except:
    pass

if not file_valid:
    input("Please open this script by dragging and dropping a tenor url file.")
    sys.exit() 


# Get gif link
page = BeautifulSoup(requests.get(url).content, "html.parser")
gif = page.find("link", attrs={"class": "dynamic", "rel": "image_src"})["href"]

# Write gif to file
with open(f"{os.path.basename(os.path.splitext(input)[0])}.gif", "wb") as output:
    output.write(requests.get(gif).content)
os.remove(input)