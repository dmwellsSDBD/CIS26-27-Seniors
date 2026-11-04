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
