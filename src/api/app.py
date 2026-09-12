"""API Gateway Lambda Handler.

Copyright (c) 2026

This software is released under the MIT License.
https://opensource.org/licenses/MIT
"""

from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.event_handler.openapi.models import Server
from aws_lambda_powertools.utilities.typing import LambdaContext

from api.system_rooter import router as system_rooter

app = APIGatewayHttpResolver()
app.enable_swagger(
    path="/swagger",
    title="APIサンプル",
    description="APIサンプル",
    version="1.0.0",
    servers=[Server(url="http://127.0.0.1:3000/", description="ローカル環境")],
)
app.include_router(system_rooter)


@app.exception_handler(Exception)
def handle_exception(error: Exception) -> dict:
    """例外ハンドラ.

    Args:
        error (Exception): 発生した例外.

    Returns:
        dict: ステータスメッセージ.
    """
    return {
        "error": str(error),
    }


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """Lambda Handler.

    Args:
        event (dict): API Gatewayイベント.
        context (LambdaContext): ラムダランタイムコンテキスト.

    Returns:
        dict: ステータスメッセージ.
    """
    return app.resolve(event, context)
