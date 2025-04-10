
```markdown
# 🧘‍♂️ PainTrack – Get Things Done or Pay the Price

> A habit-forming productivity app where commitment has real value. Bet points on your tasks, gain them back when you succeed — or lose them when you don’t.

---

## 🔥 Project Summary

**PainTrack** is a personal productivity and accountability platform that blends task management with behavioral psychology. Users commit to completing tasks within set deadlines by betting PainTrack Points. If they succeed, points are returned. If not, points are deducted. These stakes create a subtle but effective push to follow through on commitments.

This project is being built as a microservices-based SaaS using **FastAPI**, with a future roadmap for web + mobile clients.

---

## ✨ Features

- ✅ Create tasks with time-bound goals
- 🎯 Assign PainTrack Points to tasks (accountability currency)
- 🔁 Reuse points only after successful task completion
- 💸 Point deduction on task failure or delay
- 🔒 Auth system for secure account management
- 📊 Leaderboard / task history (future)
- 🧠 Optional peer review mode (future feature: challenge friends)
- 📱 Mobile-first UI planned

---

## ⚙️ Tech Stack

| Layer             | Technology        |
|------------------|-------------------|
| Backend API      | FastAPI (Python)  |
| Auth             | OAuth2 / JWT      |
| Database         | PostgreSQL        |
| Caching/Queue    | Redis (for scoring, email tasks etc.) |
| Containerization | Docker            |
| DevOps           | GitHub Actions + Docker Compose |
| Frontend         | Next.js (Planned) |
| Deployment       | Fly.io / Railway / Vercel |

---

## 🚀 Getting Started

Clone this repo and get started with the core API service locally.

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/PainTrack.git
cd PainTrack
```

### 2. Spin up local dev environment

```bash
docker-compose up --build
```

### 3. API will be running on:

```
http://localhost:8000/docs
```

Use the Swagger UI to test endpoints interactively.

---

## 📌 Roadmap

- [x] Task + User Models
- [x] Auth + JWT
- [ ] Task scoring engine (points logic)
- [ ] Notifications (reminders, task status)
- [ ] Leaderboard / analytics
- [ ] Mobile PWA or Flutter frontend
- [ ] Peer challenge feature

---

## 🤝 Contributing

Pull requests are welcome as the project evolves. Please open an issue first to discuss any major changes.

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 🌐 Links

- Live Site (coming soon)
- [Domain Check: PainTrack.in | betdone.com](https://godaddy.com/)
- Product Hunt Launch (planned)

---

> “Discipline equals freedom. And PainTrack makes sure you stick to your word.”  
> — The PainTrack Team
```
