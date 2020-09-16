########################################################
# Development build                                    #
########################################################
FROM python:3.7-slim AS development

# Install git
RUN apt-get update
RUN apt-get -y install git

# workdir
ENV WORK_DIR /usr/src/app
WORKDIR ${WORK_DIR}

COPY requirements.txt ${WORK_DIR}
RUN chmod +x -R ${WORK_DIR}/requirements.txt

RUN pip install -r requirements.txt

COPY . ./

RUN cp .env.example .env

CMD flask run

EXPOSE 5000

########################################################
# Production environment                               #
########################################################
FROM python:3.7-slim AS production

# Install git
#RUN apt-get update
#RUN apt-get -y install git

# workdir
ENV WORK_DIR /usr/src/app
WORKDIR ${WORK_DIR}

COPY requirements.txt ${WORK_DIR}
RUN chmod +x -R ${WORK_DIR}/requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD python waitress_server.py