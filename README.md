To reproduce:

```
git clone https://github.com/chadrik/zuban-test/
cd zuban-test/http-client/
uv run --with=zuban zuban mypy
```

Result:

```
src/http_client/client.py:1: error: Cannot find implementation or library stub for module named "httpx"  [import-not-found]
Found 1 error in 1 file (checked 2 source files)
```
