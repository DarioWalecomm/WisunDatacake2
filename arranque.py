# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:18:24 2023

@author: Dario
"""
import os
import time
UARTSENT = "COM9" # configuracion del puerto al que se hace referencia 
#C:\Users\Dario\Downloads\PYSPINELWatterMeter1.0\
os.system("python spinelcli.py -u "+UARTSENT)
time.sleep(30)
os.system("Network")



        
            
    