
import pandas as pd
import matplotlib.pyplot as plt
def average():
    course1 = float(input("Enter the mark of course 1: "))
    course2 = float(input("Enter the mark of course 2: "))
    course3 = float(input("Enter the mark of course 3: "))
    ave = (course1 + course2 + course3) /3
    return ave
names =[]
all_averages = []
number_of_students = int(input("Enter the number of students: "))
for i in range (1,number_of_students+1):
    print(f"Student number: {i}")
    name =input("Enter the student name: ")
    avg = average()
    print(f"Average of {name}: {avg:.2f}")
    names.append(name)
    all_averages.append(avg)

min_avg = min(all_averages)


max_avg = max(all_averages)
print(f"The minimum average is: {min_avg:.2f}")
print(f"The maximum average is: {max_avg:.2f}")

data ={
    "Name": names,
    "Average": all_averages }
df = pd.DataFrame(data)
print(df)
df.to_csv("students.csv", index=False)
plt.bar(names, all_averages)
plt.title("Average of all students")
plt.xlabel("Students")
plt.ylabel("Average marks")
plt.show()
df = pd.read_csv("students.csv")