from utils import (
    clear_screen,
    pause,
    width,
    line,
    divider,
)
from paths import VERSION, CODENAME, FULL_VERSION

def about():
    
    clear_screen()
    
    line()
    print("AUREUS".center(width))
    print(FULL_VERSION.center(width))
    line()
    print()
    
    print("Prime-Indexed Fibonacci Prime Research Application")
    print()
    
    print(
        "Aureus is an open research project dedicated to the search,\n"
        "discovery, and analysis of Prime-Indexed Fibonacci Primes (PIFPs)."
    )
    print()
    
    print(
        "The project combines efficient searching, statistical analysis,\n"
        "performance telemetry, resumable sessions, and persistent save\n"
        "management into a single modular application."
    )
    
    print()
    divider()
    print("Current Features")
    divider()
    
    print("✓ Live search dashboard")
    print("✓ Runtime history")
    print("✓ Performance telemetry")
    print("✓ Autosave")
    print("✓ Save slots")
    print("✓ Resume interrupted searches")
    print("✓ Session persistence")
    print("✓ Statistical analysis")
    print("✓ Custom search ranges")
    
    print()
    divider()
    print("Project")
    divider()
    
    print(f"Version : v{VERSION}")
    print(f"Codename: {CODENAME}")
    print("Language : Python")
    print("Libraries: SymPy")
    
    print()
    divider()
    print("Created by")
    divider()
    
    print("Created by\nJony C.S.P.")
    print("Developed with ChatGPT")
    
    print()
    line()
    print()
    
    print("Ad astra per veritatem.")
    print('"To the stars through truth."')
    
    print()
    
    pause()

