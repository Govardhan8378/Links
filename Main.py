import streamlit as st

st.set_page_config(page_title="My Link List", layout="centered")

# Proper background styling using Streamlit classes
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #000000;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Remove padding around the content */
        .main > div {
            padding: 2rem 1rem;
        }

        .title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #ffffff;
            margin-top: 20px;
        }

        .subtitle {
            text-align: center;
            font-size: 1.3em;
            margin-bottom: 30px;
        }

        .link-button {
            display: block;
            width: 60%;
            margin: 10px auto;
            padding: 15px;
            background-color: #1f1f1f;
            color: #ffffff;
            border: 1px solid #444;
            border-radius: 10px;
            text-align: center;
            font-size: 1.1em;
            text-decoration: none !important;
            transition: all 0.3s ease;
        }

        .link-button:hover {
            background-color: #333333;
            transform: scale(1.03);
        }

        .contact {
            margin-top: 40px;
            text-align: center;
        }

        .contact a {
            color: #ffffff;
            font-weight: bold;
            text-decoration: none !important;
        }

        .contact a:hover {
            text-decoration: underline !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<div class='title'>🔗 My Link List</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your favorite places in one place ✨</div>", unsafe_allow_html=True)
# Updated links including Facebook and Instagram
link_data = {
    "🌐 GitHub": "https://github.com/Govardhan8378/",
    "💼 LinkedIn": "https://www.linkedin.com/in/kethireddygovardhan/",
    "🖥️ Portfolio": "https://govardhan8378.github.io/",
    "✍️ Blog": "govardhanreddy8378.blogspot.com",
    "🎥 YouTube": "https://www.youtube.com/@govardhanreddy1839",
    "📘 Facebook": "https://www.facebook.com/kethireddy.govardhan.5",
    "📸 Instagram": "https://www.instagram.com/govardhanreddy8378/"
}

# Display links
for name, url in link_data.items():
    st.markdown(f"<a class='link-button' href='{url}' target='_blank'>{name}</a>", unsafe_allow_html=True)

# Contact section
st.markdown("""
    <div class='contact'>
        <h4>📬 Contact Me</h4>
        <p>Want to collaborate? <a href='mailto: govardhanreddy4988@gmail.com'>Send an Email</a></p>
    </div>
""", unsafe_allow_html=True)
