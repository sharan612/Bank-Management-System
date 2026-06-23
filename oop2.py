# class student:
#     def __init__(self):
#         self.name=input("enter name:")
#         self.course=input("enter course:")
#     def display(self):
#             print(f"name is {self.name} and course is {self.course}")
# s1=student()
# s2=student()
# s1.display()
# s2.display()

class employee:
    def __init__(self):
        self.name=input("enter name:")
        self.designation=input("enter designation:")
        self.salary=int(input("enter salary:"))
    def display(self):
        print(f"The employee {self.name} working as a {self.designation} has a salary of  {self.salary}")
        
    employee_list=[]
    n=int(input("enter number of employees you want:"))
    for i in range(1,n+1):
        e1=employee()
        employee_list.append(e1)
    for e in employee_list:
        e.display()
            


    
       




    # def highest(e1,e2,e3):
    #     if e1.salary>e2.salary and e1.salary>e3.salary:
    #         print(f"{e1.name} has highest salary")
    #     elif e2.salary>e1.salary and e2.salary>e3.salary:
    #         print(f"{e2.name} has highest salary")
    #     elif e3.salary>e1.salary and e3.salary>e2.salary:
    #         print(f"{e3.name} has highest salary")
    
# e1=employee()        
# e2=employee()
# e3=employee()
# e1.display()
# e2.display()
# e3.display()
# e1.highest(e2,e3)
