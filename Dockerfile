FROM python:3.8-alpine3.15
ENV FLASK_ENV=development
ENV PROD_DATABASE_URI=""
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/EncrypterMicroService/.local/bin

#crear usuario
RUN adduser -S -D -H EncrypterMicroService
RUN mkdir /home/EncrypterMicroService
RUN chown -R EncrypterMicroService /home/EncrypterMicroService

#seleccionar la carpeta del usuario
WORKDIR /home/EncrypterMicroService

RUN mkdir main
#TODO: Agregar env flask_env=production
#copia la carpeta del proyecto a la imagen
COPY ./main ./main
COPY ./app.py .

#Instala dependencias del sistema

RUN apk add --update curl gcc g++ libffi-dev openssl-dev build-base linux-headers && \
    rm -rf /var/cache/apk/*

ADD requirements.txt ./requirements.txt
USER EncrypterMicroService
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install gevent gunicorn==20.1.0

#puerto por el que escucha la imagen
EXPOSE 5000

#HEALTCHECK --interval=10s --timeout=10s --start-period=55s CMD \
#curl -f --retry 10 --max-time 15 --retry-delay 10 --retry-max-time 60 ""http://localhost:5000/api/v1/healt" || exit 1

#ejecuta la aplicacion
#CMD ["gunicorn", "--workers", "1", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "app:create_app()"]
CMD ["python3", "./app.py"]