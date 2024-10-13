from dotenv import load_dotenv

load_dotenv()  ## load all env variable
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure api Key
genai.configure(api_key="123")


## function to load googel gemini model and provide sql query as response
def get_gemini_response(questions, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], questions])
    return response.text


## func to retrieve query from sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define Your Prompt
prompt =[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION,MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

st.set_page_config(page_title="Sql Query Retrieval")
st.header("Retrieve SQL Data")
questions = st.text_input("input: ",key="input")
submit = st.button("Ask question")

## ON SUBMIT CLICK
if submit:
    response=get_gemini_response(questions,prompt)
    print(response)
    data = read_sql_query(response,'student.db')
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)
