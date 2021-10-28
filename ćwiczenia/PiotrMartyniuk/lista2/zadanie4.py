def przeliczTemp(temp, temp_type):
    if temp >= -273.15:
        if temp_type == 'Fahrenheit' or temp_type == 'f':
            Fahrenheit = (temp * 9 / 5) + 32
            return Fahrenheit
        elif temp_type == 'Rankine' or temp_type == 'r':
            Rankine = (temp + 273.15) * 1.8
            return Rankine
        elif temp_type == 'Kelvin' or temp_type == 'k':
            Kelvin = temp + 273.15
            return Kelvin
        else:
            return "Bad type"
    else:
        return "Invalid temp"

print(przeliczTemp(10,'f'))
print(przeliczTemp(10,'r'))
print(przeliczTemp(10,'k'))