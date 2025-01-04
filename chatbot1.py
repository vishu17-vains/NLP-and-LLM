import streamlit as st
from nltk.chat.util import Chat, reflections

# Define the chatbot logic
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today ?"]],
    [r"(.*)help(.*)", ["I can help you "]],
    [r"(.*) your name ?", ["My name is assistly, but you can just call me robot and I'm a chatbot."]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind that"]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great!"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there"]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse"]],
    [r"(.*)created(.*)", ["vishwajeet created me using Python's NLTK library", "Top secret ;)"]],
    [r"(.*) (location|city) ?", ["vadodara, India"]],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain"]],
    [r"how (.*) health (.*)", ["Health is very important, but I am a computer, so I don't need to worry about my health"]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket"]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli"]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ["Our customer service will reach you"]]
]

# Initialize chatbot
chat = Chat(pairs, reflections)

# Streamlit App
st.set_page_config(page_title="Chatbot - Assistly", layout="wide")

# Custom CSS for background and chatbot avatar
st.markdown("""
    <style>
        body {
            background-image: url('https://source.unsplash.com/random/1920x1080/?technology,ai');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .chat-container {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }
        .bot-avatar {
            display: inline-block;
            width: 50px;
            height: 50px;
            margin-right: 10px;
            background-image: url('https://i.imgur.com/qkdpN.jpg');
            background-size: cover;
            border-radius: 50%;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Chatbot - Assistly")
st.write("Hi, I'm your assistant! Type below to start a conversation. Type 'quit' to leave.")

# Input and chat handling
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Input field handler
def handle_input():
    user_input = st.session_state.input
    if user_input:
        bot_response = chat.respond(user_input)
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", bot_response))
        # Clear the input field
        st.session_state.input = ""

# Input field with callback
st.text_input("You:", key="input", placeholder="Type your message here...", on_change=handle_input)

# Display chat history
for sender, message in st.session_state["messages"]:
    if sender == "You":
        st.markdown(f"**{sender}:** {message}")
    else:
        st.markdown(f"""
        <div class="chat-container">
            <div class="bot-avatar"></div>
            <strong>{sender}:</strong> {message}
        </div>
        """, unsafe_allow_html=True)


           
