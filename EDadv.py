from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("400x250")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()
        status_label.config(text="File encrypted successfully", fg="green")

def decrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()
        status_label.config(text="File decrypted successfully", fg="green")

def clear_entry():
    entry1.delete('1.0', END)

b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=80, y=10)

b2 = Button(root, text="Decrypt", command=decrypt_image)
b2.place(x=180, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=80, y=50)

clear_button = Button(root, text="Clear", command=clear_entry)
clear_button.place(x=200, y=50)

status_label = Label(root, text="", fg="red")
status_label.place(x=80, y=80)

root.mainloop()

