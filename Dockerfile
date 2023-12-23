FROM python:3.11

# Install dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
