def init_database():
    n = ["Alice", "Bob", "Jeff", "Catherine", "Muhammed"]
    r = ["Captain", "Engineer", "Commander", "Communications Officer", "Lieutenant"]
    d = ["Navigation", "Engineering", "Operations", "Communications", "Security"]
    i = ["101", "102", "103", "104", "105"]
    return n, r, d, i

def view_crew(names, ranks, ids):
    print("\n--- Current Crew List ---")
    for index in range(len(names)):
        print("ID: " + str(ids[index]) + " | " + names[index] + " - " + ranks[index])

def add_crew(names, ranks, divs, ids):
    new_id = input("New ID: ")
    if new_id in ids:
        print("Error: ID already exists!")
        return
    names.append(input("Name: "))
    ranks.append(input("Rank: "))
    divs.append(input("Division: "))
    ids.append(new_id)
    print("Crew member added.")

def remove_crew(names, ranks, divs, ids):
    rem_id = input("Enter ID to remove: ")
    if rem_id in ids:
        idx = ids.index(rem_id)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Crew member removed.")
    else:
        print("ID not found.")

def calculate_payroll(ranks):
    total_pay = 0
    for rank in ranks:
        if rank == "Captain":
            total_pay += 100001
        elif rank == "Commander":
            total_pay += 80000
        elif rank == "Lieutenant":
            total_pay += 70000
        elif rank == "Engineer":
            total_pay += 99999
        elif rank == "Communications Officer":
            total_pay += 60000
        else:
            total_pay += 500
    return total_pay

def search_crew(names, ids):
    searchid = input("Enter ID to search: ")
    if searchid in ids:
        idx = ids.i(searchid) 
        print("Found: " + names[idx])
    else:
        print("Crew member not found.")

def update_rank(names, ranks, ids):
    updateid = input("Enter ID to update rank: ")
    if updateid in ids:
        idx = ids.index(updateid)
        ranks[idx] = input("Enter new rank for " + names[idx] + ": ")
        print("Rank updated.")
    else:
        print("ID not found.")

def main():
    n, r, d, i = init_database()
    name = input("Login Name: ")
    
    while True:
        print("\nTerminal Active: " + name)
        print("1. View | 2. Add | 3. Remove | 4. Payroll | 5. Search | 6. Update | 7. Exit")
        opt = input("Choice: ")
        
        if opt == "1": view_crew(n, r, i)
        elif opt == "2": add_crew(n, r, d, i)
        elif opt == "3": remove_crew(n, r, d, i)
        elif opt == "4":
            total = calculate_payroll(r)
            print("Total Payroll: $" + str(total))
        elif opt == "5": search_crew(n, i)
        elif opt == "6": update_rank(n, r, i)
        elif opt == "7":
            print("Shutting down...")
            break

main()