# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document outlines the software requirements for the PainTrack application, a productivity tool that uses psychological triggers like loss aversion and gamification to improve task commitment and accountability.

### 1.2 Scope
PainTrack allows users to stake points when creating tasks. If the user completes the task on time, points are returned (with possible rewards). Failure results in a penalty (points deduction). The platform encourages accountability, social competition, and personal growth.

### 1.3 Intended Audience
- Product Owners
- Backend Developers
- Frontend Developers
- QA Engineers
- Designers
- Potential Contributors

### 1.4 Definitions and Abbreviations
- **MVP**: Minimum Viable Product  
- **OOP**: Object-Oriented Programming  
- **CI/CD**: Continuous Integration / Continuous Deployment  
- **API**: Application Programming Interface  

---

## 2. Overall Description

### 2.1 Product Perspective
This app will be built using a microservices architecture with FastAPI, PostgreSQL, Docker, and deployed with GitHub Actions. The frontend is optionally React-based.

### 2.2 Product Functions
- Register/Login with OAuth
- Create and manage tasks with point stakes
- Visualize progress and history
- Social features like peer challenges and leaderboards

### 2.3 User Classes and Characteristics
- **Freelancers**: Need structure and independence
- **Students**: Seek external motivation
- **Solopreneurs**: Want productivity tools with accountability

### 2.4 Operating Environment
- OS: Cross-platform
- Browsers: Chrome, Firefox, Safari
- API: RESTful using FastAPI

---

## 3. Functional Requirements

### 3.1 User Authentication
- Register via email or OAuth
- Secure login and session handling

### 3.2 Task Management
- Create, edit, and delete tasks
- Set deadlines and point stakes
- Mark as complete or auto-complete on deadline

### 3.3 Points System
- Deduct/add points based on task outcome
- Points ledger and analytics

### 3.4 Notifications
- Task reminders
- Failure warnings
- Optional email/push notifications

### 3.5 Social Features
- Friend challenges
- Public leaderboards
- Peer accountability

---

## 4. Non-Functional Requirements

### 4.1 Performance
- API response time < 300ms
- App should handle 10K concurrent users in MVP phase

### 4.2 Security
- HTTPS by default
- JWT-based authentication
- Data encryption for sensitive user data

### 4.3 Maintainability
- Modular codebase
- Unit tests + API tests
- Docker-based deployments

### 4.4 Scalability
- Horizontal scaling via microservices
- Stateless APIs for easy load balancing

---

## 5. External Interfaces

### 5.1 User Interface (UI)
- Clean, minimalist interface
- Responsive layout for mobile and desktop

### 5.2 API Interfaces
- REST API for all core functions
- Auth endpoints: /login, /register
- Task endpoints: /tasks, /tasks/{id}
- User endpoints: /profile, /points

### 5.3 Hardware Interfaces
- None required

### 5.4 Software Interfaces
- PostgreSQL DB
- OAuth providers: Google, GitHub

---

## 6. Future Enhancements

- Paid plans with real money stakes
- Integration with Slack, Google Calendar
- Mobile app (React Native or Flutter)
- Gamified task templates

---

## 7. Appendix

- Architecture Diagrams
- Sequence Flows
- Database Schema
