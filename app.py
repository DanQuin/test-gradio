import gradio as gr

description = "Story generation with GPT-2"
title = "Generate your own story"
examples = [["Adventurer is approached by a mysterious stranger in the tavern for a new quest."]]

interface = gr.Interface.load("huggingface/pranavpsv/gpt2-genre-story-generator",
            description=description,
            examples=examples
)

interface.launch()