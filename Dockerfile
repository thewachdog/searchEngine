FROM python:latest
WORKDIR /home
COPY . /home
RUN ls -la && \
    pwd && \
    python --version

# Java Machine
FROM openjdk:13
WORKDIR /home
COPY --from=0 /home .
RUN ls -la && \
    pwd && \
    java --version

# Python again
FROM python:latest
WORKDIR /home
COPY --from=1 /home .
RUN ls -la && \
    pwd && \
    python --version
