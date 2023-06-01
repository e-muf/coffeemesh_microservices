from pathlib import Path

import yaml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  debug=True, openapi_url="/openapi/orders.json", docs_url="/docs/orders"
)
app.add_middleware(
  CORSMiddleware,
  allow_origins="*"
)

oas_doc = yaml.safe_load((Path(__file__).parent / '../../oas.yaml').read_text())

app.openapi = lambda: oas_doc

from orders.web.api import api