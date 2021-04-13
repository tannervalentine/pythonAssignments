def hourglass():
    print("|", end = "")
    for i in range(10):
        print('\"', end = '')
    print("|")
    for i in range(4):
        print((i+1)*" ", end = "")
        print("\\", end = "")
        for j in range(8-(i*2)):
            print(":", end = "")
        print("/")
    print("     ||")
    for i in range(4):
        print((4-i)*" ", end = "")
        print("/", end = "")
        for j in range(2+(i*2)):
            print(":", end = "")
        print("\\")
    print("|", end = "")
    for i in range(10):
        print("\"", end = "")
    print("|")
hourglass()
