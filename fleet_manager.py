def view_crew():
    print("crew list:")
    for i in range(len(n)):
        print(n[i] + " - " + r[i])
if opt== "1":
    view_crew()
def add_crew():
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_division = input("Division: ")
    n.append(new_name)
    r.append(new_rank)
    d.append(new_division)
    print("Crew member added.")
if opt == "2":
    add_crew()
def remove_crew():
    rem = input("Name to remove: ")
    if rem in n:
        idx = n.index(rem)
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        print("Removed.")
    else:
        print("no such name found")
