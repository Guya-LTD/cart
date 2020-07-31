# build version
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

# workdir
ARG WORK_DIR
WORKDIR ${WORK_DIR}

COPY requirements.txt ${WORK_DIR}
RUN chmod +x -R ${WORK_DIR}/requirements.txt

COPY requirements-dev.txt ${WORK_DIR}
RUN chmod +x -R ${WORK_DIR}/requirements-dev.txt

RUN pip install -r requirements-dev.txt

CMD flask run