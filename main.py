#Jaunel Deans
#November 3, 2023
#Modifying the code so that the user can see even number products from 0 - 12

number = int(input("Please input number to see the product of even numbers from 0 to 12: "))#Ask the user to input a number to see if the even number products from 0 to 12
counter = 0 # Set the counter to 0 so I can get the even number products 

while counter < 13:
  product = (number * counter)#Created the variable product and assigned the value of the number inputted times the counter. 
  print(str(number) + " multiplied by " + str(counter) + " equals " + str(product) + ".")#Edit the print statment to say the value of 'number' multiplied by 'counter' equals 'product'
  counter = counter + 2 #set counter to increase by 2 instead of one so the even number products are only printed
print('The loop has finished')#When the while loop conditional no longer true, the loop ends and the print statment will run and output "The loop has finished".