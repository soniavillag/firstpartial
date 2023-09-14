#Write a program that calculates the tip for a meal.
#The user should input the cost of the meal and the percentage of tip they want to give.
#The program should display the total to pay, the tip, and the original cost.
def name():
  print("Hello!, Did you eat at a restaurant today?")
  variable=input()
  print("How much did it cost?")
  number = input()
  print("Do you want me to calculate the 10 percent tip of the total cost?")
  variable= input()
  result=int(number)*.10
  print("The total will be", result)

name()

#BE CAREFUL ABT THE EITHER USING VARIABLE OF NUMBER AND ALSO THE FORMULA INT(NUMBER) PLS
