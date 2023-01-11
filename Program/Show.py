class Timing:
    def time1(self):
        print("You have selected Show timing of 11am")
    def time2(self):
        print("You have selected Show timing of 3pm")
    def time3(self):
        print("You have selected Show timing of 6pm")
class Show(Timing):
    def shows(self):
        theater = str(input('Enter Theater No. 1/2/3: '))
        if (theater == "1"):
                print("Shows in Theater 1: Avataar-2/Drishyam-2/Freddy: ")
                ph=print(str(input("Select movies name: ")))
                a="Avataar-2"
                b="Drishyam-2"
                c="Freddy"
                if(ph.__eq__(a)):
                       print("Avataar-2 show timings: 11am,3pm,6pm")
                       ch = str(input("Select show timigs: "))
                       if(ch=="11am"):
                           Timing.time1(self)
                       elif(ch=="3pm"):
                           Timing.time2(self)
                       elif(ch=="6pm"):
                           Timing.time3(self)

                elif(ph.__eq__(b)):
                           print(" Drishyam-2 show timings: 11am,3pm,6pm")
                           ch1 = str(input("Select show timigs: "))
                           if (ch1 == "11am"):
                               Timing.time1(self)
                           elif (ch1 == "3pm"):
                               Timing.time2(self)
                           else:
                               Timing.time3(self)
                elif(ph.__eq__(c)):
                           print(" Freddy show timings: 11am,3pm,6pm")
                           ch2 = str(input("Select show timigs: "))
                           if (ch2 == "11am"):
                               Timing.time1(self)
                           elif (ch2 == "3pm"):
                               Timing.time2(self)
                           elif (ch2 == "6pm"):
                               Timing.time3(self)
        else:
               print("end")

show = Show()
show.shows()