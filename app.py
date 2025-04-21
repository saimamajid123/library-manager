import streamlit as st
import pandas as pd
import os

# CSV file path
LIBRARY_FILE = "library.csv"

# Load or create CSV file
def load_data():
    if os.path.exists(LIBRARY_FILE):
        return pd.read_csv(LIBRARY_FILE)
    else:
        return pd.DataFrame(columns=["Title", "Author", "Year", "Status"])

def save_data(df):
    df.to_csv(LIBRARY_FILE, index=False)

# UI
st.set_page_config(page_title="Library Manager", layout="centered")
st.title("📚 Personal Library Manager")

# Load existing data
df = load_data()

# Add New Book
st.subheader("➕ Add a New Book")
with st.form(key="add_book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    status = st.selectbox("Status", ["To Read", "Reading", "Finished"])
    submit = st.form_submit_button("Add Book")

    if submit:
        if title and author and year:
            new_row = {"Title": title, "Author": author, "Year": year, "Status": status}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            save_data(df)
            st.success("Book added!")
        else:
            st.error("Please fill in all fields.")

# Search or filter
st.subheader("🔍 Search / Filter")
search = st.text_input("Search by title or author").lower()

if search:
    filtered_df = df[df["Title"].str.lower().str.contains(search) | df["Author"].str.lower().str.contains(search)]
else:
    filtered_df = df

# Show book list
st.subheader("📖 Your Books")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

