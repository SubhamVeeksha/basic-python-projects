c=int(input("Temperature_celsius:"))
f=0
k=0
def temperature_converting(f,k):
    f=(c*(9/5)+32)
    k=273.15+c
    print(f"Temperature in Fahrenheit:{f}")
    print(f"Temperature in Kelvin:{k}")
temperature_converting(f,k)