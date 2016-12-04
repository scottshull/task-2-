def returning():
    print "Returning Customer"
def newcustomer():
    print "New Customer"
def guest():
    print "Hello Guest"

print "[======================]"
print "  1. Returning Customer"
print "  2. New Customer"
print "  3. Guest"
print "[======================]\n"

selection = 0
while selection >= 0:
    try:
        if selection <1 or selection >3:
            selection = int(raw_input("Choose a valid selection:  "))
            continue

        elif selection == 1:
            returning()
            break
        elif selection == 2:
            newcustomer()
            break
        elif selection == 3:
            guest()
            break
        else:
            print "Not a valid selection"
            continue

    except ValueError:
        if selection != 1 or selection != 2 or selection != 3:
            selection = int(raw_input("Please select your customer type\n Enter a number between 1 and 3: "))
        elif selection == 1:
            print "Welcome Back"
            break
        elif selection == 2:
            print "Please Fill out the following information"
            break
        elif selection == 3:
            print "Hello Guest"
            break
