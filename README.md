# GifManipulationScripts
A few scripts that deal with gifs.
These scripts work by dropping and dragging appropriate files onto the script. You may have to install python libraries.

These scripts have only been tested on **Windows**, but they may work on other platforms.

## Scripts
``getTenorGif.py`` Drag and drop a ``.url`` file to create a gif from the Tenor page referenced in the file (primary done by dragging Tenor gifs from Discord). Deletes the original file. _Requires bs4_

``frameSkippingGif.py`` Drag and drop a ``.gif`` file to create a gif that skips every other frame. May produce undesirable effects in the output gif. _Requires wand.image_

``frameSkippingGifOdd.py`` Drag and drop a ``.gif`` file to create a gif that skips every other frame starting from the first frame. May produce undesirable effects in the output gif. _Requires wand.image_

``frameSkippingApng.py`` Drag and drop an animated ``.png`` file to create an apng that skips every other frame. _Requires APNG_

``minimumDelayApng.py`` Drag and drop an animated ``.png`` file to create an apng with each frame set to the lowest delay rendered (11ms in Firefox and Chromium). _Requires APNG_
