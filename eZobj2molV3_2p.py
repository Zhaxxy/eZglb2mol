

#vertoffset = 584 * 2
#texoffset = 373324 * 2
#faceoffset = 652880 * 2
#normoffset = 186952 * 2 HAHA NO MORE!


#vertoffset = 1114
#texoffset = 747616
#faceoffset = 1307494

import ntpath
from collections import OrderedDict
import re
from decimal import Decimal
import struct
import numpy
import os
import sys
from binascii import a2b_hex
import tkinter as tk
import shutil
import os, errno
from tkinter import messagebox
from pathlib import Path
from tkinter import *
import webbrowser
import mmap
from tkinter import filedialog

#Special thanks to Znowu mam bana no ja nie moge v2#4634 (his discord https://discord.gg/bFyaySkUDQ) for programming the orginal importer, this one was programmed by Zhaxxy however with help from random sites

def notifytheuserlol():
    import winsound         # for sound  
    import time             # for sleep

    winsound.Beep(440, 250) # frequency, duration
    time.sleep(0.25)        # in seconds (0.25 is 250ms)



def fourhex(sadnum):
    sadnum = hex(sadnum)[2:].rjust(8, '0')
    return sadnum

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))

def silentremove(Zhaxxtempfilesclean):
    try:
        os.remove(Zhaxxtempfilesclean)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred
def hex2complement(number):
    hexadecimal_result = format(number, "03X")
    return hexadecimal_result.zfill(4) # .zfill(n) adds leading 0's if the integer has less digits than n

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = tk.Tk()
v = StringVar()


v.set("made by Zhaxxy (bit.ly/zhaxxy)")

root.iconbitmap(resource_path("PS4poopybench.ico"))
root.config(bg='#000000')
root.title('eZobj2mol')
textnum1 = tk.Label( root, text='Converts .obj files to', bg='black', fg='white', font='none 25')
textnum2 = tk.Label( root, text='a decompressed .mol file,', bg='black', fg='white', font='none 25')
textnum3 = tk.Label( root, textvariable=v, bg='black', fg='white', font='none 25')
textnumbruhcredit = tk.Label( root, text='and with help from KamiQu and ennuo', bg='black', fg='white', font='none 25')

textnumICANNT = tk.Label( root, text='V3.2p (public)', bg='black', fg='white', font='none 25')
textnum4 = tk.Label( root, text='Your obj file must be prepared via products.aspose.app/3d/conversion/obj-to-glb', bg='black', fg='red', font='none')
textnum5 = tk.Label( root, text='then back to products.aspose.app/3d/conversion/glb-to-obj!', bg='black', fg='red', font='none')
textnum6 = tk.Label( root, text='This may freeze up during conversion, just wait untill the dialog pops up', bg='black', fg='green', font='none')
textnum7 = tk.Label( root, text='You can delete the eZDONT_DELETE_OR_OVERWRITE files when this isnt running', bg='black', fg='white', font='none')


textnum1.pack()
textnum2.pack()
textnum3.pack()
textnumbruhcredit.pack()
textnumICANNT.pack()
textnum4.pack()
textnum5.pack()
textnum6.pack()
textnum7.pack()
root.update()



def quitandclean():
    cleanbruhPS4()
    
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("PS4poopybench.ico"))
    imacheckthiskk = tk.messagebox.showinfo(title='eZobj2mol', message='Exiting...!')
    sys.exit()

def lehobjaintright():
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("PS4poopybench.ico"))
    imacheckthiskk = tk.messagebox.askokcancel(title='eZobj2mol', message='Your obj is not ready, or it is not even an obj. You need to prepare it using these sites, products.aspose.app/3d/conversion/obj-to-glb, then products.aspose.app/3d/conversion/glb-to-obj. Do you want to open these sites?')
    if imacheckthiskk == 1:
        webbrowser.open('https://products.aspose.app/3d/conversion/glb-to-obj')
        webbrowser.open('https://products.aspose.app/3d/conversion/obj-to-glb')
        
        quitandclean()
        
    else:
        
        quitandclean()

