FROM python:3.12-slim AS builder

WORKDIR /application

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --target /python-dependencies

COPY . .

# Stage - 2

FROM python:3.12-slim

WORKDIR /application

COPY --from=builder /python-dependencies /usr/local
COPY --from=builder /application /application

EXPOSE 9000
git
CMD ["python","app.py"]