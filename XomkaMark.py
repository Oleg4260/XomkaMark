import pygame
from random import randint
import time

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("XomkaMark CPU Benchmark")
arial40 = pygame.font.SysFont("arial",40)

objectsQnt = 10000

def setQuantity():
    try:
        objectsQnt = int(input("Enter objects quantity \nDefault 10000, minimum 1000 \nMore objects - more measurement accuracy.\n> "))
        print("Quantity set to " + str(objectsQnt) + ".")
    except:
        objectsQnt = 10000
        print("Error! Set to default.")

    if(objectsQnt < 1000):
        objectsQnt = 1000
        print("Error! Set to minimum.")
    return objectsQnt

def rects():
    starttime = time.time()
    for i in range(objectsQnt):
        pygame.draw.rect(window,(randint(0,255),randint(0,255),randint(0,255)),(randint(-50,450),randint(-50,450),randint(25,100),randint(25,100)))
        pygame.display.update()
    endtime = time.time()
    elapsedtime = int(endtime - starttime)
    marks = int(objectsQnt / elapsedtime)
    print("Drawn " + str(objectsQnt) + " rects in " + str(elapsedtime) + " seconds.")
    window.fill((0,0,0))
    pygame.display.update()
    return marks
def circles():
    starttime = time.time()
    for i in range(objectsQnt):
        pygame.draw.circle(window,(randint(0,255),randint(0,255),randint(0,255)),(randint(0,450),randint(0,450)),randint(20,100))
        pygame.display.update()
    endtime = time.time()
    elapsedtime = int(endtime - starttime)
    marks = int(objectsQnt / elapsedtime)
    print("Drawn " + str(objectsQnt) + " circles in " + str(elapsedtime) + " seconds.")
    window.fill((0,0,0))
    pygame.display.update()
    return marks
def lines():
    starttime = time.time()
    for i in range(objectsQnt):
        pygame.draw.line(window,(randint(0,255),randint(0,255),randint(0,255)),(randint(-50,550),randint(-50,550)),(randint(-50,550),randint(-50,550)))
        pygame.display.update()
    endtime = time.time()
    elapsedtime = int(endtime - starttime)
    marks = int(objectsQnt / elapsedtime)
    print("Drawn " + str(objectsQnt) + " lines in " + str(elapsedtime) + " seconds.")
    window.fill((0,0,0))
    pygame.display.update()
    return marks
def texts():
    starttime = time.time()
    for i in range(objectsQnt):
        testText = arial40.render("test",True,(randint(0,255),randint(0,255),randint(0,255)))
        window.blit(testText,(randint(-50,500),randint(-50,500)))
        pygame.display.update()
    endtime = time.time()
    elapsedtime = int(endtime - starttime)
    marks = int(objectsQnt / elapsedtime)
    print("Drawn " + str(objectsQnt) + " texts in " + str(elapsedtime) + " seconds.")
    window.fill((0,0,0))
    pygame.display.update()
    return marks
def everything():
    starttime = time.time()
    rects()
    circles()
    lines()
    texts()
    endtime = time.time()
    elapsedtime = int(endtime - starttime)
    marks = int(objectsQnt * 4 / elapsedtime)
    print("Drawn " + str(objectsQnt) + " every object in " + str(elapsedtime) + " seconds.")
    window.fill((0,0,0))
    pygame.display.update()
    return marks

def help():
    print("XomkaMark CPU Benchmark\nList of commands:\nhelp - print this list\neverything - all tests in one(recommended)\nexit - exit\nrects - rects test\ncircles - circles test\nlines - lines test\ntexts - texts test\nsetQnt - set objects quantity(default 10000)")

help()

while(True):
    command = input("> ")
    if(command == "everything"):
        benchmarkResult = everything()
        print("You got " + str(benchmarkResult) + " marks in everything test.")
    elif(command == "exit"):
        break
    elif(command == "help"):
        help()
    elif(command == "rects"):
        benchmarkResult = rects()
        print("You got " + str(benchmarkResult) + " marks in rects test.")
    elif(command == "circles"):
        benchmarkResult = circles()
        print("You got " + str(benchmarkResult) + " marks in circles test.")
    elif(command == "lines"):
        benchmarkResult = lines()
        print("You got " + str(benchmarkResult) + " marks in lines test.")
    elif(command == "texts"):
        benchmarkResult = texts()
        print("You got " + str(benchmarkResult) + " marks in texts test.")
    elif(command == "setQnt"):
        objectsQnt = setQuantity()
    else:
        print('Unknown command! Type "help"')
pygame.quit()
