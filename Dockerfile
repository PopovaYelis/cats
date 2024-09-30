FROM python:3.8
WORKDIR /cats
COPY requirements.txt /cats/requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn app:create_app --workers 4  --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:5000
