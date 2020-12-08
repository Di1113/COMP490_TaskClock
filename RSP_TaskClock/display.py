##############################################################
##############################################################


#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

sys.path.append('/home/pi/Documents/Comps/TaskClock/waveshare_epd_lib')
import logging
from waveshare_epd_lib import epd4in2b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

sys.path.append('g_cal')
from quickstart import * 

def disp_main():
    sys.path.append('.')
    logging.basicConfig(level=logging.DEBUG)

    try:
        logging.info("Task Clock Main Page Demo")
        
        epd = epd4in2b_V2.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        #time.sleep(1)
        
        # Drawing on the image
        logging.info("Drawing")    
        nh_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 40)
        nh_it_font = ImageFont.truetype('font/Neue_Italic.ttf', 15)
       
        # get google calendar event 
        event = getNextEvt()
        eventName = getEvtTitle(event)

        HBlackimage = Image.new('1', (epd.width, epd.height), 255)  # 298*126
        drawblack = ImageDraw.Draw(HBlackimage)
        drawblack.text((30, 130), eventName, font = nh_font, fill = 0)
        drawblack.text((30, 100), "Coming up:", font = nh_it_font, fill = 0)
        
        HRYimage = Image.new('1', (epd.width, epd.height), 255)  # 298*126  ryimage: red or yellow image  
        drawry = ImageDraw.Draw(HRYimage)
        
        epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
        time.sleep(10)
        
        
        
        # logging.info("3.read bmp file")
        # HBlackimage = Image.open(os.path.join(picdir, '4in2b-b.bmp'))
        # HRYimage = Image.open(os.path.join(picdir, '4in2b-r.bmp'))
        # epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
        # time.sleep(2)
        
        
        #logging.info("Clear...")
        #epd.init()
        #epd.Clear()
        
        #logging.info("Goto Sleep...")
        #epd.sleep()
        #epd.Dev_exit()
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2b_V2.epdconfig.module_exit()
        exit()

def disp_sub():
    sys.path.append('.')
    logging.basicConfig(level=logging.DEBUG)

    try:
        logging.info("Task Clock Sub-Page Demo")
        
        epd = epd4in2b_V2.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        #time.sleep(1)
        
        # Drawing on the image
        logging.info("Drawing")  

        HBlackimage = Image.new('1', (epd.width, epd.height), 255) 
        drawblack = ImageDraw.Draw(HBlackimage)

        HRYimage = Image.new('1', (epd.width, epd.height), 255)  # 298*126  ryimage: red or yellow image  
        drawry = ImageDraw.Draw(HRYimage)

        event = getNextEvt()

        if eventGoingOn(event): 
            dispEvtTitle(drawblack, event)
            dispTimeInfo(drawblack, event)
            dispProgBar(drawblack, drawry)
            dispNotes(drawblack, event)
            dispNextEvt(drawblack, event)
        else: 
            dispRestPage(drawblack, drawry)
       
        epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
        time.sleep(10)
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2b_V2.epdconfig.module_exit()
        exit()

def dispRestPage(blackcanvas, redcanvas):
    nh_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 40)    
    nh_it_font = ImageFont.truetype('font/Neue_Italic.ttf', 15)
    blackcanvas.text((30, 130), "Rest Period.", font = nh_font, fill = 0)
    redcanvas.text((30, 180), "No task.", font = nh_it_font, fill = 0)

def dispEvtTitle(canvas, event):
    nh_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 40)
    eventName = getEvtTitle(event)  
    canvas.text((30, 30), eventName, font = nh_font, fill = 0)

def dispTimeInfo(canvas, event):
    nh_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 15)    
    stTimeOb = getEvtStartTime(event)
    endTimeOb = getEvtEndTime(event)
    currEvtTimeInfo = getStEndTimeText(stTimeOb, endTimeOb)
    currEvtCountDown = getEndCtDn(endTimeOb)
    timeinfo = currEvtTimeInfo + " End in " + currEvtCountDown
    canvas.text((30, 90), timeinfo, font = nh_font, fill = 0)

def dispProgBar(blackcanvas, redcanvas):
    past_block = 13
    past_block_coord = ()
    rest_block = 24 - past_block
    for i in range(past_block):
        x0 = 30 + i * 14
        x1 = 38 + i * 14
        blackcanvas.rectangle([x0, 120, x1, 134], fill="#000000", outline=None, width=None)
        past_block_coord = (x0 + 14, x1 + 14)
    for i in range(rest_block):
        x0, x1 = past_block_coord
        x1 -= 2
        redcanvas.rectangle([x0 + i * 14, 122, x1 + i * 14, 132], fill="#000000", outline=None, width=None)

def dispNotes(canvas, event):
    title_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 15)    
    notes_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 12)    
    currEvtNotes = getEvtNotes(event)
    canvas.text((30, 160), "Notes:", font = title_font, fill = 0)
    canvas.text((50, 190), currEvtNotes, font = notes_font, fill = 0)

def dispNextEvt(canvas, event):
    title_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 15)    
    notes_font = ImageFont.truetype('font/NHaasGroteskTXPro-65Md.ttf', 12)    
    folEvt = getFolEvt()
    folEvtTitle = getEvtTitle(folEvt)
    folEvtStartIn = getFolEvtCtDn(folEvt)
    folinfo = folEvtTitle + " in " + folEvtStartIn + "."
    canvas.text((30, 220), "Next:", font = title_font, fill = 0)
    canvas.text((50, 250), folinfo, font = notes_font, fill = 0)


