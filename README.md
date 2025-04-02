# Data Reconciliation Dashboard

A modern, responsive dashboard for visualizing and managing data reconciliation results. This dashboard provides a user-friendly interface for monitoring reconciliation status, tracking discrepancies, and managing data quality.

## Features

- **Dark/Light Theme**: Toggle between dark and light themes for comfortable viewing
- **Responsive Design**: Fully responsive layout that works on desktop and mobile devices
- **Real-time Statistics**: View key metrics and statistics at a glance
- **Interactive Charts**: Visualize reconciliation status and discrepancy trends
- **Notification System**: Stay updated with real-time notifications
- **Search Functionality**: Quickly find specific records or discrepancies
- **Mobile-friendly Navigation**: Collapsible sidebar for better mobile experience

## Technologies Used

- HTML5
- CSS3 (with CSS Variables for theming)
- JavaScript (ES6+)
- Chart.js for data visualization
- Font Awesome for icons

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Basic understanding of web development (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd data-reconciliation-ui
   ```

3. Open the project in your preferred code editor.

### Running the Dashboard

You can run the dashboard using any of the following methods:

1. Using Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.

2. Using VS Code's Live Server extension:
   - Install the "Live Server" extension
   - Right-click on `index.html`
   - Select "Open with Live Server"

3. Using Node.js's http-server:
   ```bash
   npm install -g http-server
   http-server
   ```
   Then open `http://localhost:8080` in your browser.

## Project Structure

```
data-reconciliation-ui/
├── css/
│   └── style.css
├── js/
│   └── main.js
├── images/
│   ├── logo.svg
│   └── avatar.svg
└── index.html
```

## Customization

### Theme Colors

The dashboard uses CSS variables for theming. You can modify the colors in the `:root` section of `style.css`:

```css
:root {
    --primary-color: #6C5CE7;
    --secondary-color: #A8A4E6;
    --background-dark: #1A1B1E;
    /* ... other variables ... */
}
```

### Chart Configuration

Chart configurations can be modified in `main.js`. The dashboard uses Chart.js for data visualization:

```javascript
const reconciliationChart = new Chart(
    document.getElementById('reconciliationChart'),
    {
        type: 'doughnut',
        data: {
            // ... chart data ...
        },
        options: {
            // ... chart options ...
        }
    }
);
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Chart.js](https://www.chartjs.org/) for the charting library
- [Font Awesome](https://fontawesome.com/) for the icons
- The open-source community for inspiration and resources 