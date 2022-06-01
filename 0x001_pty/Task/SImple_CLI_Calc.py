# bulding a caculator that completes simple arithmetic operations


num1 = input("Enter first number: ")
arithmeticOpp= input("Enter an arithmeticOpp: ")
num2 = input("Enter second number: ")
result=(float(num1) + float(num2)) 


if arithmeticOpp == "+":
    print("result= " + str(float(num1) + float(num2))) 
    
elif arithmeticOpp == "-":
     print("result= " + str(float(num1) - float(num2)))

elif arithmeticOpp == "*":
     print("result= " + str(float(num1) * float(num2)))

elif arithmeticOpp == "/":
     print("result= " + str(float(num1) / float(num2))) 

elif arithmeticOpp == "%":
  print("result= " + str(float(num1) % float(num2)))

else: print("Invalid input")