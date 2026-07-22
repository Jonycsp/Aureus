import os
import sys
import shutil
from datetime import datetime
from paths import FULL_VERSION

def terminal_width():
    
    try:
        return shutil.get_terminal_size().columns
    
    except OSError:
        return 80

width = terminal_width()

def line():
    print("=" * width)

def divider():
    print("-" * width)

def format_datetime(timestamp):
    
    if not timestamp:
        return "---"
    
    try:
        
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%d/%m/%Y %H:%M")
    
    except (ValueError, TypeError):
        
        return "---"

def format_time(t):
    hours = int(t // 3600)
    minutes = int((t % 3600) // 60)
    seconds = t % 60
    return hours, minutes, seconds

def short_time(seconds):
    
    h, m, s = format_time(seconds)
    
    if h:
        return f"{h}h {m}m {s:.1f}s"
    elif m:
        return f"{m}m {s:.1f}s"
    else:
        return f"{s:.1f}s"

def clear_screen():
    
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue...")
    clear_screen()

def progress_bar(progress, width=None):
    if width is None:
        width = max(10, terminal_width() - 25)
        
    filled = int(width * progress / 100)
    return "█" * filled + "░" * (width - filled)

def handle_navigation(choice):
    
    choice = choice.strip().lower()
    
    if choice == "q":
        goodbye()
        sys.exit()
    
    return choice == "b"

def goodbye():
    clear_screen()
    
    line()
    print("GOODBYE".center(width))
    line()
    
    print()
    print("Thanks for using Aureus.")
    print()
    print(FULL_VERSION)
    print()