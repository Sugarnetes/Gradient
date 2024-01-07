from dotenv import load_dotenv
from langchain_community.llms.huggingface_hub import HuggingFaceHub
import os
from pdfreader import PdfReader

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

summarizer = HuggingFaceHub(
    repo_id="facebook/bart-large-cnn",
    model_kwargs={"temperature":0, "max_length":2800}
)

class Summarizer():

    def __init__(self, text):
        self.text = text
    
    def summarize(self, llm):
        llm(f"Summarize this: {self.text}!")

summarize(summarizer, customer_email)
