# Minnesota Tennis Ball Cricket Men’s 2025 League Rankings App

## Overview
A web application to display live and historical team rankings for the Minnesota Tennis Ball Cricket Men’s 2025 League. The app will feature a professional, responsive UI and interactive charts.

## Functional Requirements

- Display current team rankings with points, wins, losses, NRR, etc.
- Show team details and match history on click.
- Visualize rankings and stats with interactive charts.
- Responsive design for desktop and mobile.
- Admin interface for updating results (optional).
- Fetch data from a backend API.

## Non-Functional Requirements

- Fast load times and smooth navigation.
- SEO-friendly pages.
- Secure API endpoints.
- Scalable to support league growth.
- Automated testing for reliability.

## Tech Stack

- **Frontend:** Next.js, Tailwind CSS, Recharts
- **Backend:** Node.js, Express.js
- **Database:** MongoDB
- **Hosting:** Vercel (frontend), AWS/Heroku (backend & DB)

## API Endpoints (Sample)

- `GET /api/rankings` – List current team rankings
- `GET /api/teams/:id` – Team details and match history
- `POST /api/results` – (Admin) Add match result

## Data Model (Simplified)

- **Team:** _id, name, logo, matches_played, wins, losses, points, nrr
- **Match:** _id, date, team1_id, team2_id, team1_score, team2_score, winner_id

## Security

- Use HTTPS for all endpoints.
- Admin endpoints require authentication.

## Deployment

- Frontend deployed on Vercel.
- Backend and database hosted on AWS or Heroku.
