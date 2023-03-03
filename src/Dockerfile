FROM python:3.10-bullseye

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get update && apt-get install libgl1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# RUN pip uninstall opencv-python

# RUN pip install opencv-python-headless

EXPOSE 3000

CMD [ "python3", "app.py" ]