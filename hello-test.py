# Print the following

print('hey, welcome you all!!!')

# Print the following by passing the variable

variable = 'hi, I am coming from variable'
print(variable)

# Print the value by using runtime input and using format to append  into the string

name = input('Please enter your name: ')
message= 'hey {} how are you!!'.format(name)
print(message)

# Scenario 1: add two number. the output is concatinated!
# first_value = 10, second_value = 20, then the print(result) is 1020. Because input of the default type is string

first_value = input('Enter the first number to add: ')
second_value = input('Enter the Second number to add: ')
add = first_value+second_value
result = 'The sum of {} and {} is {}'.format(first_value,second_value,add)
print(result)


# Scenario 2: add two number. Doing typecasting
# first_value = 10, second_value = 20, then the print(result) is 30.

first_value = input('Enter the first number to add: ')
second_value = input('Enter the Second number to add: ')
add = int(first_value)+int(second_value)
result = 'The sum of {} and {} is {}'.format(first_value,second_value,add)
print(result)
