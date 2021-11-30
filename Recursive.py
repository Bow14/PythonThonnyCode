import turtle

bo = turtle.Turtle()


def recursive_tree(length, angle, bo):
    """Draw a tree recursively"""
    if length > 5:
        bo.forward(length)
        bo.right(angle)
        recursive_tree(length - 20, angle, bo)
        bo.left(angle * 3)
        recursive_tree(length - 15, angle, bo)
        bo.right(angle)
        bo.backward(length)
        
recursive_tree(55, 34, bo)
turtle.mainloop()