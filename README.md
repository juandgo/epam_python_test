This is an exercice using CICD, Docker and Kubernetes


comand to verify if the toml file is in sync with the project

uv lock --locked


comand to check
uvx ruff check .

command to format de code
uvx ruff format .

comand to format import
ruff check --select I --fix .

to verify if all files are formated correctly
uvx ruff format --check .

uv add --dev pyright

uv pyright .