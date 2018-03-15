import math #math.degrees(math.atan(math.sqrt(3)/1))


              
class Beacon:

    def angle_from_car(self):
        return math.degrees(math.atan(self.x1 / self.y1))
    
    def __init__(self,hypotenuse=0, angle=99, X=0.0, Y=0.0):
        self.hypotenuse = hypotenuse    #relative to car
        self.angle = angle              #relative to car
        self.x = X      #absolute Location of Beacon on Grid
        self.y = Y      #absolute Location of Beacon on Grid
    def __repr__(self):
        print("x:", self.x," y:",self.y)



def common_points(Beacon1 b1, Beacon2 b2):
    #distance between centers of circles
    R = math.sqrt( pow(b2.x - b1.x, 2) + pow(b2.y - b1.y, 2)) 
    
    Car_x = 0.5*(b1.x + b2.x) + pow(b1.hypotenuse, 2) - pow(b2.hypotenuse, 2) /2.0/R/R  \
              * (b2.hypotenuse - b1.hypotenuse)                                         \    
              + 0.5*math.sqrt(2*(pow(b1.hypotenuse,2)+pow(b2.hypotenuse,2))/R/R         \
              - pow(pow(b1.hypotenuse,2)-pow(b2.hypotenuse,2),2)/R/R/R/R  - 1)          \
              * (b2.y - b1.y)
    print(Car_x)



hypotenuse2 = 80
angle2 = -15
x2 = 600
y2 = 400
beacon2 = Beacon(hypotenuse2, angle2, x2, y2)

hypotenuse1 = 60    #calculated from image
angle1 = 20         #calculated from image
X1 = 200    #Given this
Y1 = 50     #Given this

beacon1 = Beacon(hypotenuse1, angle1, X1, Y1)

common_points(beacon1, beacon2)









