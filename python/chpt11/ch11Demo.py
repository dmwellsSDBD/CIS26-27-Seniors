# Variables, Arithmetic, and importing Modules

# Demo 1 - variables and assignment
def demo1_variables():
    CAN_VOLUME = 0.355      # IN LITERS
    BOTTLE_VOLUME = 2.0     # IN LITERS

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six-pack volume:", packVolume, "liters")
    print("Tow-liter bottle:", BOTTLE_VOLUME, "liters")

demo1_variables()

# = means "is set to" or "gets"
lives = 3
print("Lives at start:", lives)
lives = lives + 2       # adding 2 lives to your total
print("After a power-up:", lives)

# ------------------------------------------------------------
# DEMO 3 - Operators and precedence (11.2)
# ------------------------------------------------------------
print("\n\nOperators and precidence:")
def demo3_operators():
    a = 10
    b = 4
    print("a + b / 2 =", a + b / 2)     # 12.0 (division first)
    print("(a + b) / 2 =", (a + b) / 2) # 7.0 
    print("10 - 2 - 3 =", 10 - 2 - 3)   # 5
    print("7 + 4.0 = ", 7 + 4.0)        # 11.0

    # Powers
    print("10 * 2 ** 3 =", 10 * 2 ** 3)  # 80 (** before *)
    print("2 ** 3 ** 2 =", 2 ** 3 ** 2)  # 512 (*** right to left)

    # Compund interest: balance * (1 + rate/100) ** years
    balance = 1000.0
    rate = 5.0
    years = 10
    future = balance * (1 + rate / 100) ** 10
    print("Future value: ", future)

demo3_operators()


# Demo 4 - Floor division and modulus 
print("\n\nFloor Division & Modulus")

def demo4_floor_and_mod():
    print("17 / 5 =", 17 / 5)       # 3.4
    print("17 // 5 =", 17 // 5)     # 3
    print("17 % 5 = ", 17 % 5)      # 2
    
    # Convert a video length in seconds to minutes and seconds
    videoSeconds = 754
    minutes = videoSeconds // 60
    seconds = videoSeconds % 60
    print("Video length:", minutes, "min", seconds, "sec")  # 12 min 34 sec

    # Digit Tricks
    n = 2027
    print("Last digit:", n % 10) # 6
    print("Without last digit:", n // 10)  #202
    print("Even? remainder is:", n % 2)  # 0

demo4_floor_and_mod()

# DEMO 5 - Built-in functions, the math module, roundoff (11.2)
print("\n\nDEMO 5 - Built-in functions, the math module, roundoff (11.2)")

def demo5_functions():
    from math import sqrt, pi

    # Built-in functions: no import need
    print("abs(-42) =", abs(-42))    # 42
    print("round(3.14159) =", round(3.14159))    #  3
    print("round(3.14159, 3) =", round(3.14159, 3))  #  3.142
    print("max(52, 64, 37, 89, 34) =", max(52, 64, 37, 89, 34))  # 89
    print("min(52, 64, 37, 89, 34) =", min(52, 64, 37, 89, 34))  #34

    # math module functions: must be imported
    a = 3 
    b = 4
    hypotenuse = sqrt(a ** 2 + b ** 2)
    print("Hypotenuse:", hypotenuse)       # 5.0

    print("\n\nFind the area of a circle:")
    radius = 2.5
    area = pi * radius ** 2
    print("Circle area:", round(area, 2))  

    print("\n\n Roundoff error: binary can't store 4.35 exactly") 
    price = 4.35
    quantity = 100
    total = price * quantity
    print("Total:", total)
    print("Rounded:", round(total, 2))

demo5_functions()