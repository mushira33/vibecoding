// Theme Management
const themeToggle = document.querySelector('.theme-toggle');
const body = document.body;

// Check for saved theme preference
const savedTheme = localStorage.getItem('theme') || 'dark';
body.classList.toggle('light-theme', savedTheme === 'light');

themeToggle.addEventListener('click', () => {
    body.classList.toggle('light-theme');
    localStorage.setItem('theme', body.classList.contains('light-theme') ? 'light' : 'dark');
});

// Mobile Menu Toggle
const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});

// Close sidebar when clicking outside on mobile
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && 
        !sidebar.contains(e.target) && 
        !menuToggle.contains(e.target)) {
        sidebar.classList.remove('active');
    }
});

// Initialize Charts
const reconciliationChart = new Chart(
    document.getElementById('reconciliationChart'),
    {
        type: 'doughnut',
        data: {
            labels: ['Matched', 'Unmatched', 'Pending'],
            datasets: [{
                data: [65, 20, 15],
                backgroundColor: [
                    '#00B894', // Success color
                    '#FF7675', // Error color
                    '#FDCB6E'  // Warning color
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: getComputedStyle(document.body).getPropertyValue('--text-primary')
                    }
                }
            }
        }
    }
);

const discrepancyChart = new Chart(
    document.getElementById('discrepancyChart'),
    {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Discrepancies',
                data: [12, 19, 15, 25, 22, 30],
                borderColor: '#6C5CE7',
                backgroundColor: 'rgba(108, 92, 231, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: getComputedStyle(document.body).getPropertyValue('--border-color')
                    },
                    ticks: {
                        color: getComputedStyle(document.body).getPropertyValue('--text-secondary')
                    }
                },
                x: {
                    grid: {
                        color: getComputedStyle(document.body).getPropertyValue('--border-color')
                    },
                    ticks: {
                        color: getComputedStyle(document.body).getPropertyValue('--text-secondary')
                    }
                }
            }
        }
    }
);

// Search Functionality
const searchInput = document.querySelector('.search-bar input');
searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    // Implement search functionality here
    console.log('Searching for:', searchTerm);
});

// Notification System
const notificationBtn = document.querySelector('.notification-btn');
const notificationCount = document.querySelector('.notification-count');

// Example notification data
const notifications = [
    {
        type: 'critical',
        title: 'Data Mismatch Detected',
        message: 'Transaction ID 12345 has different amounts in source and target systems',
        timestamp: '2 minutes ago'
    },
    {
        type: 'warning',
        title: 'Reconciliation Pending',
        message: '5 transactions are pending reconciliation',
        timestamp: '1 hour ago'
    },
    {
        type: 'info',
        title: 'System Update',
        message: 'New reconciliation rules have been applied',
        timestamp: '2 hours ago'
    }
];

// Update notification count
notificationCount.textContent = notifications.length;

// Handle notification click
notificationBtn.addEventListener('click', () => {
    // Implement notification dropdown functionality here
    console.log('Notifications clicked');
});

// Handle discrepancy actions
document.querySelectorAll('.action-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const action = e.target.textContent;
        const discrepancyItem = e.target.closest('.discrepancy-item');
        const title = discrepancyItem.querySelector('h3').textContent;
        
        console.log(`Performing ${action} action on: ${title}`);
        // Implement action handling here
    });
});

// Update charts on window resize
window.addEventListener('resize', () => {
    reconciliationChart.resize();
    discrepancyChart.resize();
});

// Handle view all button click
document.querySelector('.view-all-btn').addEventListener('click', () => {
    console.log('View all discrepancies clicked');
    // Implement view all functionality here
});
