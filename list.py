justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
#1
print("The number of members in the Justice League = ",len(justice_league))
print(justice_league)
#2.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding of new members ")
print(justice_league)
#3.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)
#4.
justice_league.remove('Superman')
justice_league.insert(4, 'Superman')
print(justice_league)
#5.
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)
#6.
justice_league.sort()
print(justice_league)
print("New Leader : ",justice_league[0])