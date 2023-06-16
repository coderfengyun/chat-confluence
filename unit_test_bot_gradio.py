import gradio as gr
import random
import time
from unit_test_generator import unit_tests_from_function
from threading import Thread

with gr.Blocks() as demo:
    msg = gr.TextArea(lines=20, placeholder="Enter your function under test here")
    chatbot = gr.Chatbot()
    submit_button = gr.Button("Submit")
    clear = gr.ClearButton([msg, chatbot])

    def user(user_message, history):
        return user_message, history + [[None, None]]

    def bot(msg, history):
        def print_to_console(text: str, end: str = "\n"):
            if end == "\n":
                # create a new entry in the history
                history[-1][1] = ""
            history[-1][1] += text
            print(text, end=end)
        unit_tests_from_function(msg, print_text=True, print_function=print_to_console, approx_min_cases_to_cover=10)
        return history

    def on_submit_click():
        chatbot.clear()
        bot_thread = Thread(target=bot, args=(msg.get(), chatbot))
        bot_thread.start()

    response = submit_button.click(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, [msg, chatbot], [chatbot]
    )

demo.queue()
demo.launch()
