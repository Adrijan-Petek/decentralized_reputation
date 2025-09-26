#!/bin/bash
echo "Running Decentralized Reputation System demo..."
mkdir -p outputs charts
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python src/demo_reputation.py
