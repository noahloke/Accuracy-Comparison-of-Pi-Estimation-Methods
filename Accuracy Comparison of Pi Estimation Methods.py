# Name: Noah Loke
# Project
# This program calculates estimations of pi with four different methods: Archimedes Approach, Leibniz Accumulator Formula, Wallis Accumulator Formula, and the Monte Carlo Method

'''
importing math for sin, radians, pi
importing time for time()
importing random for random() to get random float between [0, 1]
importing matplotlib.pyplot as plt to graph data
'''
import math
import time
import random
import matplotlib.pyplot as plt

'''
I learned about the method and implemented my own function. The method is quite simple, so there were not many changes to be made.
I combined several lines of code. A polygon of n sides is split into many triangles, and with a hypotenuse (or “radius”) of 1,
the outer edge length is calculated using trigonometry, and the total perimeter (or “circumference”) is determined. By dividing the perimeter by 2,
you get an estimation of pi. I record the elapsed execution time in nanoseconds and send it to the function call.
I also call another function to calculate the accuracy of archimedesPi compared to math.pi and send it to the function call.
'''
def archimedesPi(numOfSides):
    startTime = time.time()
    angle = 360.0 / numOfSides / 2
    sideLength = math.sin(math.radians(angle)) * 2
    circumference = sideLength * numOfSides
    archimedesPi = circumference / 2
    
    endTime = time.time()
    elaspedSec = endTime - startTime
    elaspedNanosec = elaspedSec * pow(10, 9)
    
    yield elaspedNanosec
    yield accurPerc(archimedesPi, math.pi)
    
'''
The idea of this technique to estimate pi is very straightforward, so my implementation does not have much to improve upon the textbooks example.
I use the more clear pow() function to add and subtract terms from the accumulation.
I record the elapsed execution time in nanoseconds and send it to the function call.
I also call another function to calculate the accuracy of leibnizPi compared to math.pi and send it to the function call.
'''
def leibnizPi(numOfTerms):
    startTime = time.time()
    leibnizPi = 0
    denom = 1
    
    for i in range(numOfTerms):
        leibnizPi += pow(-1, i) * 4 / denom
        denom += 2
        
    endTime = time.time()
    elaspedSec = endTime - startTime
    elaspedNanosec = elaspedSec * pow(10, 9)
    
    yield elaspedNanosec
    yield accurPerc(leibnizPi, math.pi)

'''
I manipulated the values of the numerator and denominator before multiplying them to the pi approximation, but in a different way than the textbook.
The textbook multiplys by pairs, but my method can multiply by odd numbers of terms. I initialize the pi estimate with 2, as that saves code.
I used the modulus operation to increment the numerator and denominator every other element, also shortening the implementation.
I record the elapsed execution time in nanoseconds and send it to the function call. I also call another function to calculate the accuracy of wallisPi compared to math.pi and send it to the function call.
'''
def wallisPi(numOfTerms):
    startTime = time.time()
    wallisPi = 2
    numer = 0
    denom = 1
    
    for i in range(numOfTerms):
        numer += 2 * ((i - 1) % 2)
        wallisPi *= numer / denom
        denom += 2 * ((i + 1) % 2)
    
    endTime = time.time()
    elaspedSec = endTime - startTime
    elaspedNanosec = elaspedSec * pow(10, 9)
    
    yield elaspedNanosec
    yield accurPerc(wallisPi, math.pi)
    
'''
This method creates two random floats between 0 and 1, which are the coordinates of the “dart” or point.
I use the pythagorean theorem to calculate the distance the point is from the center (0, 0).
The circle has a radius of 1, so if the distance is greater than 1, the point is not in the circle.
The ratio of points in the circle to total points is calculated and multiplied by 4 to estimate pi.
The more points generated, the better the approximation of pi. I record the elapsed execution time in nanoseconds and send it to the function call.
I also call another function to calculate the accuracy of monteCarloPi compared to math.pi and send it to the function call.
'''
def monteCarloPi(numOfPoints):
    startTime = time.time()
    
    pointsInQuartCircle = 0
    for i in range(numOfPoints):
        xCoord = random.random()
        yCoord = random.random()
        
        distFromCenter = math.sqrt(pow(xCoord, 2) + pow(yCoord, 2))
        
        if distFromCenter <= 1:
            pointsInQuartCircle += 1
    
    monteCarloPi = pointsInQuartCircle / numOfPoints * 4
    
    endTime = time.time()
    elaspedSec = endTime - startTime
    elaspedNanosec = elaspedSec * pow(10, 9)
    
    yield elaspedNanosec
    yield accurPerc(monteCarloPi, math.pi)

'''
This function that I wrote takes in two parameters: an experimental value and a theoretical value.
I calculates the percent error of the experimental value and subtracts that from 100.
The accurPerc(sameNum, sameNum) comparing the same number would return a value of 100 (%).
This is used to compare the estimations of pi I have generated to Python’s math.pi value.
'''
def accurPerc(eValue, tValue):
    accurPerc = 100 - (abs(eValue - tValue) / tValue * 100)
    return accurPerc

'''
I store the data of all four functions in lists to graph using matplotlib.
The variable numOfIter specifies how many times each pi estimating function will be called, with increasing complexity and iteration.
For example, the archimedesPi function will calculate pi with a 1 sided polygon, 2 sided polygon, 3 sided polygon, and so on.
The execution times of each function call are recorded as x values and the percent accuracy is recorded as y values.
'''
def main():
    x_archimedesPi = []
    y_archimedesPi = []
    x_leibnizPi = []
    y_leibnizPi = []
    x_wallisPi = []
    y_wallisPi = []
    x_monteCarloPi = []
    y_monteCarloPi = []
    
    numOfIter = 50
    
    for i in range(1, numOfIter + 1):
        result = archimedesPi(i)
        x_archimedesPi.append(next((result)))
        y_archimedesPi.append(next((result)))

        result = leibnizPi(i)
        x_leibnizPi.append(next((result)))
        y_leibnizPi.append(next((result)))
        
        result = wallisPi(i)
        x_wallisPi.append(next((result)))
        y_wallisPi.append(next((result)))
        
        result = monteCarloPi(i)
        x_monteCarloPi.append(next((result)))
        y_monteCarloPi.append(next((result)))
    
    #Graphing Number of Iterations vs Percent Accuracy
    xValues = [i for i in range(1, numOfIter + 1)]
    plt.plot(xValues, y_archimedesPi, label = "Archimedes")
    plt.plot(xValues, y_leibnizPi, label = "Leibniz")
    plt.plot(xValues, y_wallisPi, label = "Wallis")
    plt.plot(xValues, y_monteCarloPi, label = "Monte Carlo")
    plt.legend()
    plt.xlabel('Number of Iterations')
    plt.ylabel('Percent Accuracy to Pi (%)')
    plt.title('Different Pi Estimations')
    plt.show()

    #Graphing Execution Time vs Percent Accuracy (Intermittent Errors)
    '''
    plt.plot(x_archimedesPi, y_archimedesPi, label = "Archimedes")
    plt.plot(x_leibnizPi, y_leibnizPi, label = "Leibniz")
    plt.plot(x_wallisPi, y_wallisPi, label = "Wallis")
    plt.plot(x_monteCarloPi, y_monteCarloPi, label = "Monte Carlo")
    plt.legend()
    plt.xlabel('Execution Time (nanoseconds)')
    plt.ylabel('Percent Accuracy to Pi (%)')
    plt.title('Different Pi Estimations')
    plt.show()
    '''
    
main()