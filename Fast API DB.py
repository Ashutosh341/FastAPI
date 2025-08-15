from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pyodbc # type: ignore


server = 'ASHUTOSH\MSSQLSERVER03'       # e.g., 'DESKTOP-12345\\SQLEXPRESS'
database = 'NamasteSQl'
username = 'Ashutosh/ashut'
##password = 'YOUR_DB_PASSWORD'
driver = '{ODBC Driver 17 for SQL Server}'

app=FastAPI()
def get_connection():
    return pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'Trusted_Connection=yes;'

    )

class Book(BaseModel):
    id:int
    title: str
    author: str
    year: int


@app.post("/books")
def create_book(book:Book):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO Books (id,title, author, year) VALUES (?, ?, ?,?)",
        (book.id,book.title, book.author, book.year)
    )
    conn.commit()
    conn.close()
    return {"message": "Book added successfully"}

@app.get("/books")
def get_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year FROM Books")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": row[0], "title": row[1], "author": row[2], "year": row[3]}
        for row in rows
    ]


