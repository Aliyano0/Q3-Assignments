from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

def is_overlapping(rect, eraser_pos):
    """Check if a cell overlaps with the eraser."""
    cell_p1 = rect.getP1()
    cell_p2 = rect.getP2()
    
    cell_left = cell_p1.getX()
    cell_top = cell_p1.getY()
    cell_right = cell_p2.getX()
    cell_bottom = cell_p2.getY()

    eraser_left = eraser_pos.getX()
    eraser_top = eraser_pos.getY()
    eraser_right = eraser_left + ERASER_SIZE
    eraser_bottom = eraser_top + ERASER_SIZE

    # Check if rectangles overlap
    return not (cell_right < eraser_left or cell_left > eraser_right or
                cell_bottom < eraser_top or cell_top > eraser_bottom)

def erase_objects(rectangles, eraser_pos):
    """Turn blue rectangles under the eraser white."""
    for rect in rectangles:
        if rect.config['fill'] == 'blue' and is_overlapping(rect, eraser_pos):
            rect.setFill('white')

def main():
    win = GraphWin("Eraser Demo", CANVAS_WIDTH, CANVAS_HEIGHT)
    win.setBackground("white")

    rectangles = []

    # Create the grid of blue rectangles
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            rect = Rectangle(Point(left_x, top_y), Point(left_x + CELL_SIZE, top_y + CELL_SIZE))
            rect.setFill("blue")
            rect.draw(win)
            rectangles.append(rect)

    # Wait for user to click to start erasing
    click = win.getMouse()
    eraser = Rectangle(click, Point(click.getX() + ERASER_SIZE, click.getY() + ERASER_SIZE))
    eraser.setFill("pink")
    eraser.draw(win)

    while True:
        pt = win.checkMouse()
        if pt:
            # Move eraser
            eraser.undraw()
            eraser = Rectangle(pt, Point(pt.getX() + ERASER_SIZE, pt.getY() + ERASER_SIZE))
            eraser.setFill("pink")
            eraser.draw(win)

            # Erase overlapping rectangles
            erase_objects(rectangles, pt)

        time.sleep(0.05)

if __name__ == "__main__":
    main()
