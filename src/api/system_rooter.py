"""システム機能ルータ.

Copyright (c) 2026

This software is released under the MIT License.
https://opensource.org/licenses/MIT
"""

from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import BaseModel

TAGS: list[str] = ["システム"]
router = Router()


class HealthResponseModel(BaseModel):
    """システム状態."""

    status: str


@router.get(
    "/health",
    tags=TAGS,
    summary="ヘルスチェック",
    description="システム状態を取得する.",
)
def get_health() -> HealthResponseModel:
    """システム状態を取得する.

    Returns:
        HealthResponseModel: システム状態.
    """
    return HealthResponseModel(status="ok")
