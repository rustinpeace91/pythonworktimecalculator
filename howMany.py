
# import pdb
# def howMany():
#         try:
#            hours = input("How many hours? \n->");
#            hours = int(hours);
#            hours = abs(hours);
#         except ValueError:
#            print("That's not an integer!");
#            howMany();

#         try:
#            minutes = input("How many minutes? \n->");
#            minutes = int(minutes); 
#            hours = abs(hours);
#         except ValueError:
#            print("That's not an integer!");
#            howMany();
    
#         minutes = abs(minutes);
#         print([hours,minutes]);

# if __name__ == "__main__":
#     howMany();


import pdb
def howMany():
       hours = 0;
       minutes = 0;
       hours = input("How many hours? \n->");
       if hours.isnumeric():
         hours = int(hours);
         hours = abs(hours);
       else:
         print("That's not an integer!");
         return howMany();


       minutes = input("How many minutes? \n->");
       if minutes.isnumeric():
         minutes = int(minutes); 
         minutes = abs(minutes);
       else:
         print("That's not an integer!");
         return howMany();
    

       print([hours,minutes]);

if __name__ == "__main__":
    howMany();
