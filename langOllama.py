from langchain_ollama import ChatOllama
from constants import HUMAN_PROMPT, SYSTEM_PROMPT
from langchain_core.messages import HumanMessage, SystemMessage


def generate_questions(cv_content, jd_content):
    prompt = HUMAN_PROMPT.format(cv_content=cv_content, jd_content=jd_content)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]
    model = ChatOllama(model="deepseek-r1:1.5b", temperature=0)
    response = model.invoke(messages)
    return response.content
