#################################################
## This test file previews UI design on Pillow ##
#################################################
import sys
import os
import logging
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
    
# Drawing on the image
logging.info("Drawing")    
nh_font = ImageFont.truetype('./Fonts/NHaasGroteskTXPro-65Md.ttf', 65)
#font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
HBlackimage = Image.new('1', (400, 300), 255)  # 298*126
drawblack = ImageDraw.Draw(HBlackimage)
drawblack.text((30, 100), 'hello world', font = nh_font, fill = 0)

# HRYimage = Image.new('1', (400, 300), 255)  # 298*126  ryimage: red or yellow image  
# drawry = ImageDraw.Draw(HRYimage)
# drawblack.line((20, 50, 70, 100), fill = 0)
# drawblack.rectangle((20, 50, 70, 100), outline = 0)    
# drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
# drawry.chord((200, 50, 250, 100), 0, 360, fill = 0)

HBlackimage.show()
# HRYimage.show()

exit()
