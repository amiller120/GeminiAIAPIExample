import pathlib
import re
import textwrap
import google.generativeai as genai
import os
from IPython.display import display
from IPython.display import Markdown
from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
app = FastAPI()

class chatText(BaseModel):
   userInput: str

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    return FileResponse("index.html")

@app.post("/chat")
async def read_items(text: chatText):
    global chat
    try:
      response = chat.send_message(text.userInput);
    except:
      print("An Error occured processing the request")
      return "An Error occured";
    
    return to_markdown(response.text).data
    
    return response

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '', predicate=lambda _: True))