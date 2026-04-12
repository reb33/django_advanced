# Stage 1: Build stage
FROM python:3.12-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install poetry
RUN pip install poetry==2.2.1

# install dependencies
COPY pyproject.toml poetry.lock ./
# Install dependencies (skip dev dependencies for production)
# --no-root skips installing the project itself, which saves time if only code changed
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR


# Stage 2: Runtime stage
FROM python:3.12-alpine as runtime

ENV VIRTUAL_ENV=/usr/src/app/.venv \
    PATH="/usr/src/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /usr/src/app
COPY . .

