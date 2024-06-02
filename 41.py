h=float(input("Enter height in meters : "))
w=float(input("Enter weight in kilograms : "))
b=w/(h*h)
if(b>=30):
    print("Obesity")
elif(b>25 and b<=29):
    print("Overweight")
elif(b>=18.5 and b<=25):
    print("Normal")
elif(b<18.5):
    print("Underweight")

    


     