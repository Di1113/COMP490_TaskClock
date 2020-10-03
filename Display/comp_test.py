##############################################################
## This test file previews UI design on the 4.2 E-ink board ##
##############################################################


#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd4in2b_V2 Demo")
    
    epd = epd4in2b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    nh_font = ImageFont.truetype('../../../../font/NHaasGroteskTXPro-65Md.ttf', 65)
    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    # font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    #logging.info("1.Drawing on the Horizontal image...") 
    HBlackimage = Image.new('1', (epd.width, epd.height), 255)  # 298*126
    HRYimage = Image.new('1', (epd.width, epd.height), 255)  # 298*126  ryimage: red or yellow image  
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.text((30, 100), 'hello world', font = nh_font, fill = 0)
    #drawblack.text((10, 20), '4.2inch e-Paper bc', font = font24, fill = 0)
    #drawblack.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    #drawblack.line((20, 50, 70, 100), fill = 0)
    #drawblack.line((70, 50, 20, 100), fill = 0)
    #drawblack.rectangle((20, 50, 70, 100), outline = 0)    
    #drawry.line((165, 50, 165, 100), fill = 0)
    #drawry.line((140, 75, 190, 75), fill = 0)
    #drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
    #drawry.rectangle((80, 50, 130, 100), fill = 0)
    #drawry.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)
    
    
    
    #logging.info("3.read bmp file")
    #HBlackimage = Image.open(os.path.join(picdir, '4in2b-b.bmp'))
    #HRYimage = Image.open(os.path.join(picdir, '4in2b-r.bmp'))
    #epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    #time.sleep(2)
    
    
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2b_V2.epdconfig.module_exit()
    exit()
