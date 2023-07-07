from opengpt.models.completion.evagpt4.model import Model
from flask import Flask,request

app = Flask(__name__)

@app.route('/EvaGPT4',methods=['POST'])
def EvaGPT4():
    evagpt4 = Model()
    messages = request.json["messages"]


    # messages = [
    #         {"role": "system", "content": "You are Ava, an AI Agent."},
    #         {"role": "assistant", "content": "Hello! How can I help you today?"},
    #         {"role": "user", "content": """GPT4"""}
    #     ]  # List of messages in the chat history

    result = evagpt4.ChatCompletion(messages)
    return result

# app.run(debug=True)
