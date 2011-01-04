"""
Screensaver for World Design Capital Helsinki 2012.

Copyright (C) 2011 Juha Autero

"""
import objc

from AppKit import NSImage, NSRectFill
from ScreenSaver import *
from Foundation import NSZeroRect, NSHomeDirectory, NSBundle



class WDCSaver(ScreenSaverView):
  interval=10.0

  def startAnimation(self):
    super(AconSaver, self).startAnimation()
 	  self.setAnimationTimeInterval_(self.interval)

  def animateOneFrame(self):
    pass
