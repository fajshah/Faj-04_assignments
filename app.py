from tkinter import Canvas, Tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    """Eraser function to clear cells."""
    x, y = event.x, event.y
    overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    for item in overlapping:
        canvas.itemconfig(item, fill='white')

# Create window
root = Tk()
root.title("Eraser Program")

canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Create grid
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Eraser binds to mouse motion
canvas.bind("<B1-Motion>", erase)

root.mainloop()
