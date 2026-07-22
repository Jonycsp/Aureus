#imports
import sys
from datetime import datetime
from utils import(
    format_time,
    clear_screen,
    pause,
    handle_navigation,
    short_time,
    line,
    divider,
    width,
    goodbye,
)
from history import load_history
from search import(
    run_search,
)
from discoveries import(
    load_discoveries,
)
from telemetry import(
    load_telemetry,
)
from save_manager import(
    load_slot,
    choose_save_slot,
    clear_autosave,
    load_autosave,
    autosave_exists,
)
from about import about
from logo import startup_logo, menu_logo

DEFAULT_workload = 10000
DEFAULT_START = 2
DEFAULT_END = 10000


def search_menu(history):
    
    #startup
    line()
    print(" Prime-Indexed Fibonacci Prime Search".center(width))
    line()
    print()
    
    print(f"Default workload: {DEFAULT_workload:,}")
    
    print()
    
    #known runtimes (menu)
    if history:
        
        print("Known runtimes:\n")
        
        for key in sorted(history):
            
            runs = history[key]
            
            average = sum(runs) / len(runs)
            
            h, m, s = format_time(average)
            
            if h:
                text = f"{h} h {m} min {s:.1f} s"
            elif m:
                text = f"{m} min {s:.1f} s"
            else:
                text = f"{s:.1f} s"
            
            start, end = key.split("-")
            
            display = f"{int(start):,} → {int(end):,}"
            
            print(
                f"{display:<18} -> {text}"
                f"  ({len(runs)} run{'s' if len(runs) != 1 else ''})"
            )
    else:
        
        print("Known runtimes: None")
    
    print()
    
    #other menu stuff
    while True:
        
        line()
        print("Search mode".center(width))
        line()
        print()
        
        print("1) Search from 2 to an upper workload")
        print("2) Search a custom range")
        print()
        print("B) Back")
        print("Q) Quit")
        print()
        
        mode = input("> ").strip()
        
        clear_screen()
        
        if mode == "1":
            
            START = DEFAULT_START
            
            back = False
            
            while True:
                
                clear_screen()
                
                line()
                print("Upper workload".center(width))
                line()
                print()
                print(f"ENTER → {DEFAULT_END:,}")
                print("B    → Back")
                print("Q    → Quit")
                print()
                
                user = input("> ").strip().lower()
                
                MAX_END = 10_000_000
                
                if handle_navigation(user):
                    back = True
                    break
                
                try:
                    if user == "":
                        END = DEFAULT_END
                    else:
                        END = int(user)
                    
                    if END > MAX_END:
                        clear_screen()
                        print(f"Maximum upper limit is {MAX_END:,}.")
                        pause()
                        continue
                    
                    if END >= 2:
                        START = DEFAULT_START
                        break
                
                except ValueError:
                    pass
                
                print("\nPlease enter an integer greater than 1.")
                pause()
            
            if back:
                clear_screen()
                continue
            
            return START, END
        
        
        elif mode == "2":
            
            back = False
            
            while True:
                
                clear_screen()
                
                line()
                print("Custom Range".center(width))
                line()
                print()
                print("B    → Back")
                print("Q    → Quit")
                print()
                
                start_input = input("Start\n> ").strip()
                
                if handle_navigation(start_input):
                    back = True
                    break
                
                end_input = input("\nEnd\n> ").strip()
                
                if handle_navigation(end_input):
                    back = True
                    break
                
                try:
                    start = int(start_input)
                    end = int(end_input)
                    
                    if start >= 2 and end > start:
                        START = start
                        END = end
                        break
                
                except ValueError:
                    pass
                
                print("\nInvalid range.")
                pause()
            
            if back:
                clear_screen()
                continue
            
            return START, END
        
        elif mode == "b":
            return None
        
        elif mode == "q":
            goodbye()
            sys.exit()
        
        else:
            clear_screen()
            
            print("Invalid choice.\n")
            pause()

def resume_menu(session):
    
    if session is None:
        print("No saved session found.")
        
        pause()
        
        return
    
    line()
    print("Saved session detected.".center(width))
    line()
    print()
    
    print(f"Range      : {session['start']:,} → {session['end']:,}")
    print(f"Global idx : {session['global_i']:,}")
    print(f"Elapsed    : {session['elapsed']:.1f} s")
    print(f"Successes  : {len(session['successes'])}")
    
    print()
    
    while True:
        
        choice = input("[R]esume    [D]iscard    [M]enu : ").strip().lower()
        
        clear_screen()
        
        if choice in ("r", "d", "m"):
            break
    
    if choice == "r":
        
        return session
    
    elif choice == "d":
        
        clear_autosave()
        print("\nSession discarded.")
        
        pause()
        
        return
    
    elif choice == "m":
        
        
        return

def autosave_menu(session):
    
    
    while True:
        
        clear_screen()
        
        line()
        print("AUTOSAVE FOUND".center(width))
        line()
        print()
        
        print("An autosave file was found.")
        print("It contains an interrupted search.")
        print()
        
        print(f"Range      : {session['start']:,} → {session['end']:,}")
        print(f"Global idx : {session['global_i']:,}")
        print(f"Elapsed    : {session['elapsed']:.1f} s")
        print(f"Successes  : {len(session['successes'])}")
        
        print()
        divider()
        print()
        
        print("Y → Resume autosave")
        print("N → Continue to save slots")
        print("B → Back")
        print("Q → Quit")
        print()
        
        
        choice = input("> ").strip().lower()
        
        if choice == "y":
            return "autosave"
        
        if choice == "n":
            return "slots"
        
        if choice == "b":
            return None
        
        if choice == "q":
            goodbye()
            sys.exit()
        
            print("Invalid choice.")
            pause()

