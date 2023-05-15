# pip install git+https://github.com/huggingface/transformers@v4.29.0
OPEN_AI_KEY = "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"
from transformers import OpenAiAgent
import textract

PDF_FILE = "documents/evotec__evotec__annual__report_2021_ae1ebc54-6a37-4639-a22d-e1eb91477436.pdf"

text = textract.process(PDF_FILE).decode('utf-8')

agent = OpenAiAgent(model="text-davinci-003", api_key=OPEN_AI_KEY)

agent.run("What is the purpose of sustinability reporting?")
agent.run("Can you summarize 'text' for me?", text=text)
agent.run ("Based on 'text', what country borders Pakistan on thw West?", text=text)