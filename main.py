import hours;

worktime = []
currentHours = 0;
currentMinutes = 0;
totalHours = 0;
totalMinutes = 0;

def printTime(hours, minutes):
    print(str(hours) + " hours and " + str(minutes) + " minutes");

def readFromModule():
    worktime = hours.user();
    readFromArray(worktime);

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

def calculateTotal():
    global totalHours;
    global totalMinutes;
    totalHours += int(totalMinutes / 60);
    totalMinutes = totalMinutes % 60;
    printTime(totalHours, totalMinutes);


def howMany():
        hours = input("How many hours? \n->");
        try:
           hours = int(hours);
        except ValueError:
           print("That's not an integer!")
        minutes = input("How many minutes? \n->");
        try:
           minutes = int(minutes);
        except ValueError:
           print("That's not an integer!")
        
        hours = abs(hours);
        minutes = abs(minutes);
        return [hours,minutes];

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
    

if __name__ == "__main__":
    menu();


    
    
