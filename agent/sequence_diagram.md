# Data Reconciliation System Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant WebUI
    participant Integration
    participant InsightAgent
    participant DataStore
    participant Visualizer

    %% Initial Load
    User->>WebUI: Access Dashboard
    WebUI->>Integration: Request Dashboard Data
    Integration->>InsightAgent: Load Mock Data
    InsightAgent->>DataStore: Read Sample Data
    DataStore-->>InsightAgent: Return Data
    InsightAgent->>InsightAgent: Process Data
    InsightAgent->>Visualizer: Generate Visualizations
    Visualizer-->>InsightAgent: Return Plot Files
    InsightAgent-->>Integration: Return Insights
    Integration-->>WebUI: Return Dashboard Data
    WebUI-->>User: Display Dashboard

    %% Data Upload Flow
    User->>WebUI: Upload Data File
    WebUI->>Integration: Process Upload
    Integration->>DataStore: Save File
    DataStore-->>Integration: Confirm Save
    Integration->>InsightAgent: Load New Data
    InsightAgent->>InsightAgent: Analyze Data
    InsightAgent->>Visualizer: Generate New Visualizations
    Visualizer-->>InsightAgent: Return Updated Plots
    InsightAgent-->>Integration: Return New Insights
    Integration-->>WebUI: Return Success
    WebUI-->>User: Show Updated Dashboard

    %% API Access Flow
    User->>WebUI: Request API Data
    WebUI->>Integration: Get Insights
    Integration->>InsightAgent: Request Analysis
    InsightAgent-->>Integration: Return Insights
    Integration-->>WebUI: Return JSON Data
    WebUI-->>User: Display API Response

    %% Visualization Request Flow
    User->>WebUI: Request Visualization
    WebUI->>Integration: Get Plot
    Integration->>InsightAgent: Check Visualization
    alt Visualization Exists
        InsightAgent-->>Integration: Return Plot Path
    else Visualization Missing
        InsightAgent->>Visualizer: Generate Plot
        Visualizer-->>InsightAgent: Return New Plot
        InsightAgent-->>Integration: Return Plot Path
    end
    Integration-->>WebUI: Serve Plot File
    WebUI-->>User: Display Visualization
```

## Component Descriptions

1. **User**: The end user interacting with the system
2. **WebUI**: Flask web application serving the dashboard
3. **Integration**: Bridge between web interface and agent
4. **InsightAgent**: Core analysis engine
5. **DataStore**: File system storing data files
6. **Visualizer**: Matplotlib/Seaborn visualization generator

## Flow Descriptions

### Initial Load
- User accesses the dashboard
- System loads mock data
- Generates initial visualizations
- Displays dashboard with insights

### Data Upload Flow
- User uploads new data file
- System processes and saves the file
- Generates new analysis and visualizations
- Updates dashboard with new insights

### API Access Flow
- User requests data through API
- System retrieves current insights
- Returns formatted JSON response

### Visualization Request Flow
- User requests specific visualization
- System checks if visualization exists
- Generates new visualization if needed
- Serves the plot file to user 