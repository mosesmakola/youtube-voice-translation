import streamlit as st
from pytube import YouTube
import time

def responseStream(response):
    for word in str(response).split():
        yield word + " "
        time.sleep(0.06)

def handleYoutubeLink(url):
    try:
        yt = YouTube(url)
    except:
        print("failed")

    return yt

def chatResponse(prompt):
    return (f"Man said {prompt}")

st.title("Youtube Translation")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])

if userPrompt := st.chat_input(placeholder="Enter Youtube Link"):
    # Add user message to task history
    st.session_state.messages.append({"role": "user", "content": userPrompt})

    with st.chat_message("user"):
        st.markdown(userPrompt)

    with st.chat_message("assistant"):
        # Collect the response from the generator
        yt = handleYoutubeLink(userPrompt)
        

        response = st.write_stream(responseStream(yt.captions)) 
        
        # Append the response to the session state
        st.session_state.messages.append({"role": "assistant", "content": response})


# if userPrompt := st.chat_input(placeholder="Enter Youtube Link"):
#     with messages.chat_message("User"):
#         prompt = st.write(userPrompt)

#     # response = handleYoutubeLink(userPrompt)
    
#     messages.chat_message("assistant").write(userPrompt)

