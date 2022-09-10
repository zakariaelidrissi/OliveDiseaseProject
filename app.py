import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import model_cl1 as md1
import model_cl2 as md2


# ---------------- Create Window ----------------
window = Tk()
window.geometry("500x500+450+100")
window.title('Olive Disease Detection')
window.configure(background="#333237")
window.resizable(False, False)



# Create function command
def showImage():
    global fln
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image file", filetypes=(
        ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("JPEG File", "*.jpeg")))
    img = Image.open(fln)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    lbl = Label(frame_principal, bg='white')
    lbl.place(x=75, y=65)
    lbl.configure(image=img)
    lbl.image = img


def prediction(url):
    result, proba = md1.predictionCl1(url)
    frame_principal.destroy()
    framePredOne(result, proba)


def checkDisease(url):
    result, proba = md2.predictionCl2(url)
    print("##############################")
    print(result)
    print("##############################")
    frame_pred_one.destroy()
    framePredTwo(result, proba)


def back(frame):
    frame.destroy()
    framePrincipal()


# -----------------------------------------------------

# Create Frame
def framePrincipal():
    global frame_principal
    frame_principal = Frame(window, bg='#333237')
    frame_principal.place(x=1, y=1, width=499, height=499)
    title = Label(frame_principal, text='Olive Disease Detection', bg='white', fg='#04AE62', font=('monospace', 13, 'bold'))
    title.pack(fill=X)

    # Show image Button
    btn = tk.Button(frame_principal, text=" Browse Image ", command=showImage, bg='white',
                    fg='#04AE62', font=('monospace', 9, 'bold'))
    btn.pack(pady=5)

    # First Prediction Button
    pred = Button(frame_principal, text='Prediction', bg='white', fg='#04AE62', width=10,
                  font=('monospace', 9, 'bold'), command=lambda: prediction(fln))
    pred.place(x=160, y=460)

    # Exit Button
    quit_window = Button(frame_principal, text='Exit', bg='white', fg='#04AE62', width=10,
                         font=('monospace', 9, 'bold'), command=lambda: exit())
    quit_window.place(x=260, y=460)



def framePredOne(result, proba):
    global frame_pred_one
    frame_pred_one = Frame(window, bg='#333237')
    frame_pred_one.place(x=1, y=1, width=499, height=499)
    title = Label(frame_pred_one, text='Olive Disease Detection', bg='white', fg='#04AE62',
                  font=('monospace', 13, 'bold'))
    title.pack(fill=X)

    # textArea
    t = Text(frame_pred_one, width=44, height=10, wrap='word')
    t.place(x=75, y=65)

    # Back Button
    back_btn = Button(frame_pred_one, text='Back', bg='white', fg='#04AE62', width=10,
                           font=('monospace', 9, 'bold'), command=lambda: back(frame_pred_one))
    back_btn.place(x=100, y=460)

    # Second Prediction Button
    check_disease = Button(frame_pred_one, text='Check Disease', bg='white', fg='#04AE62', width=12,
                           font=('monospace', 9, 'bold'), command=lambda: checkDisease(fln))

    # Exit Button
    quit_window = Button(frame_pred_one, text='Exit', bg='white', fg='#04AE62', width=10,
                         font=('monospace', 9, 'bold'), command=lambda: exit())
    quit_window.place(x=310, y=460)


    if result == "Olive":
        check_disease.place(x=200, y=460)
        t.delete(0.0, 'end')
        t.insert(0.0, "This image is Olive\n"
                      f"Probability : {proba*100:.0f}%")
    else:
        back_btn.place(x=155, y=460)
        quit_window.place(x=255, y=460)
        t.delete(0.0, 'end')
        t.insert(0.0, "Sorry, this image is not Olive\n"
                      "I can't predict")

def framePredTwo(result, proba):
    global frame_pred_two
    frame_pred_two = Frame(window, bg='#333237')
    frame_pred_two.place(x=1, y=1, width=499, height=499)
    title = Label(frame_pred_two, text='Olive Disease Detection', bg='white', fg='#04AE62',
                  font=('monospace', 13, 'bold'))
    title.pack(fill=X)

    # textArea
    t = Text(frame_pred_two, width=44, height=10, wrap='word')
    t.place(x=75, y=65)


    # Back Button
    back_btn = Button(frame_pred_two, text='Back', bg='white', fg='#04AE62', width=10,
                           font=('monospace', 9, 'bold'), command=lambda: back(frame_pred_two))
    back_btn.place(x=160, y=460)

    # Exit Button
    quit_window = Button(frame_pred_two, text='Exit', bg='white', fg='#04AE62', width=10,
                         font=('monospace', 9, 'bold'), command=lambda: exit())
    quit_window.place(x=260, y=460)

    if result == "Healthy":
        t.delete(0.0, 'end')
        t.insert(0.0, "Type Image : Olive\n"
                      "Type Disease : Healthy\n"
                      f"Probability : {proba*100:.0f}%")

    elif result == "aculus_olearius":
        t.delete(0.0, 'end')
        t.insert(0.0, "Type Image : Olive\n"
                      "Type Disease : Aculus Olearius\n"
                      f"Probability : {proba*100:.0f}%")
    elif result == "olive_peacock_spot":
        t.delete(0.0, 'end')
        t.insert(0.0, "Type Image : Olive\n"
                      "Type Disease : Peacock Spot\n"
                      f"Probability : {proba*100:.0f}%")
    else:
        t.delete(0.0, 'end')
        t.insert(0.0, "Sorry, I don't know this disease\n")


# window principal
framePrincipal()
window.mainloop()

