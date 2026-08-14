FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (layer caching)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

# Create non-root user (security best practice)
RUN useradd -m -u 1001 appuser && \
    chown -R appuser:appuser /app
USER 1001

EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s \
            --timeout=10s \
            --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", \
     "--workers", "2", \
     "--bind", "0.0.0.0:5000", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "app:app"]