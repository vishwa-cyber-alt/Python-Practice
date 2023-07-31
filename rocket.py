location = input("enter rocket location:")
charge = input("enter charge:")
lander = input("enter lander status:")

if location == "outsideearth":
    print("Surround Earth orbit")
elif location == "moonsurface":
    print("Charge solar panel until you surround the Moon orbit.")
if charge == "full":
    print("Reach Moon surface to deploy the lander.")
elif charge == "low":
    print("Recharge")
if lander == "reachedmoon":
    print("Move rover to land that rover use 4 wheels to go.")
