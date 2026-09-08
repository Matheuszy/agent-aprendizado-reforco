FROM python:3.12-slim AS backend

WORKDIR /app

# Install uv for fast package management
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src/ ./src/

# Install Python dependencies (without dev dependencies for production)
RUN uv sync --frozen --no-dev --no-group dev

# Expose API port
EXPOSE 8000

# Run the FastAPI server
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM node:20-alpine AS frontend

WORKDIR /app/frontend

# Copy frontend files
COPY frontend/package.json frontend/package-lock.json ./
COPY frontend/ ./

# Install dependencies and build
RUN npm install && npm run build


FROM nginx:alpine AS productio

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy frontend build
COPY --from=frontend /app/frontend/dist /usr/share/nginx/html

# Expose ports
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]