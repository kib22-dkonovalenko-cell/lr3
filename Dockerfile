FROM python:3.12-slim

WORKDIR /Konovalenko

COPY . /Konovalenko

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "gtrans3.py"]
