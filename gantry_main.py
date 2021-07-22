import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
from PIL import ImageTk, Image
import gantry_module as gantry
import gantry_startup as window

# fonts
buttonfont1 = tkfont.Font(family='Calibri', size=16)
buttonfont2 = tkfont.Font(family='Calibri', size=12)

lblfont1 = tkfont.Font(family='Calibri', size=16)


# Header Image, Label
logoimg = ImageTk.PhotoImage(Image.open("./media/SHlogo2.bmp"))
logo_lbl = tk.Label(window.panel_window, image=logoimg, borderwidth=1, relief="solid")
logo_lbl.pack(side="top", pady=5, expand="no")

Headlbl = Label(window.panel_window, text="3-Axis Gantry Control Panel", fg='red', font=("Calibri", 32))
Headlbl.place(x=100, y=60)


# ----------------------------x----------------------------x----------------------------
# MAIN BODY

# X, Y coordinates for starting position of main body
mainbody_X = gantry.mainbody_X
mainbody_Y = gantry.mainbody_Y

# Enter target coordinates label
inp_info_lbl = Label(window.panel_window, text="Enter Target Coordinates", fg='blue', font=("Calibri", 20))
inp_info_lbl.place(x=mainbody_X, y=mainbody_Y+10)

# ----------------------------x----------------------------x----------------------------
# Gx: X-coordinate of Gantry; Gy: Y-coordinate of Gantry; Gz: Z-coordinate of Gantry
# Labels to display name of respective textbox

# X_coordinate
Gx_input_lbl = Label(window.panel_window, text="X ", fg='red', font=lblfont1)
Gx_input_lbl.place(x=mainbody_X, y=mainbody_Y + 60)
# X-axis speed
Gx_speed_lbl = Label(window.panel_window, text="X-dir speed", fg='red', font=lblfont1)
Gx_speed_lbl.place(x=mainbody_X + 310 + 150, y=mainbody_Y + 20)

# Y_coordinate
Gy_input_lbl = Label(window.panel_window, text="Y ", fg='red', font=lblfont1)
Gy_input_lbl.place(x=mainbody_X, y=mainbody_Y + 100)
# Y-axis speed
Gy_speed_lbl = Label(window.panel_window, text="Y-dir speed", fg='red', font=lblfont1)
Gy_speed_lbl.place(x=mainbody_X + 310 + 150, y=mainbody_Y + 60)

# Z_coordinate of gantry
Gz_input_lbl = Label(window.panel_window, text="Height", fg='red', font=lblfont1)
Gz_input_lbl.place(x=mainbody_X + 310 + 150, y=mainbody_Y + 100)

# Z-coordinates will be set by-default and will be changed by the user only when required

# END OF MAIN BODY
# ----------------------------x----------------------------x----------------------------
# ACTION PANEL

# Action panel starting coordinates: AP_x; AP_y
AP_x = mainbody_X
AP_Y = mainbody_Y + 170

# Pick/place button
Pickplace = Button(window.panel_window, textvariable=window.panel_window.Pickorplace, bd=3, fg='blue', font=buttonfont1, width=5, command=gantry.getGz_pickorplace)
Pickplace.place(x=260, y=330)
window.panel_window.Pickorplace.set('Pick')

# Home button
Home = Button(window.panel_window, text="Home", fg='blue', font = buttonfont1, width=5, bd=3, command=gantry.home)
Home.place(x=260, y=390)

# MOVE Buttons

# moveBy
MoveBy = Button(window.panel_window, text="+", fg='blue', font=buttonfont1, bd=3, command=lambda: gantry.call_moveBy('+'))
MoveBy.place(x=mainbody_X + 150, y=mainbody_Y + 70)
MoveBy_negative = Button(window.panel_window, text="-", fg='blue', font=buttonfont1, bd=3, command=lambda: gantry.call_moveBy('-'))
MoveBy_negative.place(x=mainbody_X + 200, y=mainbody_Y + 70)

# moveTo
MoveToXY = Button(window.panel_window, text="MOVE To X, Y", fg='blue', bd=3, font=buttonfont2, command=gantry.call_moveTo)
MoveToXY.place(x=mainbody_X + 135, y=mainbody_Y + 130)

# END OF ACTION PANEL
# ----------------------------x----------------------------x----------------------------
# DISPLAY PANEL

# X-motor status display
X_motor = Label(window.panel_window, text="X motor:", fg='Green', font=lblfont1)
X_motor.place(x=420, y=300)
X_motorstatus = Entry(window.panel_window, textvariable=window.panel_window.xmotorstatus, fg='Green', borderwidth=2 ,font=lblfont1, width=5)
X_motorstatus.place(x=520, y=300)
X_motorstatus.configure(state='disabled')
window.panel_window.xmotorstatus.set('OFF')

# Y-motor status display
Y_motor = Label(window.panel_window, text="Y motor:", fg='Green', font=lblfont1)
Y_motor.place(x=420, y=330)
Y_motorstatus = Entry(window.panel_window, textvariable=window.panel_window.ymotorstatus, fg='Green', borderwidth=2 ,font=lblfont1, width=5)
Y_motorstatus.place(x=520, y=330)
Y_motorstatus.configure(state='disabled')
window.panel_window.ymotorstatus.set('OFF')

# Z-motor status display
Z_motor = Label(window.panel_window, text="Z motor:", fg='Green', font=lblfont1)
Z_motor.place(x=420, y=360)
Z_motorstatus = Entry(window.panel_window, textvariable=window.panel_window.zmotorstatus, fg='Green', borderwidth=2 ,font=lblfont1, width=5)
Z_motorstatus.place(x=520, y=360)
Z_motorstatus.configure(state='disabled')
window.panel_window.zmotorstatus.set('OFF')

# Gripper status display
Gripper = Label(window.panel_window, text="Gripper:", fg='Green', font=lblfont1)
Gripper.place(x=420, y=410)
Gripper_status = Entry(window.panel_window, textvariable=window.panel_window.gripperstatus, fg='Green', borderwidth=2 ,font=lblfont1, width=5)
Gripper_status.place(x=520, y=410)
Gripper_status.configure(state='disabled')
window.panel_window.gripperstatus.set('OFF')

# Current coordinates display
coord_lbl = Label(window.panel_window, text="Coordinates", fg='black', font=lblfont1)
coord_lbl.place(x=75, y=330)
coordinate = Label(window.panel_window, textvariable=window.panel_window.variable, fg='black', borderwidth=3, relief="ridge", font=("Calibri", 20), width=10)
coordinate.place(x=50, y=370)
window.panel_window.variable.set(str(gantry.register['current'][0])+', '+str(gantry.register['current'][1])+', '+str(gantry.register['current'][2]))



# END OF DISPLAY PANEL
# ----------------------------x----------------------------x----------------------------

window.panel_window.mainloop()
