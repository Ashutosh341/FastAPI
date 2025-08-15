from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for request/response
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books_db: List[Book] = []


@app.post("/books", response_model=Book, status_code=201, tags=["Books"])
def create_book(book: Book):
    # Check if ID already exists
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book


@app.get("/books", response_model=List[Book], tags=["Books"],summary="Fetch a specific book",
    description="Get detailed information about a book using its unique ID.")
def get_books():
    return books_db


@app.get("/books/{book_id}", response_model=Book, tags=["Books"])
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book, tags=["Books"])
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204, tags=["Books"])
def delete_book(book_id: int):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Book not found")
