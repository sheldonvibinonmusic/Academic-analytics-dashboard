import pandas as pd

df=pd.read_csv("academic_data.csv")

print("\n========== DATASET OVERVIEW ==========\n")
print(df.describe()) #prints all basic info 
print("\n",df.columns) #returns column names

subject=["Maths","Physics","Chemistry","English"]

print("\n========== SUBJECT ANALYSIS ==========\n")

for sub in subject:

    print("\nMean marks of",sub,"is",df[sub].mean())
    print("Max marks of",sub,"is",df[sub].max())
    print("Min marks of",sub,"is",df[sub].min())

df["Total"]=df["Maths"]+df["Physics"]+df["Chemistry"]+df["English"]
print("\nCalculating Total and Percentage...")
df["Percentage"]=df["Total"]*100/400

#MARKS ANALYSIS
print("\n========== PERFORMANCE ANALYSIS ==========\n")

highest=df.loc[df["Percentage"].idxmax()]
print("Highest scorer is: ",highest["Name"],highest["Percentage"])

lowest=df.loc[df["Percentage"].idxmin()]
print("Lowest scorer is: ",lowest["Name"],lowest["Percentage"])

for i in range(len(df)):
    if (df["Percentage"][i]>=90):
        print("Excellent performers:",df["Name"][i])

    elif(df["Percentage"][i]>=75 and df["Percentage"][i]<90):
        print("Good performers:",df["Name"][i])

    elif(df["Percentage"][i]>=60 and df["Percentage"][i]<75):
        print("Can do better:",df["Name"][i])

    elif(df["Percentage"][i]<60):
        print("Need serious improvement:",df["Name"][i])           


#ATTENDANCE ANALYSIS
print("\n========== ATTENDANCE ANALYSIS ==========\n")

high_attend=df.loc[df["Attendance"].idxmax()]
print("Student with high attendance: ",high_attend["Name"])

low_attend=df.loc[df["Attendance"].idxmin()]
print("Student with low attendance: ",low_attend["Name"])

#STUDY HOURS ANALYSIS
print("\n========== STUDY HOURS ANALYSIS ==========\n")

max_hr=df.loc[df["HoursStudied"].idxmax()]
print("Student studying most: ",max_hr["Name"])

min_hr=df.loc[df["HoursStudied"].idxmin()]
print("Student studying least: ",min_hr["Name"])

#EACH STUDENT ANALYSIS
print("\n========== STUDENT INSIGHTS ==========\n")

for i in range(len(df)):
    marks=[df["Maths"][i],df["Physics"][i],df["Chemistry"][i],df["English"][i]]
    print("For",df["Name"][i],"max marks in",subject[marks.index(max(marks))],"and min marks in",subject[marks.index(min(marks))])


#SORTING
print("\n========== TOP 10 STUDENTS ==========\n")
print(df.sort_values("Percentage",ascending=False).head(10))

print("\n========== BOTTOM 10 STUDENTS ==========\n")
print(df.sort_values("Percentage",ascending=False).tail(10))


#GROUPBY
attendance_badge=[]

for i in range(len(df)):
    if df["Attendance"][i]>=90:
        attendance_badge.append("High")

    elif df["Attendance"][i]>=75:
        attendance_badge.append("Medium")

    else:
        attendance_badge.append("Low")        

df["Attendance review"]=attendance_badge

#GROUPBY INSIGHTS

print("\n========== GROUPBY SUMMARY ==========\n")
print(df.groupby("Attendance review")["Percentage"].agg(["count","mean","max","min"]))