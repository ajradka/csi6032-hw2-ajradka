FROM python:3.13-slim-bookworm

ARG COPILOT_CLI_VERSION=1.0.87

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
        gh \
        git \
        nodejs \
        npm \
    && npm install --global --omit=dev "@github/copilot@${COPILOT_CLI_VERSION}" \
    && npm cache clean --force \
    && apt-get purge --auto-remove -y \
        npm \
        curl \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.npm \
    && useradd --create-home --shell /bin/bash dev \
    && mkdir --parents /workspace \
    && chown dev:dev /workspace

USER dev
WORKDIR /workspace
