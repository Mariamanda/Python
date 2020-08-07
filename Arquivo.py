print("Today's date?")
date = input()

print("Breakfast calories?")
first_number = int(input())

print("Lunch calories?")
seconde_number = int(input())

print("Dinner calories?")
third_number = int(input())

print("Snake calories?")
bedroom_number = int(input())

sum = first_number + seconde_number + third_number + bedroom_number
print("Calorie content for " + date + ":" + str(sum))