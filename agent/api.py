from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from insight_agent import InsightAgent
import uvicorn

app = FastAPI(title="Data Reconciliation Insight Agent")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the agent
agent = InsightAgent()
agent.load_mock_data()

@app.get("/")
async def root():
    return {"message": "Data Reconciliation Insight Agent API"}

@app.get("/insights")
async def get_insights():
    """Get all insights from the agent"""
    try:
        return agent.get_insights()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/trends")
async def get_trends():
    """Get trend analysis"""
    try:
        return agent.analyze_trends()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/anomalies")
async def get_anomalies():
    """Get detected anomalies"""
    try:
        return agent.detect_anomalies()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/category-analysis")
async def get_category_analysis():
    """Get category-wise analysis"""
    try:
        return agent.category_analysis()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 