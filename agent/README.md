# Data Reconciliation Insight Agent

This agent provides data analysis and insights for the data reconciliation system.

## Features

- Trend Analysis
- Anomaly Detection
- Category Analysis
- Visualization Generation
- Web Dashboard Integration

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

### Running the Web Dashboard

1. Start the Flask application:
```bash
python web_integration.py
```

2. Open your browser and navigate to `http://localhost:5000`

### Using the Integration API

```python
from integration import ReconciliationIntegration

# Initialize the integration
integration = ReconciliationIntegration()

# Load data
integration.load_data('path/to/your/data.csv')

# Get dashboard data
dashboard_data = integration.get_dashboard_data()

# Get insights
insights = integration.get_insights()

# Get visualization paths
trend_plot = integration.get_visualization_path('trend_plot.png')
anomaly_plot = integration.get_visualization_path('anomaly_plot.png')
category_plot = integration.get_visualization_path('category_plot.png')
```

## API Endpoints

- `GET /`: Dashboard home page
- `GET /api/insights`: Get all insights
- `GET /api/dashboard-data`: Get formatted dashboard data
- `GET /api/visualizations/<filename>`: Get visualization images
- `POST /api/upload`: Upload new data file

## Data Format

The system expects CSV files with the following columns:
- timestamp: Date and time of the reconciliation
- source_value: Value from the source system
- target_value: Value from the target system
- discrepancy: Difference between source and target values
- status: MATCH or MISMATCH
- category: Category of the data (e.g., Sales, Inventory, Orders, Payments)

## Sample Data

A sample data file (`sample_data.csv`) is provided for testing. You can use this to explore the features of the insight agent.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 