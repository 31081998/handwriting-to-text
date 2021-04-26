from fpdf import FPDF
import os
import pdfToTxt
from PIL import Image
import pdfgenerator
background_img = Image.open("myfont/bg.png")
sizeOfSheet =background_img.width
x, y  = 0,0
#[~!@#$%^&*()_+-]
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

def writee(char):
    global x, y
    if char == '\n':
        pass
    else:
        char.lower()
        alphabet = Image.open("myfont/%s.png"%char)
        background_img.paste(alphabet, (x, y))
        size_of_alphabet = alphabet.width
        x += size_of_alphabet
        del alphabet

def letterwrite(word):
    global x, y
    if x > sizeOfSheet - 95*(len(word)):
        x = 0
        y += 200
    for letter in word:        
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'            
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            elif letter == '~':
                letter = 'compliment'
            #elif letter == '[':
            #    letter = 'squarebracket'
            elif letter == ']':
                letter == 'squarebracketclose'
           # elif letter == '=':
           #     letter = 'equalsto'
            #elif letter == '_':
             #   letter = 'underscore'
            elif letter == '@':
                letter = 'attherate'
            elif letter == '+':
                letter = 'adder'                       
                            
            writee(letter)



def worddd(Input):
    wordlist=Input.split(' ')
    
    for letter in wordlist:
        letterwrite(letter)
        writee('space')



if __name__ == '__main__':
    pngfile=[]
    imagelist=[]
    noOfPages=pdfToTxt.pdftotxtconverter()
    with open('final_output.pdf','wb'):
        pass
    
    try:
        for curr_page in range(noOfPages):
            
            with open(f'output{curr_page}.txt', 'r') as file:
                data = file.read().replace('\n', '')
        
            len_of_pg_data=len(data)
            nn=len_of_pg_data//600
            chunk_size =len_of_pg_data//(nn+1)
            chunk_data=[ data[i:i+chunk_size] for i in range(0, len_of_pg_data, chunk_size) ]
            pngfile.append(chunk_data)
            
            for index in range(0,len(chunk_data)):
                worddd(chunk_data[index])
                writee('\n')
                background_img.save('%doutt.png'%curr_page)
                new_background_img= Image.open("myfont/bg.png")
                background_img=new_background_img
                x = 0
                y = 0

    except ValueError as exception:
        print("{}\nTry again".format(exception))

    
    for png_in_file in range(0,len(pngfile)):
        imagelist.append('%doutt.png'%png_in_file)
        
    pdfgenerator.converter(imagelist)
    

