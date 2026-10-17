import numpy as np
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Python": [85, 92, 45, 78, 88],
    "Maths": [78, 89, 52, 74, 91],
    "Science": [90, 94, 48, 82, 86]
}

df = pd.DataFrame(data)

marks = df[["Python", "Maths", "Science"]].to_numpy()

df["Total"] = np.sum(marks, axis=1)
df["Average"] = np.mean(marks, axis=1).round(2)

df["Result"] = np.where(
    (marks >= 35).all(axis=1),
    "Pass",
    "Fail"
)

print("\nSTUDENT PERFORMANCE REPORT")
print(df.to_string(index=False))

topper = df.loc[df["Average"].idxmax()]

print("\nCLASS TOPPER:", topper["Name"])
print("TOPPER AVERAGE:", topper["Average"])

subject_avg = df[["Python", "Maths", "Science"]].mean()

print("\nSUBJECT-WISE AVERAGE")
print(subject_avg.round(2))

high_scorers = df[df["Average"] > 75]

print("\nSTUDENTS WITH AVERAGE ABOVE 75")
print(high_scorers[["Name", "Average"]].to_string(index=False))

print("\nCLASS SUMMARY")
print("Total Students:", len(df))
print("Passed:", (df["Result"] == "Pass").sum())
print("Failed:", (df["Result"] == "Fail").sum())
print("Class Average:", round(df["Average"].mean(), 2))
