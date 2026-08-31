# Incident Management REST API Design

## 1. Purpose

This document defines the REST API design for the Incident Management capability.

The API provides HTTP endpoints that allow clients to create, retrieve, list, and update IT support incidents.

---

## 2. API Versioning

The API uses URL-based versioning.

Base path:

`/api/v1`

This allows future versions to be introduced without breaking existing clients.

---

## 3. Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/incidents` | Create an incident |
| GET | `/api/v1/incidents` | List incidents |
| GET | `/api/v1/incidents/{incident_id}` | Retrieve an incident |
| PATCH | `/api/v1/incidents/{incident_id}` | Update an incident |

---

## 4. Request Flow

Client
↓
FastAPI Router
↓
Request Validation
↓
Incident Service
↓
Incident Repository
↓
Persistence

---

## 5. Create Incident

### Request

`POST /api/v1/incidents`

The client submits the incident information.

### Expected Result

A successful request creates an incident and returns the created incident representation.

Expected HTTP status:

`201 Created`

---

## 6. List Incidents

### Request

`GET /api/v1/incidents`

### Expected Result

Returns the incidents currently available through the repository.

Expected HTTP status:

`200 OK`

---

## 7. Get Incident

### Request

`GET /api/v1/incidents/{incident_id}`

### Expected Result

Returns the requested incident.

If the incident does not exist, the API returns an appropriate HTTP error.

---

## 8. Update Incident

### Request

`PATCH /api/v1/incidents/{incident_id}`

### Expected Result

Updates the requested incident according to the supported update fields.

---

## 9. Layer Responsibilities

### API Layer

Responsible for:

- HTTP routing
- Request/response models
- HTTP status codes
- API error translation

### Service Layer

Responsible for:

- Business rules
- Incident lifecycle operations
- Coordination between API and repository

### Repository Layer

Responsible for:

- Persistence abstraction
- Creating incidents
- Retrieving incidents
- Listing incidents
- Updating incidents

---

## 10. Design Principle

The API layer should not contain persistence logic.

The dependency direction is:

API → Service → Repository

This keeps the application modular and makes the persistence implementation replaceable.

---

## 11. Current Persistence

The current implementation uses an in-memory repository.

This is intentional for the current development phase.

A future PostgreSQL implementation can replace the persistence layer while keeping the API contract and business logic stable.

---

## 12. Future Evolution

Future versions may introduce:

- PostgreSQL persistence
- Authentication and authorization
- Pagination
- Filtering
- Sorting
- Audit logging
- Event publishing
- AI-powered incident classification
- Automated remediation