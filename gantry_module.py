import time
import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
import gantry_startup as window

# Define variable values
xMotor = False
yMotor = False
zMotor = False

# Defining variables for variable text and assigning them to StringVar
window.panel_window.variable = StringVar()
window.panel_window.xmotorstatus = StringVar()
window.panel_window.ymotorstatus = StringVar()
window.panel_window.zmotorstatus = StringVar()
window.panel_window.gripperstatus = StringVar()
window.panel_window.Pickorplace = StringVar()


# Define a dictionary called register where each element contains a list of x,y,z values defining the state.MotorStatus contains a list of booleans to indicate x,y,z motor statuses. gripperStatus defines status of gripper using a string (default:free, pick, place)
register = {'current': [0, 0, 0], 'next': [0, 0, 0], 'speed': [0, 0, 0], 'motorStatus': [xMotor, yMotor, zMotor], 'gripperStatus': [False]}

# ----------------------------x----------------------------x----------------------------
# API FUNCTIONS


def setSpeedX(speedX):
    """
    The purpose of the function is to set the speed of x-axis motor.

    Arguments:
    speedX: Value of speed the x-axis motor has to be set to
    """

    register['speed'][0] = speedX
    return


def setSpeedY(speedY):
    """
    The purpose of the function is to set the speed of y-axis motor.

    Arguments:
    speedY: Value of speed the y-axis motor has to be set to
    """

    register['speed'][1] = speedY
    return


def setSpeedZ(speedZ):
    """
    The purpose of the function is to set the speed of z-axis motor.

    Arguments:
    speedZ: Value of speed the z-axis motor has to be set to
    """

    register['speed'][2] = speedZ
    return


def xMotorOn(speedX):
    """
    The purpose of the function is to turn the x-axis motor on and update the motor status in the register.

    Arguments:
    speedX: Value of speed the x-axis motor has to be set to
    """

    register['motorStatus'][0] = True
    setSpeedX(speedX)
    return


def xMotorOff():
    """
    The purpose of the function is to turn the x-axis motor off and update the motor status in the register.
    """

    register['motorStatus'][0] = False
    setSpeedX(0)
    return


def yMotorOn(speedY):
    """
    The purpose of the function is to turn the y-axis motor on and update the motor status in the register.

    Arguments:
    speedY: Value of speed the y-axis motor has to be set to
    """

    register['motorStatus'][1] = True
    setSpeedY(speedY)
    return


def yMotorOff():
    """
    The purpose of the function is to turn the y-axis motor off and update the motor status in the register.
    """

    register['motorStatus'][1] = False
    setSpeedY(0)
    return


def zMotorOn():
    """
    The purpose of the function is to turn the z-axis motor on and update the motor status in the register and
    sets default z speed to 1.
    """

    register['motorStatus'][2] = True
    setSpeedZ(1)
    return


def zMotorOff():
    """
    The purpose of the function is to turn the x-axis motor off and update the motor status in the register.
    """

    register['motorStatus'][2] = False
    setSpeedZ(0)
    return


def home():
    """
    Returns all axes arms back to the home position (0,0,0), the order being x->y->z. Updates the current and next coordinate values in the register.
    """

    # Update next values in register
    register['next'][0] = 0
    register['next'][1] = 0
    register['next'][2] = 0
    # Update current coordinates label
    update_label()
    print(register)
    return


def homeX():
    """
    Returns the x-axis arm back to the home position (0,0,0). Updates the current and next x coordinate values in the register.
    """

    # Update next value in register
    register['next'][0] = 0
    # Switch on x motor
    xMotorOn(getSpeedX())
    # Calculate time delay and update current value in register
    xTimeDelay = abs((register['current'][0] - register['next'][0]) / register['speed'][0])
    register['current'][0] = register['next'][0]
    time.sleep(xTimeDelay)
    xMotorOff()
    return


def homeY():
    """
    Returns the y-axis arm back to the home position (0,0,0). Updates the current and next y coordinate values in the register.
    """

    # Update next value in register
    register['next'][1] = 0
    # Switch on y motor
    yMotorOn(getSpeedY())
    # Calculate time delay and update current value in register
    yTimeDelay = abs((register['current'][1] - register['next'][1]) / register['speed'][1])
    register['current'][1] = register['next'][1]
    time.sleep(yTimeDelay)
    yMotorOff()
    return


