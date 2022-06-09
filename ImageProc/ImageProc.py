from PIL import Image, ImageDraw, ImageFont
file = input("file: ")
text = input("text: ")
im = Image.open(file)

w = h = 16
font = ImageFont.truetype("msyh.ttc", w)
childImg = Image.new(im.mode, (w, h))
imDst = Image.new(im.mode, (im.width*w, im.height*h))
pen = ImageDraw.Draw(childImg)
textW, textH = font.getsize("嘿")

offsetX = (w - textW) >> 1
offsetY = (h - textH) >> 1


def proc():
    charIndex = 0
    for y in range(im.height):
        for x in range(im.width):
            pen.rectangle((0, 0, w, h), fill="lightgray")
            pen.text((offsetX, offsetY),
                     text[charIndex], font=font, fill=im.getpixel(
                         (x, y)))
            imDst.paste(childImg, (x*w, y*h))
            charIndex += 1
            if charIndex == len(text):
                charIndex = 0
        print(f"真正操作第{y+1}行, 剩{im.height-y-1}行.")
    imDst.save("out.png")
    print("Saving...")


proc()
imDst.show()
