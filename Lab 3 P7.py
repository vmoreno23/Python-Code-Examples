print("Note: Sunday will be day 0, Monday day 1, etc.")#Gives user knowledge of the format for input 
user_start_day = input("Enter starting day number (0-6): ")
starting_day = int(user_start_day) #Converts string value to integer value 

user_length_stay = input("Enter the length of your stay: ")
trip_length = int(user_length_stay) #Converts string value to integer value

if trip_length >= 7:
    length_computed = (starting_day + trip_length)- 7 #if the length of the trip is equal to or higher than 7 days, it will subtract 7 since the week is limited from 0 to 6
else:
    length_computed = starting_day + trip_length #if the trip length is less than 7 days, it will add trip length to starting day without subtraction involved

print("You will return on day:", length_computed)

#Victor Moreno
#1/30/24
#Program recieves the starting day and trip length from user input and calculates which day the user will return
