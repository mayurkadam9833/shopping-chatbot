from langchain_core.prompts import ChatPromptTemplate

system_prompt=(
    "you are question answered AI assitance "
    "you are friendly chatbot "
    "strictly answer in only in four sentences maximum "
    "\n\n"
    "{context}"
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","previous chat:{chat_history}\n\n human:{input}"),
    ]
)