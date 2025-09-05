This workspace is in a dev container running on "Ubuntu 22.04.5 LTS".

Some of the command line tools available on the `PATH`: `apt`, `dpkg`, `git`, `curl`, `wget`, `ssh`, `scp`, `gpg`, `ps`, `top`, `find`, `grep`, `zip`, `unzip`, `tar`, `gzip`, `bzip2`, `xz`"

The devcontainer includes `node`, `npm` and `eslint` pre-installed and available on the `PATH` to enable use of supporting tools.

This dev container is primarily aimed at Python FastAPI server development.

The dependecies are managed by uv.
Linting is done with ruff. Type checking is done with mypy.
Testing is done with pytest.

Always define type annotations on function and method arguments and return values. Run "make check" to check linting and types and "make test" to run the tests.
