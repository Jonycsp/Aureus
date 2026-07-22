import csv
import os
from datetime import datetime
from paths import DISCOVERIES_FILE

def save_discovery(
    prime,
    index,
):
    
    found_at = datetime.now().isoformat()
    
    
    # Check if this discovery already exists
    if os.path.exists(DISCOVERIES_FILE):
        
        with open(DISCOVERIES_FILE, "r", newline="") as f:
            
            reader = csv.reader(f)
            
            for row in reader:
                
                if not row:
                    continue
                
                if int(row[0]) == prime:
                    return
    
    # Append the new discovery
    with open(DISCOVERIES_FILE, "a", newline="") as f:
        
        writer = csv.writer(f)
        
        writer.writerow([
            prime,
            index,
            found_at,
        ])

def load_discoveries():
    
    discoveries = []
    
    try:
        
        with open(DISCOVERIES_FILE, "r", newline="") as f:
            
            reader = csv.reader(f)
            
            for row in reader:
                
                if not row:
                    continue
                
                discoveries.append(
                    {
                        "prime": int(row[0]),
                        "index": int(row[1]),
                        "found_at": row[2],
                    }
                )
    
    except FileNotFoundError:
        pass
    
    return discoveries

