user_temperature_F = input("Enter temperature in degrees Fahrenheit: ")
temperature_F = float(user_temperature_F) #float value allows for decimals in temperature

temperature_C = 5/9 *(temperature_F - 32) #Equation for Fahrenheit to Celsius

print(user_temperature_F, "degrees fahrenheit", "is", temperature_C, "degrees celsius")

#Victor Moreno
#1/29/24
#Program recieves temperature in fahrenheit from input and converts it to temperature in celsius
