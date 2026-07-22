from utils import progress_bar, clear_screen, width, line

def dashboard(
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
        successes,
        largest,
        success_list
        ):
    
    clear_screen()
    
    bar = progress_bar(progress)
    
    line()
    print("AUREUS v0.9".center(width))
    line()
    print()
    
    
    print(" SEARCH ".center(width, "-"))
    print(f"Range           {START:,} → {END:,}")
    print(f"Workload        {workload:,} primes")
    print(f"Current Prime   {p:,}")
    print(f"Prime Index     {global_i:,}")
    
    print()
    
    print(" PROGRESS ".center(width, "-"))
    print(f"{bar} {progress:6.2f}%")
    
    print()
    
    print(" TIME ".center(width, "-"))
    print(f"Elapsed         {elapsed_h:02}h {elapsed_m:02}m {elapsed_s:04.1f}s")
    
    if progress >= 100:
        print("ETA             Completed")
    elif eta_ready:
        print(f"ETA             {eta_h:02}h {eta_m:02}m {eta_s:04.1f}s")
    else:
        print("ETA             Calculating...")
    
    if spi == "DONE":
        print("Avg. Time       DONE")
    else:
        print(f"Avg. Time       {spi} s/prime")
    
    
    print()
    
    print(" RESULTS ".center(width, "-"))
    print(f"Successes       {successes}")
    if largest is None:
        print("Largest         ---")
    else:
        print(f"Largest         {largest:,}")
    
    print()
    
    print(" DISCOVERIES ".center(width, "-"))
    
    if not success_list:
        
        print("---")
    else:
        print("First")
        
        for x in success_list[:2]:
            print(f"• {x:,}")
        
        if len(success_list) > 5:
            print("...")
            print()
        
        print("Recent")
        
        recent = success_list[-5:]
        
        for x in recent:
            print(f"• {x:,}")
    
    
    print()
    
    
    if progress < 100:
        line()
        print("Ctrl + C → Save progress and exit\n(Current iteration will need to be recomputed)".center(width))
        line()
    else:
        line()
        print("Search completed successfully".center(width))
        line()
