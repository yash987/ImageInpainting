from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import tkinter.font as font
import cv2 
import numpy as np
# loading Python Imaging Library 
from PIL import ImageTk, Image 
  
# To get the dialog box to open when required  
from tkinter import filedialog
original_image=None
mask_image=None
def demo(original,mask,x1,y1):
    global img1
    print(mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    print(mask)
    output = cv2.inpaint(original, mask, 3, flags=cv2.INPAINT_TELEA)
    #cv2.imshow('result',output)
    #output = output - 18
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    img= Image.fromarray(output)
    img1 =Image.fromarray(output)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(newwindow, image = img)
    panel.image = img
    panel.place(x=x1,y=y1)
    
def open_img(x1,y1,ori): 
    # Select the Imagename  from a folder  
    x = openfilename() 
  
    # opens the image 
    img = Image.open(x) 
    print(type(img))
    if ori==True:
        global original_image
        original_image=img
        
        original_image=np.array(original_image)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        #print(original_image)
        #cv2.imshow('original',original_image)
    else:
        global mask_image
        mask_image=img 
        mask_image=np.array(mask_image)
        #print(mask_image)
        #cv2.imshow('mask',mask_image)
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((250, 250), Image.ANTIALIAS) 
    
    
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
   
    # create a label 
    panel = Label(newwindow, image = img) 
      
    # set the image as img  
    
    panel.image = img 
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    panel.place(x=x1,y=y1)



   



def openwindow():
   
    global newwindow
    
    newwindow = Toplevel(root)
    newwindow.geometry("1050x1050")
    newwindow.title("NEW WINDOW")
    newwindow.configure(bg="LightBlue1")
    #newwindow.resizable(False,False)
    #lbl = Label(newwindow,text="I am in new window").place(x = 480, y = 30)
    #lbl.pack()
    myFont1 = font.Font(family='Courier', weight='bold')
    btn1 = Button(newwindow, text="Close Me",bg='MediumPurple1',font = myFont1 , command=lambda: newwindow.destroy()).place(x =487 , y = 40)

    #btn1.pack()
    btn2 = Button(newwindow, text ='Open Image',bg='MediumPurple1',font = myFont1 ,width =10,height =3, command = lambda : open_img(100,300,True)).place( 
                                        x = 180, y = 150) 

    btn3 = Button(newwindow, text ='Mask Image',bg='MediumPurple1',font = myFont1 ,width =10,height =3, command = lambda : open_img(400,300,False)).place( 
                                        x = 480, y = 150) 
    btn4 = Button(newwindow, text ='Inpaint',bg='MediumPurple1',font = myFont1 ,width =10,height =3, command = lambda: demo(original_image,mask_image,700,300)).place( 
                                             x = 780, y = 150)

    btn5 = Button(newwindow, text='Save Image', bg='MediumPurple1', font = myFont1 , width=10, height=2, command=savefile).place(x=782, y=580)


    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
def openfilename():
    

    filename = filedialog.askopenfilename(title ='open') 
    return filename

def savefile():
    global img1
    
    filename = filedialog.asksaveasfile(mode='w', defaultextension='.jpg')
    if not filename:
        return
    img1.save(filename)



  

  

root = Tk()
root.title("Home Page")
# Set the resolution of window 
root.geometry("1050x1050")
image2 =Image.open("C:\\Users\\HP\\Desktop\\image inpainting\\yash.png")
image1 = ImageTk.PhotoImage(image2)
background_label = Label(root, image= image1 ,justify=CENTER, width= 1531, height=991, bg="black")
background_label.place()
background_label.pack()




lbl2 = Label(root, text= "WELCOME TO IMAGE INPAINTING")
lbl2.config(width=200,height=13)
lbl2.config(font=("Courier", 30))
myFont = font.Font(family='Courier', size=15, weight='bold')
button = Button(root, text=' START IMAGE INPAINTING',bg='MediumPurple1',font=myFont,command=openwindow).place(x=510,y=590)
button['font'] = myFont
button.pack()
        
 
  

  

# Allow Window to be resizable 
#root.resizable(width = True, height = True) 
  
# Create a button and place it into the window using grid layout 

mainloop() 