#lets clean up
def cleanbruhPS4():

    silentremove('eZDONT_DELETE_OR_OVERWRITEobjface.ezobjface')
    silentremove('eZDONT_DELETE_OR_OVERWRITEobjtex.ezobjtex')
    silentremove('eZDONT_DELETE_OR_OVERWRITEobjvert.ezobjvert')
    silentremove('eZDONT_DELETE_OR_OVERWRITEps4face.ezface')
    silentremove('eZDONT_DELETE_OR_OVERWRITEps4tex.eztex')
    silentremove('eZDONT_DELETE_OR_OVERWRITEps4vert.ezvert')
    silentremove('eZDONT_DELETE_OR_OVERWRITEworking.molt')
    silentremove('eZDONT_DELETE_OR_OVERWRITEthechosen.obj')
    silentremove('eZDONT_DELETE_OR_OVERWRITEreadytouse.Pmol')
    silentremove('eZDONT_DELETE_OR_OVERWRITEps4norm.eznorm')
    silentremove('eZDONT_DELETE_OR_OVERWRITEobjnorm.ezobjnorm')
cleanbruhPS4()


#done start stuff
#ease of access shit

try:
    droppedFile = sys.argv[1]
    root.filename = droppedFile
    shutil.copyfile(droppedFile,'eZDONT_DELETE_OR_OVERWRITEthechosen.obj')
except IndexError:
    
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("PS4poopybench.ico"))
    root.filename = filedialog.askopenfilename( title="Select your ready .obj to import/convert, idk", filetypes=(("obj 3d model file", "*.obj"),("obj support only", "*.*")))
    if root.filename == '':
        quitandclean()
    shutil.copyfile(root.filename,'eZDONT_DELETE_OR_OVERWRITEthechosen.obj')


with open('eZDONT_DELETE_OR_OVERWRITEthechosen.obj', 'rb', 0) as getsussedkk, \
    mmap.mmap(getsussedkk.fileno(), 0, access=mmap.ACCESS_READ) as lastsuskk:
    if lastsuskk.find(b'# Aspose.3D Wavefront OBJ Exporte') != -1:
        pass
    else:
        getsussedkk.close()
        lastsuskk.close()
        cleanbruhPS4()
        lehobjaintright()

      


with open('eZDONT_DELETE_OR_OVERWRITEthechosen.obj', 'r') as f:
    for eachcoord in f:
        if "v " in eachcoord:
            with open('eZDONT_DELETE_OR_OVERWRITEobjvert.ezobjvert' , 'a') as wr:
                wr.write(eachcoord)

with open('eZDONT_DELETE_OR_OVERWRITEthechosen.obj', 'r') as f:
    for eachcoord in f:
        if "vt " in eachcoord:
            with open('eZDONT_DELETE_OR_OVERWRITEobjtex.ezobjtex' , 'a') as wr:
                wr.write(eachcoord)

with open('eZDONT_DELETE_OR_OVERWRITEthechosen.obj', 'r') as f:
    for eachcoord in f:
        if "f " in eachcoord:
            with open('eZDONT_DELETE_OR_OVERWRITEobjface.ezobjface' , 'a') as wr:
                wr.write(eachcoord)

with open('eZDONT_DELETE_OR_OVERWRITEthechosen.obj', 'r') as f:
    for eachcoord in f:
        if "vn " in eachcoord:
            with open('eZDONT_DELETE_OR_OVERWRITEobjnorm.ezobjnorm' , 'a') as wr:
                wr.write(eachcoord)


silentremove('eZDONT_DELETE_OR_OVERWRITEps4norm.eznorm')

tobedonenorm = ""

