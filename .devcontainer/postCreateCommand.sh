#! /usr/bin/env bash

cd /workspaces/fastrender/

# Install Dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install --install-hooks
