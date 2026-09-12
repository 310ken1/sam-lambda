# syntax=docker/dockerfile:1.7
FROM public.ecr.aws/amazonlinux/amazonlinux:2023-minimal

# 変数定義
# ユーザ設定
ARG USER=vscode
ARG UID=1001
ARG GID=1001
ARG HOME=/home/${USER}

# 環境変数
ENV LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8

# パッケージインストール
RUN --mount=type=cache,target=/var/cache/dnf \
    dnf update -y && dnf install -y \
    shadow-utils \
    libatomic \
    sudo \
    procps-ng \
    tar \
    tree \
    unzip \
    git \
    findutils \
    graphviz \
    docker \
    glibc-langpack-ja \
    ipa-gothic-fonts && \
    dnf clean all

# ユーザ設定
RUN groupadd -g ${GID} ${USER} && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    mkdir -p ${HOME}/.cache && \
    chown -R ${UID}:${GID} ${HOME}

# プロジェクト設定
RUN mkdir -p /workspace && chown -R ${UID}:${GID} /workspace
ENV PATH="/workspace/scripts/:$PATH"

USER ${USER}
WORKDIR ${HOME}
