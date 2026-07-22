import json
import os
import sys
from sympy import primerange
from datetime import datetime
from paths import(
    SAVE_FILES,
    AUTOSAVE_TMP,
    AUTOSAVE_FILE,
    CURRENT_SORT,
    SORT_NAMES,
)
from utils import(
    clear_screen,
    format_datetime,
    pause,
    format_time,
    width,
    line,
    divider,
    goodbye,
)

def slot_path(slot):
    
    if not 1 <= slot <= len(SAVE_FILES):
        raise ValueError("Invalid slot number.")
    
    return SAVE_FILES[slot - 1]

def load_slot(slot):
    
    path = slot_path(slot)
    
    try:
        
        with open(path, "r") as f:
            
            data = json.load(f)
            
            if not data:
                return None
            
            return data
    
    except (FileNotFoundError, json.JSONDecodeError):
        
        return None

def slot_empty(slot):
    
    return load_slot(slot) is None

def delete_slot(slot):
    
    path = slot_path(slot)
    
    with open(path, "w") as f:
        
        json.dump({}, f, indent=4)

def default_save_name(slot):
    return f"Save Slot {slot}"

def ask_save_name(slot, old):
    
    clear_screen()
    
    line()
    print("SAVE NAME".center(width))
    line()
    print()
    
    if old is None:
        
        default = default_save_name(slot)
        
        print("Enter a name for this save.")
        print()
        print(f"Press ENTER to use: \"{default}\"")
        print()
    
    else:
        
        default = old.get("name", default_save_name(slot))
        
        print(f'Current name: "{default}"')
        print()
        print("Enter a new name.")
        print("Press ENTER to keep the current name.")
        print()
    
    while True:
    
        name = input("> ").strip()
        
        if name == "":
            return default
        
        if len(name) > 50:
            
            print()
            print("Please keep the name under 50 characters.")
            continue
        
        return name

def save_slot(
    slot,
    start,
    end,
    local_i,
    global_i,
    elapsed,
    successes,
    workload,
):
    
    path = slot_path(slot)
    
    # Read existing save (if any)
    old = load_slot(slot)
    
    now = datetime.now().isoformat()
    
    if old is None:
        created = now
    else:
        created = old.get("created", now)
    
    name = ask_save_name(slot, old)
    
    data = {
        "name": name,
        
        "created": created,
        "modified": now,
        
        "start": start,
        "end": end,
        
        "local_i": local_i,
        "global_i": global_i,
        
        "elapsed": elapsed,
        
        "successes": successes,
        
        "workload": workload,
    }
    
    with open(path, "w") as f:
        
        json.dump(
            data,
            f,
            indent=4,
        )

def list_slots(sort_by="slot"):
    
    slots = []
    
    for slot in range(1, 5):
        
        data = load_slot(slot)
        
        slots.append(
            {
                "slot": slot,
                "empty": data is None,
                "data": data,
            }
        )
    
    if sort_by == "name":
        
        slots.sort(
            key=lambda s:
                (
                    s["empty"],
                    "" if s["empty"] else s["data"]["name"].lower()
                )
        )
    
    elif sort_by == "slot":
        
        slots.sort(
            key=lambda s: s["slot"]
        )
    
    elif sort_by == "modified":
        
        slots.sort(
            key=lambda s:
                (
                    s["empty"],
                    "" if s["empty"] else s["data"]["modified"]
                ),
            reverse=True,
        )
    
    elif sort_by == "discoveries":
        
        slots.sort(
            key=lambda s:
                (
                    s["empty"],
                    0 if s["empty"] else len(s["data"]["successes"])
                ),
            reverse=True,
        )
    
    elif sort_by == "progress":
        
        slots.sort(
            key=lambda s:
                (
                    s["empty"],
                    0 if s["empty"] else
                    100 * s["data"]["local_i"] / s["data"]["workload"]
                ),
            reverse=True,
        )
    
    return slots

def save_autosave(
    START,
    END,
    local_i,
    global_i,
    elapsed,
    good,
    workload,
    save_slot_id,
):
    
    data = {
        "start": START,
        "end": END,
        "local_i": local_i,
        "global_i": global_i,
        "elapsed": elapsed,
        "saved_at": datetime.now().isoformat(),
        "successes": good,
        "workload": workload,
        "save_slot_id": save_slot_id,
    }
    
    with open(AUTOSAVE_TMP, "w") as f:
        json.dump(data, f, indent=4)
        f.flush()
        os.fsync(f.fileno())
    
    os.replace(AUTOSAVE_TMP, AUTOSAVE_FILE)

