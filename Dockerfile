FROM alpine:3.18

RUN apk add --no-cache \
        libxml2 \
        libxslt \
        python3 \
        py3-lxml \
        && \
    python3 -m ensurepip && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir 'dbb-ranking-parser==0.5.0-dev' && \
    rm -rf /var/cache/apk/*

# Only relevant for HTTP server mode.
EXPOSE 8080

ENTRYPOINT ["dbb-ranking-parser"]
