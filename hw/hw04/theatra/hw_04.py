
def temp_converter():
    temp_c = int(input('Please enter the value in Celsius you want to convert: '))

    if temp_c < -273.15:
        print("Temperature below absolute zero (-273.15)")
    else:
        temp_f = (temp_c * 9/5) + 32
        print(temp_f)

temp_converter()


