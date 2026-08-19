FROM python:3.14.3-slim

RUN echo 'alias uvr="uv run"' >> ~/.bashrc

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock .

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY . .

EXPOSE 8000

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]
