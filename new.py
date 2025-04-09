import numpy as np
import pandas as pd

# students=[]
# def add_student():
#     name=input("enter student name :")
#     age=int(input("enter student age :"))
#     marks=list(map(float,input("enter marks for 3 subjects(separated by sapce):").split()))

#     student={"name":name,"age":age,"marks":np.array(marks)}
#     students.append(student)
#     print(f"student '{name}' added successfully! \n")

# def show_student():
#     if not students:
#         print("\n no students available")
#         return
    
#     df=pd.DataFrame([{"name":s["name"],"age":s["age"],"average marks":np.mean(s["marks"])} for s in students])
#     print("\n student records:\n",df)

# def analyze_data():
#     if not students:
#         print("\n no data avilable for analysis!")
#         return
    
#     age=np.array([s["age"] for s in students])
#     avg_ages=np.mean(age)

#     all_marks=np.concatenate([s["marks"] for s in students])
#     avg_marks=np.mean(all_marks)
#     max_marks=np.max(all_marks)
#     min_marks=np.min(all_marks)

#     print("\ndata analysis:")
#     print(f"average age of students :{avg_ages:.2f}")
#     print(f"average marks:{avg_marks:.2f}")
#     print(f"highest marks:{max_marks}")
#     print(f"lowest marks:{min_marks}\n")

# def save_data():
#     if not students:
#         print("\n no data to save!")
#         return
    
#     df=pd.DataFrame([{"name":s["name"],"age":s["age"],"marks":', '.join(map(str,s["marks"]))} for s in students])
#     df.to_csv("student.csv",index=False)
#     print("\n student data saved to 'student.csv' successfully!\n")

# def main():
#     while True:
#         print("\n student data management")
#         print("1. add students")
#         print("2. show students")
#         print("3.analyze students")
#         print("4.save sata to csv")
#         print("5. exit")

#         choice=input("enter an option from 1-5")
#         if choice== "1":
#             add_student()

#         elif choice=="2":
#             show_student()

#         elif choice=="3":
#             analyze_data()

#         elif choice=="4":
#             save_data()

#         elif choice=="5":
#             print("see you soon")
#             break
        
#         else :
#             print("enter a valid option")
# main()
import random
a = [1, 2, 3, 4, 5] 
b = [6, 7, *a, 8, 9] 
ff=random.randint(1,100)
f=random.randint(1,100)
print(ff,"\n",f)
print()