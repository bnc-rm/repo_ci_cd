FROM python:3.6
WORKDIR /var/www
COPY . /var/www
RUN pip install Flask scikit-learn
EXPOSE 80
CMD ["python", "app.py"]