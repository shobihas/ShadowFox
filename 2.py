y = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
p={
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
y1=sum(list(y.values()))
p1=sum(list(p.values()))
print("Your Total expenses : ",y1)
print("Your Partner's Total expenses : ",p1)
if(y1>p1):
    print("You spent more money ")
elif(y1==p1):
     print("You and your partner spent the same amount overall.")
else:
    print("Your partner spent more money")

s= max(y,key=lambda x: abs(y[x]-p[x]))
d= abs(y[s]-p[s])
print("The expense category with significant difference is:", s)
print("The difference in spending is:", d)