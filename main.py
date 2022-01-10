import turtle as drawLib
from datetime import datetime

def main():
    enterDepth = int(input("Введите глубину фрактала - "))
    drawWindow = drawLib.Screen()
    startPoints = [[-150,-100],[0,150],[150,-100]]
    #mainTriangle(startPoints)
    serpinskyTriangle(startPoints,enterDepth)

def mainTriangle(startP):
    drawLib.up()
    drawLib.goto(startP[0][0], startP[0][1])
    drawLib.down()
    drawLib.goto(startP[1][0], startP[1][1])
    drawLib.goto(startP[2][0], startP[2][1])
    drawLib.goto(startP[0][0], startP[0][1])
    
def serpinskyTriangle(startP, depth):
    mainTriangle(startP)
    if depth>0:
        serpinskyTriangle([startP[0], schitalke(startP[0],startP[1]), schitalke(startP[0], startP[2])], depth-1)
        serpinskyTriangle([startP[1], schitalke(startP[0],startP[1]), schitalke(startP[1], startP[2])], depth-1)
        serpinskyTriangle([startP[2], schitalke(startP[2],startP[1]), schitalke(startP[0], startP[2])], depth-1)
        
def schitalke(p1,p2):
   return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)


start_time = datetime.now()
main()
print("Время выполнения - ", datetime.now() - start_time)
input("Нажмите для продолжения...")
