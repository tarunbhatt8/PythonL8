''' Q.3- Create a Temperature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius. '''

class Temperature:
    ''' class to convert temberatures between fahrenheit and celcius '''
        

    def convertFahrenheit(self,celcius):
        '''method to convert celcius into fahrenheit'''
        return (((9/5)*(celcius))+32)

    def convertCelsius(self,fahrenheit):
        '''method to convert fahrenheit to celsius'''
        return ((fahrenheit-32)*(5/9))

t1=Temperature()
ch='y'
while ch=='y':
    c1=input("Enter 1 to Convert Celcius to Fahrenheit\nEnter 2 to convert Fahrenheit to Celcius\n")
    if c1=='1':
        c=float(input("Enter temperatur in Celcius"))
        f=t1.convertFahrenheit(c)
        print("Temperature in Fahrenheit=",f)
    elif c1=='2':
        f=float(input("Enter temperatur in Fahrenheit"))
        c=t1.convertCelsius(f)
        print("Temperature in Celcius=",c)
    else:
        print("Wrong Input")

    ch=input("Do you want to do more conversions?? y//n: ")

print("Program Ended")
