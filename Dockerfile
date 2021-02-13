FROM alpine:3.13

RUN apk add --no-cache \
        libxml2 \
        libxslt \
        python3 \
        py3-lxml \
        && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install 'dbb-ranking-parser==0.4.1' && \
    rm -rf /var/cache/apk/*

# Only relevant for HTTP server mode.
EXPOSE 8080

ENTRYPOINT ["dbb-ranking-parser"]
