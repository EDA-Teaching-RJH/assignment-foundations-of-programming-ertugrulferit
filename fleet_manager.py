def init_database():
    n = ["Jean-Luc Picard", "William Riker", "Data", "Geordi La Forge", "Beverly Crusher"]
    r = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Commander"]
    d = ["Command", "Command", "Operations", "Operations", "Sciences"]
    i = ["1701", "1702", "1703", "1704", "1705"]
    return n, r, d, i

def display_menu(user_name):
    print(f"\nStarfleet Terminal Active | Officer: {user_name}")
    print("1. Roster | 2. Add | 3. Remove | 4. Payroll | 5. Search")
    print("6. Update | 7. Filter | 8. Count | 9. Exit")
    return input("Select Option: ")

def display_roster(names, ranks, divs, ids):
    print("\n" + "="*55)
    print(f"{'ID':<8} {'NAME':<20} {'RANK':<15} {'DIV':<10}")
    print("-" * 55)
    for i in range(len(names)):
        print(f"{ids[i]:<8} {names[i]:<20} {ranks[i]:<15} {divs[i]:<10}")

def add_member(names, ranks, divs, ids):
    new_id = input("New Service ID: ")
    if new_id in ids:
        print("Error: ID already exists.")
        return

    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    name = input("Name: ")
    rank = input("Rank: ")
    if rank not in valid_ranks:
        print("Invalid Starfleet rank. Entry aborted.")
        return

    names.append(name)
    ranks.append(rank)
    divs.append(input("Division (Command/Operations/Sciences): "))
    ids.append(new_id)

def remove_member(names, ranks, divs, ids):
    rem_id = input("Enter ID to remove: ")
    if rem_id in ids:
        idx = ids.index(rem_id)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member removed.")
    else:
        print("ID not found.")

def calculate_payroll(ranks):
    total = 0
    for rank in ranks:
        if rank == "Captain": total += 1000
        elif rank == "Commander": total += 800
        elif rank == "Lt. Commander": total += 600
        else: total += 400
    return total

def search_crew(names, ranks, divs, ids):
    term = input("Search name: ").lower()
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"[{ids[i]}] {names[i]} - {ranks[i]}")

def update_rank(names, ranks, ids):
    up_id = input("Enter ID to update: ")
    if up_id in ids:
        idx = ids.index(up_id)
        ranks[idx] = input(f"New rank for {names[idx]}: ")
    else:
        print("ID not found.")

def filter_by_division(names, divs):
    choice = input("Enter Division: ")
    print(f"\n--- {choice} Division ---")
    for i in range(len(names)):
        if divs[i] == choice:
            print(f"- {names[i]}")

def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1
    return count

def main():
    n, r, d, i = init_database()
    user = input("Enter Full Name: ")
    
    while True:
        opt = display_menu(user)
        
        if opt == "1": display_roster(n, r, d, i)
        elif opt == "2": add_member(n, r, d, i)
        elif opt == "3": remove_member(n, r, d, i)
        elif opt == "4": print(f"Total Payroll: {calculate_payroll(r)} Credits")
        elif opt == "5": search_crew(n, r, d, i)
        elif opt == "6": update_rank(n, r, i)
        elif opt == "7": filter_by_division(n, d)
        elif opt == "8": print(f"Senior Officers: {count_officers(r)}")
        elif opt == "9":
            print("Logging out...")
            break

main()