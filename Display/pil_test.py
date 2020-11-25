#################################################
## This test file previews UI design on Pillow ##
#################################################
import sys
import os
import logging
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys
sys.path.append('../Google_Cal')
from quickstart import getCurrEvent

logging.basicConfig(level=logging.DEBUG)
    
def dispMain():
    # Drawing on the image
    logging.info("Drawing")    
    nh_font = ImageFont.truetype('./Fonts/NHaasGroteskTXPro-65Md.ttf', 40)
    nh_it_font = ImageFont.truetype('./Fonts/Neue_Italic.ttf', 15)
        
    eventName = getCurrEvent()    
    HBlackimage = Image.new('1', (400, 300), 255)  # 298*126
    drawblack = ImageDraw.Draw(HBlackimage)
    drawblack.text((30, 100), "Coming up:", font = nh_it_font, fill = 0)
    drawblack.text((30, 120), "Articulation Group", font = nh_font, fill = 0)
    drawblack.text((30, 100), "Coming up:", font = nh_it_font, fill = 0)

    HBlackimage.show()

def dispSubPage():
    pass 

def dispEvtTitle():
def dispTimeInfo():
def dispProgBar():
def dispNotes():
def dispNextEvt():

if __name__ == '__main__':
    # main()
    dispMain()
    exit()
