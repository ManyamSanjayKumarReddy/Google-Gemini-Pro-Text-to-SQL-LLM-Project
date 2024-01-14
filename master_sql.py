import sqlite3
import csv

# Connect to sqlite
connection = sqlite3.connect("master.db")
cursor = connection.cursor()

# Create a table
table_info = """
CREATE TABLE MASTER (
    "S.No." INTEGER,
    Name VARCHAR(25),
    Registration VARCHAR(25),
    DOB DATE,
    Gender VARCHAR(10),
    "Department" VARCHAR(25),
    "Section" VARCHAR(25),
    "Specialization" VARCHAR(25),
    CGPA REAL,
    "Active Backlogs" INTEGER,
    "History Arrears" INTEGER,
    "Academic Gap" INTEGER,
    "Diploma-Percentage" REAL,
    "Diploma-Specialization" VARCHAR(25),
    "12-Percentage" REAL,
    "10th-Percentage" REAL,
    Aadhar VARCHAR(25),
    PAN VARCHAR(25),
    City VARCHAR(25),
    "City Pincode" VARCHAR(10),
    District VARCHAR(25),
    State VARCHAR(25),
    "Mobile-1" VARCHAR(15),
    Email VARCHAR(50)
);
"""

cursor.execute(table_info)

# Read data from CSV and insert into the database
with open('master.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        cursor.execute(
    "INSERT INTO MASTER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        row["S.No."],
        row["Name"],
        row["Registration"],
        row["DOB"],
        row["Gender"],
        row["Department"],
        row["Section"],
        row["Specialization"],
        row["CGPA"],
        row["Active Backlogs"],
        row["History Arrears"],
        row["Academic Gap"],
        row["Diploma-Percentage"],
        row["Diploma-Specialization"],
        row["12-Percentage"],
        row["10th-Percentage"],
        row["Aadhar"],
        row["PAN"],
        row["City"],
        row["City Pincode"],
        row["District"],
        row["State"],
        row["Mobile-1"],
        row["Email"]
    )
)

# Display all records in the MASTER table
print("The Inserted Records are ..")
data = cursor.execute('SELECT * FROM MASTER')
for row in data:
    print(row)

# Commit and close the connection
connection.commit()
connection.close()