with open('eZDONT_DELETE_OR_OVERWRITEobjnorm.ezobjnorm', 'r') as f:
    for oml in f:
        vertnorm = oml
        vertnorm = vertnorm.replace("vn ", "", 1)
        vertnorm = vertnorm.split()
        vertnorm = [float(vertnorm) for vertnorm in vertnorm]

        def pack12_11_1(normal):
            x = round(normal[0] * 0x7ff) & 0xfff;
            y = round(normal[1] * 0x3ff) & 0x7ff
            z = int(normal[2] < 0)
            return (x | (y << 12) | (z << 23))
        vertnorm = pack12_11_1(vertnorm)    

        vertnorm = hex(vertnorm)
        vertnorm = vertnorm[2:]
        if vertnorm == '0':
            vertnorm = '000000'
        if len(vertnorm) < 6:  #at least i tried?
            if len(vertnorm) == 5:
                vertnorm = vertnorm + '0'
            if len(vertnorm) == 4:
                vertnorm = vertnorm + '00'            
            if len(vertnorm) == 3:
                vertnorm = vertnorm + '000' # ah yes, some nice code, also i found a better way of doind this, 'fourhex' but cba
            if len(vertnorm) == 2:
                vertnorm = vertnorm + '0000'
            if len(vertnorm) == 1:
                vertnorm = vertnorm + '00000'                
        vertnorm = "0000FF00" + vertnorm + "000000000000000000"    
        tobedonenorm = tobedonenorm + vertnorm  # ill fix this inconsitenty later




silentremove('eZDONT_DELETE_OR_OVERWRITEps4vert.ezvert')

with open('eZDONT_DELETE_OR_OVERWRITEobjvert.ezobjvert', 'r') as f:
    for oml in f:
        vert = oml
        vert = vert.replace("v ", "", 1)




        vert = vert.split()


        vert1 = vert[0]
        vert1 = float(vert1)

        vert1 = float_to_hex(vert1)

        vert1 = vert1[2:]
        if vert1 == "0":
            vert1 = "00000000"



        vert2 = vert[1]
        vert2 = float(vert2)

        vert2 = float_to_hex(vert2)

        vert2 = vert2[2:]
        if vert2 == "0":
            vert2 = "00000000"
        


        vert3 = vert[2]
        vert3 = float(vert3)

        vert3 = float_to_hex(vert3)

        vert3 = vert3[2:]
        if vert3 == "0":
            vert3 = "00000000"

        finalvert = vert1 + vert2 + vert3
        finalvert = finalvert + "000000FF"
        
        with open('eZDONT_DELETE_OR_OVERWRITEps4vert.ezvert' , 'a') as wr:
            wr.write(finalvert)

silentremove('eZDONT_DELETE_OR_OVERWRITEps4tex.eztex')

with open('eZDONT_DELETE_OR_OVERWRITEobjtex.ezobjtex', 'r') as f:
    for oml in f:
        texturecoord = oml
        texturecoord = texturecoord.replace("vt ", "", 1)

        texturecoord = texturecoord.split()

        texturecoord1 = texturecoord[0]
        texturecoord1 = float(texturecoord1)

        
        texturecoord1 = float_to_hex(texturecoord1)

        texturecoord1 = texturecoord1[2:]
        if texturecoord1 == "0":
            texturecoord1 = "00000000"

        texturecoord2 = texturecoord[1]
        texturecoord2 = float(texturecoord2)
        texturecoord2 = 1 - texturecoord2

        texturecoord2 = float_to_hex(texturecoord2)

        texturecoord2 = texturecoord2[2:]
        if texturecoord2 == "0":
            texturecoord2 = "00000000"

        finaltexturecoord = texturecoord1 + texturecoord2 + texturecoord1 + texturecoord2 + texturecoord1 + texturecoord2



        with open('eZDONT_DELETE_OR_OVERWRITEps4tex.eztex' , 'a') as wr:
        
            wr.write(finaltexturecoord)

silentremove('eZDONT_DELETE_OR_OVERWRITEps4face.ezface')

