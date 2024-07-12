import os
from langchain import HuggingFaceHub
os.environ['HUGGINGFACEHUB_API_TOKEN']='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'
import streamlit as st
def summarize_text(text):
    open_hug = HuggingFaceHub(repo_id='Falconsai/text_summarization', model_kwargs={"temperature": 0.9, "max_length": 64})
    summary = open_hug(text)
    return summary
def main():
    st.title("Text Summarization App")
    
    # Text input box for user to enter text
    input_text = st.text_area("Enter your text:")
    
    # Check if the user has entered any text
    if st.button("Summarize"):
        if input_text:
            # Call the summarization function
            summary = summarize_text(input_text)
            st.write("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")
            
if __name__ == "__main__":
    main()
