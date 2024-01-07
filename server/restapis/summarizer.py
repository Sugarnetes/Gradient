from dotenv import load_dotenv
from langchain_community.llms.huggingface_hub import HuggingFaceHub
import os
from pdfreader import PdfReader

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

summarizer = HuggingFaceHub(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    model_kwargs={"temperature":1, "max_length":2800}
)

class Summarizer():
    
    def summarize(self, llm, topic, points):
        return llm(f"For the {topic}, summarize the following bullet points {points} in point format. Do not leave any text out. Make sure the summary is concise. Make sure that the summary is shorter than the original points (do not leave any content out but make sure you reduce any redunancy wherever possible). You can keep on giving larger points than the original - you should be summarizing and giving smaller points.")

if __name__ == "__main__":
    pdfTest = PdfReader(r"C:\umer files\Programming PREJE'S\Medicall\server\restapis\denis.pdf")
    text_to_return, list_of_topics = pdfTest.extractor()
    print(text_to_return)
    list_of_outputs = []
    massive_text = ""

    for text in text_to_return:
        SummarizedTopic = Summarizer()

        summed = SummarizedTopic.summarize(summarizer, text[0], text[1])
        print(text[0] + summed)
    
    print(massive_text)
        


