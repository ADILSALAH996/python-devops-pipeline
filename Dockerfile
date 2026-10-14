FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --system --no-create-home appuser

COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 8000

CMD ["python", "-u", "app.py"]