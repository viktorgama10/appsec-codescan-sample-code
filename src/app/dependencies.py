from starlette.requests import Request
from starlette.responses import Response


# Dependency
def get_db(request: Request):
    return request.state.db
