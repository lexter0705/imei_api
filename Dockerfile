FROM ubuntu:latest
LABEL authors="lexte"

ENTRYPOINT ["top", "-b"]