import turtle
import time
import random
import math

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)

delay = 1

class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)
        
        # Block Shape
        square = [[1]]

        horizontal_line = [[1]]

        vertical_line = [[1]]

        left_l = [[1]]
                   
        right_l = [[1]]
                   
        left_s = [[1]]
                  
        right_s = [[1]]
                  
        t = [[1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # Choose a random shape each time
        self.shape = random.choice(shapes)

                      
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        
        # print(self.height, self.width)

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1
        
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1
    
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = self.color
                
    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = 0
                    
    def can_move(self, grid):
        result = True
        for x in range(self.width):
            # Check if bottom is a 1
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result
    
    def rotate(self, grid):
        # First erase_shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):     
            self.shape = rotated_shape
            # Update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])
         





grideee = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5 ,0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 5],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5],
    [5, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]

grid=[]##ee


autos=20

ta=3
te=18
ll=math.ceil(ta/2)
print(ll)
for l in range (ta+2):
    aux=[]
    for i in range(te+2):
        if(l==0 or l==ta+2-1):
            aux.append(5)
        elif(i==0 or i==te+2-1):
            aux.append(5)
        
        elif(i==1 and l==ll):
            aux.append(2)
            
        elif(i==te and l==ll):
            aux.append(3)
        else:
            a=random.randint(1,6)
            if(autos>0 and a==3):
                autos-=1
                aux.append(1)
            else:
                aux.append(0)


    grid.append(aux)##ee




# Create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(1)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top = 100
    left = -210
    
    colors = ["black", "lightblue", "red", "orange", "yellow", "green", "purple", "red"]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


def check_grid(grid):
    # Check if each row is full
    print()
    y = len(grid)-1
    while y > 0:
        is_full = True
        for x in range(len(grid[1])):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))
    

# Create the basic shape for the start of the game
shape = Shape()

# Put the shape in the grid
#grid[shape.y][shape.x] = shape.color

# Draw the initial grid
# draw_grid(pen, grid)


##wn.listen()
#wn.onkeypress(lambda: shape.move_left(grid), "a")
#wn.onkeypress(lambda: shape.move_right(grid), "d")
#wn.onkeypress(lambda: shape.rotate(grid), "space")

# Set the score to 0
#score = 0

#draw_score(pen, score)
def semueve(grid):
    x1=0
    x2=0
    y1=0
    y2=0
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]==2):
                x1=i
                y1=j
            elif(grid[i][j]==3):
                x2=i
                y2=j
    h=distance(x1,x2,y1,y2)
    return h

def distance(xi,xii,yi,yii):
       sq1 = (xi-xii)*(xi-xii)
       sq2 = (yi-yii)*(yi-yii)
       return math.sqrt(sq1 + sq2)
# Main game loop




draw_grid(pen, grid)
llego=True
while llego:
    wn.update()
    l=0
    f=0
    h=semueve(grid)
    print(h)

    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]==2 and grid[i][j+1]!=5  and l==0 and h!=0 ):
                l=1
                if(grid[i][j+1]==1):

                    if(grid[i+1][j]==1 or grid[i+1][j]==5 ):
                        print("casi12212321")
                        if(grid[i-1][j]==5):
                            print(i,j,"hola")
                        elif(grid[i-1][j]==1):
                            print("YHEI")
                        else:
                            print("nope")
                            grid[i][j]=0
                            grid[i-1][j]=2

                    elif(grid[i-1][j]==1 or grid[i-1][j]==5 ):
                        print("casi")
                        if(grid[i+1][j]==5):
                            print(i,j)
                        else:
                            grid[i][j]=0
                            grid[i+1][j]=2
                    
                    else:
                        a=random.randint(0,1)
                        if(a==1):
                            grid[i][j]=0
                            grid[i+1][j]=2
                        else:
                            grid[i][j]=0
                            grid[i-1][j]=2
                else:
                    grid[i][j]=0
                    grid[i][j+1]=2
            elif(h==1):
                if(grid[i][j]==2):
                    if(grid[i+1][j]==3):
                        grid[i][j]=0
                        grid[i+1][j]=2
                    elif(grid[i-1][j]==3):
                        grid[i][j]=0
                        grid[i-1][j]=2
                    elif(grid[i][j+1]==3):
                        grid[i][j]=0
                        grid[i][j+1]=2
                print(i,j)


    draw_grid(pen, grid)
    time.sleep(delay)
    
wn.mainloop()

