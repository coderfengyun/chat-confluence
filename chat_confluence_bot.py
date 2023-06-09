import streamlit as st
from streamlit_chat import message

from assistant import (
    initiate_agent,
)

### CHATBOT APP

# --- GENERAL SETTINGS ---
PAGE_TITLE: str = "Confluence Retrieval Bot"
PAGE_ICON: str = "🤖"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Confluence Chatbot")
st.subheader("Learn things - random things!")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "What kind of search?", ("Standard vector search", "HyDE")
)

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

def query(question):
    response = st.session_state["chat"].ask_assistant(question)
    return response


prompt = st.text_input("What do you want to know: ", "", key="input")

if st.button("Submit", key="generationSubmit"):
    with st.spinner("Thinking..."):
        # Initialization
        if "agent" not in st.session_state:
            st.session_state["agent"] = initiate_agent()

        print("enter call chain, chat_history:")
        agent = st.session_state["agent"]
        response = agent({"question": prompt})

        print(response)
        st.session_state.past.append(prompt)
        st.session_state.generated.append(response["answer"])
        st.session_state.latest_source_documents = agent.last_source_documents

if len(st.session_state["generated"]) > 0:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")

    with st.expander("See search results"):
        if ("latest_source_documents" in st.session_state):
            results = list(st.session_state.latest_source_documents)
            st.write(results)
