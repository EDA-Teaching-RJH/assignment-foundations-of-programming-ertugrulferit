def init_database():
    n = ["Alice", "Bob", "Jeff", "Catherine", "Muhammed"]
    r = ["Captain", "Engineer", "Commander", "Communications Officer", "Lieutenant"]
    d = ["Navigation", "Engineering", "Operations", "Communications", "Security"]
    i = ["101", "102", "103", "104", "105"]
    return n, r, d, i

def view_crew(n, r):
    print("crew list:")
    for i in range(len(n)):
        print(n[i] + " - " + r[i])

def add_crew(n, r, d):
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_division = input("Division: ")
    n.append(new_name)
    r.append(new_rank)
    d.append(new_division)
    print("Crew member added.")

def main():
    n, r, d, i = init_database()
    
    while True:
        print("\n1. View Crew")
        print("2. Add Crew")
        print("3. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":
            view_crew(n, r)
        elif opt == "2":
            add_crew(n, r, d)
        elif opt == "3":
            print("Shutting down.")
            break

main()