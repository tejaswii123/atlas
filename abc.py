import cv2
import numpy as np
import pytesseract
from tkinter import *
flag=0
    
impath=""
def delete():
    entry.delete(0,END)
    label1.config(text="")    
    
def printSomething():
    impath=entry.get()
    img=cv2.imread(impath)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.GaussianBlur(img, (3, 3), 0)
    img=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img= cv2.addWeighted(img, 1.5, 0, 0, 0)
    cv2.imwrite('thres.png',img)
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
    text = pytesseract.image_to_string(img, lang='tel')
    text.encode("utf-8")
    with open("output.html", "w",encoding = "utf-8") as f:

        f.write(text)
   
    label1.config(text= text)
    
    label1.pack() 
window = Tk()
window.title("user input")
label = Label(window,text="Image path:")
label1=Label(window,text="")
label.config(font=("Consolas",16))
label1.config(font=("",16))
label.pack(side=LEFT)

def printLive():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        frame = cv2.resize(frame, (1280,720))
        cv2.imshow("Camera",frame)
        key=cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite('svd_img.png',frame)
            entry.insert(0,"svd_img.png")
            flag=1
            cap.release()
            break
        
        elif key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        
        
        
delete = Button(window,text="Delete",command=delete)
delete.pack(side = RIGHT)

button = Button(window,text="Print",command=printSomething)
button.pack(side = RIGHT)

button = Button(window,text="Camera",command=printLive)
button.pack(side = TOP)


entry = Entry()
entry.config(font=('Ink Free',50)) 
entry.config(bg='#111111') 
entry.config(fg='#00FF00') 
entry.config(width=10) 
entry.pack()
window.mainloop()


