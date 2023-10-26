#This is an animation of someone throwing a basketball into a hoop
from tkinter import *
from time import *

myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="sky blue")
screen.pack()

#sun
screen.create_oval(750, -50, 850, 50, fill="yellow")

#floor
screen.create_rectangle(0, 450, 800, 600, fill="orange")
screen.create_oval(300, 450, 800, 600, fill="black")
screen.create_oval(310, 450, 800, 600, fill="orange", outline="orange")
screen.create_oval(450, 450, 950, 600, fill="black")
screen.create_oval(460, 450, 950, 600, fill="orange", outline="orange")
for floor in range(5):
  screen.create_line(0, 30 * floor + 450, 800, 30 * floor + 450, fill="black")

#basketball net
screen.create_line(750, 300, 750, 550, width=25)
screen.create_rectangle(725, 300, 775, 175, fill="white")
screen.create_oval(650, 290, 750, 300, fill="red")

#person
headx1 = 150
heady1 = 400
for frame in range(100):
  if frame <= 16:  #person jumps
    heady1 = 0.5 * frame**2 - 8 * frame + 400
    hair = screen.create_arc(headx1, heady1 - 5, headx1 + 50, heady1 + 45, fill="black", start=20, extent=140)
    head = screen.create_oval(headx1,  heady1, headx1 + 50, heady1 + 50, fill="#CAA661")
    eye1 = screen.create_oval(headx1 + 10, heady1 + 10, headx1 + 15, heady1 + 15, fill="black")
    eye2 = screen.create_oval(headx1 + 35, heady1 + 10, headx1 + 40, heady1 + 15, fill="black")
    body = screen.create_line(headx1 + 25, heady1 + 50, headx1 + 25, heady1 + 100, width=15, fill="green")
    leg1 = screen.create_line(headx1 + 25, heady1 + 100, headx1, heady1 + 125, width=10, fill="navy blue")
    leg2 = screen.create_line(headx1 + 25, heady1 + 100, headx1 + 50, heady1 + 125, width=10, fill="navy blue")
    arm1 = screen.create_line(headx1 + 25, heady1 + 75, headx1 + 50, heady1 + 50, width=8, fill="#CAA661")
    sleeve = screen.create_line(headx1 + 25, heady1 + 75, headx1 + 45, heady1 + 55, width=10, fill="green")
  if frame <= 7: #ball goes up with the person
    ball = screen.create_oval(headx1 + 50, heady1 + 75,  headx1 + 100, heady1 + 25, fill="orange")
    ballline1 = screen.create_line(headx1 + 75, heady1 + 75, headx1 + 75, heady1 + 25)
    ballline2 = screen.create_line(headx1 + 50, heady1 + 50, headx1 + 100, heady1 + 50)
  if frame > 7: #ball being thrown
    x2 = 15 * frame + 80 #80 is 200 - (15 * 8), because frame starts at 8 so the equation should be 15 * (frame - 18) + 200
    y2 = 0.5 * frame**2 - 30 * frame + 475 + 30 * 6
    if x2 > 675: #ball hits backboard
      x2 = 675
    if y2 > 550: #bal hits ground
      y2 = 550
    ball = screen.create_oval(x2, y2, x2 + 50, y2 - 50, fill="orange")
    ballline1 = screen.create_oval(x2 + 25, y2, x2 + 25, y2 - 50)
    ballline2 = screen.create_line(x2, y2 - 25, x2 + 50, y2 - 25)
  screen.update()
  sleep(0.1)
  if frame < 16:  #make sure the guy stops when needed
    screen.delete(head, body, leg1, leg2, arm1, sleeve, hair, eye1, eye2)
  if frame != 99:
    screen.delete(ball, ballline1, ballline2)

screen.update()
input()