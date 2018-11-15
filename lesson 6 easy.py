from math import sqrt
class Triangle:
       def __init__(self,x1,y1,x2,y2,x3,y3):
              self.x1=x1
              self.y1=y1
              self.x2=x2
              self.y2=y2
              self.x3=x3
              self.y3=y3
              self.AB = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
              self.BC = sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
              self.AC = sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
       def  tr_square(self):
            return  ((self.x1 - self.x3)*(self.y2-self.y3)-(self.x2-self.x3)*(self.y1-self.y3))/2
       def tr_perimetr(self):
           return self.AB + self.BC + self.AC
       def tr_vysota(self):
           return (abs((self.y2-self.y3)*self.x1)+(self.x3-self.x2)*self.y1+(self.x2*self.y3-self.x3*self.y2))/self.AC


tr_coord = Triangle(2,-3,1,1,-6,5)

print(" Площадь треугольника равна: {}".format( tr_coord.tr_square()))
print(" Периметр треугольника равен: {}".format( tr_coord.tr_perimetr()))
print(" Длина высоты AA2, опущенная из вершины A на прямую  BC равна: {}".format( tr_coord.tr_square()))



"""Опять не хватило времени на ДЗ. Я фрилансер, и иногда сижу вообще без работы (тогда-то на курсы и записалась),
 а иногда работаю без выходных-проходных"""