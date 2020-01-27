# ASCII-Art
Turns a picture of your choice to ASCII Art and prints it in your command prompt. Uses the Pillow library to process images.

## Installation:
```shell
python -m pip install pip
python -m pip install Pillow
```
## Usage:
Type in command prompt at the file location where you have downloaded ASCII Art. Make sure you also have Python installed on your system.
```shell
python "ASCII Art.py"
```

### Original:
[![](https://i.imgur.com/CNfMQJA.jpg)]()

### ASCII ART:
[![](https://i.imgur.com/cN4V2Gy.png)]()

## Troubleshooting:
- **ASCII art is too zoomed in**
    - Zoom out from the command prompt by holding Ctrl and scrolling mouse wheel down.
    
- **ASCII art is not displaying the picture properly/ASCII art doesn't resemble picture inputted**
    - Minimize command prompt window and then maximize
    
- **Prints out "Error, please try again." in console after choosing a file**
    - The file type of the picture is not supported by Pillow, please only use files found in <a href="https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html" target="_blank">**this list.**</a>
    
## Features to be added:
- Resize picture based on command prompt window and picture dimensions
- Add colour
