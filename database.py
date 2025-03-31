
import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="neondb",  # Tumhara Neon Database Name
        user="neondb_owner",  # Tumhara Neon User
        password="npg_umU8LsfQ7Tnb",  # Tumhara Neon Password
        host="ep-old-darkness-a5hnbzi7-pooler.us-east-2.aws.neon.tech",  # Tumhara Neon Host
        port="5432",  # Default PostgreSQL Port
        sslmode="require"  # SSL Mode Required hai Neon ke liye
    )

# Function to Add a Book
def add_book(name, author, genre, year, read_status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (name, author, genre, year, read_status) VALUES (%s, %s, %s, %s, %s)",
                   (name, author, genre, year, read_status))
    conn.commit()
    conn.close()

# Function to Delete a Book
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    conn.close()

# Function to Update Read Status
def update_book_status(book_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET read_status = %s WHERE id = %s", (new_status, book_id))
    conn.commit()
    conn.close()

# Function to Get All Books
def get_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books
