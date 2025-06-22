from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from difflib import get_close_matches
import random

app = FastAPI()

knowledge_data = {
    "What is blockchain?": "Blockchain is a decentralized digital ledger...",
    "What is cryptocurrency?": "Cryptocurrency is digital money...",
    "What is Ethereum?": "Ethereum is a blockchain supporting smart contracts...",
    "What is NFT?": "NFTs are unique digital assets stored on blockchain...",
    "What is a DAO?": "A DAO is a decentralized autonomous organization...",
    "What is a crypto wallet?": "A crypto wallet stores private keys for cryptocurrency access..."
}

@app.post("/")
async def ask(req: Request):
    data = await req.json()
    question = data.get("question", "").strip().lower()
    matches = get_close_matches(question, list(knowledge_data.keys()), n=1, cutoff=0.5)
    answer = knowledge_data[matches[0]] if matches else "Sorry, I don't know that."

    suggestions = [k for k in knowledge_data if any(w in k.lower() for w in question.split())]
    suggestions = random.sample(suggestions, min(3, len(suggestions))) if suggestions else random.sample(list(knowledge_data.keys()), 3)

    return JSONResponse({"answer": answer, "suggestions": suggestions})
