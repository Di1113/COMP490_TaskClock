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
from quickstart import *

logging.basicConfig(level=logging.DEBUG)
    
def dispMain():
    # Drawing on the image
    logging.info("Drawing")    
    nh_font = ImageFont.truetype('./Fonts/NHaasGroteskTXPro-65Md.ttf', 40)
    nh_it_font = ImageFont.truetype('./Fonts/Neue_Italic.ttf', 15)
        
    event = getNextEvt()
    eventName = getEvtTitle(event)    
    HBlackimage = Image.new('1', (400, 300), 255)  # 298*126
    drawblack = ImageDraw.Draw(HBlackimage)
    drawblack.text((30, 100), "Coming up:", font = nh_it_font, fill = 0)
    # drawblack.text((30, 120), "Articulation Group", font = nh_font, fill = 0)
    drawblack.text((30, 120), eventName, font = nh_font, fill = 0)

    HBlackimage.show()

def dispSubPage():
    # HBlackimage = Image.new('1', (400, 300), 255) 
    HBlackimage = Image.new('RGB', (400, 300), "#FFFFFF") 
    drawblack = ImageDraw.Draw(HBlackimage)
    event = getNextEvt()
    if eventGoingOn(event): 
        dispEvtTitle(drawblack, event)
        dispTimeInfo(drawblack, event)
        dispProgBar(drawblack)
        dispNotes(drawblack, event)
        dispNextEvt(drawblack, event)
    else: 
        dispRestPage(drawblack)

    HBlackimage.show()

def dispRestPage(canvas):
    nh_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 40)    
    nh_it_font = ImageFont.truetype('../Display/Fonts/Neue_Italic.ttf', 15)
    canvas.text((30, 120), "Rest Period.", font = nh_font, fill = 0)
    canvas.text((30, 180), "No task.", font = nh_it_font, fill = 0)

def dispEvtTitle(canvas, event):
    nh_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 40)
    eventName = getEvtTitle(event)  
    canvas.text((30, 30), eventName, font = nh_font, fill = 0)

def dispTimeInfo(canvas, event):
    nh_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 15)    
    stTimeOb = getEvtStartTime(event)
    endTimeOb = getEvtEndTime(event)
    currEvtTimeInfo = getStEndTimeText(stTimeOb, endTimeOb)
    currEvtCountDown = getEndCtDn(endTimeOb)
    timeinfo = currEvtTimeInfo + " End in " + currEvtCountDown
    canvas.text((30, 90), timeinfo, font = nh_font, fill = 0)

def dispProgBar(canvas):
    past_block = 12
    past_block_coord = ()
    rest_block = 24 - past_block
    for i in range(past_block):
        x0 = 30 + i * 14
        x1 = 38 + i * 14
        canvas.rectangle([x0, 120, x1, 134], fill="#000000", outline=None, width=None)
        past_block_coord = (x0 + 14, x1 + 14)
    for i in range(rest_block):
        x0, x1 = past_block_coord
        x1 -= 2
        canvas.rectangle([x0 + i * 14, 122, x1 + i * 14, 132], fill="#B22222", outline=None, width=None)

def dispNotes(canvas, event):
    title_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 15)    
    notes_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 10)    
    currEvtNotes = getEvtNotes(event)
    canvas.text((30, 160), "Notes:", font = title_font, fill = 0)
    canvas.text((50, 180), currEvtNotes, font = notes_font, fill = 0)

def dispNextEvt(canvas, event):
    title_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 15)    
    notes_font = ImageFont.truetype('../Display/Fonts/NHaasGroteskTXPro-65Md.ttf', 10)    
    folEvt = getFolEvt()
    folEvtTitle = getEvtTitle(folEvt)
    folEvtStartIn = getFolEvtCtDn(folEvt)
    folinfo = folEvtTitle + " in " + folEvtStartIn + "."
    canvas.text((30, 220), "Next:", font = title_font, fill = 0)
    canvas.text((50, 240), folinfo, font = notes_font, fill = 0)

if __name__ == '__main__':
    # main()
    dispMain()
    # dispSubPage()
    exit()
