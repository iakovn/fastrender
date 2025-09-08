"""Command-line entrypoint helpers for running the fastrender app."""

from __future__ import annotations

import sys
from collections.abc import Iterable

from .api import app


def main(argv: Iterable[str] | None = None) -> None:
    """Run the application via uvicorn.

    This will prefer invoking the `uvicorn` CLI (if available on PATH) so the
    user gets the normal CLI flags and behavior. If the CLI isn't available
    we fall back to importing `uvicorn` and calling `uvicorn.run`.
    """
    argv = list(argv) if argv is not None else list(sys.argv[1:])

    class UvicornImportError(RuntimeError):
        def __init__(self) -> None:
            super().__init__("uvicorn import failed")

    try:
        import uvicorn
    except Exception as exc:  # pragma: no cover - diagnostic/fallback
        raise UvicornImportError() from exc

    # Minimal default if no args provided
    if not argv:
        uvicorn.run(app, host="127.0.0.1", port=8000)
        return

    # crude parsing for `--host` and `--port`
    host = "127.0.0.1"
    port = 8000
    try:
        for i, a in enumerate(argv):
            if a in ("--host", "-h") and i + 1 < len(argv):
                host = argv[i + 1]
            if a == "--port" and i + 1 < len(argv):
                port = int(argv[i + 1])
    except Exception:  # pragma: no cover - defensive
        host = "127.0.0.1"
        port = 8000

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":  # pragma: no cover - manual run
    main()
