# 电网灵活负荷编排器

工程用于记录负荷资源、时段计划和执行告警，异步消息通过 RabbitMQ 传递。Python 模块位于 `app/`，测试位于 `tests/`，持久化文件由 `DATA_DIR` 指定。

执行 `docker compose up --build` 启动 RabbitMQ 与 API，健康检查地址为 `:8000/healthz`。测试命令为 `pytest`，接口基于 FastAPI。
