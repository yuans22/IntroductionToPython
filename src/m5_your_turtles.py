"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Shuai Yuan.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

zhang = rg.SimpleTurtle('turtle')
zhang.pen = rg.Pen('blue', 5)
zhang.speed = 10
radius = 150
for k in range(6):
    zhang.draw_circle(radius)
    zhang.pen_up()
    zhang.right(45)
    zhang.forward(10)
    zhang.left(45)
    zhang.pen_down()
    radius = radius - 12

zheng = rg.SimpleTurtle('turtle')
zheng.pen = rg.Pen ('red', 5)
zheng.speed = 10
size = 100
for k in range (6):
    zheng.draw_regular_polygon(10,size)
    zheng.pen_up()
    zheng.right(45)
    zheng.forward(10)
    zheng.left(45)
    zheng.pen_down()
    size = size - 12

zz = rg.SimpleTurtle('turtle')
zz.pen = rg.Pen('green', 5)
zz.speen = 10
side = 100
for k in range (6):
    zz.draw_square(side)
    zz.pen_up()
    zz.right(45)
    zz.forward(10)
    zz.left(45)
    zz.pen_down()
    side = side -12