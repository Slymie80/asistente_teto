FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir rvc-python

EXPOSE 5050

CMD ["python", "-m", "rvc_python", "api", "-p", "5050", "-l", "-md", "/app/rvc_models"]
