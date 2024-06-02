a = ["Sydney","Melbourne","Brisbane","Perth"]
u= ["Dubai","Abu Dhabi","Sharjah","Ajman"]
I= ["Mumbai","Bangalore","Chennai","Delhi"]
s=input("Enter 1st city name:")
p=input("Enter 2nd city name:")
if((s in a and p in a) or (s in u and p in u) or(s in I and p in I)):
    print("Both cities are in India")
else:
    print("They don't belong to the same country")