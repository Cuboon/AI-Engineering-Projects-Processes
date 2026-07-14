import gradio as gr
from huggingface_hub import HfFolder

def combine_sentences(a, b):
    return a +" " + b

    # Define the interface
demo = gr.Interface(
    fn=combine_sentences, 
    inputs=[gr.Textbox(label="Input 1"),gr.Textbox(label ="Input 2")], # Create two numerical input fields where users can enter numbers
    outputs=gr.Textbox(label="Output") # Create numerical output fields
)

demo.launch(server_name="127.0.0.1", server_port= 7860)
