from opengpt.models.completion.evagpt4.model import Model as EvaGPT4_Model
from opengpt.models.image.hotpot.model import Model as Hotpot_Model
from opengpt.models.completion.chatbase.model import Model as ChatBase_Model
from opengpt.models.completion.chatllama.model import Model as ChatLlama_Model

from flask import Flask,request
import pandas as pd
app = Flask(__name__)

@app.route('/EvaGPT4',methods=['POST'])
def EvaGPT4():
    evagpt4 = EvaGPT4_Model()
    messages = request.json["messages"]
    df=pd.DataFrame(messages)
    df=df[["role","content"]]
    df=df.to_dict(orient="records")
    # messages = [
    #         {"role": "system", "content": "You are Ava, an AI Agent."},
    #         {"role": "assistant", "content": "Hello! How can I help you today?"},
    #         {"role": "user", "content": """GPT4"""}
    #     ]  # List of messages in the chat history

    result = evagpt4.ChatCompletion(df)
    return result

@app.route('/Hotpot',methods=['POST'])
def Hotpot():
    request_data = request.get_json()
    style="Hotpot Art 9"
    width=1250
    height=1000
    prompt=None

    if request_data:
        if "style" in request_data:
            style = request_data["style"]

        if "width" in request_data:
            width = request_data["width"]

        if "height" in request_data:
            height = request_data["height"]

        if "prompt" in request_data:
            prompt = request_data["prompt"]

    Hotpot = Hotpot_Model(style=style)

    result = Hotpot.Generate(prompt=prompt,width=width,height=height)

    return {"url":result.url}

@app.route('/ChatBase',methods=['POST'])
def ChatBase():
    messages = request.json["messages"]
    df=pd.DataFrame(messages)
    df=df.loc[len(df)-1,"content"]
    chatbase = ChatBase_Model()
    result =chatbase.GetAnswer(prompt=df, model="gpt-4")

    return result


@app.route('/ChatLlama',methods=['POST'])
def ChatLlama():
    messages = request.json["messages"]
    df=pd.DataFrame(messages)
    df=df.loc[len(df)-1,"content"]
    ChatLlama = ChatLlama_Model()
    result =ChatLlama.GetAnswer(prompt=df)
    return result


app.run(debug=True)