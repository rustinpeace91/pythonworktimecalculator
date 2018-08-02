

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


def readFromArray():
    global currentHours;
    global currentMinutes;
    for i in worktime:
        a = i.split(":");

        currentHours += int(a[0]);
        currentMinutes += int(a[1]);
        currentHours += int(currentMinutes / 60);
        currentMinutes = int(currentMinutes % 60);
    print(currentHours);
    print(currentMinutes);
    

def readFromInput():
    pass;
    

if __name__ == "__main__":
    readFromArray();

    
    
