#!/bin/bash
# this is the entrypoint for this application,
# you can extend the startup features by modifying this file
# e.g apply migrations, etc.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
