def calcAverage( avg1, avg2, avg3, avg4, avg5, avg6):
    agerage = ( average1 + average2 + average3 + average4 + average )/5
    return average
def determineGrade( userAverage ):
    if(userAverage <40 ):
       return "F"
    elif( userAverage < 50 ):
           return "D"
    elif( userAverage < 60 ):
        return "C"
    elif( userAverage < 70 ):
        return "B"
    elif( userAverage < 101):
        return "A"
def askForAverages():
    average1 = float( input("please enter score 1: " ) )
    average2 = float( input("please enter score 2: " ) )
    average3 = float( input("please enter score 3: " ) )
    average4 = float( input("please enter score 4: " ) )
    average5 = float( input("please enter score 5: " ) )
    return average1, average2, average3, average4, average5
def printTableOfResults( average1, average2, average3, average4, average5 ):
    print( "Average\tLetter Grade" )
    print( str( average1 ) + "\t\t" + determineGrade (average1 ), \
           str( average2 ) + "\t\t" + determineGrade (average2 ), \
           str( average3 ) + "\t\t" + determineGrade (average3 ), \
           str( average4 ) + "\t\t" + determineGrade (average4 ), \
           str( average5 ) + "\t\t" + determineGrade (average5 ), sep = "\n" )
           
    
def main():
    average1, average2, average3, average4, average5 = askForAverages()
    printTableOfResults(  average1, average2, average3, average4, average5 )

main()    
    
    
                             
                          
                          
          
