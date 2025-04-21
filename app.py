import streamlit as st
import json
import os
from datetime import datetime
import time
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
from collections import Counter

# --- Helper Functions ---

def load_lottieurl(uri):
    try:
        r = requests.get(uri)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def load_library():
    try:
        if os.path.exists('library.json'):
            with open('library.json', 'r') as file:
                st.session_state.library = json.load(file)
    except Exception as e:
        st.error(f"Error loading library: {e}")

def save_library():
    try:
        with open('library.json', 'w') as file:
            json.dump(st.session_state.library, file, indent=4)
        return True
    except Exception as e:
        st.error(f"Error saving library: {e}")
        return False

def add_book(title, author, publication_year, genre, read_status):
    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status,
        'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time.sleep(0.5)

def search_books(search_term, search_by):
    search_term = search_term.lower()
    results = []

    for book in st.session_state.library:
        if search_by == "Title" and search_term in book['title'].lower():
            results.append(book)
        elif search_by == "Author" and search_term in book['author'].lower():
            results.append(book)
        elif search_by == "Genre" and search_term in book['genre'].lower():
            results.append(book)

    st.session_state.search_results = results

def get_library_stats():
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book['read_status'] == 'Read')
    unread_books = total_books - read_books

    genres = [book['genre'] for book in st.session_state.library]
    genre_count = dict(Counter(genres))

    authors = [book['author'] for book in st.session_state.library]
    author_count = dict(Counter(authors))

    decades = [str(int(book['publication_year']) // 10 * 10) + 's' for book in st.session_state.library]
    decade_count = dict(Counter(decades))

    return total_books, read_books, unread_books, genre_count, author_count, decade_count

# --- UI Setup ---

st.set_page_config(page_title="📚 Personal Library", layout="wide")
st.title("📚 My Personal Library Manager")

if 'library' not in st.session_state:
    st.session_state.library = []
    load_library()

if 'search_results' not in st.session_state:
    st.session_state.search_results = []

if 'book_added' not in st.session_state:
    st.session_state.book_added = False

# --- Lottie Animation ---
with st.sidebar:
    st_lottie(load_lottieurl("https://lottie.host/3a41bc5e-bf16-4ee5-90c1-5c9ac0cd1cc6/DGS3sAG5r3.json"),
              height=200, key="reading")

# --- Add Book ---
st.header("➕ Add a New Book")
with st.form("add_book_form", clear_on_submit=True):
    title = st.text_input("Title")
    author = st.text_input("Author")
    publication_year = st.text_input("Publication Year")
    genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Fantasy", "Biography", "Other"])
    read_status = st.radio("Read Status", ["Read", "Unread"])
    submitted = st.form_submit_button("Add Book")
    if submitted:
        if title and author and publication_year:
            add_book(title, author, publication_year, genre, read_status)
            st.success(f"'{title}' added to your library!")
        else:
            st.error("Please fill in all the fields.")

# --- Search ---
st.header("🔍 Search Library")
search_term = st.text_input("Search")
search_by = st.selectbox("Search by", ["Title", "Author", "Genre"])
if st.button("Search"):
    search_books(search_term, search_by)
    st.subheader("Search Results")
    if st.session_state.search_results:
        for book in st.session_state.search_results:
            st.write(f"📖 **{book['title']}** by {book['author']} ({book['publication_year']}) - *{book['genre']}* - **{book['read_status']}**")
    else:
        st.info("No matching books found.")

# --- Show All Books ---
st.header("📚 Library Books")
if st.session_state.library:
    for book in st.session_state.library:
        st.markdown(f"**{book['title']}** by *{book['author']}* ({book['publication_year']}) | Genre: {book['genre']} | Status: **{book['read_status']}**")
else:
    st.info("Your library is empty. Add some books!")

# --- Stats and Visuals ---
st.header("📊 Library Statistics")
if st.session_state.library:
    total, read, unread, genre_data, author_data, decade_data = get_library_stats()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Books", total)
    col2.metric("Books Read", read)
    col3.metric("Unread Books", unread)

    st.subheader("📈 Books by Genre")
    st.plotly_chart(px.pie(names=list(genre_data.keys()), values=list(genre_data.values()), title="Genres"))

    st.subheader("🧑‍💻 Top Authors")
    top_authors = dict(sorted(author_data.items(), key=lambda item: item[1], reverse=True)[:5])
    st.plotly_chart(px.bar(x=list(top_authors.keys()), y=list(top_authors.values()), labels={'x': 'Author', 'y': 'Books'}))

    st.subheader("📅 Books by Decade")
    st.plotly_chart(px.bar(x=list(decade_data.keys()), y=list(decade_data.values()), labels={'x': 'Decade', 'y': 'Books'}))
else:
    st.info("Add books to see your library stats!")
