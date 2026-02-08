FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG user=user_bot
ARG name_bot=impulse_day_bot
ARG workdir=/app/bots/$name_bot
ARG userdir=/home/$user

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install system packages
RUN apt update --yes --quiet && apt install --yes --quiet --no-install-recommends \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN useradd $user

RUN mkdir -p $workdir && chown -R $user:$user $workdir \
    && mkdir -p $userdir && chown -R $user:$user $userdir

WORKDIR $workdir

# Entrypoints
COPY entrypoints/impulse_day_bot_start.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY pyproject.toml uv.lock .

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Copy data bot in root catalog
COPY --chown=$user:$user app/bots/impulse_day_bot $workdir

# Lock and sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv lock && uv sync --locked

USER $user

ENTRYPOINT ["/entrypoint.sh"]


