# Incident Management API Architecture

## Purpose

This document describes the architecture of the first
Incident Management REST API.

## Request Flow

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
Data Store

## API Layer

The API layer is responsible for:

- HTTP routing
- Request handling
- Response formatting
- HTTP status codes

## Schema Layer

The schema layer is responsible for:

- Request validation
- Response structure
- Type safety
- API contract enforcement

## Service Layer

The service layer is responsible for:

- Business rules
- Incident creation
- Incident retrieval
- Incident listing

## Repository Layer

The repository layer is responsible for:

- Data access
- Storing incidents
- Retrieving incidents
- Abstracting persistence

## Initial Persistence

The first implementation will use in-memory storage.

This allows the API architecture and business logic to be
implemented before introducing a database.

## Future Persistence

The repository layer will later be adapted to PostgreSQL.

The API and service layers should not need to know the
details of the database implementation.

## Design Principle

Each layer should have a clear responsibility.

This separation improves:

- Maintainability
- Testability
- Extensibility
- Separation of concerns