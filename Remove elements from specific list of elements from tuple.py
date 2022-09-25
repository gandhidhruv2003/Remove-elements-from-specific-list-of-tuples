try:
    def extract():
        thistuple = (1,)
        n = int(input("Enter the number of elements you wish to add in tuple: "))
        y = list(thistuple)
        for i in range(n):
            s = int(input("Enter the number you which to add: "))
            y.append(s)
        y.pop(0)
        thistuple = tuple(y)
        l = [0]
        n = int(input("Enter the number of elements you wish to remove from tuple: "))
        for i in range(n):
            num = int(input("Enter the number you wish to remove from the tuple: "))
            l.append(num)
        l.pop(0)
        for x in l:
            if x in y:
                y.remove(x)
        print("Input: " + str(thistuple))
        print("Output: " + str(tuple(y)))
    extract()
except ValueError:
    print("Enter a number")
except:
    print("Enter properly")