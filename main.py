

worktime = [
    "00:15",
    "02:17",
    "00:31",
    "00:25",
    "30:45",
    "00:14",
    "04:17",
    "00:32",
    "05:15",
    "00:15",
    "20:30",
]
currentHours = 0;
currentMinutes = 0;
totalHours = 0;
totalMinutes = 0;

def printTime(hours, minutes):
    print(str(hours) + " hours and " + str(minutes) + " minutes");

def readFromArray():
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
    totalHours += int(totalMinutes / 60);
    totalMinutes = totalMinutes % 60;
    printTime(totalHours, totalMinutes);
    
    

def readFromInput():
    pass;
    

if __name__ == "__main__":
    readFromArray();

    
    
