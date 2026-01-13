import streamlit as st

# Page config
st.set_page_config(page_title="Chatbot AI", page_icon="🤖")

st.title("🤖 Simple Chatbot AI")
st.write("Ask me anything!")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def chatbot_reply(user_text):
    user_text = user_text.lower()

    if "hello" in user_text:
        return "Hello 👋 How can I help you?"
    elif "your name" in user_text:
        return "I am a Streamlit Chatbot 🤖"
    elif "bye" in user_text:
        return "Goodbye! Have a great day 😊"
    else:
        return "Sorry, I am still learning. Try asking something else."

# If user sends message
if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Bot response
    bot_response = chatbot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    st.rerun()
