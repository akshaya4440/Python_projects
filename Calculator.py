def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        print("Error!, Division by Zero")
    else: 
        return x/y
        
print("Select Operation: ") 
print("1.Additiom")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice=input("Enter choice (1,2,3,4):")
    if choice in ("1","2","3","4"):
        try:
            x=float (input("Enter 1st number:"))
            y=float(input("Enter 2nd number:"))
        except ValueError:
            print("Invalid input!")   
            continue 
        
        if choice=="1":
            print(f"The result is:{add(x,y)}")
        elif choice=="2":
            print(f"The result is:{subtract(x,y)}")
        elif choice=="3":
            print(f"The result is:{multiply(x,y)}")    
        elif choice=="4":
            print(f"The result is:{division(x,y)}")    
    else:
        print ("Invalid choise!")
    next_op=input ("Do uou want to calculate again? (yes/no):").lower()
    if next_op!="yes":
        break  
               
print("Thankyou for using the calculator!")               