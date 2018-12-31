# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:12:38 2018

@author: sujeeth.kumaravel
Tests the Plino_Spam_Detector function
"""
from spam_detector_plino import spam_detector_plino

text = 'You won one million dollars. Open email and click link to get the money.'

r = spam_detector_plino(text)

print(r)

