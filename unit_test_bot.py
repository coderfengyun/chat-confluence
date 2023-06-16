import streamlit as st
from streamlit_chat import message
from unit_test_generator import unit_tests_from_function

PAGE_TITLE: str = "Java Unit Test Generator"
PAGE_ICON: str = "🤖"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
st.title("Java Unit Test Generator")

if "console_text" not in st.session_state:
    st.session_state["console_text"] = ""

def reset_col3(col3_place_holder):
    col3_place_holder.markdown(f'''
<div style="height:500px; overflow-y:scroll; border: 1px solid #e0e0e0; padding: 10px; border-radius: 5px;">
</div>
''', unsafe_allow_html=True) 
    
def reset_row2(row2_place_holder):
    row2_place_holder.markdown(f'''''')
                               
col1, col2, col3 = st.columns([4,1,4])

with col1:
    st.markdown("Enter your java function here:")
    function_to_test = col1.text_area("enter your java function", height=500, label_visibility="collapsed")

with col2:
    submit_clicked = col2.button("Generate Test Cases", key="generationSubmit")

with col3:
    st.markdown("Generated test cases:")
    col3_place_holder = col3.empty()
    reset_col3(col3_place_holder=col3_place_holder)

row2_place_holder = st.empty()

def print_to_console(text: str, end: str = "\n"):
    st.session_state["console_text"] += text + ("  " if end == "\n" else end)
    print(text, end=end)

    console_text = st.session_state["console_text"]
    markdown_container_1 = f'''
<div id="scrollContainer"; style="background-color: #f0e68c; padding: 10px; border-radius: 5px; height:300px; overflow-y:scroll;">
    {console_text}
</div>
'''
    row2_place_holder.markdown(markdown_container_1, unsafe_allow_html=True)

if submit_clicked:
    with col2:
        with st.spinner("Generating..."):
            reset_col3(col3_place_holder=col3_place_holder)
            reset_row2(row2_place_holder=row2_place_holder)
            generated = unit_tests_from_function(function_to_test, print_text=True, print_function=print_to_console, approx_min_cases_to_cover=10)
            markdown_container = f'''
<div style="height:500px; overflow-y:scroll; border: 1px solid #e0e0e0; padding: 10px; border-radius: 5px;">
    {generated}
</div>
'''
            col3_place_holder.markdown(markdown_container, unsafe_allow_html=True)