def load_autosave():
    
    try:
        with open(AUTOSAVE_FILE, "r") as f:
            return json.load(f)
            
    except (FileNotFoundError, json.JSONDecodeError):
        
        return None

def clear_autosave():
    
    try:
        os.remove(AUTOSAVE_FILE)
    except FileNotFoundError:
        pass

def choose_save_slot(mode, allow_main_menu=False):
    
    while True:
        
        clear_screen()
        
        
        slots = list_slots(CURRENT_SORT)
        
        line()
        print("SAVE FILES".center(width))
        line()
        print()
        
        for slot in slots:
            
            divider()
            
            if slot["empty"]:
                
                print(f'{slot["slot"]}) ○ Empty')
                print()
            
            else:
                
                data = slot["data"]
                
                workload = data.get("workload")
                
                if workload:
                    progress = 100 * data["local_i"] / workload
                else:
                    progress = 0
                
                h, m, s = format_time(data["elapsed"])
                
                print(f'{slot["slot"]}) ● {data["name"]}')
                print(f'    Last saved : {format_datetime(data["modified"])}')
                print(f'    Range      : {data["start"]:,} → {data["end"]:,}')
                print(f'    Progress   : {progress:.2f}%')
                
                largest = max(data["successes"]) if data["successes"] else None
                
                print(f'    Elapsed      : {h}h {m}m {s:.1f}s')
                print(f'    Discoveries  : {len(data["successes"])}')
                
                if largest is None:
                    print("    Largest PIFP : ---")
                else:
                    print(f"    Largest PIFP : {largest:,}")
                
                print(f"    Prime Index  : {data['global_i']:,}")
                
                print()
        
        if mode == "load" and autosave_exists():
            
            session = load_autosave()
            
            print()
            divider()
            print("Recovery")
            print()
            print("A) Autosave")
            print(f"   Range        : {session['start']:,} → {session['end']:,}")
            print(f"   Discoveries  : {len(session['successes'])}")
        
        divider()
        print()
        print("Choose a slot (1-4)")
        print("S → Sort Saves")
        print("R → Rename Save")
        print("D → Delete Save")
        print()
        if allow_main_menu:
            print("M → Return to the Main Menu")
        print("B → Back")
        print("Q → Quit")
        print()
        
        
        choice = input("> ").strip().lower()
        
        if choice in ("1", "2", "3", "4"):
            
            slot = int(choice)
            
            saved = load_slot(slot)
            
            if mode == "load":
                
                if saved is None:
                    
                    clear_screen()
                    
                    line()
                    print("SAVE SLOT".center(width))
                    line()
                    print()
                    print("That save slot is empty.")
                    print()
                    
                    pause()
                    
                    continue
                
                return slot
            
            elif mode == "save":
                return slot
        
        elif choice == "m" and allow_main_menu:
            return "menu"
        
        elif choice == "a" and mode == "load":
            
            if autosave_exists():
                return "autosave"
            
            clear_screen()
            print("No autosave found.")
            pause()
        
        elif choice == "s":
            
            sort_menu()
            
            continue
        
        elif choice == "r":
            
            rename_slot_menu()
            
            continue
        
        elif choice == "d":
            
            delete_slot_menu()
            
            continue
        
        elif choice == "b":
            return None
        
        elif choice == "q":
            goodbye()
            sys.exit()
        
        else:
            clear_screen()
            
            print("Invalid choice.")
            pause()

