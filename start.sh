#!/bin/bash
nohup python -m fastapi run ./model/model_api_wrapped.py &

sleep 10

python bot/bot.py