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
    
    


demo4_floor_and_mod()