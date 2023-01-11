
class Student:

    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def show(self):
        print("Student ID: ",self.eid)
        print("Student Name: ",self.ename)


    def std_class(eclass):
        eclass=12
        print("Class: ",eclass)
    def english(self):
        marks = float(input("Enter English marks: "))
        print("English: ",marks)
    def subjects(self):
        sub1 = str(input("Choose language subject Hindi/Sanskrit: "))
        if (sub1 == "Hindi"):
            mark1 = float(input("Enter Hindi marks: "))
            print("Hindi: ",mark1)

        else:
            mark1 = float(input("Enter Sanskrit marks: "))
            print("Sanskrit: ", mark1)

        sub2 = str(input("Choose Subject background category Science/Commerce: "))

        if (sub2=="Science"):
            print("You have entered Science background")
            phy = float(input("Enter Physics Marks: " ))
            chem = float(input("Enter Chemistry Marks: " ))
            maths = float(input("Enter Maths Marks: " ))
            print("Physics: ",phy,"\n","Chemistry: ",chem,"\n","Maths: ",maths)
        else:
            print("You have entered Commerce background")



st=Student(100,"Rajesh")
st.show()
st.std_class()
st.english()
st.subjects()