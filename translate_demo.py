import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="Machine Translation Demo", page_icon="🌍", layout="wide")

with open("translate_css.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

st.title('🌍 Welcome to Eloquence, the Machine Translation Demo App! 🌍')
st.write("Translate your text to the language of your choice!")

input_text = st.text_area('Enter the text you want to translate:', placeholder='Type your text here...', height=150)

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

option = st.selectbox('Select the target language:', list(languages.keys()))

if st.button('Translate'):
    if input_text.strip():
        translator = Translator()
        try:
            translation = translator.translate(input_text, dest=languages[option])
            st.success(f"**Translation in {option}:**")
            st.write(translation.text)
        except Exception as e:
            st.error("Error during translation. Please try again later.")
    else:
        st.warning("Please enter some text to translate.")

st.write("Powered by Google Translate API and Streamlit")

with st.sidebar:
    st.header("Quick Actions")
    st.markdown("""
    - [Explore Streamlit Apps](https://share.streamlit.io/user/cherimedz)
    - [GitHub Profile](https://github.com/cherimedz)
    - [LinkedIn Profile](https://www.linkedin.com/in/medha-reju-pillai-42551b277/)
    """)

st.sidebar.subheader("👩‍💻 About Me")
st.sidebar.write("""
Hi there! I’m Medha Reju Pillai, currently pursuing an MSc in Computer Science and Data Analytics. I’m deeply passionate about technology and AI, and I’m excited about exploring cutting-edge innovations and making meaningful contributions in these dynamic fields. Let’s connect and drive technological advancements together!

Feel free to connect with me:
- [GitHub Profile](https://github.com/cherimedz) 🤍
- [LinkedIn Profile](https://linkedin.com/in/medha-reju-pillai-42551b277) 🌐
""")

st.sidebar.subheader("💻 Check Out My Other Apps")
st.sidebar.write("Explore more of my projects and apps here:")
st.sidebar.write("🔗 [Streamlit Apps](https://share.streamlit.io/user/cherimedz)")

st.sidebar.subheader("📬 Contact Me")
st.sidebar.write("""
For inquiries or further discussions, connect with me via my [GitHub](https://github.com/cherimedz) or [LinkedIn](https://linkedin.com/in/medha-reju-pillai-42551b277) profiles. I’d love to hear from you!
""")

st.sidebar.subheader("💬 Feedback")
feedback = st.sidebar.text_area("I value your feedback! Share your thoughts here:")
if st.sidebar.button("Submit Feedback"):
    if feedback:
        st.sidebar.write("Thank you for your feedback! 😊 Your input helps me improve.")
        with open("feedback.txt", "a") as f:
            f.write(feedback + "\n")
    else:
        st.sidebar.write("Please enter your feedback before submitting.")