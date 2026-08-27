# Incident Management API Contract

## 1. Purpose

The Incident Management API provides REST endpoints for creating,
retrieving, and listing IT support incidents.

The API is the first functional capability of the Enterprise AI
Support & Autonomous Incident Resolution Platform.

---

# 2. API Version

Current API version:

`v1`

Base path:

`/api/v1`

Example:

`/api/v1/incidents`

API versioning allows future versions to be introduced without
breaking existing clients.

---

# 3. Incident Lifecycle

An incident represents an IT support problem that requires
investigation, resolution, or monitoring.

Initial lifecycle:

```text
                    ┌─────────────┐
                    │    OPEN     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ INVESTIGATING│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  RESOLVED   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   CLOSED    │
                    └─────────────┘