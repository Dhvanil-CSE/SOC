FROM python:3.10-slim
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
# Since cloud server is inside container it's port is not exposed to other socket programs which are outside container.
# Hence we have to expose the port.
EXPOSE 9998
RUN pip install numpy
RUN pip install sagemath
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD ["python", "CS.py"]

