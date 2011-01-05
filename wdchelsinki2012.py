"""
Screensaver for World Design Capital Helsinki 2012.

Copyright (C) 2011 Juha Autero

"""
import objc

from AppKit import NSImage, NSRectFill
from ScreenSaver import *
from Foundation import NSZeroRect, NSHomeDirectory, NSBundle
import math, random

class Bubble:
  def __init__(self,x=0,y=0,radius=0,text=None):
    self.setValues(x,y,radius,text)
  def setValues(self,x,y,radius,text):
    self.x=x
    self.y=y
    self.radius=radius
    self.text=text

class WDCSaver(ScreenSaverView):
  interval=10.0
  num_bubbles=20

  def startAnimation(self):
    super(WDCServer, self).startAnimation()
    self.bubbles=[None for x in range(self.num_bubbles)]
    self.bubble_index=0
 	  self.setAnimationTimeInterval_(self.interval)
 	  NSColor.whiteColor().set()
 	  NSRectFill(self.bounds())
 	  
  def animateOneFrame(self):
    current_bubble=self.bubbles[self.bubble_index]
    if not current_bubble:
      current_bubble=self.createNewBubble()
      self.bubbles[self.bubble_index]=current_bubble
    if self.checkCollision(current_bubble):
      self.clearBubble(current_bubble)
      self.bubbles[self.bubble_index]=None
    else:
      self.drawBubble(current_bubble)
      current_bubble.radius+=1
      
  def checkCollision(self,bubble1):
    for bubble2 in self.bubbles:
      if bubble1 != bubble2 and self.getDistance(bubble1,bubble2) <= bubble1.radius + bubble2.radius + 1:
        return True
    return False
  
  def getDistance(self,bubble1,bubble2):
    return math.sqrt((bubble1.x-bubble2.x)**2+(bubble1.y-bubble2.y)**2)

  def clearBubble(self,bubble):
    pass
  def createNewBubble(self):
    width=self.bounds().size.width
    height=self.bounds().size.height 
    minx=self.bounds().origin.x
    miny=self.bounds().origin.y
    maxx=minx+width
    maxy=miny+height
    text=self.chooseText()
    bubble=Bubble(random.randrange(minx,maxx),random.randrange(miny,maxy),
      random.randrange(self.minradius,self.maxradius),text)
    while(self.checkCollision(bubble)):
      bubble.setValues(random.randrange(minx,maxx),random.randrange(miny,maxy),
        random.randrange(self.minradius,self.maxradius),text)
    return bubble
  def drawBubble(self,bubble):
    pass