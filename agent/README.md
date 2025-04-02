# Data Reconciliation Insight Agent

This agent analyzes reconciliation results and provides valuable insights through statistical analysis, anomaly detection, and visualization.

## Features

- Trend Analysis
- Anomaly Detection
- Category-wise Analysis
- Automated Visualization Generation
- RESTful API Interface

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the API Server

```bash
python api.py
```

The server will start on `http://localhost:8000`

### API Endpoints

- `GET /`: Welcome message
- `GET /insights`: Get all insights
- `GET /trends`: Get trend analysis
- `GET /anomalies`: Get detected anomalies
- `GET /category-analysis`: Get category-wise analysis

### Running the Agent Directly

```bash
python insight_agent.py
```

This will run the agent with mock data and print a summary of insights.

## Integration with Main Application

1. Import the agent in your main application:
```python
from agent.insight_agent import InsightAgent
```

2. Initialize and use the agent:
```python
agent = InsightAgent()
# Load your actual data here
agent.data = your_dataframe
insights = agent.get_insights()
```

3. Use the API endpoints in your frontend:
```javascript
// Example fetch call
fetch('http://localhost:8000/insights')
  .then(response => response.json())
  .then(data => {
    // Handle insights data
  });
```

## Data Format

The agent expects data in the following format:
```python
{
    'timestamp': datetime,
    'source_value': float,
    'target_value': float,
    'discrepancy': float,
    'status': str,
    'category': str
}
```

## Visualization Output

The agent generates two types of visualizations:
1. Discrepancy Trends Over Time
2. Category Distribution

These are saved in the `plots` directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 