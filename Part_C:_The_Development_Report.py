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
 # PART_C_2
#The Problem:
# Using parallel lists is risky because the only thing connecting a name to an ID is their position in the list (the index).
# If you delete a name from the names list but forget to delete the ID from the ID list, everything shifts.
# The person at the top might end up with someone else's rank or ID, which ruins the whole database.

#The Fix:
# In my fleet_manager.py code, I made sure that every time I use .pop(), I use it on every single list at the same time using the same index variable.
# By doing this in one step, the "rows" always stay aligned and the data stays correct.