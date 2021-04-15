import streamlit as st
from transformers import pipeline
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

st.write("# TLDR-izer")
article = st.text_area('Text to be summarized:', height=200)

if st.button("Do the magic"):
    summarizer = pipeline("summarization")
    output = summarizer(article, min_length=50, max_length=90)
    st.write(output[0]['summary_text'])
