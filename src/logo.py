from time import sleep

from paths import FULL_VERSION
from utils import clear_screen, width, line

def startup_logo():
    
    clear_screen()
    
    print(r"""
      /\ 
     /  \      A U R E U S
    / /\ \
   / ____ \     
  /_/    \_\
""")
    
    print(FULL_VERSION.center(width))
    print()
    print("Ad astra per veritatem.".center(width))
    print()
    print("Initializing...")
    
    sleep(1.5)
    
    clear_screen()

def menu_logo():
    
    print(r"""
     _                              
    / \   _   _ _ __ ___ _   _ ___
   / _ \ | | | | '__/ _ \ | | / __|
  / ___ \| |_| | | |  __/ |_| \__ \
 /_/   \_\\__,_|_|  \___|\__,_|___/
""")
    
    print(FULL_VERSION.center(width))
    line()
    print()
