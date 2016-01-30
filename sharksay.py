import sys
import os.path
import textwrap
from PIL import Image, ImageFont, ImageDraw

def sharksay(message):
    lines = textwrap.wrap(message.replace('\t','  '), 40)
    message = '\n'.join(lines)

    image_path =  os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            'static/businessoptics-mascot.png'
            )
    shark = Image.open(image_path)

    image = Image.new("RGBA", (20*30+270,max(256,70+25*len(lines))), (255,255,255))
    image.paste(shark, (0,0))
    usr_font = ImageFont.truetype("resources/DejaVuSans.ttf", 20)
    d_usr = ImageDraw.Draw(image)

    text_size = d_usr.textsize(message, usr_font)
    d_usr.polygon([
        (220, 100),
        (250, 60),
        
        (250, 40),
        (265+text_size[0], 40),
        
        (265+text_size[0], 60+text_size[1]),
        (250, 50+text_size[1]+10),
        (250, 80),
        (220, 100),
        ],
        '#919191',
        '#919191'
        )
    d_usr.text((255, 50), message, fill='white', font=usr_font)

    image = image.crop((0, 0, 275+text_size[0], max(256, 70+text_size[1])))

    return image

if __name__ == '__main__':
    image = sharksay(sys.stdin.read())
    image.show()
