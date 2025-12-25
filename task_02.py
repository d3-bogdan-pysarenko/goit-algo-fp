import turtle

def draw_pythagoras_tree(branch_len, level, angle):
    """
    function is using recursion for drawing
    branch_len: branch length
    level: recursion level
    angle: angle for branches
    """
    if level > 0:
        # Main branch
        turtle.forward(branch_len)
        
        # Right branch
        turtle.right(angle)
        draw_pythagoras_tree(branch_len * 0.75, level - 1, angle)
        
        # Returning + left branch
        turtle.left(2 * angle)
        draw_pythagoras_tree(branch_len * 0.75, level - 1, angle)
        
        # Returning to start
        turtle.right(angle)
        turtle.backward(branch_len)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Fractal: Дерево Піфагора")

    turtle.speed(0)
    turtle.left(90)
    turtle.color("darkgreen")
    turtle.pensize(2)

    # Request to set recursion level
    try:
        level = int(screen.numinput("Recursion level", "Set recursion level (from 1 to 15):", minval=1, maxval=15))
        
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()

        draw_pythagoras_tree(100, level, 30)
        
        print("Drawing completed")
    except (TypeError, ValueError):
        print("Please provide valid input")

    screen.exitonclick()

if __name__ == "__main__":
    main()