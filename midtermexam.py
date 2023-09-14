#Robot's name is Juan :D
#Vibration Machine is $20,000 and has a 10% discount
#Thermal Shock Machine is $16,500 
#Temperatur Machine is $15,000 
#How much is it for all of them to add a 10% extra discount at the end?

def name():
  print("Hello! My name is Juan!, Do you need help calculating the price of machines?")
  variable = input()
  print("OK, What's the price of the first machine?")
  number= input()
  print("Does the first machine have a discount and if yes, of how much?")
  discount = input ()
  result = int(number) - int(number)*.10
  print("The final price of the first machine will be", result)
  variable = input()
  print("What's the price for the second machine?")
  second = input()
  print("What's the price for the third machine?")
  third = input()
  answer = int(result) + int(second) + int(third)
  print("This will be your total amount", answer)
  print("Do you have an extra discount in the total amount?")
  variable = input()
  print("Of how much?")
  extra = input()
  total = int(answer) - int(answer)*.10
  print("OK, this will be your final price to pay with an extra discount", total)
  variable = input()

name()
  
  
