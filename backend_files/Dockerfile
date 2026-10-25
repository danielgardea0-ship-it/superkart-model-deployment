FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache--dir -r requirements.text

COPY . .

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:superkart_api"]