def homeZ():
    """
    Returns the z-axis arm back to the home position (0,0,0). Updates the current and next z coordinate values in the register.
    """

    # Update next values in register
    register['next'][0] = register['current'][0]
    register['next'][1] = register['current'][1]
    register['next'][2] = 0
    # update label
    update_label()
    return


def update_label():
    """
    A helper function to provide motion and update the current position and motor status in real time in the GUI. Shows the real time information in the form of a label on the control panel.
    """
    coordinate = register['current']
    speed = register['speed']

    # X-axis update
    if register['next'][0] != register['current'][0]:
        xMotorOn(getSpeedX())
        window.panel_window.xmotorstatus.set('ON')
        xTimeDelay = abs((register['current'][0] - register['next'][0]) / register['speed'][0])
        x_time_taken = xTimeDelay
        seconds = 0
        while(seconds < x_time_taken):
            seconds = seconds + 0.1
            if register['next'][0] > register['current'][0]:
                coordinate[0] = coordinate[0] + 0.1*speed[0]
            elif register['next'][0] < register['current'][0]:
                coordinate[0] = coordinate[0] - 0.1*speed[0]
            window.panel_window.variable.set(str(coordinate[0])[0:4]+', '+str(coordinate[1])[0:3]+', '+str(coordinate[2])[0:3])
            window.panel_window.update()
            time.sleep(0.1)
        xMotorOff()
        window.panel_window.xmotorstatus.set('OFF')

    # Y-axis update
    if register['next'][1] != register['current'][1]:
        yMotorOn(getSpeedY())
        window.panel_window.ymotorstatus.set('ON')
        yTimeDelay = abs((register['current'][1] - register['next'][1]) / register['speed'][1])
        y_time_taken = yTimeDelay
        seconds = 0
        while(seconds < y_time_taken):
            seconds = seconds + 0.1
            if register['next'][1] > register['current'][1]:
                coordinate[1] = coordinate[1] + 0.1*speed[1]
            elif register['next'][1] < register['current'][1]:
                coordinate[1] = coordinate[1] - 0.1*speed[1]
            window.panel_window.variable.set(str(register['next'][0])+', '+str(coordinate[1])[0:4]+', '+str(coordinate[2])[0:3])
            window.panel_window.update()
            time.sleep(0.1)
        yMotorOff()
        window.panel_window.ymotorstatus.set('OFF')

    # Z-axis update
    if register['next'][2] != register['current'][2]:
        zMotorOn()
        window.panel_window.zmotorstatus.set('ON')
        zTimeDelay = abs((register['current'][2] - register['next'][2]) / register['speed'][2])
        z_time_taken = zTimeDelay
        seconds = 0
        while(seconds < z_time_taken):
            seconds = seconds + 0.1
            if register['next'][2] > register['current'][2]:
                coordinate[2] = coordinate[2] + 0.1*speed[2]
            elif register['next'][2] < register['current'][2]:
                coordinate[2] = coordinate[2] - 0.1*speed[2]
            window.panel_window.variable.set(str(register['next'][0])+', '+str(register['next'][1])+', '+str(coordinate[2])[0:4])
            window.panel_window.update()
            time.sleep(0.1)
        zMotorOff()
        window.panel_window.zmotorstatus.set('OFF')

    # Current register values update
    register['current'][0] = register['next'][0]
    register['current'][1] = register['next'][1]
    register['current'][2] = register['next'][2]
    window.panel_window.variable.set(str(register['next'][0])+', '+str(register['next'][1])+', '+str(register['next'][2]))
    return


def moveTo(x, y):
    """
    Function to move the gantry robot to a particular set of coordinates.

    Arguments:
    x: X coordinate to be moved to
    y: Y coordinate to be moved to
    """

    register['next'][0] = x
    register['next'][1] = y
    register['next'][2] = register['current'][2]

    update_label()
    return


def moveBy(x_sign, y_sign, dx, dy):
    """
    Function to move the gantry robot by a particular amount

    Arguments:
    x_sign: The sign of x amount, positive or negative
    y_sign: The sign of y amount, positive or negative
    dx: X coordinate to be moved by
    dy: Y coordinate to be moved by
    """

    if str(x_sign) == '+':
        register['next'][0] = register['current'][0] + int(dx)
    elif str(x_sign) == '-':
        register['next'][0] = register['current'][0] - int(dx)

    if str(y_sign) == '+':
        register['next'][1] = register['current'][1] + int(dy)
    elif str(y_sign) == '-':
        register['next'][1] = register['current'][1] - int(dy)

    update_label()
    return


