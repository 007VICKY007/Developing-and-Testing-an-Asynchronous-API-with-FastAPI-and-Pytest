# FastAPI CRUD API with PostgreSQL 📝

A practical, production-ready REST API built with FastAPI, PostgreSQL, and Docker. This project demonstrates modern Python API development with proper testing, database management, and containerization.

## What This Project Does

This is a **notes management API** that lets you create, read, update, and delete notes. Think of it as a backend for a note-taking app, but it's designed to be a solid foundation you can adapt for any CRUD application.

## Why This Stack?

- **FastAPI** - Because it's fast, modern, and makes writing APIs actually enjoyable
- **PostgreSQL** - A reliable, battle-tested database that won't let you down
- **Docker** - So "it works on my machine" actually means it works everywhere
- **Pytest** - Testing shouldn't be painful, and with pytest, it isn't

## Visual Walkthrough 📸

### Docker Desktop - Container Overview
<img width="1915" height="1079" alt="image" src="https://github.com/user-attachments/assets/b5aa8083-30db-4b85-a940-1b114b286356" />

*The Docker Desktop interface showing our running containers. You can see the `fastapi-crud` container actively running with CPU and memory usage metrics displayed.*

### Docker Compose Services Status
<img width="1197" height="662" alt="Screenshot 2025-11-12 134017" src="https://github.com/user-attachments/assets/da01dece-0373-4916-8758-f501dbb960a5" />

*Terminal output showing all four services successfully built and started: fastapi-crud-web, Network, Container for database, and Container for web application.*

### Testing the API with curl
<img width="1169" height="674" alt="Screenshot 2025-11-12 135335" src="https://github.com/user-attachments/assets/60c60b04-9f13-460b-a935-15b02e0db079" />

*Making a POST request to create a new note. The API returns a 201 Created status with the note data including the auto-generated ID.*

### Verification of Running Services
<img width="438" height="113" alt="Screenshot 2025-11-12 134419" src="https://github.com/user-attachments/assets/79d76b3a-1a8c-4b97-bde8-558233257516" />

*Confirmation that all Docker Compose services are up and running smoothly.*

### Database Query Verification
<img width="1182" height="255" alt="Screenshot 2025-11-12 135353" src="https://github.com/user-attachments/assets/b58d6a52-b2e0-4815-b89a-1419afff3861" />

*Direct database verification using `docker-compose exec` to query PostgreSQL and confirm the note was actually persisted.*

## What's Working Right Now ✅

### Stage 1: Basic FastAPI Setup
Got the FastAPI app running in Docker. The classic "hello world" moment, but containerized:
```bash
curl http://localhost:8000/
→ {"hello": "world"}
```

### Stage 2: Database Integration
Added PostgreSQL and hooked everything up with Docker Compose. Now the app and database talk to each other like old friends:
- `web` service running FastAPI on port 8000
- `db` service running PostgreSQL on port 5432
- Both containers chatting away on the same network

### Stage 3: Full CRUD + Testing
Built the complete notes API with all four operations:
- **POST** `/notes/` - Create a new note
- **GET** `/notes/{id}/` - Grab a specific note
- **PUT** `/notes/{id}/` - Update an existing note
- **DELETE** `/notes/{id}/` - Remove a note

And here's the best part - **12 tests, all passing**:
```bash
docker-compose run --rm web python -m pytest -q
→ 12 passed in 1.09s ✨
```

### Stage 4: Database Migrations (In Progress)
Started setting up Alembic for proper database version control. Because manually updating schemas is so 2010.

## How to Get Started

### Prerequisites
Just Docker and Docker Compose. That's it. No "but first install 37 dependencies" nonsense.

### Quick Start

1. **Clone and enter the project**
   ```bash
   cd fastapi-crud
   ```

2. **Fire it up**
   ```bash
   docker-compose up -d --build
   ```

3. **Check it's alive**
   ```bash
   curl http://localhost:8000/
   ```

4. **Explore the API docs**
   Open your browser to `http://localhost:8000/docs` - FastAPI generates beautiful, interactive docs automatically.

## Project Structure

```
fastapi-crud/
├── app/
│   ├── main.py           # FastAPI app and routes
│   ├── db.py             # Database connection setup
│   └── models.py         # SQLAlchemy models
├── tests/
│   ├── conftest.py       # Test fixtures and setup
│   └── test_notes.py     # API endpoint tests
├── Dockerfile            # Container definition
├── docker-compose.yml    # Multi-container orchestration
└── requirements.txt      # Python dependencies
```

## Playing with the API

### Create a note
```bash
curl -X POST "http://localhost:8000/notes/" \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Note","description":"This actually works!"}'
```

### Get a note
```bash
curl http://localhost:8000/notes/1/
```

### Update a note
```bash
curl -X PUT "http://localhost:8000/notes/1/" \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","description":"Changed my mind"}'
```

### Delete a note
```bash
curl -X DELETE http://localhost:8000/notes/1/
```

## Running Tests

Tests run inside Docker, so they use the same environment as production:

```bash
# Run all tests
docker-compose run --rm web python -m pytest

# Run with verbose output
docker-compose run --rm web python -m pytest -v

# Run with coverage
docker-compose run --rm web python -m pytest --cov=app
```

## Checking the Database

Want to peek inside PostgreSQL?

```bash
# Jump into the database container
docker-compose exec db psql -U hello_fastapi -d hello_fastapi_dev

# Then run SQL
SELECT * FROM notes;
```

## What's Next? 🚀

### Immediate Todos
- [ ] Finish Alembic setup and create initial migration
- [ ] Remove manual schema creation (let migrations handle it)
- [ ] Add migration commands to CI/CD

### Future Enhancements
- [ ] Add JWT authentication (Stage 5)
- [ ] Create user management system
- [ ] Add integration tests with real database
- [ ] Set up GitHub Actions for automated testing
- [ ] Add API rate limiting
- [ ] Implement pagination for list endpoints

## Technical Highlights

### Why This Approach Works

**Docker Compose for Everything**: Development, testing, and production use the same containers. No more "works on my machine" excuses.

**Test-Driven Development**: The tests came *with* the features, not after. All 12 tests passed on the first run because we built them alongside the API.

**Database Mocking in Tests**: Unit tests mock the database, so they're lightning-fast. Integration tests (coming soon) will use a real database.

**Environment Variables**: Configuration lives in `docker-compose.yml`, making it easy to change settings without touching code.

## Common Issues (and Fixes)

**Port 8000 already in use?**
```bash
docker-compose down
# or change the port in docker-compose.yml
```

**Database connection errors?**
Wait a few seconds after starting - PostgreSQL needs a moment to initialize.

**Tests failing?**
Make sure you rebuilt the Docker image after changing requirements:
```bash
docker-compose build
```

## Contributing

Found a bug? Have an idea? PRs are welcome! Just keep the philosophy in mind: clarity over cleverness.

*Last updated: November 12, 2025*
