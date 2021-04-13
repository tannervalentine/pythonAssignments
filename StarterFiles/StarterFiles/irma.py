import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    data = open("data/irma.csv", "r")
    for line in data:
        if "Date" in line:
            pass
        else:
            line=line.split(",")
            line = line[2:5]
            lat = float(line[0])
            lon = float(line[1])
            wind = float(line[2])
            if wind < 74:
                cat = 0
            elif 74 <= wind <= 95:
                cat = 1
            elif 96 <= wind <= 110:
                cat = 2
            elif 111 <= wind <= 129:
                cat =3
            elif 130 <= wind <= 156:
                cat = 4
            elif 157 <= wind:
                cat = 5
            colors = ["white","blue","green","yellow","orange","red"]
            t.pencolor(colors[cat])
            t.pensize(cat*2)
            t.goto(lon,lat)
            if cat > 0:
                t.write(str(cat))
    t.done()

if __name__ == "__main__":
    irma()
