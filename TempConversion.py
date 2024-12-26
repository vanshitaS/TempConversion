#Temperature Conversion
# 0 Celsius=32 Fahrenheit
# 9/5=1.8
# F=(C*(9/5))+32
# C=(F-32*(5/9))


unit= input("Is this temperature in Celsius or Fahrenheit (C/F):")
temp=float(input("Enter the temperature:"))

if unit=="C":
    temp=round((9*temp)/5+32)
    print(f"The Temperature in Fahrenheit is:{temp}F")

elif unit=="F":
    temp=round((temp-32)*5/9)
    print(f"The Temperature in Celsius is:{temp}C")  

else:
    print(f"Enter proper unit of measurment")