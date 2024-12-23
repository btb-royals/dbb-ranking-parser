FROM alpine:3.21

ENV VIRTUAL_ENV=/opt/venv

RUN apk add --no-cache python3 && \
    python3 -m venv $VIRTUAL_ENV && \
    rm -rf /var/cache/apk/*

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m ensurepip && \
    pip3 install --no-cache-dir 'dbb-ranking-parser==0.5.0-dev'

# Only relevant for HTTP server mode.
EXPOSE 8080

ENTRYPOINT ["dbb-ranking-parser"]
