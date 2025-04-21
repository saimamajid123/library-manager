import streamlit as st
import pandas as pd 
import json 
import os 
import datatime import datatime 
import time 
import random 
import plotly.express as px 
import plotly.graph_objects as go
from streamlit_lottie import streamlit_lottie
import requests 

#set page configuration 
st.set_page_config(
    page_title="personal Library Management System", 
    page_icon="📚", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

#custom css for styling 
st.markdown("""
<style> 
    .main-header {
    font-size: 3rem !important; 
    color: #1E3A8A; 
    font-weight: 700; 
    margin-bottom: 1rem; 
    text-align: center;
     text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    } 

    .sub_header {
    font-size: 1.8rem !important;
    color: 3B82F6;
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.success-message {
    padding: 1rem;
    background-color: #ECFDF5;
    border-left: 5px solid #10B981;
    border-radius: 0.375rem; 
}

.warning-message {
    padding: 1rem;
    background-color: #FEF3C7;
    border-left: 5px solid #F59E0B;
    border-radius: 0.375rem;
}

.book-card {
    background-color: #F3F4F6;
    border-radius: 0.5rem;
    padding: 1rem;
    margin-bottom: 1rem;
    border-left: 5px solid #3B82F6;
    transition: transform 0.3s ease;
}

.book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3pc rgba(0,0,0,0,.1);
}
.read-badge {
    background-color:  #10B981;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.875rem;
    font-weight: 600;
}
.unread-badge {
    background-color:  #F87171;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.875rem;
    font-weight: 600;
}
.action-button {
    margin-right: 0.5rem;
}
.stButton>button {
    border-radius: 0.375rem;
}
</style>
""", unsaf_allow_html=True)

#next video 2 code continue:
def load_lottieur(uri)
if r.status_code != 200:
    return None
return r.json()
except:
    return None

if 'library' not in st.session_state:
    st.session_state.library = []
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'book_added' not in st.session_state:
    st.session_state.book_added = False
if 'book_removed' not in st.session_state:
    st.session_state.book_removed = False
if 'current_view' not in st.session_state:
    st.session_state.current_view = "library"


def load_lirary():
    try:
        if os.path.exists('library.json'):
        with open('library.json' , 'r') as file:
            return False
except Exception as e:
    st.error(f"Error loading library: {e}")
    return False

#save library
def save_library():
    try:
        with open ('library.json', 'w') as file:
            json.dum(st.session_state.library, file)
            retne True
    except Exception as e:
        st.error(f"Error loading library: {e}")
        return False

#add a book to library
def add_book(title, author , publication_year,genre, read_status):
    book = {
        'title'= title,
        'author' = author,
        'publication_year'= publication_year,
        'genre' = genre,
        'read_status' = read_status,
        'added_data': datatime.now().strtime("%Y-%m-%d %H:%M:%S") 
    } 
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time,sleep(0.5)  #animation delay

#remove books
def remove_book(index):
    if 0 <= index < len(st.session_state.library):

        del st.session_state,library[index]
        save_library()
        st.session_state.book_removed = True
        return True
    return False

#search books
def search_book(search_term, search_by):
    search_term = search_term.lower()
    return = []

    for book in st.session_state.library:
        if search_by == "Title" and search_term in book['titel'].lower():
            results.append(book)
        elif search_by == "Author" and search_term in book['author'].lower():
            results.append(book)
         elif search_by == "Genre" and search_term in book['genre'].lower():
            results.append(book)
    st.session_state.search_results = results 

#calculate library
def get_library_stats():
    total_books = len(st.session_state.library)
    read-books =sum(1 for book in st.session_state.library if book['read_status'])
    percent_read = (read_book / total_books * 100) if total_books > 0 else 0

    genres = {}
    authors = {}
    decades = {}

for book in st.session_state.library
if book['genre'] in genres:
    genres [book['genre']] += 1
else:
    genres[book['genre']] = 1

#count author
if book['author'] in authors:
    authors [book['author']] += 1
else:
    authors[book['author']] = 1

#count decades
decades = (book ['publication_year'] // 10) * 10
if decades in decades:
    decades[decade] += 1
else:
    decades[decades] = 1

#sort by count
genres =dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
authors =dict(sorted(authors.items(), key=lambda x: x[1], reverse=True))
decades =dict(sorted(decades.items(), key=lambda x: x[0]))

return {
    'total_books' : total_books,
    'read_books'  :read_books,
    'percent_read' : percent_read,
    'genres' genres,
    'authors' : authors,
    'decades' : decades,
}

def create_visulation(stats)
    if stats['total_books'] > 0:
        fig_read_status = go.figure(data=[go.pie(
            labels=['reads' , 'Unread'],
            values=[stats['read_books'], stats['total_books'] - stats['read_book']],
            hole=.4,
            marker_colors=['#10B981' , '#F87171']
        )])
        fig_read_status.update_layout(
            titel_text="Read vs Unread Books",
            showlegend =True,
            height=400
        )
        st.plotly_chart(fig_read_status, use_container_width=True)
#bar chart genres
if stats['genres']:
    genre_df = pd.DataFrame({
        'Genre': list(stats'[genres'].keys()),
        'Count': list(stats['genres'].values())
    })
    fig_genres = px.bar(
        genre_df,
        x='Genre',
        y='Count',
        color= 'Count',
        color_continous_scale=px.colors.sequential.Blues
    )
    fig_genres.update_layout(
        titel_text='Book by publication genres',
        xaxis_text='Genres',
        yaxis_title='Numbers of books',
        height=400
    )
    st.plotly_chart(fig_genres, use_container_width=True)
if stats['decades']:
    decades_df =pd.DataFrame({
        'Decade': [if"{decade}s" for decade in stats['decades'].keys()],
        'Count': list(stats['decades'].values())
    })
    fig_decades = px.line(
        decades_df,
        x='Decades',
        y='Count',
        markers=True,
        line_sape="spline"
    )
    fig_decades.update_layout(
        titel_text= 'Book by publication decade',
        xaxis_title='Decade',
        yaxls_title='Numbers of books',
        height=400
    )
    st.plotly_chart(fig_decades, use_container_width=True)

    #load library
load_library()
st.sidebar.markdown("<h1 style='text-align: center;'> Navgation</h1>" ,unsafe_allow_html=True)
lottie_book = load_lottieurl("https://assests9.lottieflies.com/temp/1f20_aKAfln.json")
if lottie_book:
    with st.sidebar:
        st lottie(lottie_book, height=200, key='book_animation')

#Navigation options
nav_options = st.sidebar.radio(
    "choose an option:",
    ["View Library", "Add book", "Search Books", "Library Statistics"]
)

# change current view based on navigation
if nav_options == "View Library":
    st.session_state.current_view = "library"
elif nav_options == "Add Book":
    st.session_state.current_view = "add"
elif nav_options == "Search Books":
    st.session_state.current_view = "search"
elif nav_options == "Libarry Statistics":
    st.session_state.current_view ="stats"

st.markdown("<h1 class='main-header'> Personal Library Manger </h1>", unsaf_allow_html=True)
if st.session_state.current_view =="add":
    st.markdown("<h2 class='sub-header'> Add a new book📖</h2>", unsaf_allow_html=True)

#adding books input form
with st.form(key='add_book_form'):
    col1, col2 = st.columns(2)

    with col1:
        titel = st.text_input("Book Title", max_chars=100)
        author = st.text_input("Author", max_chars=100)
        publication_year = st.number_input("publication year",min_value=1000, max_value=datetime.now()-year, step=1, value=2023)
        with col2:
            genre = st.selectbox(Genre,[
                "Friction","Non-Friction", "Science","Technology", asy"Fanst","Romance","Poetry","Self-help","Art","Religion","History", "Other"
        ])
        read_status =st.radio("Read Status",["Read","Unread"], horizontal=True)
        read_bool = read_status == "read"
    submit_button = st.form_submit_button(label="Add Book")

    if submit_button and titel and author:
        add_book(titel,author,publication_year,genre,read,bool)

    if  st.session_state.book_added:
        st.markdown("<divv class='success-message'> Book added successfully!</div>", unsafe_allow_html=True)
        st.balloon()
        st.session_state.book_added = False
elif st.session_state.current_view =="library":
    st.markdown("<h2> class ='sub_header'> your Libarry </h2>", unsaf_allow_html=True)
    
    if not st.session_state.library:
        st.markdown("<div class='warning-message'> your library is empty. Add some books to get started!</div>", unsaf_allow_html=True)
    else:
        cols = st.columns(2)
        for i , book in enumerate(st.session_state.library):
            with cols[i % 2]:
                st.markdown(f"""<div class = 'book-card'>
                    <h3>{book['title']}</h3>
                    <p><strong>Author:</strong> {book['author']}</p>
                    <p><strong>publication year:</strong> {book['publiction_year']}</p>
                    <p><strong>Genre:</strong> {book['genr']}</p>
                    <p><span class='{"read-badge" if book["read_status"] else "unread-badge"}'>{
                        "Read" if book["read_status"] else "Unread"
                    }</spand></p>
                    </div>

""", unsaf_allow_html=True)

                col1, col2 =st.columns(2)
                with col1:
                    if st.button(f" Remove", key=f"remove_(i)", use_container_width=True):
                        if remove_book(i)
                        st.rerun()
                with col2:
                    new_status = not book ['read_status']
                    stauts_label =  else "Mark as read" if not book['read_status'] else "mark as Unread"
                    if st.button(status_label , key=f"status_(i), use_container_width"=True):
                        st.session_state.library[i][read_status]= new_status
                        save_library()
                        st.return()
    if st.session_state.book_removed:
        st.markdow("<div class='success-message'> Book book removed successfully!</div>", unsafe_allow_html=True)
        st.session_state.book_removed = False
elif st.session_state.current_view == "search"
    st.markdow("<h2 clss='sub-header> search books</h2>", unsaf_allow_html=True)
    search_by = st. selectbox("Search by:",["Title","Author","Genre"])
    search_term = st.text_input("Enter search term:")

    if st.button("search" ,use_container_width=False:)
        if search_term:
            time. st.sleep(0.5)
            search_books(search_term, search_by)
    if hasattr(st.session_state, 'search_results'):
        if st.session_state.search_results:
            st.markdown(f"<h3> Found {len(st.session_state.search_results)} results:</h3>", unsaf_allow_html=True)

            for i, book in enumerate (st.session_state.search_results):
                st.markdown(f"""
                            <div class = 'book_card'>
                            <h3>{book['title']}</h3>
                    <p><strong>Author:</strong> {book['author']}</p>
                    <p><strong>publication year:</strong> {book['publiction_year']}</p>
                    <p><strong>Genre:</strong> {book['genr']}</p>
                    <p><span class='{"read-badge" if book["read_status"] else "unread-badge"}'>{
                        "Read" if book["read_status"] else "Unread"
                    }</spand></p>
                    </div>

""", unsaf_allow_html=True)
        elif search_term:
            st.markdown("<div class=' warning-message'> No books found matching your search.</div>", unsaf_allow_html=True)

elif st.session_state.current_view =="stats":
    st.markdown("<h2 class= 'sub_header'> Library statistics</h2>", unsaf_allow_html=True)

    if not st.session_state.Libarry:
        st.markdown("<div class='warning-message'> your library is empty. Add .some books to see stats!</div>", unsaf_allow_html=True)
    else:
        stats = get_library_stats()
        col1,col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Book", stats['total_books'])
        with col2:
             st.metric("Books Read", stats['read_books'])
        with col3:
              st.metric("Percentage Read", f"{stats['percentage_read'] :.1f}%")

        # Create visualizations
        create_visulations(stats)

        #Disply top authors
        if stats['authors']:
            st.markdown("<h3> Top Authors</h3>", unsaf_allow_html=True)
            top_authors = dict(list(stats['authors'].items())[:5])
            for authors, count in top_authors.items():
                st.markdown(f"**{author}**": {count} book{'s' if count > 1 else ''}"")

# Footer
st.markdown("---")
st.markdown("@ 2025 Saima Majid Personal Library Manager | Created with Love and Streamlit", unsaf_allow_html=True)
""") 



    
    

