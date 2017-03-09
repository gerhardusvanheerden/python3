print("Coding Exercise 5")
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f

for t in temperatures:
    file=open("txt_temperatures.txt","a")
    file.write(str(c_to_f(t) ) + "\n")
    file.close()
    
