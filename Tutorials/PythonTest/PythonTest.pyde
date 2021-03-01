BACKGROUND_COLOR = '#070D5C'

saved_lines = []

def setup():
    size(520, 400)
    stroke(255)

def draw():
    background(BACKGROUND_COLOR)
    
    for new_line in saved_lines:
        line(width/2, height/2, new_line[0], new_line[1])
    
    line(width/2, height/2, mouseX, mouseY)
    
def mousePressed():
    saved_lines.append([mouseX, mouseY])
