FROM alpine:3.3

RUN apk add \
        build-base \
        ca-certificates \
        libxml2 \
        libxml2-dev \
        libxslt \
        libxslt-dev \
        python3 \
        python3-dev \
        && \
    python3 -m ensurepip && \
    pip3 install dbb-ranking-parser && \
    apk del build-base python3-dev libxml2-dev libxslt-dev && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["dbb-ranking"]

CMD ["--help"]
