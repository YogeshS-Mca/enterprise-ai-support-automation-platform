# Pydantic and Domain Modeling

## Purpose

The Incident Management API uses Pydantic models to define
and validate API request and response data.

## Why Validation Matters

An API should not blindly trust incoming client data.

Validation protects the application from:

- Missing required fields
- Invalid data types
- Invalid enum values
- Strings that are too short
- Strings that exceed allowed limits

## Request Model

`IncidentCreate` represents data accepted from the client.

Example:

```json
{
  "title": "Database failure",
  "description": "Production database is unavailable",
  "priority": "critical"
}