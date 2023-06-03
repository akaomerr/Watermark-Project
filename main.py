from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

root = Tk()
root.title("Image Watermarking App")
root.geometry("1350x700")
frame = ttk.Frame(root, padding=50)
frame.grid()
empty_frame = Frame(root, width=1000, height=650)
empty_frame.grid(column=0, row=0, columnspan=10, rowspan=10)

raw_img = None
resized_img = None
watermark_photo = None

def resizer_func(img, hor, ver):
    img_resize = Image.open(img)
    resized_img = img_resize.resize((hor, ver))
    return resized_img

def watermark_func():
    global watermark_photo
    if watermark_photo is not None:
        text_color = text_color_entry.get()
        font_x = int(font_x_entry.get())
        font_y = int(font_y_entry.get())
        font_size = int(font_size_entry.get())
        watermark_text = watermark_text_entry.get()
        font = ImageFont.truetype("arial.ttf", font_size)
        watermark_position = (font_x, font_y)
        draw = ImageDraw.Draw(watermark_photo)
        draw.text(watermark_position, watermark_text, fill=text_color, font=font)
        watermark_img=ImageTk.PhotoImage(watermark_photo)
        loaded_watermarked_label=Label(root, image=watermark_img)
        loaded_watermarked_label.image=watermark_img
        loaded_watermarked_label.grid(column=0, row=0, columnspan=10, rowspan=10)



def load_image():
    global raw_img, resized_img, watermark_photo, loaded_photo
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global raw_img_width, raw_img_height
        raw_img = Image.open(file_path)
        raw_img_width=int(raw_img.size[0])
        raw_img_height=int(raw_img.size[1])
        resized_img = resizer_func(file_path, 1000, 650)
        watermark_photo = resized_img.copy()
        global loaded_image_label
        loaded_photo = ImageTk.PhotoImage(resized_img)
        loaded_image_label = Label(root, image=loaded_photo)
        loaded_image_label.image = loaded_photo
        loaded_image_label.grid(column=0, row=0, columnspan=10, rowspan=10)

def save_image():
    global watermark_photo
    if watermark_photo is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if save_path:
            watermark_photo_resize=watermark_photo.resize((raw_img_width, raw_img_height))
            watermark_photo_resize.save(save_path)
            print("Image saved successfully.")


def delete_watermark_func():
    global watermark_photo
    loaded_image_label=Label(root, image=loaded_photo)
    loaded_image_label.image=loaded_photo
    loaded_image_label.grid(row=0, column=0, rowspan=10, columnspan=10)
colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Orange": "#FFA500",
    "Purple": "#800080",
    "Pink": "#FFC0CB",
    "Brown": "#A52A2A",
    "Turquoise": "#40E0D0",
    "Gold": "#FFD700",
    "Lime": "#00FF00",
    "Indigo": "#4B0082",
    "Teal": "#008080",
    "Olive": "#808000",
    "Maroon": "#800000",
    "Navy": "#000080",
    "Silver": "#C0C0C0",
    "Gray": "#808080",
    "Crimson": "#DC143C",
    "Violet": "#EE82EE",
    "Cyan": "#00FFFF",
    "Magenta": "#FF00FF",
    "SlateBlue": "#6A5ACD",
    "SandyBrown": "#F4A460",
    "HotPink": "#FF69B4",
    "DarkGreen": "#006400",
    "CornflowerBlue": "#6495ED",
    "Chocolate": "#D2691E"
}


save_button = Button(root, text="Save Settings", command=save_image)
save_button.grid(row=10, column=4, pady=10, padx=5)

add_button = Button(root, text="Add Image", command=load_image)
add_button.grid(row=10, column=5, pady=10, padx=5)

color_label=Label(root, text="Choose the color of watermark:")
color_label.grid(row=0, column=10)
text_color_entry = ttk.Combobox(root, values=list(colors.keys()))
text_color_entry.grid(row=0, column=11)

font_x_label=Label(root, text="Set the x-position of the watermark:")
font_x_label.grid(row=1, column=10)
font_x_entry = Entry(root)
font_x_entry.grid(row=1, column=11)

font_y_label=Label(root, text="Set the y-position of the watermark:")
font_y_label.grid(row=2, column=10)
font_y_entry = Entry(root)
font_y_entry.grid(row=2, column=11)

font_size_label=Label(root, text="Set the font size of the watermark:")
font_size_label.grid(row=3, column=10)
font_size_entry = Entry(root)
font_size_entry.grid(row=3, column=11)

watermark_text_label=Label(root, text="Enter the text what you want:")
watermark_text_label.grid(row=4, column=10)
watermark_text_entry = Entry(root)
watermark_text_entry.grid(row=4, column=11)

watermark_button = Button(root, text="Add Watermark", command=watermark_func)
watermark_button.grid(row=6, column=10)

delete_watermark_button=Button(root, text="Delete Watermarks", command=delete_watermark_func)
delete_watermark_button.grid(row=6, column=11)


root.mainloop()
