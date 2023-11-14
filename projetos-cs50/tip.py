
def main ():
    dollars = dollars_to_float(input("How Much was the meal? "))
    percent = percent_to_float(input("What Percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollar_str):
    try:
        dollars = float(dollar_str.replace ("$"," "))
        return dollars
    except ValueError:
        print("Please entrer a valid number for the meal cost")
        return 0.0
    
def percent_to_float(percent_str):
    try:
        percent = float (percent_str.replace('%'," ")) / 100.00
        return percent
    except ValueError:
        print("Please, entrer a valid number for the tip percentage")
        return 0.0
main()