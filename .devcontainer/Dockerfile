ARG IMAGE_SHA=sha256:40add84e86664c56683c1cfd69406ad84246a5a5dc8b8a7556c04e0126c0b855

# mcr.microsoft.com/devcontainers/python:dev-3.14-bookworm
FROM mcr.microsoft.com/devcontainers/python@${IMAGE_SHA}

ARG GCLOUD_VERSION=550.0.0
ARG GCLOUD_MD5=e3bc1b41229fa6f9c51cfea30357069c
ARG GCLOUD_FILE=google-cloud-cli-${GCLOUD_VERSION}-linux-x86_64.tar.gz

WORKDIR /tmp

RUN curl -fL -O https://storage.googleapis.com/cloud-sdk-release/${GCLOUD_FILE} \
  && echo "${GCLOUD_MD5}  ${GCLOUD_FILE}" | md5sum -c - \
  && tar -xf ${GCLOUD_FILE} -C /usr/local/ \
  && /usr/local/google-cloud-sdk/install.sh --quiet --usage-reporting=false \
  && rm -f ${GCLOUD_FILE}

ENV PATH="/usr/local/google-cloud-sdk/bin:${PATH}"

# nodeのインストール
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash \
  && . "/usr/local/share/nvm//nvm.sh" \
  && nvm install 24
RUN npm install -g @anthropic-ai/claude-code @google/gemini-cli @openai/codex