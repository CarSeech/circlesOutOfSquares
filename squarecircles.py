import turtle


def draw_CircOutOfSquares():
     
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green")
    brad.speed(50)
    
    for i in range (1,200):
        brad.right(25)
        
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
        
    


draw_CircOutOfSquares()