from flask import Flask, render_template, jsonify, request, send_file
from flask_cors import CORS
import os
from integration import ReconciliationIntegration

# Initialize Flask app
app = Flask(__name__, 
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static'))
CORS(app)

# Initialize the integration
integration = ReconciliationIntegration()

# Load mock data for demonstration
integration.agent.load_mock_data()

# Create necessary directories
os.makedirs(os.path.join(os.path.dirname(__file__), 'templates'), exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(__file__), 'static'), exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(__file__), 'plots'), exist_ok=True)

# Create the dashboard template
with open(os.path.join(os.path.dirname(__file__), 'templates', 'dashboard.html'), 'w') as f:
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Reconciliation Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .card { border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; }
        .card-header { background-color: #6c5ce7; color: white; border-radius: 10px 10px 0 0 !important; }
        .stat-card { text-align: center; padding: 20px; }
        .stat-value { font-size: 2rem; font-weight: bold; color: #6c5ce7; }
        .stat-label { color: #6c757d; font-size: 0.9rem; }
        .visualization-container { margin-top: 20px; }
        .visualization-img { max-width: 100%; border-radius: 5px; }
        .anomaly-item { border-left: 4px solid #ff7675; padding-left: 10px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container-fluid py-4">
        <h1 class="mb-4">Data Reconciliation Dashboard</h1>
        
        <!-- Summary Stats -->
        <div class="row mb-4">
            <div class="col-md-3">
                <div class="card stat-card">
                    <div class="stat-value">{{ data.summary.total_records }}</div>
                    <div class="stat-label">Total Records</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stat-card">
                    <div class="stat-value">{{ data.summary.mismatch_rate }}</div>
                    <div class="stat-label">Mismatch Rate</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stat-card">
                    <div class="stat-value">{{ data.summary.avg_discrepancy }}</div>
                    <div class="stat-label">Avg Discrepancy</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stat-card">
                    <div class="stat-value">{{ data.summary.anomaly_count }}</div>
                    <div class="stat-label">Anomalies Detected</div>
                </div>
            </div>
        </div>
        
        <!-- Visualizations -->
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Discrepancy Trends</div>
                    <div class="card-body visualization-container">
                        <img src="/api/visualizations/discrepancy_trend.png" alt="Discrepancy Trends" class="visualization-img">
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Category Distribution</div>
                    <div class="card-body visualization-container">
                        <img src="/api/visualizations/category_distribution.png" alt="Category Distribution" class="visualization-img">
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Category Analysis -->
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Category Analysis</div>
                    <div class="card-body">
                        <p><strong>Worst Category:</strong> {{ data.summary.worst_category }}</p>
                        <p><strong>Best Category:</strong> {{ data.summary.best_category }}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Recent Anomalies</div>
                    <div class="card-body">
                        {% if data.recent_anomalies %}
                            {% for anomaly in data.recent_anomalies %}
                                <div class="anomaly-item">
                                    <p><strong>Timestamp:</strong> {{ anomaly.timestamp }}</p>
                                    <p><strong>Category:</strong> {{ anomaly.category }}</p>
                                    <p><strong>Discrepancy:</strong> {{ anomaly.discrepancy }}</p>
                                </div>
                            {% endfor %}
                        {% else %}
                            <p>No anomalies detected.</p>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Data Upload -->
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">Upload Data</div>
                    <div class="card-body">
                        <form action="/api/upload" method="post" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label for="file" class="form-label">Select CSV or JSON file</label>
                                <input class="form-control" type="file" id="file" name="file" accept=".csv,.json">
                            </div>
                            <button type="submit" class="btn btn-primary">Upload</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    ''')

@app.route('/')
def index():
    """Render the dashboard page"""
    dashboard_data = integration.get_dashboard_data()
    return render_template('dashboard.html', data=dashboard_data)

@app.route('/api/insights')
def get_insights():
    """Get insights as JSON"""
    return jsonify(integration.get_insights_json())

@app.route('/api/dashboard-data')
def get_dashboard_data():
    """Get formatted dashboard data"""
    return jsonify(integration.get_dashboard_data())

@app.route('/api/visualizations/<path:filename>')
def get_visualization(filename):
    """Serve visualization files"""
    plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
    file_path = os.path.join(plots_dir, filename)
    
    # Check if file exists
    if not os.path.exists(file_path):
        # Generate missing visualizations
        integration.agent.generate_visualizations()
        
        # Check again if file exists after generation
        if not os.path.exists(file_path):
            return jsonify({'error': f'Visualization {filename} not found'}), 404
    
    return send_file(file_path)

@app.route('/api/upload', methods=['POST'])
def upload_data():
    """Upload and process data"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save the uploaded file
    upload_dir = os.path.join(os.path.dirname(__file__), 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    
    # Process the file based on its extension
    success = False
    if file.filename.endswith('.csv'):
        success = integration.load_data_from_csv(file_path)
    elif file.filename.endswith('.json'):
        success = integration.load_data_from_json(file_path)
    else:
        return jsonify({'error': 'Unsupported file format. Please upload CSV or JSON.'}), 400
    
    if success:
        # Save insights to JSON
        insights_path = integration.save_insights_to_json()
        return jsonify({
            'message': 'Data processed successfully',
            'insights_path': insights_path
        })
    else:
        return jsonify({'error': 'Failed to process data'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True) 