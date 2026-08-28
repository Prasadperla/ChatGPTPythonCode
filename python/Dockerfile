FROM python:3.11-slim as build
LABEL Author: prasad
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
copy . .

FROM python:3.11-slim
WORKDIR /app
COPY --from=build /install /usr/local
COPY --from=build /app /app
CMD ["python3","app.py"]

