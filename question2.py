#Question 2

def findAverage(list):

    runningTotal = 0.0
    count = 0

    #Loop through the list
    for i in list:
        runningTotal = runningTotal + i
        count = count + 1

    #The case that there are 0 elements in the list (error with divide by 0)
    if count == 0:
        return -1

    #Calculate average
    average = runningTotal / count

    return average

# list = [1, 2, 3, 4, 5]
# findAverage(list)
