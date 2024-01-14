from dotenv import load_dotenv
import streamlit as st 
import os
import sqlite3 
import google.generativeai as genai 

# Load environment variables
load_dotenv()

# Configure API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to handle errors and provide emotional responses
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.warning("Please check your input and try again.")
    return wrapper

# Function to load Google Gemini model and Provide SQL Query as the Response
@handle_errors
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])

    # Remove formatting (```sql) from the response
    clean_response = response.text.replace("```sql", "").strip()

    # Split multiple statements into a list
    sql_statements = [statement.strip() for statement in clean_response.split(';') if statement.strip()]

    return sql_statements

# Function to Retrieve query from the SQL Database
@handle_errors
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    if not rows:
        st.warning("No data found for the given query.")
    else:
        st.subheader("SQL Query Result:")
        st.table(rows)
    return rows

# Streamlit App 
st.set_page_config(page_title="Student Data Analyzer", layout="wide")
st.title("Student Data Analyzer Application using Google Gemini Pro")


# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name MASTER and includes various columns such as 
    Name, Registration, DOB, Gender, Department, Section, 
    Specialization, CGPA, Active Backlogs, History Arrears, Academic Gap, 
    Diploma-Percentage, Diploma-Specialization, 12-Percentage, 10th-Percentage, 
    Aadhar, PAN, City, City Pincode, District, State, Mobile-1, Email.
    
    Feel free to ask any SQL-related questions about the MASTER database. Here are some sample questions:
    
    1. Retrieve all records for students with a CGPA greater than 8.
    2. Find the count of students with active backlogs.
    3. Show details for students who have an academic gap of more than 1 year.
    4. Get the average CGPA for students in the 'Data Science' UG-Specialization.
    5. Find students from a specific city and state.
    6. Show the top 5 students based on their 12th percentage.
    7. Retrieve details for students born after a certain date.
    
    Remember, these are just sample questions. You can ask any SQL question, and I'll provide you with the corresponding SQL query.
    
    also, the SQL code should not have ``` in the beginning or end and sql word in output.
    """
]

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# If submit is clicked
if submit:
    with st.spinner("Fetching response..."):
        responses = get_gemini_response(question, prompt)
    
    for response in responses:
        print(response)
        data = read_sql_query(response, "master.db")
