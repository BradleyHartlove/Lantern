#!/bin/bash

docker run -d --name vllm --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    -p 5000:5000 \
    vllm/vllm-openai:latest \
    --model nomic-ai/nomic-embed-text-v1.5 \
    --port 5000 \
    --host 0.0.0.0 \
    --swap-space 0 \
    --gpu-memory-utilization 0.5 \
    --trust-remote-code