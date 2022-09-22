from fastapi.exceptions import HTTPException
from starlette import status

ScrapInfoNotFoundException = HTTPException(status_code=status.HTTP_404_NOT_FOUND)