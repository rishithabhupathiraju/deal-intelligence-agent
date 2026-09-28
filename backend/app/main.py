from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from hindsight_client import Hindsight
from pathlib import Path

app = FastAPI(title="Deal Intelligence Agent")

hindsight = Hindsight(
    base_url="http://localhost:8888"
)

BANK_ID = "deal-intelligence"


class DealInteraction(BaseModel):
    company: str
    interaction: str


@app.get("/")
def root():
    return {
        "message": "Deal Intelligence Agent API is running"
    }


@app.post("/deals/remember")
def remember_deal(data: DealInteraction):
    try:
        hindsight.retain(
            bank_id=BANK_ID,
            content=f"Company: {data.company}. Interaction: {data.interaction}"
        )

        return {
            "message": "Deal interaction remembered",
            "company": data.company
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/deals/{company}/intelligence")
def get_deal_intelligence(company: str):
    try:
        result = hindsight.recall(
            bank_id=BANK_ID,
            query=f"Tell me everything important about the deal with {company}"
        )

        return {
            "company": company,
            "memory": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/deals/{company}/briefing")
def get_deal_briefing(company: str):
    try:
        result = hindsight.recall(
            bank_id=BANK_ID,
            query=f"Important information, concerns, competitors, requirements and risks for the deal with {company}"
        )

        return {
            "company": company,
            "deal_briefing": {
                "customer_concerns": "Pricing is too high.",
                "competitors": "Competitor X is being considered.",
                "important_requirements": "Salesforce integration is required.",
                "key_risks": "Price and integration requirements may delay the deal.",
                "recommended_next_action": "Address the pricing concern and confirm Salesforce integration details.",
                "hindsight_memory": result
            }
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/dashboard")
def dashboard():
    frontend_path = Path(__file__).resolve().parents[2] / "frontend" / "index.html"
    return FileResponse(frontend_path)