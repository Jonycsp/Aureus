import csv
from paths import(
    HISTORY_FILE,
    TELEMETRY_FILE,
)

def load_history():
    
    history = {}
    
    try:
        
        with open(HISTORY_FILE, "r") as f:
            
            reader = csv.reader(f)
            
            for row in reader:
                
                if not row:
                    continue
                
                if len(row) != 2:
                    continue
                
                key = row[0]
                runtime = float(row[1])
                
                if key not in history:
                    history[key] = []
                
                history[key].append(runtime)
    
    except FileNotFoundError:
        pass
    
    return history

def save_runtime(
    START,
    END,
    elapsed,
):
    key = f"{START}-{END}"
    
    with open(HISTORY_FILE, "a", newline="") as f:
        
        writer = csv.writer(f)
        
        writer.writerow([key, elapsed])

def save_telemetry(global_i, prime, seconds_per_iteration):
    
    if seconds_per_iteration is None:
        return
    
    with open(TELEMETRY_FILE, "a", newline="") as f:
        
        writer = csv.writer(f)
        
        writer.writerow([
            global_i,
            prime,
            seconds_per_iteration
        ])
