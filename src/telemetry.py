import csv
from paths import TELEMETRY_FILE

def load_telemetry():
    
    samples = []
    
    try:
        
        with open(TELEMETRY_FILE, "r", newline="") as f:
            
            reader = csv.reader(f)
            
            for row in reader:
                
                if not row:
                    continue
                
                samples.append(
                    {
                        "index": int(row[0]),
                        "prime": int(row[1]),
                        "spi": float(row[2]),
                    }
                )
    
    except FileNotFoundError:
        pass
    
    return samples

