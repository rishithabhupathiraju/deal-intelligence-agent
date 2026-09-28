# Deal Intelligence Agent

AI-powered sales intelligence with persistent memory using Hindsight.

## Problem

Sales representatives spend a lot of time reviewing previous customer conversations before a deal meeting. Important details such as customer concerns, competitors, requirements, and risks can easily be missed.

## Solution

Deal Intelligence Agent uses Hindsight as a persistent memory layer for sales interactions.

The agent remembers important deal information and retrieves it when the sales representative prepares for a future customer call.

Instead of searching through old conversations, the salesperson can simply ask for the deal intelligence.

## How It Works

1. Sales interaction is recorded.
2. Hindsight retains the important information.
3. More interactions can be added over time.
4. When preparing for a call, the agent recalls relevant deal history.
5. The system generates a concise deal briefing and recommended next action.

## Example

### Customer
Acme Technologies

### Remembered Information

- Pricing is considered too high.
- Competitor X is being considered.
- Salesforce integration is required.
- Faster implementation is requested.

### Deal Briefing

The agent brings these details together and recommends addressing the pricing concern and confirming Salesforce integration requirements before the next call.

## Hindsight Integration

Hindsight is the core memory layer of this project.

The application uses Hindsight to:

- Retain deal interactions
- Recall relevant deal history
- Retrieve information for meeting preparation
- Maintain persistent memory across interactions

This makes memory a central part of the application rather than a simple chatbot feature.

## Features

- Persistent deal memory
- Deal interaction recording
- Deal intelligence retrieval
- AI-generated deal briefing
- Customer concern tracking
- Competitor tracking
- Requirement tracking
- Risk identification
- Recommended next action

## Tech Stack

- Python
- FastAPI
- Hindsight
- Hindsight Python Client
- HTML
- CSS
- JavaScript

## Project Structure

```text
deal-intelligence-agent/
├── backend/
│   └── app/
│       └── main.py
├── frontend/
│   └── index.html
└── .gitignore


## API Endpoints

### Remember Deal Interaction

POST /deals/remember

Stores a customer interaction in Hindsight memory.

### Get Deal Intelligence

GET /deals/{company}/intelligence

Retrieves relevant remembered information for a company.

### Get Deal Briefing

GET /deals/{company}/briefing

Generates a structured briefing containing customer concerns, competitors, requirements, risks, and recommended next action.

## Running Locally

### Start Hindsight

Run the local Hindsight server on:

http://localhost:8888

### Start the FastAPI backend

```bash
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload

```

The API will be available at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

## Why Hindsight Matters

The key capability of this project is persistent memory.

A sales interaction recorded today can be recalled later when preparing for another interaction with the same customer. This allows the agent to build useful context over time instead of treating every conversation as a completely new interaction.

## Project Status

Hack With Hyderabad 3.0 project.

Built by Team The Frontiers.