def delete_slot_menu():
    
    while True:
        
        clear_screen()
        
        slots = list_slots(CURRENT_SORT)
        
        line()
        print("DELETE SAVE".center(width))
        line()
        print()
        
        for slot in slots:
            
            if slot["empty"]:
                print(f"{slot['slot']}) ○ Empty")
            else:
                print(f"{slot['slot']}) ● {slot['data']['name']}")
        
        print()
        print("Choose a slot to delete.")
        print()
        print("B → Back")
        print("Q → Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        if choice == "b":
            return
        
        elif choice == "q":
            goodbye()
            sys.exit()
        
        elif choice in ("1", "2", "3", "4"):
            
            slot = int(choice)
            
            if slot_empty(slot):
                
                clear_screen()
                
                print("That slot is already empty.")
                print()
                
                pause()
                
                continue
            
            confirm_delete(slot)
        
        else:
            
            print("Invalid choice.")
            pause()

def rename_slot_menu():
    
    while True:
        
        clear_screen()
        
        slots = list_slots(CURRENT_SORT)
        
        line()
        print("RENAME SAVE".center(width))
        line()
        print()
        
        for slot in slots:
            
            if slot["empty"]:
                print(f"{slot['slot']}) ○ Empty")
            else:
                print(f"{slot['slot']}) ● {slot['data']['name']}")
        
        print()
        print("Choose a slot to rename.")
        print()
        print("B → Back")
        print("Q → Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        if choice == "b":
            return
        
        elif choice == "q":
            goodbye()
            sys.exit()
        
        elif choice in ("1", "2", "3", "4"):
            
            slot = int(choice)
            
            if slot_empty(slot):
                
                clear_screen()
                print("That slot is empty.")
                print()
                
                pause()
                
                continue
            
            confirm_rename(slot)
        
        else:
            
            print("Invalid choice.")
            pause()

def confirm_rename(slot):
    
    data = load_slot(slot)
    
    old_name = data["name"]
    
    new_name = ask_save_name(slot, data)
    
    if new_name == old_name:
        return
    
    data["name"] = new_name
    data["modified"] = datetime.now().isoformat(timespec="seconds")
    
    with open(slot_path(slot), "w") as f:
        
        json.dump(
            data,
            f,
            indent=4,
        )
    
    clear_screen()
    
    line()
    print("SAVE RENAMED".center(width))
    line()
    print()
    print("✓ Save renamed successfully.")
    print()
    
    print(f"Old name : {old_name}")
    print(f"New name : {new_name}")
    
    print()
    
    pause()

def confirm_delete(slot):
    
    data = load_slot(slot)
    
    while True:
        
        clear_screen()
        
        line()
        print(f"DELETE SAVE SLOT {slot}".center(width))
        line()
        print()
        
        print(f"● {data['name']}")
        print()
        print(f"Last saved : {format_datetime(data['modified'])}")
        print(f"Range      : {data['start']:,} → {data['end']:,}")
        print(f"Discoveries: {len(data['successes'])}")
        print()
        
        divider()
        print()
        print("This action cannot be undone.")
        print()
        print("Delete this save?")
        print()
        print("Y → Yes")
        print("N → No")
        print()
        
        choice = input("> ").strip().lower()
        
        if choice == "y":
            
            delete_slot(slot)
            
            clear_screen()
            
            line()
            print("SAVE DELETED".center(width))
            line()
            print()
            print("✓ Save deleted.")
            print()
            
            pause()
            
            return
        
        elif choice == "n":
            return
        
        else:
            print("Invalid choice.")
            pause()

def sort_menu():
    
    global CURRENT_SORT
    
    while True:
        
        clear_screen()
        
        line()
        print("SORT SAVES".center(width))
        line()
        print()
        
        print(f"Current sort: {SORT_NAMES[CURRENT_SORT]}")
        print()
        
        print("1) Slot Number")
        print("2) Name (A–Z)")
        print("3) Last Modified")
        print("4) Progress")
        print("5) Discoveries")
        print()
        
        print("B → Back")
        print("Q → Quit")
        print()
        
        choice = input("> ").strip().lower()
        
        if choice == "1":
            CURRENT_SORT = "slot"
            print(f"✓ Saves will now be sorted by {SORT_NAMES[CURRENT_SORT]}.")
            pause()
            return
        
        elif choice == "2":
            CURRENT_SORT = "name"
            print(f"✓ Saves will now be sorted by {SORT_NAMES[CURRENT_SORT]}.")
            pause()
            return
        
        elif choice == "3":
            CURRENT_SORT = "modified"
            print(f"✓ Saves will now be sorted by the last time they were modified.")
            pause()
            return
        
        elif choice == "4":
            CURRENT_SORT = "progress"
            print(f"✓ Saves will now be sorted by {SORT_NAMES[CURRENT_SORT]}.")
            pause()
            return
        
        elif choice == "5":
            CURRENT_SORT = "discoveries"
            print(f"✓ Saves will now be sorted by {SORT_NAMES[CURRENT_SORT]}.")
            pause()
            return
        
        elif choice == "b":
            return
        
        elif choice == "q":
            goodbye()
            sys.exit()
        
        else:
            print("Invalid choice.")
            pause()

def autosave_exists():
    
    return load_autosave() is not None
