import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Any
from pydantic import BaseModel
import matplotlib
matplotlib.use('Agg')  # Set the backend to non-interactive 'Agg'
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os
import json

class ReconciliationResult(BaseModel):
    timestamp: datetime
    source_value: float
    target_value: float
    discrepancy: float
    status: str
    category: str

class InsightAgent:
    def __init__(self):
        self.data = pd.DataFrame()
        self.anomaly_detector = IsolationForest(contamination=0.1, random_state=42)
        self.scaler = StandardScaler()
        
    def load_mock_data(self):
        """Generate mock data for testing"""
        dates = pd.date_range(start='2024-01-01', end='2024-04-02', freq='D')
        n_samples = len(dates)
        
        # Generate random data
        np.random.seed(42)
        source_values = np.random.normal(1000, 100, n_samples)
        target_values = source_values + np.random.normal(0, 50, n_samples)
        
        # Create discrepancies
        discrepancies = target_values - source_values
        status = ['MATCH' if abs(d) < 50 else 'MISMATCH' for d in discrepancies]
        categories = np.random.choice(['Sales', 'Inventory', 'Orders', 'Payments'], n_samples)
        
        # Create DataFrame
        self.data = pd.DataFrame({
            'timestamp': dates,
            'source_value': source_values,
            'target_value': target_values,
            'discrepancy': discrepancies,
            'status': status,
            'category': categories
        })
        
    def analyze_trends(self) -> Dict[str, Any]:
        """Analyze trends in the data"""
        daily_stats = self.data.groupby(self.data['timestamp'].dt.date).agg({
            'discrepancy': ['mean', 'std', 'count'],
            'status': lambda x: (x == 'MISMATCH').mean()
        }).round(2)
        
        return {
            'daily_stats': daily_stats.to_dict(),
            'total_records': len(self.data),
            'mismatch_rate': (self.data['status'] == 'MISMATCH').mean(),
            'avg_discrepancy': self.data['discrepancy'].mean(),
            'max_discrepancy': self.data['discrepancy'].max()
        }
    
    def detect_anomalies(self) -> List[Dict[str, Any]]:
        """Detect anomalies in the data"""
        # Prepare data for anomaly detection
        X = self.data[['source_value', 'target_value', 'discrepancy']].values
        X_scaled = self.scaler.fit_transform(X)
        
        # Fit and predict
        self.anomaly_detector.fit(X_scaled)
        predictions = self.anomaly_detector.predict(X_scaled)
        
        # Get anomaly records
        anomalies = self.data[predictions == -1]
        
        return [
            {
                'timestamp': row['timestamp'].isoformat(),
                'source_value': row['source_value'],
                'target_value': row['target_value'],
                'discrepancy': row['discrepancy'],
                'category': row['category']
            }
            for _, row in anomalies.iterrows()
        ]
    
    def category_analysis(self) -> Dict[str, Any]:
        """Analyze discrepancies by category"""
        category_stats = self.data.groupby('category').agg({
            'discrepancy': ['mean', 'std', 'count'],
            'status': lambda x: (x == 'MISMATCH').mean()
        }).round(2)
        
        return {
            'category_stats': category_stats.to_dict(),
            'worst_category': category_stats[('status', '<lambda>')].idxmax(),
            'best_category': category_stats[('status', '<lambda>')].idxmin()
        }
    
    def generate_visualizations(self) -> Dict[str, str]:
        """Generate visualizations for insights"""
        # Create plots directory if it doesn't exist
        os.makedirs('plots', exist_ok=True)
        
        # Discrepancy over time
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=self.data, x='timestamp', y='discrepancy')
        plt.title('Discrepancy Trends Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('plots/discrepancy_trend.png')
        plt.close()
        
        # Category distribution
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.data, x='category', y='discrepancy')
        plt.title('Discrepancy Distribution by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('plots/category_distribution.png')
        plt.close()
        
        return {
            'discrepancy_trend': 'plots/discrepancy_trend.png',
            'category_distribution': 'plots/category_distribution.png'
        }
    
    def get_insights(self) -> Dict[str, Any]:
        """Generate comprehensive insights"""
        return {
            'trends': self.analyze_trends(),
            'anomalies': self.detect_anomalies(),
            'category_analysis': self.category_analysis(),
            'visualizations': self.generate_visualizations()
        }

# Example usage
if __name__ == "__main__":
    # Initialize agent
    agent = InsightAgent()
    
    # Load mock data
    agent.load_mock_data()
    
    # Generate insights
    insights = agent.get_insights()
    
    # Print summary
    print("\n=== Insight Summary ===")
    print(f"Total Records: {insights['trends']['total_records']}")
    print(f"Mismatch Rate: {insights['trends']['mismatch_rate']:.2%}")
    print(f"Average Discrepancy: {insights['trends']['avg_discrepancy']:.2f}")
    print(f"Worst Category: {insights['category_analysis']['worst_category']}")
    print(f"Best Category: {insights['category_analysis']['best_category']}")
    print(f"Number of Anomalies: {len(insights['anomalies'])}") 