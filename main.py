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
    for i in worktime:
        a = i.split(":");
        currentHours = int(a[0]);
        currentMinutes = int(a[1]);
        totalHours += int(currentHours);
        totalMinutes += int(currentMinutes);
        printTime(currentHours, currentMinutes);
    print("------------------------------------------");
    print("TOTAL:");

def calculateTotal:
    global totalHours;
    global totalMinutes;
    totalHours += int(totalMinutes / 60);
    totalMinutes = totalMinutes % 60;
    printTime(totalHours, totalMinutes);


    

def readFromInput():
    print("user Input coming soon!");
    pass;

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


    
    
