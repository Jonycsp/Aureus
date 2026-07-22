from utils import goodbye
from menus import startup_logo, main_menu
import sys

if __name__ == "__main__":
    try:
        startup_logo()
        main_menu()
    
    except (KeyboardInterrupt, EOFError):
        goodbye()
        sys.exit()
