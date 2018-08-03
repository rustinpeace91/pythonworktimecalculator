#Importing the file that can be altered by the user 

import hours;

# worktime is the array that acts as the temporary "memory" of the program, since the program only spits out a calculation, an array works just fine. 
# for now the program uses global variables (maybe not the best way. too much repetition) to store and dispaly user input and calculate totals. 

worktime = []
currentHours = 0;
currentMinutes = 0;
totalHours = 0;
totalMinutes = 0;

# initial menu that displays when the program is run. 
# the user can either total their hours from the hours.py file, or input them in the program itself

def menu():
    introText = "Would you like to: \n a)read from the file or \n b)read from user input?"
    selection = input(introText + "\n->");
    if selection == "a":
        readFromModule();
    elif selection == "b":
        readFromInput();
    else:
        print("please type a valid answer!");
        selection();

# sets the worktime array to the values displayed in the user file 

def readFromModule():
    worktime = hours.user();
    readFromArray(worktime);

# prints a string for hours and minutes


def readFromInput():
    global currentHours;
    global currentMinutes;
    global worktime;
    global totalHours;
    global totalMinutes;
    done = False;
    while done == False:
        choiceText = "what would you like to do? \n a)input another time \n b)get the total? \n->";
        choice = input(choiceText);
        if choice == "a":
            currentWorkperiod = howMany();
            currentHours = currentWorkperiod[0];
            currentMinutes = currentWorkperiod[1] ;
            printTime(currentHours, currentMinutes);
            totalHours += currentHours;
            totalMinutes += currentMinutes;
            timeString = str(currentWorkperiod[0]) + ":" + str(currentWorkperiod[1]);
            worktime.append(timeString);
            
        if choice == "b":
            readFromArray(worktime);

# cycles through the array, adds up the total and prints all of the individual entries 

# takes in the user input and, validates it and converts it to an integer, then returns an array of hours and minutes. 

def howMany():
        try:
           hours = input("How many hours? \n->");
           hours = int(hours);
        except ValueError:
           print("That's not an integer!");
           return howMany();

        try:
           minutes = input("How many minutes? \n->");
           minutes = int(minutes);
        except ValueError:
           print("That's not an integer!");
           return howMany();
    
        hours = abs(hours);
        minutes = abs(minutes);
        return [hours,minutes];

def printTime(hours, minutes):
    print(str(hours) + " hours and " + str(minutes) + " minutes");

# takes user input, and modifies the array and total based on input

def readFromArray(worktime):
    global currentHours;
    global currentMinutes;
    global totalHours;
    global totalMinutes;
    totalHours = 0;
    totalMinutes = 0;
    print(worktime);
    for i in worktime:
        a = i.split(":");
        currentHours = int(a[0]);
        currentMinutes = int(a[1]);
        totalHours += int(currentHours);
        totalMinutes += int(currentMinutes);
        printTime(currentHours, currentMinutes);
    print("------------------------------------------");
    print("TOTAL:");
    calculateTotal();

# converts the excess minutes to hours and displays the final total

def calculateTotal():
    global totalHours;
    global totalMinutes;
    totalHours += int(totalMinutes / 60);
    totalMinutes = totalMinutes % 60;
    printTime(totalHours, totalMinutes);

    

if __name__ == "__main__":
    menu();