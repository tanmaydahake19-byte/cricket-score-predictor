Runs=int(input("Enter the number of runs scored: "))

overs=float(input("enter the overs bowled:"))

overs_left=20-overs
balls_left=overs_left*6

print("Overs left:", overs_left)
print("Balls left:", balls_left)

projected_score=(Runs/overs)*overs_left

print("Projected runs:", projected_score)
