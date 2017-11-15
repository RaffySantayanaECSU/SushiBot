"""
All coordinates assume a screen resolution of 1600x900 and Chrome window is maximized with the
bookmarks bar enabled.
The page is scrolled to the very top.
x_pad = 304
y_pad = 242
Play area = x_pad+1, y_pad+1, 944, 722
"""

from PIL import ImageGrab, ImageOps
import os
import time
import win32api
import win32con
import numpy

#Globals
x_pad = 304
y_pad = 242

sushiTypes = {
        2677:'gunkan',
        2670:'onigiri',
        3143:'caliroll'
    }

foodOnHand = {'shrimp':5,               #This is a list of items that the game starts with
    'rice':10,                          #Although shrimp, salmon, and unagi is never used in
    'nori':10,                          #level 1, I have included it if I ever felt compelled
    'roe':10,                           #to continue to other levels.
    'salmon':5,
    'unagi':5}

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+479)                      #This function will take a screenshot of the screen within the
    im = ImageGrab.grab(box)                                            #given bounds. Assuming all the conditions from above are met,
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +     #then (x_pad+1, y_pad+1, x_pad+640, y_pad+479) will take a
            '.png', 'PNG')                                              #screenshot of the entire play area defined as box. That screenshot
    return im                                                           #is then saved as "full_snap_" with numbers generated based on time.

#def grab():
    #box = (x_pad+1, y_pad+1, x_pad+640, y_pad+479)                      #Similar to screenGrab(), box is defined as the bounds (x_pad+1, y_pad+1, x_pad+640, y_pad+479)
    #im = ImageOps.grayscale(ImageGrab.grab(box))                        #Then it converts box into a grayscale image. Afterwards, an array is created of the colors
    #a = numpy.array(im.getcolors())                                     #the grayscale image. Finally, the sum of the color values is created. These values are what
    #a = a.sum()                                                         #allows the bot to consistently know what sushi to make thanks to sushiTypes
    #print(a)
    #return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)                             #This function tells the bot to left click down, then up
    time.sleep(.1)                                                                      #which constitutes as a full click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print("Click")          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print("Left down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("Left release")

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))           #This moves the cursor position to the position instructed

def get_cords():
    x, y = win32api.GetCursorPos()          #get_cords() is a function that takes the cursors current
    x = x - x_pad                           #x and y coordinates. It then subtracts the x_pad and y-pad
    y = y - y_pad                           #values. This allows the top left corner of the game to be
    print(x,y)                              #the origin rather than the entire screen itself.

def startGame():
    # location of first menu
    mousePos((267, 202))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((337, 392))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((593, 457))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((326, 384))
    leftClick()
    time.sleep(.1)

class Cord:                         #The class of Cords consists of the coordinates of the following menus
    #FOOD MENU
    shrimp = (29, 330)
    rice = (95, 338)
    nori = (37, 387)
    roe = (95, 392)
    salmon = (42, 450)
    unagi = (95, 450)

#---------------------------
    #PHONE MENU
    phone = (576, 347)

    #TOPPINGS MENU
    menu_toppings = (538, 278)
    phone_shrimp = (491, 229)
    phone_nori = (491, 273)
    phone_roe =(578, 278)
    phone_unagi = (581, 228)
    phone_salmon = (495, 335)
    phone_exit = (599, 336)

    #RICE MENU
    menu_rice = (588, 301)
    buy_rice = (544, 255)

    #DELIVERY MENU
    delivery_free = (498, 295)

class blank:            #From the grab() function, the following values are the sum
    seat_1 = 8119       #of color values within the area in which the sushi icons
    seat_2 = 5986       #appear. These values are used to tell the bot that if the
    seat_3 = 11596      #seat is found to be at its respective value, then the seat
    seat_4 = 10613      #is empty.
    seat_5 = 7286
    seat_6 = 9119

def clear_tables():
    mousePos((88, 214))         #When clear_tables() is called, then the cursor will move to each
    leftClick()                 #coordinate and click. By doing so, the plates will be cleared.
                                #If there is no plate, then nothing happens upon clicking.
    mousePos((188, 214))
    leftClick()

    mousePos((288, 214))
    leftClick()

    mousePos((388, 214))
    leftClick()

    mousePos((488, 214))
    leftClick()

    mousePos((588, 214))
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((Cord.rice[0]+40,Cord.rice[1]))        #The foldMat() function takes the cursor 40 pixels further along
    leftClick()                                     #the x axis, but maintain the y axis value of the rice coordinate.
    time.sleep(.1)                                  #The bot then clicks, which makes the mat create the sushi made.

