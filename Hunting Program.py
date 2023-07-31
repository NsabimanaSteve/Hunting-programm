##########################################################################
#A06_steve.nsabimana.py
#Author: Steve Nsabimana
#Username: steve_nsabimana
#
#Purpose: Hunting Activities
###########################################################################
import turtle
# create the turtle screen and set the background image
wn = turtle.Screen()
wn.bgpic("somewhere.gif")
wn.setup(width=1300, height=900)
# add the foreground images
turtle.addshape("rabbit1-removebg-preview.gif") 
#https://www.deviantart.com/casualgee/art/Mr-Norja-bunny-RUN-animated-103185362
turtle.addshape("dog-removebg-preview.gif") #https://www.myfamilyvets.co.uk/top10-facts-about-dogs
turtle.addshape("My project (2).gif") #https://www.south-africa-tours-andtravel.com/history-of-durban.html
# create the turtle objects for the foreground images
title=turtle.Turtle()
title.penup()
title.goto(-500,350)
title.color('yellow')
title.write(" Hunting where Dog running on the rabbit", font=('Times New Roman', 40, 'bold', 'italic'))
title.hideturtle()
# set the position and shape of the turtle objects
image1 = turtle.Turtle()
image2 = turtle.Turtle()
image3 = turtle.Turtle()
x = 0
y = 0
z = 0
def moverabit(x,n):
 
 image1.penup()
 image1.goto(n, -300)
 image1.shape("rabbit1-removebg-preview.gif")
 image1.backward(x)
def movedog(y,n):
 
 image2.penup()
 image2.goto(n, -270)
 image2.shape("dog-removebg-preview.gif")
 image2.backward(y)
def movehunter(z,n):
 image3.penup()
 image3.goto(n, -200)
 image3.shape("My project (2).gif")
 image3.backward(z)
 
n = 700
for i in range(2):
 moverabit(x, n)
 
 movedog(y, n)