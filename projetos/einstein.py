def calc_emc(): 
    print("Welcome to the Einstein brain simulator")
    print("Discover how much energy you can generate with:")

    c = 300000000  
    m = float(input("m: "))  
    E = m * (c ** 2)

    print("E =", E, "J")

calc_emc()
