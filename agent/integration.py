import pandas as pd
import json
import os
from datetime import datetime
from insight_agent import InsightAgent

class ReconciliationIntegration:
    """
    Integration class to connect the insight agent with the main application.
    This class handles data loading, processing, and visualization integration.
    """
    
    def __init__(self, data_dir=None):
        """
        Initialize the integration with optional data directory.
        
        Args:
            data_dir (str, optional): Directory containing reconciliation data files.
        """
        self.agent = InsightAgent()
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        
    def load_data_from_csv(self, file_path):
        """
        Load reconciliation data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            bool: True if data was loaded successfully, False otherwise.
        """
        try:
            df = pd.read_csv(file_path)
            
            # Ensure required columns exist
            required_columns = ['timestamp', 'source_value', 'target_value', 'discrepancy', 'status', 'category']
            if not all(col in df.columns for col in required_columns):
                print(f"Error: CSV file must contain columns: {required_columns}")
                return False
            
            # Convert timestamp to datetime if it's a string
            if df['timestamp'].dtype == 'object':
                df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Assign data to agent
            self.agent.data = df
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def load_data_from_json(self, file_path):
        """
        Load reconciliation data from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            bool: True if data was loaded successfully, False otherwise.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Convert to DataFrame
            df = pd.DataFrame(data)
            
            # Convert timestamp to datetime if it's a string
            if 'timestamp' in df.columns and df['timestamp'].dtype == 'object':
                df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Assign data to agent
            self.agent.data = df
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def get_insights_json(self):
        """
        Get insights from the agent in JSON format.
        
        Returns:
            dict: Insights data in JSON format.
        """
        insights = self.agent.get_insights()
        
        # Convert datetime objects to ISO format strings
        for anomaly in insights['anomalies']:
            if isinstance(anomaly['timestamp'], datetime):
                anomaly['timestamp'] = anomaly['timestamp'].isoformat()
        
        return insights
    
    def save_insights_to_json(self, file_path=None):
        """
        Save insights to a JSON file.
        
        Args:
            file_path (str, optional): Path to save the JSON file.
            
        Returns:
            str: Path to the saved file.
        """
        if file_path is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_path = os.path.join(self.data_dir, f'insights_{timestamp}.json')
        
        insights = self.get_insights_json()
        
        with open(file_path, 'w') as f:
            json.dump(insights, f, indent=2)
        
        return file_path
    
    def get_visualization_path(self, filename):
        """Get the path to a visualization file"""
        plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
        file_path = os.path.join(plots_dir, filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            # Generate visualizations if they don't exist
            self.agent.generate_visualizations()
        
        return file_path
    
    def get_dashboard_data(self):
        """
        Get formatted data for dashboard display.
        
        Returns:
            dict: Dashboard-ready data.
        """
        insights = self.agent.get_insights()
        
        # Format data for dashboard
        dashboard_data = {
            'summary': {
                'total_records': insights['trends']['total_records'],
                'mismatch_rate': f"{insights['trends']['mismatch_rate']:.2%}",
                'avg_discrepancy': f"{insights['trends']['avg_discrepancy']:.2f}",
                'max_discrepancy': f"{insights['trends']['max_discrepancy']:.2f}",
                'worst_category': insights['category_analysis']['worst_category'],
                'best_category': insights['category_analysis']['best_category'],
                'anomaly_count': len(insights['anomalies'])
            },
            'visualizations': self.get_visualization_path('visualization.png'),
            'recent_anomalies': insights['anomalies'][:5] if insights['anomalies'] else []
        }
        
        return dashboard_data

# Example usage
if __name__ == "__main__":
    # Initialize integration
    integration = ReconciliationIntegration()
    
    # Load mock data
    integration.agent.load_mock_data()
    
    # Get dashboard data
    dashboard_data = integration.get_dashboard_data()
    
    # Print summary
    print("\n=== Dashboard Summary ===")
    for key, value in dashboard_data['summary'].items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Save insights to JSON
    json_path = integration.save_insights_to_json()
    print(f"\nInsights saved to: {json_path}")
    
    # Print visualization paths
    print("\n=== Visualizations ===")
    for name, path in dashboard_data['visualizations'].items():
        print(f"{name}: {path}") 