def runtime_history_menu():
    
    history = load_history()
    
    clear_screen()
    
    line()
    print("RUNTIME HISTORY".center(width))
    line()
    print()
    
    if not history:
        
        print("No runtime history recorded.")
    
    else:
        
        print(
            f"{'Range':<22}"
            f"{'Runs':>6}"
            f"{'Average':>14}"
            f"{'Fastest':>14}"
            f"{'Slowest':>14}"
        )
        
        divider()
        
        for key in sorted(
            history,
            key=lambda k: int(k.split("-")[1])
        ):
            
            times = history[key]
            
            runs = len(times)
            
            average = sum(times) / runs
            fastest = min(times)
            slowest = max(times)
            
            start, end = key.split("-")
            display = f"{int(start):,} → {int(end):,}"
            
            print(
                f"{display:<22}"
                f"{runs:>6}"
                f"{short_time(average):>14}"
                f"{short_time(fastest):>14}"
                f"{short_time(slowest):>14}"
            )
    
    print()
    pause()

def discoveries_menu():
    
    discoveries = load_discoveries()
    
    clear_screen()
    
    line()
    print("DISCOVERIES".center(width))
    line()
    print()
    
    if not discoveries:
        
        print("No discoveries recorded.")
    
    else:
        
        print(
            f"{'ID':<5}"
            f"{'Prime':>12}"
            f"{'Index':>12}"
            f"{'Date':>18}"
        )
        
        divider()
        
        for i, d in enumerate(discoveries, start=1):
            
            dt = datetime.fromisoformat(d["found_at"])
            date = dt.strftime("%d/%m/%Y")
            
            print(
                f"{i:<5}"
                f"{d['prime']:>12,}"
                f"{d['index']:>12,}"
                f"{date:>18}"
            )
        
        print()
        divider()
        print(f"Total discoveries : {len(discoveries)}")
        print(f"Largest prime     : {discoveries[-1]['prime']:,}")
    
    print()
    pause()

def telemetry_menu():
    
    samples = load_telemetry()
    
    clear_screen()
    
    line()
    print("TELEMETRY".center(width))
    line()
    print()
    
    if not samples:
        
        print("No telemetry recorded.")
    
    else:
        
        spi = [x["spi"] for x in samples]
        
        print(f"Samples recorded : {len(samples):,}")
        print()
        print(f"Average s/prime  : {sum(spi)/len(spi):.7f}")
        print(f"Fastest sample   : {min(spi):.7f}")
        print(f"Slowest sample   : {max(spi):.7f}")
    
    print()
    pause()

def statistics_menu():
    
    while True:
        
        clear_screen()
        
        line()
        print("STATISTICS".center(width))
        line()
        print()
        
        print("1) Runtime History")
        print("2) Discoveries")
        print("3) Telemetry")
        print()
        print("B) Back")
        print("Q) Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        if handle_navigation(choice):
            return
        
        if choice == "1":
            runtime_history_menu()
        
        elif choice == "2":
            discoveries_menu()
        
        elif choice == "3":
            telemetry_menu()
        
        else:
            clear_screen()
            
            print("Invalid choice.")
            pause()

def main_menu():
    
    while True:
        
        history = load_history()
        
        clear_screen()
        
        menu_logo()
        
        print("1) New Search")
        
        if autosave_exists():
            print("2) Resume Search (Autosave Found!)")
        else:
            print("2) Resume Search")
        
        print("3) Statistics")
        print("4) About")
        print()
        print("Q) Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        clear_screen()
        
        if choice == "1":
            result = search_menu(history)
            
            if result is None:
                continue
            
            START, END = result
            
            clear_screen()
            
            print(f"Searching from {START:,} to {END:,}\n")
            
            #see if there are known runtimes in the history log
            key = f"{START}-{END}"
            
            if key in history:
                    
                    avg = sum(history[key]) / len(history[key])
                    
                    h, m, s = format_time(avg)
                    
                    print(f"Previous average runtime: {h}h {m}m {s:.1f}s")
            else:
                
                print("No previous runtime recorded.")
            
            print()
            
            input("Press ENTER to begin...")
            
            run_search(
                START,
                END,
                save_slot_id=None,
            )
        
        elif choice == "2":
            
            if autosave_exists():
                
                session = load_autosave()
                
                result = autosave_menu(session)
                
                if result == "autosave":
                    
                    run_search(
                        session["start"],
                        session["end"],
                        local_i=session["local_i"],
                        global_i=session["global_i"],
                        elapsed_before=session["elapsed"],
                        good=session["successes"],
                        save_slot_id=session.get("save_slot_id"),
                    )
                    
                    continue
                
                elif result is None:
                    continue
            
            
            slot = choose_save_slot("load")
            
            if slot is None:
                continue
            
            if slot == "autosave":
                
                session = load_autosave()
                
                clear_autosave()
                
                run_search(
                session["start"],
                session["end"],
                local_i=session["local_i"],
                global_i=session["global_i"],
                elapsed_before=session["elapsed"],
                good=session["successes"],
                save_slot_id=session.get("save_slot_id"),
                )
                
                continue
            
            
            saved = load_slot(slot)
            
            run_search(
                saved["start"],
                saved["end"],
                local_i=saved["local_i"],
                global_i=saved["global_i"],
                elapsed_before=saved["elapsed"],
                good=saved["successes"],
                save_slot_id=slot,
            )
        
        elif choice == "3":
            
            statistics_menu()
        
        elif choice == "4":
            
            about()
        
        elif choice == "q":
            
            goodbye()
            break
        
        else:
            
            print("Invalid choice.")
            
            pause()
