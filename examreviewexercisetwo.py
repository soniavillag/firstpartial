#Create a program that converts a temperature in degrees Celsius to Fahrenheit. 
#The user should input the temperature in Celsius, and the program will display 
#the equivalent temperature in Fahrenheit and Kelvin.

def name():
  print("Hi, how are you?")
  variable = input()
  print("Ok, how is the weather today?")
  number = input()
  print("Would you like to know how much is that in Fahrenheit?")
  variable = input()
  result = int(number)+32
  print("The result will be", result)
  print("Would you like to know how much is the original degrees Kelvin?")
  variable = input()
  answer = int(number)+273.15
  print("The result will be", answer)

name()
