from PIL import Image, ImageDraw, ImageFont

def resizer_func(img, hor, ver):
    raw_img=Image.open(img)
    resized_img=raw_img.resize((hor,ver))
    resized_img.save(f"resized_{img}")

def watermarker_func(img, text, text_x, text_y):# Kullanıcı isterse renklendirebilecek bu butonları da halletmek gerek.
    raw_img=Image.open(img)
    watermark_font=ImageFont.truetype("arial.ttf",30)
    copied_img=raw_img.copy()
    draw_img=ImageDraw.Draw(copied_img)
    draw_img.text((text_x,text_y), text, font=watermark_font)
    copied_img.save(f"watermarked_{img}")


img_url=input("Enter the image name:\n")
# hor=int(input("Enter the horizontal size of the image:\n"))
# ver=int(input("Enter the vertical size of the image:\n"))
# resizer_func(img_url, hor, ver)

watermark_text=input("Enter anything:\n")
text_x=int(input("Enter the X-Position what you want:\n"))
text_y=int(input("Enter the Y-Position what you want:\n"))
watermarker_func(img_url, watermark_text,text_x , text_y)