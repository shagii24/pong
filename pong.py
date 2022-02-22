from __future__ import with_statement
from asyncore import write
from turtle import Screen, Turtle, mainloop
import turtle
import winsound

class gameObjects(Turtle):
    def __init__(self,x,y):
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.pensize(10)
        self.color("white")
        self.speed(0)
        self.pu()
        self.sety(y)
        self.setx(x)


class paddle(gameObjects):
    def __init__(self,x,y):
        super().__init__(x,y)
        #self.ondrag(self.shift)
        
    def shiftUp(self):
        y = self.ycor()
        y +=20
        self.sety(y)
    def shiftDown(self):
        y = self.ycor()
        y -=20
        self.sety(y)

class ball(gameObjects):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shapesize(stretch_wid=1,stretch_len=1)
        #ball moves by 2 pixels - d in this case means "delta" - change of x and change of y (x speed)
        self.dx = 4
        self.dy = -4
        self.scores=[0,0]
    def ballMovement(self,leftPaddle,rightPaddle,writer):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
            
        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1
            
        if self.xcor() > 390:
            self.goto(0,0)
            self.dx *= -1
            self.scores[0]+=1
            writer.clear()
            writer.write(f"Player A: {self.scores[0]} PlayerB: {self.scores[1]}",align="center",font=("Arial",30,("bold","italic")))
            self.dx = abs(self.dx) + 1
            self.dy = abs(self.dy) + 1
        if self.xcor()< -390:
            self.goto(0,0)
            self.dx *= -1
            self.scores[1]+=1
            writer.clear()
            writer.write(f"Player A: {self.scores[0]} PlayerB: {self.scores[1]}",align="center",font=("Arial",30,("bold","italic")))
            self.dx = abs(self.dx) + 0.1
            self.dy = abs(self.dy) + 0.1
        if abs(leftPaddle.ycor())-40 <= abs(self.ycor()) <= abs(leftPaddle.ycor())+40 and self.xcor() < -340 and self.xcor()>-350:
            self.setx(-340)
            self.dx*=-1
            winsound.PlaySound('./bounce.wav', winsound.SND_ASYNC)
        if abs(rightPaddle.ycor())-40 <= abs(self.ycor()) <= abs(rightPaddle.ycor())+40 and self.xcor() > 340 and self.xcor()< 350:
            self.setx(340)
            self.dx*=-1
            winsound.PlaySound('./bounce.wav',winsound.SND_ASYNC)
        
        self.ballMovement(leftPaddle,rightPaddle,writer)

def main():

    global screen,paddle_a,paddle_b
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800,height=600)
    screen.tracer(1)
    writer = Turtle()
    writer.color("White")
    writer.pu()
    writer.ht()
    writer.goto(0,260)
    #Paddle A
    paddle_a=paddle(-350, 0)
    paddle_b=paddle(350, 0)
    myBall=ball(0,0)
    turtle.listen()
    turtle.onkey(paddle_a.shiftUp,"Up")
    turtle.onkey(paddle_a.shiftDown,"Down")
    turtle.onkey(paddle_b.shiftUp,"w")
    turtle.onkey(paddle_b.shiftDown,"s")
    writer.write(f"Player A: {myBall.scores[0]} PlayerB: {myBall.scores[1]}",align="center",font=("Arial",30,("bold","italic")))
    myBall.ballMovement(paddle_a,paddle_b,writer)

# while True:
#     
#     
#     writer.pu()
#     writer.goto(1,1.15)
#     writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
#     # Border checking

# #main game loop
if __name__=="__main__":
    msg=main()
    print(msg)
    screen.mainloop()

