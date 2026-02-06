# 1. Equals Sign: The code used if opt = "1". This is a bug because one = is for giving a value, but you need == to compare things.
# 2. Infinite Loop: The loading screen stayed at 0 forever. I had to add loading += 1 so the loop actually ends.
# 3. List Crash: The code tried to print 10 names even if there were only 4. I changed it to range(len(n)) so it only looks at the names we actually have.
# 4. Missing Data: When adding a crew member, the code only saved the name. I fixed it to append the rank and division as well.
# 5. Remove Crash: If you tried to remove a name that wasn't there, the program crashed. I added an if name in n check to prevent this.
# 6. The "Or" Bug: The code said if rank == "Captain" or "Commander". This is always true in Python. I fixed it to if rank == "Captain" or rank == "Commander".
# 7. Math Printing: You can't print a word and a number together. I had to put str(count) to turn the number into text.
# 8. Not Starting: The function at the bottom didn't have () after the name, so the program never actually started when I clicked run.
# 9. Missing Input: The code had a variable for new_rank but never actually asked the user to type it in. I added the input() prompt.
# 10. Scope Issues: I added the global keyword so the function could actually change the lists stored outside of it.
n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    global n, r, d
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_division = input("Division: ")
            n.append(new_name)
            r.append(new_rank)
            d.append(new_division)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem in n:
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("no such name found")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": 
                    count = count + 1
            print("High ranking officers: " + str(count))
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()
