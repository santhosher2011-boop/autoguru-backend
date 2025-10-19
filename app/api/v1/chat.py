from fastapi import APIRouter
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
router = APIRouter()
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
class ChatRequest(BaseModel):
    question: str
@router.post("/")
async def chat_endpoint(body: ChatRequest):
    msgs = [SystemMessage(content="You are AutoGuru, a friendly Indian car expert..."),
            HumanMessage(content=body.question)]
    reply = await chat.ainvoke(msgs)
    return {"reply": reply.content}
