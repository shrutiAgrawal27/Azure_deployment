import streamlit as st

# --- Set page configuration ---
st.set_page_config(page_title="Login App", page_icon="🔐", layout="centered")

# --- Dummy user credentials ---
USER_CREDENTIALS = {
    "shruti": "password123",
    "admin": "admin123"
}

# --- Session state to manage login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- Login function ---


def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")

# --- Logout function ---


def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""


# --- App Layout ---
st.title("🔐 Streamlit Login Example")

if not st.session_state.logged_in:
    st.subheader("Please log in")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)
else:
    st.success(f"Welcome, {st.session_state.username}! 👋")
    if st.button("Logout"):
        logout()