def makeFood(food):
    if food == 'caliroll':              #When making sushi, generally, the foodOnHand value for the ingredients used
        print("Making a cali roll")     #is decreased by the amount used to make the sushi. Afterwards, the cursor
        foodOnHand['rice'] -= 1         #is then moved the coordinates of the ingredients and performs a click.
        foodOnHand['nori'] -= 1         #Extra steps are performed when making gunkan and onigiri which I will explain
        foodOnHand['roe'] -= 1          #later. Once all of the necessary ingredients are placed on the mat, then
        mousePos(Cord.rice)             #foldMat() is called to create the sushi.
        leftClick()
        time.sleep(.05)
        mousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print("Making an onigri")
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.nori)
        time.sleep(.1)
        mousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        print("Making a gunkan")
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.roe)            # I found that gunkan and onigiri was not consistent when being made.
        leftClick()                     # Onigiri occasionally makes slop and gunkan occasionally makes caliroll
        time.sleep(.05)                 # The second click in the same coordinate would sometimes not work.
        mousePos(Cord.nori)           # My "fix" was to command the first click, sleep, move the coordinate to any coordinate,
        time.sleep(.05)                 # not click, move the coordinate back to its original position, then finally
        mousePos(Cord.roe)            # click again. This ended the inconsistency.
        time.sleep(.05)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def buyFood(food):
    if food == 'rice':                  #buyFood() moves the cursor to the phone, clicks, then clicks on either
        mousePos(Cord.phone)            #toppings or rice depending on what ingredient is called to be bought.
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)        #For rice, the coordinate of the rice menu button is clicked,
        time.sleep(.5)                  #then the bot checks if it is possible to buy rice by checking
        leftClick()                     #if the RBG value of the buy_rice coordinate is (118, 83, 85).
        s = screenGrab()                #These RGB values are the values of the buy rice icon if it is not clickable.
        #print("Test")                  #In other words, the bot does not have enough money to buy rice.
        time.sleep(.1)                  #Therefore, if the RGB value isn't (118, 83, 85), then we can buy rice.
        #print(s.getpixel(Cord.buy_rice))
        if s.getpixel(Cord.buy_rice) != (118, 83, 85):
            print("Rice is available")
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_free)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print("Rice is NOT available")
            mousePos(Cord.phone_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':              #For nori, the coordinate of the toppings menu button is clicked,
        mousePos(Cord.phone)        #then the coordinate of the nori icon is checked if it is possible
        time.sleep(.1)              #to buy nori using the same logic as the rice above. Roe is the same.
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print("Test")
        time.sleep(.1)
        if s.getpixel(Cord.nori) != (33, 30, 11):
            print("Nori is available")
            mousePos(Cord.nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_free)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print("Nori is NOT available")
            mousePos(Cord.phone_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.roe) != (127, 61, 0):
            print("Roe is available")
            mousePos(Cord.roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_free)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print("Roe is NOT available")
            mousePos(Cord.phone_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():                                 #checkFood() checks if any of the three ingredients necessary for level one
        if i == 'nori' or i == 'rice' or i == 'roe':                #have an inventory level of 3 or less. This is done using a for loop of
            if j <= 4:                                              #i and j variables. i checks each ingredient in foodOnHand and j checks
                print ("%s is low and needs to be replenished" % i) #the inventory value of that ingredient.
                buyFood(i)

def get_seat_one():
    box = (x_pad + 26, y_pad + 62, x_pad + 26 + 63, y_pad + 62 + 16)                    #All of the get_seat_#() functions work the same way that grab() works.
    im = ImageOps.grayscale(ImageGrab.grab(box))                                        #Only that get_seat_#() only gets the greyscale image of the order request
    a = numpy.array(im.getcolors())                                                     #bubble rather than the whole gameplay screen.
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    box = (x_pad + 127, y_pad + 62,x_pad + 127 + 63, y_pad + 62 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (x_pad + 228, y_pad +  62,x_pad +  228 + 63, y_pad +  62 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (x_pad + 329, y_pad +  62,x_pad +  329 + 63, y_pad +  62 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (x_pad + 430,  y_pad + 62,x_pad +  430 + 63,  y_pad + 62 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (x_pad + 531,  y_pad + 62,x_pad +  531 + 63, y_pad +  62 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = numpy.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def check_bubs():
    checkFood()                                                         #check_bubs() starts off by calling checkFood() to ensure that
    s1 = get_seat_one()                                                 #there are enough ingredients in stock to make sushi. Next, it
    if s1 != blank.seat_1:                                              #checks if there is an order in the seat starting from seat 1.
        print(s1)                                                       #Once the bot recognizes the order, it makes the sushi that is
        if s1 in sushiTypes:                                            #requeted and then clears tables. This is done for all seats.
            print("Table 1 is occupied and needs %s" % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print("sushi not found!\n sushiType = %i" % s1)
    else:
        print("Table 1 unoccupied")
    clear_tables()

    checkFood()
    s2 = get_seat_two()
    if s2 != blank.seat_2:
        print(s2)
        if s2 in sushiTypes:
            print("Table 2 is occupied and needs %s" % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print("sushi not found!\n sushiType = %i" % s2)
    else:
        print("Table 2 unoccupied")
        clear_tables()

    checkFood()
    s3 = get_seat_three()
    if s3 != blank.seat_3:
        print(s3)
        if s3 in sushiTypes:
            print("Table 4 is occupied and needs %s" % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print("sushi not found!\n sushiType = %i" % s3)
    else:
        print("Table 3 unoccupied")
        clear_tables()

    checkFood()
    s4 = get_seat_four()
    if s4 != blank.seat_4:
        print(s4)
        if s4 in sushiTypes:
            print("Table 4 is occupied and needs %s" % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print("sushi not found!\n sushiType = %i" % s4)
    else:
        print("Table 4 unoccupied")
        clear_tables()

    checkFood()
    s5 = get_seat_five()
    if s5 != blank.seat_5:
        print(s5)
        if s5 in sushiTypes:
            print("Table 5 is occupied and needs %s" % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print("sushi not found!\n sushiType = %i" % s5)
    else:
        print("Table 5 unoccupied")
        clear_tables()

    checkFood()
    s6 = get_seat_six()
    if s6 != blank.seat_6:
        print(s6)
        if s6 in sushiTypes:
            print("Table 6 is occupied and needs %s" % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print("sushi not found!\n sushiType = %i" % s6)
    else:
        print("Table6 unoccupied")
        clear_tables()

def main():
    startGame()
    while True:
       check_bubs()
    # mousePos(Cord.buy_rice)
    # print(screenGrab().getpixel(Cord.buy_rice))

if __name__ == '__main__':
    main()