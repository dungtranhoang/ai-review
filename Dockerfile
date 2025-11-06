ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

WORKDIR /app

RUN apt-get update && \
    apt-get install -y bash ca-certificates curl git libexpat1 openssh-client && \
    rm -rf /var/lib/apt/lists/*

# Copy the local source code instead of installing from PyPI
COPY . /app
RUN pip install --no-cache-dir -e .

# Set the entrypoint to use the installed ai-review command
ENTRYPOINT ["ai-review"]