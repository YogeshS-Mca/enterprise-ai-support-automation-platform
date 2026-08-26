# System Architecture — Overview

## Current System

The current system is intentionally small.

```text
Browser
   |
   | HTTP GET /health
   v
Uvicorn
   |
   v
FastAPI
   |
   v
Health Check
   |
   v
JSON Response