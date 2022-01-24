value = int(input("Enter the number"))
new_value = int(value / 2) if value < 100 else -value

print(new_value)
##################################################################

value = int(input("Enter the number"))
new_value = 1 if value < 100 else 0

print(new_value)
##################################################################

value = int(input("Enter the number"))
new_value = True if value < 100 else False

print(new_value)
################################################################


my_str = str(input("Enter the string"))
new_my_str = my_str.upper()

print(new_my_str)
###############################################################


my_str = str(input("Enter the string"))
new_my_str = my_str.lower()

print(new_my_str)
##############################################################


my_str = str(input("Enter the string"))
new_my_str = my_str * 2 if len(my_str) < 5 else my_str

print(new_my_str)
################################################################


my_str = str(input("Enter the string"))
new_my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str

print(new_my_str)