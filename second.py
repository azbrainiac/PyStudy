aName = input("Please enter yo name ")
print("Your name is", aName.upper(), "and has length", len(aName))

sradius = input("Enter radius: ")
radius = float(sradius)
diameter = 2 * radius
print("diameter ", diameter, sep="=")

sage = input("Enter yo age: ")
age = int(sage)
print("%s is %d years old." % (aName, age))

sUserItem = input("Input your favourite item: ")

sCost = input("How does cost a %s? " % (sUserItem))
priceUserItem = int(sCost)

print("The %s costs %d$" % (sUserItem, priceUserItem))
print("The %+10s costs %5.2f$" % (sUserItem, priceUserItem))
print("The %+10s costs %10.2f$" % (sUserItem, priceUserItem))

itemDict = {"item": sUserItem, "cost": priceUserItem}

print("The %(item)s costs %(cost)7.1f$" % itemDict)

input("Press Enter")