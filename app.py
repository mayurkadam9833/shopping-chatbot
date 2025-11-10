from langchain.vectorstores import Chroma 
from src.prompt import * 
from src.helper import download_embeddings
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage,AIMessage
from flask import request,Flask,render_template 

app=Flask(__name__)


embeddings=download_embeddings() 

dir="vector_database" 

vector_data=Chroma(
    persist_directory=dir,
    embedding_function=embeddings
)

retrival=vector_data.as_retriever(search_type="similarity",search_kwagrs={"k":3}) 

llm=Ollama(model="gemma3")
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
question_answer_chain=create_stuff_documents_chain(llm=llm,prompt=prompt)
rag_chain=create_retrieval_chain(retrival,question_answer_chain) 

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/get",methods=["GET","POST"])
def chat(): 
    msg=request.form["msg"]
    print("User Input:",msg)

    cha_hist_str="\n".join([
        f"user:{m.content}" if isinstance(m,HumanMessage) else f"bot:{m.content}"

        for m in memory.chat_memory.messages
    ])

    response=rag_chain.invoke({"input":msg,"chat_history":cha_hist_str})
    answer=response["answer"]

    print("Response:",answer)

    memory.chat_memory.add_message(HumanMessage(content=msg))
    memory.chat_memory.add_ai_message(AIMessage(content=answer))
    return str(answer)

if __name__ =="__main__": 
    app.run(host="0.0.0.0",port=8080,debug=True)