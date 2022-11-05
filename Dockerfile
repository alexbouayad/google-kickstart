FROM    debian:10.9

RUN     apt-get update && \
        apt-get install -y --no-install-recommends software-properties-common && \
        add-apt-repository -y ppa:fish-shell/release-3 && \
        apt-get install -y --no-install-recommends \
            fish \
            python3.7 \
            python3-pip \
            pypy3 && \
        rm -rf /var/lib/apt/lists/*

RUN     python3.7 -m pip install -U \
            black \
            ipython

RUN     ulimit -s 65536
