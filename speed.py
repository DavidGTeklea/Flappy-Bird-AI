valid = True
while valid:
    frameRate = input("How fast do you want this program to be? Regular(r), fast(f), or super fast(sf): ")



    if frameRate.lower() != "r" and frameRate.lower() != "f" and frameRate.lower() != "sf":
        valid = True
    else:
        valid = False


