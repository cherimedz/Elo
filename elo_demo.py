import streamlit as st
from googletrans import Translator

# Page configuration
st.set_page_config(page_title="Elo Demo", page_icon="🌍", layout="wide")

# Load custom CSS
with open("elo.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# App title and description
st.title("🌍 Welcome to Elo, the Machine Translation Demo App! 🌍")

st.markdown("""
**Elo** is a simple translation app that allows you to translate text into various languages.

**Key Features:**
- Translate text into a selection of languages.
- Simple and intuitive user interface.
- Powered by the Google Translate API.

**How to Use:**
1. Enter the text you want to translate in the input box below.
2. Select the target language from the dropdown menu.
3. Click on the "Translate" button to get the translated text.
""")

# Input for text to translate
st.markdown("<h2 style='font-size: 24px; font-weight: bold;'>Enter the Text for Translation</h2>", unsafe_allow_html=True)
input_text = st.text_area('', placeholder='Type your text here...', height=150)

# Language selection dropdown
languages = {
    'Malayalam': 'ml',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Bengali': 'bn',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Marathi': 'mr',
    'Odia': 'or',
    'Punjabi': 'pa',
    'Telugu': 'te',
    'Urdu': 'ur'
}

st.markdown("<h2 style='font-size: 24px; font-weight: bold;'>Select the Target Language</h2>", unsafe_allow_html=True)
option = st.selectbox('', list(languages.keys()))

# Initialize previous translations in session state
if 'previous_translations' not in st.session_state:
    st.session_state.previous_translations = []

# Translation button and logic
if st.button('Translate'):
    if input_text.strip():
        translator = Translator()
        try:
            translation = translator.translate(input_text, dest=languages[option])
            st.success(f"**Translation in {option}:**")
            st.write(translation.text)
            
            # Store the translation in session state
            translation_entry = f"Translation in {option}: {translation.text}"
            st.session_state.previous_translations.append(translation_entry)
            # Keep only the last 5 translations
            if len(st.session_state.previous_translations) > 5:
                st.session_state.previous_translations = st.session_state.previous_translations[-5:]

        except Exception as e:
            st.error("Error during translation. Please try again later.")
    else:
        st.warning("Please enter some text to translate.")

# Sidebar with additional features
with st.sidebar:
    st.header("🚀 Quick Actions")
    st.markdown("""
    - [Explore My Apps](https://share.streamlit.io/user/cherimedz)
    - [My GitHub Profile](https://github.com/cherimedz)
    - [My LinkedIn Profile](https://www.linkedin.com/in/medha-reju-pillai-42551b277/)
    """)

    # Display previous translations history
    st.subheader("📜 Previous Translations History")
    if st.session_state.previous_translations:
        for translation in st.session_state.previous_translations:
            st.markdown(f"- {translation}")
    else:
        st.write("No previous translations.")

    # About me section
    st.subheader("👩‍💻 About Me")
    st.write("""
    Hi there! I’m Medha Reju Pillai, currently pursuing an MSc in Computer Science and Data Analytics. I’m deeply passionate about technology and AI, and I’m excited about exploring cutting-edge innovations and making meaningful contributions in these dynamic fields. Let’s connect and drive technological advancements together!

    Feel free to connect with me:
    - [GitHub Profile](https://github.com/cherimedz) 🤍
    - [LinkedIn Profile](https://linkedin.com/in/medha-reju-pillai-42551b277) 🌐
    """)

    st.subheader("💻 Check Out My Other Apps")
    st.write("Explore more of my projects and apps here:")
    st.write("🔗 [Streamlit Apps](https://share.streamlit.io/user/cherimedz)")

    st.subheader("📬 Contact Me")
    st.write("""
    For inquiries or further discussions, connect with me via my [GitHub](https://github.com/cherimedz) or [LinkedIn](https://linkedin.com/in/medha-reju-pillai-42551b277) profiles. I’d love to hear from you!
    """)

    st.subheader("💬 Feedback")
    feedback = st.text_area("I value your feedback! Share your thoughts here:")
    if st.button("Submit Feedback"):
        if feedback:
            st.write("Thank you for your feedback! 😊 Your input helps me improve.")
            with open("feedback.txt", "a") as f:
                f.write(feedback + "\n")
        else:
            st.write("Please enter your feedback before submitting.")

# Footer section
st.markdown("---")
st.markdown("**About Elo:** This app was developed as part of an assignment to demonstrate basic machine translation techniques using Streamlit. Elo, short for Eloquence, currently offers simple translations in a limited set of languages. In the future, I plan to expand its capabilities to support a broader range of languages and more advanced translation features.")
