#!/usr/bin/env bash
# Idempotent bootstrap for the Ticket-park Telegram bot.
set -euo pipefail

cd "$(dirname "$0")/.."

# Ubuntu 24.04 ships Python 3.12 but not the venv module; install it once.
if ! dpkg -s python3-venv >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3-venv
fi

# Create the virtualenv if it does not already exist.
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi

.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
