
1 Input Entry Boxes
The control panel consists of 5 input entries:
X coordinate: This text box takes the x coordinate input and stores it in the data register.
Y coordinate: This text box takes the y coordinate input and stores it in the data register.
Z coordinate (height): This text box takes the z coordinate input and stores it in the data register.
X direction speed: This text box takes the x direction speed and stores it in the data register. The data register update happens when the motor is switched on, thus eliminating the need for a specific button.
Y direction speed: This text box takes the y direction speed and stores it in the data register. The data register update happens when the motor is switched on, thus eliminating the need for a specific button.

2 Buttons

2.1 Home
The home button serves the purpose of returning all arms of the gantry robot back to its origin coordinates, that is, (0,0,0).

2.2 Move To X, Y
The Move T0 X, Y button serves the purpose taking the gantry robot to the coordinates Inputted by the user, that is, (X,Y,0).

2.3 + and -
The + and - button serve the purpose of moving the gantry robot by the given values of X and Y with respect to the current position.
(Xi, Yi) -> (Xi ± X, Yi ± Y)

2.4 Pick/Place
pick or place button appears depending upon the gripper status, height inputted by user is used to update the new coordinates of the gantry and pick(or place) the object. New x and y coordinates are set to be the same as current values and then the z-coordinate value is updated. Then, this function sets the gripper status as ON ( or OFF) to pick (or place) the object, updates relevant labels of the GUI interface and returns back to its original z-coordinate height (z-home). Finally, the text variable for the button is modified to ‘Pick’ or ‘Place’.

3 Display panel
The display panel consists of:
Current position coordinates of the gantry robot (Bottom left)
X-axis motor status (ON/OFF)
Y-axis motor status (ON/OFF)
X-axis motor status (ON/OFF)
Gripper status (ON/OFF)