with open('eZDONT_DELETE_OR_OVERWRITEobjface.ezobjface', 'r') as f:
    for oml in f:
        face = oml
        if "-" in face:
            print("ERORR")
        face = face.replace("f ", "", 1)
        face = face.replace("/", " ")
        
        eachface = face.split()
        face = " ".join(sorted(set(eachface), key=eachface.index))
        
        face = face.split()
        
        face = [int(item) for item in face]
        


        face1 = face[0]

        face1 = face1 - 1

        face1 = hex2complement(face1)

        

        face2 = face[1]

        face2 = face2 - 1

        face2 = hex2complement(face2)

        

        face3 = face[2]

        face3 = face3 - 1

        face3 = hex2complement(face3)

        

        finalface = face1 + face2 + face3 + "FFFF"
        
        with open('eZDONT_DELETE_OR_OVERWRITEps4face.ezface' , 'a') as wr:
            wr.write(finalface)

#im coping the template to somewhere else, then inserting the stuff into that, NOT ANYMORE AHHAHAHAH




with open("eZDONT_DELETE_OR_OVERWRITEthechosen.obj", "r") as file:

    #read content of file to string
    vnudata = file.read()

    #get number of occurrences of the substring in the string
    vertnumlol = vertoccurrences = vnudata.count("v ")
    
vertoccurrences = hex(vertoccurrences)
vertoccurrences = vertoccurrences[2:]
vertoccurrences = vertoccurrences.rjust(8, '0')


with open("eZDONT_DELETE_OR_OVERWRITEthechosen.obj", "r") as file:


    #read content of file to string
    fadata = file.read()

    #get number of occurrences of the substring in the string
    faceoccurrences = fadata.count("f ")
indexs = faceoccurrences * 4
indexs = hex(indexs)
indexs = indexs[2:]
indexs = indexs.rjust(8, '0')

faceoccurrences = hex(faceoccurrences)
faceoccurrences = faceoccurrences[2:]
faceoccurrences = faceoccurrences.rjust(8, '0')

molhexstart = vertoccurrences + indexs + '00000000' + faceoccurrences + '0000000200000003000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000023A4FE0AF3A4FE08000000002407FAF1E4074E2CC4519EE4E00000000'

texwrite = open("eZDONT_DELETE_OR_OVERWRITEps4tex.eztex", "r+")
texdata = texwrite.read()
texwrite.close()


