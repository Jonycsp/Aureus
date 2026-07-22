#imports
import sys
import time
from datetime import datetime
from sympy import(
    primerange,
    fibonacci,
    isprime,
)
from utils import(
    format_time,
    pause,
    clear_screen,
    format_datetime,
    line,
    divider,
    width,
    goodbye,
)
from dashboard import dashboard
from history import(
    save_runtime,
    save_telemetry,
)
from save_manager import(
    save_autosave,
    clear_autosave,
    choose_save_slot,
    slot_empty,
    load_slot,
    save_slot,
    delete_slot,
)
from discoveries import save_discovery

def interrupt_search(
    START,
    END,
    local_i,
    global_i,
    elapsed,
    good,
    workload,
    save_slot_id=None,
):
    
    # If this search already belongs to a save slot,
    # update it automatically.
    if save_slot_id is not None:
        
        save_slot(
            save_slot_id,
            START,
            END,
            local_i,
            global_i,
            elapsed,
            good,
            workload,
        )
        
        clear_autosave()
        
        return "SAVE"
    
    # Otherwise ask the user what to do.
    while True:
        
        clear_screen()
        
        line()
        print("SEARCH INTERRUPTED".center(width))
        line()
        print()
        
        print("What would you like to do?")
        print()
        
        print("1) Save to Save Slot")
        print("2) Autosave & Return to Main Menu")
        print("3) Resume Search")
        print()
        print("Q) Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        if choice == "1":
            break
        
        elif choice == "2":
            
            save_autosave(
                START,
                END,
                local_i,
                global_i,
                elapsed,
                good,
                workload,
                save_slot_id,
            )
            
            clear_screen()
            
            line()
            print("AUTOSAVE UPDATED".center(width))
            line()
            print()
            print("✓ Progress saved to autosave.")
            print()
            pause()
            
            return "MENU"
        
        elif choice == "3":
            return "CONTINUE"
        
        elif choice == "q":
            goodbye()
            sys.exit()
        
        else:
            print("Invalid choice.")
            pause()
    
    # Save Slot workflow
    while True:
        
        slot = choose_save_slot("save", allow_main_menu=True)
        
        if slot == "menu":
            clear_autosave()
            return "MENU"
        
        if slot is None:
            return "CONTINUE"
        
        if slot_empty(slot):
            break
        
        clear_screen()
        
        line()
        print(f"SAVE SLOT {slot}".center(width))
        line()
        print()
        
        data = load_slot(slot)
        
        print(f"● {data['name']}")
        print()
        print(f"Last saved : {format_datetime(data['modified'])}")
        print(f"Range      : {data['start']:,} → {data['end']:,}")
        print(f"Discoveries: {len(data['successes'])}")
        print()
        
        divider()
        print()
        
        print("Overwrite this save?")
        print()
        print("Y → Yes")
        print("N → No")
        print()
        
        while True:
            
            choice = input("> ").strip().lower()
            
            if choice in ("y", "n"):
                break
            
            print("Invalid choice.")
        
        if choice == "y":
            break
    
    save_slot(
        slot,
        START,
        END,
        local_i,
        global_i,
        elapsed,
        good,
        workload,
    )
    
    clear_autosave()
    
    clear_screen()
    
    line()
    print("SEARCH INTERRUPTED".center(width))
    line()
    print()
    print("✓ Progress has been saved.")
    print("✓ Resume is available from the main menu.")
    print()
    print("Only the current iteration will need to be recomputed.")
    line()
    
    pause()
    
    return "SAVE"

#define the main program function
def run_search(
    START,
    END,
    local_i=0,
    global_i=None,
    elapsed_before=0,
    good=None,
    save_slot_id=None,
):
    
    try:
        
        start = time.time() - elapsed_before
        
        all_primes = list(primerange(START, END + 1))
        search_primes = [p for p in all_primes if p >= START]
        workload = len(search_primes)
        if global_i is None:
            global_i = len(all_primes) - len(search_primes)
        
        # Collect all successful prime-indexed primes
        if good is None:
            good = []
        checkpoints = []
        iteration_times = []
        
        resume_local_i = local_i
        
        for local_i, p in enumerate(
            search_primes[resume_local_i:],
            start=resume_local_i + 1,
            ):
            
            global_i += 1
            
            if p < START:
                continue
            
            if local_i % 25 == 0:
                
                elapsed = time.time() - start
                
                if save_slot_id is None:
                    save_autosave(
                        START,
                        END,
                        local_i,
                        global_i,
                        elapsed,
                        good,
                        workload,
                        save_slot_id,
                    )
                
                checkpoints.append({
                "index": local_i,
                "elapsed": elapsed
            })
                
                recent = iteration_times[-5:]
                
                if recent:
                    seconds_per_iteration = sum(recent) / len(recent)
                else:
                    seconds_per_iteration = None
                
                if seconds_per_iteration is not None:
                    save_telemetry(
                        global_i,
                        p,
                        seconds_per_iteration
                    )
                
                if len(checkpoints) >= 2:
                    
                    old = checkpoints[-2]
                    new = checkpoints[-1]
                    
                    delta_i = new["index"] - old["index"]
                    delta_t = new["elapsed"] - old["elapsed"]
                    
                    iteration_times.append(delta_t / delta_i)
                    
                    recent = iteration_times[-5:]
                    
                    seconds_per_iteration = sum(recent) / len(recent)
                    
                    remaining = workload - local_i
                    
                    eta = remaining * seconds_per_iteration
                
                else:
                    
                    eta = 0
                
                if len(checkpoints) < 2:
                    progress = 0
                    eta = None
                else:
                    
                    old = checkpoints[-2]
                    new = checkpoints[-1]
                    
                    delta_i = new["index"] - old["index"]
                    delta_t = new["elapsed"] - old["elapsed"]
                    
                    iteration_times.append(delta_t / delta_i)
                    
                    recent = iteration_times[-5:]
                    
                    seconds_per_iteration = sum(recent) / len(recent)
                    
                    remaining = workload - local_i
                    
                    eta = remaining * seconds_per_iteration
                    
                    progress = 100 * local_i / workload
                
                elapsed_h, elapsed_m, elapsed_s = format_time(elapsed)
                
                if eta is None:
                    eta_h = eta_m = eta_s = 0
                else:
                    eta_h, eta_m, eta_s = format_time(eta)
                
                if len(checkpoints) < 2:
                    eta_ready = False
                    eta_h = eta_m = 0
                    eta_s = 0
                else:
                    eta_ready = True
                    eta_h, eta_m, eta_s = format_time(eta)
                
                if seconds_per_iteration is None:
                    spi = "---"
                else:
                    spi = f"{seconds_per_iteration:.7f}"
                
                dashboard(
                    START,
                    END,
                    workload,
                    progress,
                    p,
                    global_i,
                    elapsed_h,
                    elapsed_m,
                    elapsed_s,
                    eta_h,
                    eta_m,
                    eta_s,
                    eta_ready,
                    spi,
                    len(good),
                    max(good) if good else None,
                    good,
                )
                
                elapsed = time.time() - start
            
            if isprime(global_i) and isprime(fibonacci(p)):
                
                good.append(p)
                
                save_discovery(
                    p,
                    global_i,
                )
                
                if len(good) > 1:
                    gap = good[-1] - good[-2]
                    ratio = good[-1] / good[-2]
                else:
                    gap = None
        
        
        line()
        print("RATIO ANALYSIS".center(width))
        line()
        
        print(f"{'Previous':>10} {'Next':>10} {'Gap':>8} {'Ratio':>10} {'Relative Gap':>15}")
        
        divider()
        
        for a, b in zip(good, good[1:]):
            
            gap = b - a
            ratio = b / a
            relative = gap / a
            
            print(
                f"{a:>10} {b:>10} {gap:>8} {ratio:>10.4f} {relative:>15.4f}"
            )
        
        end = time.time()
        
        elapsed = end - start
        
        hours, minutes, seconds = format_time(elapsed)
        
        dashboard(
        START,
        END,
        workload,
        100,
        p,
        global_i,
        hours,
        minutes,
        seconds,
        0,
        0,
        0,
        True,
        "DONE",
        len(good),
        max(good) if good else None,
        good
        )
        
        print ()
        
        if hours > 0:
            print(f"Time taken: {hours} h {minutes} min {seconds:.2f} s")
        elif minutes > 0:
            print(f"Time taken: {minutes} min {seconds:.2f} s")
        else:
            print(f"Time taken: {seconds:.2f} s")
        
        save_runtime(
            START,
            END,
            elapsed,
            )
        
        pause()
        
        clear_autosave()
        
        if save_slot_id is not None:
            delete_slot(save_slot_id)
        
        return {
            "elapsed": elapsed,
            "successes": good,
            "workload": workload,
        }
    
    except KeyboardInterrupt:
        
        elapsed = time.time() - start
        
        action = interrupt_search(
            START,
            END,
            local_i,
            global_i,
            elapsed,
            good,
            workload,
            save_slot_id,
        )
        
        if action == "SAVE":
            return
        
        elif action == "CONTINUE":
            return run_search(
                START,
                END,
                local_i=local_i - 1,
                global_i=global_i - 1,
                elapsed_before=elapsed,
                good=good,
                save_slot_id=save_slot_id,
            )
        
        elif action == "MENU":
            return