def pick(zHeight):
    """
    Function to pick up an object.

    Arguments:
    zHeight: The height by which z-axis arm should move
    """
    register['next'][0] = register['current'][0]
    register['next'][1] = register['current'][1]
    register['next'][2] = zHeight
    register['gripperStatus'][0] = True

    update_label()
    window.panel_window.gripperstatus.set('ON')
    homeZ()
    window.panel_window.Pickorplace.set('Place')
    return


def place(zHeight):
    """
    Function to place an object.

    Arguments:
    zHeight: The height by which z-axis arm should move
    """
    register['next'][0] = register['current'][0]
    register['next'][1] = register['current'][1]
    register['next'][2] = zHeight

    register['gripperStatus'][0] = False

    update_label()
    window.panel_window.gripperstatus.set('OFF')
    homeZ()
    window.panel_window.Pickorplace.set('Pick')
    return


# END OF API FUNCTIONS
# ----------------------------x----------------------------x----------------------------
# X, Y coordinates for starting position of main body
mainbody_X = 50
mainbody_Y = 140

# Rectangle (Lines) border around coordinate inputs
bordercanvas = Canvas(window.panel_window)
bordercanvas.place(x=mainbody_X - 5, y=mainbody_Y)

# Coordinate input border
bordercanvas.create_rectangle(3, 3, 300, 175)

# Speed, height input and status display border
bordercanvas2 = Canvas(window.panel_window)
bordercanvas2.place(x=mainbody_X + 335, y=mainbody_Y)

bordercanvas2.create_rectangle(3, 3, 275, 250)

bordercanvas3 = Canvas(window.panel_window)
bordercanvas3.place(x=mainbody_X + 335, y=mainbody_Y+140)
bordercanvas3.create_rectangle(3, 3, 275, 180)

# TEXTBOX ENTRIES
# Textbox initializations for entry of coordinates and speeds

# X coordinate entry
Gx_input = Entry(window.panel_window, font=("Times New Roman", 16), borderwidth= 2, width=5)
Gx_input.place(x=mainbody_X + 30, y=mainbody_Y + 60)
# Y coordinate entry
Gy_input = Entry(window.panel_window, font=("Times New Roman", 16), borderwidth= 2, width=5)
Gy_input.place(x=mainbody_X + 30, y=mainbody_Y + 100)
# Z coordinate entry
Gz_input = Entry(window.panel_window, font=("Times New Roman", 16), borderwidth= 2, width=5)
Gz_input.place(x=mainbody_X + 380, y=mainbody_Y + 100)

# X speed entry
Gx_speed_input = Entry(window.panel_window, font=("Times New Roman", 16), borderwidth= 2, width=5)
Gx_speed_input.place(x=mainbody_X + 380, y=mainbody_Y + 20)
# Y speed entry
Gy_speed_input = Entry(window.panel_window, font=("Times New Roman", 16), borderwidth= 2, width=5)
Gy_speed_input.place(x=mainbody_X + 380, y=mainbody_Y + 60)

# END OF TEXTBOX ENTRIES
# ----------------------------x----------------------------x----------------------------
# CALLBACK FUNCTIONS


def getSpeedX():
    """
    Gets the speed from the (x) speed textbox.
    returns the speed obtained from the textbox.
    """

    speedX = int(Gx_speed_input.get())
    return speedX


def getSpeedY():
    """
    Gets the speed from the (y) speed textbox.
    returns the speed obtained from the textbox.
    """

    speedY = int(Gy_speed_input.get())
    return speedY


def getGz_pickorplace():
    """
    Gets the the value of height and calls pick function.
    """

    Gz = int(Gz_input.get())
    if window.panel_window.Pickorplace.get() == ('Pick'):
        pick(Gz)
    elif window.panel_window.Pickorplace.get() ==('Place'):
        place(Gz)
    print(register)
    return


def call_moveTo():
    """
    Gets the (x) coordinate and (y) coordinate user input and calls moveTo function.
    """

    x = int(Gx_input.get())
    y = int(Gy_input.get())
    moveTo(x, y)
    print(register)
    return


def call_moveBy(sign):
    """
    Gets the (x) coordinate and (y) coordinate user input and calls moveBy function.
    """

    dx = Gx_input.get()
    dy = Gy_input.get()
    moveBy(sign, sign, dx, dy)
    print(register)
    return

# END OF CALLBACK FUNCTIONS
# ----------------------------x----------------------------x----------------------------
