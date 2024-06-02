a = ["Sydney","Melbourne","Brisbane","Perth"]
u= ["Dubai","Abu Dhabi","Sharjah","Ajman"]
I= ["Mumbai","Bangalore","Chennai","Delhi"]
s=input("Enter a city name:")
if s in a:
    print(s,"is in Australia")
elif(s in u):
    print(s,"is in UAE")
else:
    print(s,"is in India")