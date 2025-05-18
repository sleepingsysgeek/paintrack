from python:3.13
Workdir /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./code
ENV PYTHONPATH=/code
expose 8000
cmd ["uvicorn", "auth.app.main:app", "--host", "0.0.0.0", "--port", "8000"]