UVshexstart = hex(len(texdata)//2)[2:]
UVshexstart = UVshexstart.rjust(8, '0')


facewrite = open("eZDONT_DELETE_OR_OVERWRITEps4face.ezface", "r+")
facedata = facewrite.read()
facewrite.close()


facehexstart = hex(len(facedata)//2)[2:].rjust(8, '0') 

vertwrite = open("eZDONT_DELETE_OR_OVERWRITEps4vert.ezvert", "r+")
vertdata = vertwrite.read()
vertwrite.close()

#get the length of the data
number_of_characters = hex(len(vertdata)//2)[2:].rjust(8, '0') # shortcut for the normal offsets realtive to the vertices
bytecountforverts = hex(len(vertdata))[2:].rjust(8, '0') # nahh this is too much of a shortcut


verthexstart = number_of_characters + bytecountforverts + bytecountforverts








def byebyehash():
    changehash.destroy()
    changehash.quit()

def notahash():
    yourhash.delete(0, END)
    yourhash.insert(0, 'Invalid SHA1 hash')
    yourhash.configure(foreground="red")

def checkactualhash():
    checkinghash = yourhash.get().replace(" ", "")     
    try:
       
        int(checkinghash, 16)
        
        if len(checkinghash) == 40:
            
            global gmathash 
            gmathash = str(checkinghash)
            byebyehash()
        else:
            notahash()
    except ValueError:
        notahash()


def click(event):
   yourhash.configure(state=NORMAL)
   yourhash.delete(0, END)
   yourhash.unbind('<Button-1>', clicked)
   
changehash = tk.Tk()
changehash.iconbitmap(resource_path("PS4poopybench.ico"))
changehash.resizable(False, False)
changehash.geometry('512x128')
changehash.config(bg='#000000')
changehash.title('eZobj2mol')

label = Label( changehash, text='Enter your .gmat SHA1 hash here:', bg='black',font=('', 25), fg='white' )
label.place(relx=0, rely=-0.04, anchor='nw')

def changeforegroundcolour():
    yourhash.configure(foreground="black")
    yourhash.update()

checkifmod = StringVar()

checkifmod.trace("w", lambda name, index,mode, checkifmod=checkifmod: changeforegroundcolour())

yourhash=Entry(changehash,  font=('', 25), width=27, highlightthickness=0, textvariable=checkifmod)
clicked = yourhash.bind('<Button-1>', click)

yourhash.insert(0, 'Enter your .gmat SHA1 hash here:')
yourhash.configure(foreground="blue")
yourhash.place(relx=0.96, rely=0.45, anchor='e')




okhash = Button(changehash, text ="Okay", font=('', 12), command=checkactualhash)
okhash.place(relx=0.1, rely=0.8, anchor='e')

forgetthishash = Button(changehash, text ="Cancel", font=('', 12), command = byebyehash)
forgetthishash.place(relx=0.25, rely=0.8, anchor='e')



changehash.protocol("WM_DELETE_WINDOW", quitandclean)

changehash.mainloop()

vert4prim = fourhex(vertnumlol - 1)


try:
    gmathash
except NameError:
    gmathash = '42494720424947204348554E4755532042494721'
else:
    pass

primtivesforfly = '00000000000000000C' + vert4prim + '00000000' + indexs
facehexlast = '000000010000000001' + gmathash + primtivesforfly + '00000000'
   

with open(resource_path("ps4mol.moltemplate"), 'r') as basewritelol:
    basedatalol = basewritelol.read()


thegrandfinale = molhexstart + verthexstart + vertdata + tobedonenorm + UVshexstart + texdata + facehexstart + facedata + facehexlast + basedatalol

#open text file
text_file = open("eZDONT_DELETE_OR_OVERWRITEworking.molt", "w")
 
#write string to file
text_file.write(thegrandfinale)
 
#close file
text_file.close()



with open("eZDONT_DELETE_OR_OVERWRITEworking.molt", "r") as f:
    hexdump = f.read().strip()
with open("eZDONT_DELETE_OR_OVERWRITEreadytouse.Pmol", "wb") as f:
    f.write(bytearray.fromhex(hexdump))

if gmathash == '42494720424947204348554E4755532042494721':
    del gmathash

try:
    droppedFile
except NameError:
    pass
else:
    autoname = ntpath.basename(droppedFile.removesuffix('.obj') + '.mol')
    shutil.copyfile('eZDONT_DELETE_OR_OVERWRITEreadytouse.Pmol',autoname)
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("PS4poopybench.ico"))
    
    try:
        gmathash
    except NameError:
        horay2 = tk.messagebox.showinfo(title='eZobj2mol AUTO', message='Done, enjoy! (Dragged and dropped)')
    else:
        horay2 = tk.messagebox.showinfo(title='eZobj2mol AUTO', message='Done, enjoy! (Dragged and dropped) (.gmat dependency changed!)')
    quitandclean()

thefinalname = os.path.basename(root.filename.removesuffix('.obj'))

finalmol = filedialog.asksaveasfile(defaultextension='.mol',

                                    filetypes=[

                                        ("decompressed mol lbp 3d model",".mol"),

                                        

                                        ("as anything else lol", ".*"),
                                        
                                        
                                        

                                    ],initialfile = thefinalname,title="Save the imported/converted, idk, decompressed mol")

if finalmol == None:
    quitandclean()
else:
    shutil.copyfile('eZDONT_DELETE_OR_OVERWRITEreadytouse.Pmol',finalmol.name)
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("PS4poopybench.ico"))
    try:
        gmathash
    except NameError:
        horay = tk.messagebox.showinfo(title='eZobj2mol', message='Done, enjoy!')
    else:
        horay = tk.messagebox.showinfo(title='eZobj2mol', message='Done, enjoy! (.gmat dependency changed!)')
    
    quitandclean()
    
root.protocol("WM_DELETE_WINDOW", quitandclean)
root.mainloop()