from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

raw_img=""
def resizer_func(img, hor, ver):
    raw_img=Image.open(img)
    resized_img=raw_img.resize((hor,ver))
    return resized_img

# def watermarker_func(img, text, text_x, text_y):  Kullanıcı isterse renklendirebilecek bu butonları da halletmek gerek.
#     watermark_font=ImageFont.truetype("arial.ttf",30)
#     copied_img=img.copy()
#     draw_img=ImageDraw.Draw(copied_img)
#     draw_img.text((text_x,text_y), text, font=watermark_font)
#     copied_img.save("watermarked_img.jpg")


root=Tk()

root.title("Image Watermarking App")
root.geometry("1200x700")
frame=ttk.Frame(root, padding=50)
frame.grid()
empty_frame = Frame(root, width=1000, height=650)
empty_frame.grid(column=0, row=0, columnspan=10, rowspan=10)



def save_func():
    label2=Label(root, text="Button Clicked!\n")
    label2.grid(column=11,row=0)


def load_image():
    global raw_img
    file_path=filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global raw_img
        raw_img=Image.open(file_path)
        loaded_image=resizer_func(file_path, 1000,650)
        loaded_photo=ImageTk.PhotoImage(loaded_image)
        loaded_image_label=Label(root, image=loaded_photo)
        loaded_image_label.image=loaded_photo
        loaded_image_label.grid(column=0, row=0, columnspan=10, rowspan=10)


def save_image():
    global raw_img
    if raw_img:
        save_path=filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if save_path:
            raw_img.save(save_path)
            print("Image saved successfully.")




save_button=Button(root, text="Save Settings", command=save_image)
save_button.grid(row=10, column=4, pady=10, padx=5)
add_button=Button(root, text="Add Image", command=load_image)
add_button.grid(row=10, column=5, pady=10, padx=5)




root.mainloop()
