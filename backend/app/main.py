from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from hindsight_client import Hindsight
from pathlib import Path


app = FastAPI(title="Deal Intelligence Agent")


# Hindsight connection
hindsight = Hindsight(
    base_url="http://localhost:8888"
)


BANK_ID = "deal-intelligence"


# Request model
class DealInteraction(BaseModel):
    company: str
    interaction: str


# Home
@app.get("/")
def root():
    return {
        "message": "Deal Intelligence Agent API is running"
    }


# Remember a deal interaction
@app.post("/deals/remember")
async def remember_deal(data: DealInteraction):
    try:
        await hindsight.aretain(
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


# Get deal intelligence
@app.get("/deals/{company}/intelligence")
async def get_deal_intelligence(company: str):
    try:
        result = await hindsight.arecall(
            bank_id=BANK_ID,
            query=f"""
            Tell me the important historical information about the sales
            deal with {company}, including customer concerns, competitors,
            requirements, risks, timelines and previous interactions.
            """
        )

        return {
            "company": company,
            "memory": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# Prepare deal briefing
@app.get("/deals/{company}/briefing")
async def get_deal_briefing(company: str):
    try:

        memory = await hindsight.arecall(
            bank_id=BANK_ID,
            query=f"""
            Retrieve the important remembered information about the sales
            deal with {company}, including customer concerns, competitors,
            requirements, timelines and risks.
            """
        )

        memory_text = str(memory).lower()


        # Customer concerns
        if "pricing" in memory_text or "price" in memory_text:
            customer_concerns = (
                "Pricing is a concern for the customer."
            )
        else:
            customer_concerns = (
                "No major pricing concern found in memory."
            )


        # Competitors
        if "competitor" in memory_text:
            competitors = (
                "The customer is considering a competitor."
            )
        else:
            competitors = (
                "No competitor information found in memory."
            )


        # Requirements
        requirements = []

        if "salesforce" in memory_text:
            requirements.append("Salesforce integration")

        if "3 months" in memory_text or "three months" in memory_text:
            requirements.append("3-month implementation timeline")

        if "onboarding" in memory_text:
            requirements.append("Clear onboarding plan")


        if requirements:
            important_requirements = (
                "Customer requirements: "
                + ", ".join(requirements)
                + "."
            )
        else:
            important_requirements = (
                "No specific requirements found in memory."
            )


        # Risks
        risks = []

        if "pricing" in memory_text or "price" in memory_text:
            risks.append("pricing")

        if "competitor" in memory_text:
            risks.append("competition")

        if "3 months" in memory_text or "three months" in memory_text:
            risks.append("implementation timeline")


        if risks:
            key_risks = (
                "Potential risks include "
                + ", ".join(risks)
                + "."
            )
        else:
            key_risks = (
                "No major risks identified from current memory."
            )


        # Recommended next action
        if "pricing" in memory_text and "salesforce" in memory_text:
            recommended_next_action = (
                "Address the pricing concern and confirm the "
                "Salesforce integration and implementation plan."
            )

        elif "pricing" in memory_text:
            recommended_next_action = (
                "Address the customer's pricing concern before "
                "the next call."
            )

        elif "salesforce" in memory_text:
            recommended_next_action = (
                "Confirm Salesforce integration details and "
                "implementation timeline."
            )

        else:
            recommended_next_action = (
                "Review the remembered deal history and confirm "
                "the next customer requirement."
            )


        return {
            "company": company,

            "deal_briefing": {
                "customer_concerns": customer_concerns,
                "competitors": competitors,
                "important_requirements": important_requirements,
                "key_risks": key_risks,
                "recommended_next_action": recommended_next_action,
                "deal_summary": (
                    f"Deal intelligence for {company} is based "
                    "on information remembered by Hindsight."
                )
            },

            "hindsight_memory": memory
        }


    except Exception as e:
        return {
            "error": str(e)
        }


# Dashboard
@app.get("/dashboard")
def dashboard():

    frontend_path = (
        Path(__file__).resolve().parents[2]
        / "frontend"
        / "index.html"
    )

    return FileResponse(frontend_path)