FROM debian:bookworm-slim@sha256:56ff6d36d4eb3db13a741b342ec466f121480b5edded42e4b7ee850ce7a418ee

RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 10001 -s /usr/sbin/nologin aka

WORKDIR /rev

COPY --chown=aka:aka NZXWE3DFONZWKX3CN5WGSZ3F /rev/NZXWE3DFONZWKX3CN5WGSZ3F
COPY --chown=aka:aka MZWGCZY /rev/MZWGCZY

RUN chmod 0555 /rev/NZXWE3DFONZWKX3CN5WGSZ3F \
 && chmod 0400 /rev/MZWGCZY

USER aka

EXPOSE 3000

ENTRYPOINT ["/rev/NZXWE3DFONZWKX3CN5WGSZ3F"]