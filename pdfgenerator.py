from fpdf import FPDF
import os
from PIL import Image
#Converting images to pdf
#Now I am opening each image
def converter(imagelist):
    for PNG_FILE in range(0 ,len(imagelist)):
            rgba = Image.open(imagelist[PNG_FILE])
            rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
            rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
            rgb.save(r"C:\Users\Gayatri Arora\Downloads\milknmocha-text_to_writing-20e102e281e2 (1)\milknmocha-text_to_writing-20e102e281e2\\final_output.pdf", append=True)
            #Now save multiple images in same pdf file
            os.remove(imagelist[PNG_FILE])
            os.remove('output%i.txt'%PNG_FILE)