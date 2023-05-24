from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import (
  CreateOrderSchema,
  GetOrderSchema,
  GetOrdersSchema,
)

ORDERS = []

@app.get('/orders', response_model=GetOrdersSchema)
def get_orders(cancelled: Optional[bool] = None, limit: Optional[int] = None):
  if cancelled is None and limit is None:
    return {"orders": ORDERS}
  query_set = ORDERS[:]
  if cancelled is not None:
    if cancelled:
      query_set = filter(lambda order: order['status'] == 'cancelled', query_set)
    else:
      query_set = filter(lambda order: order['status'] != 'cancelled', query_set)
  if limit is not None and len(query_set) > limit:
    return { "orders": query_set[:limit] }
  return { "orders": query_set }

@app.post(
  '/orders', 
  status_code=status.HTTP_201_CREATED, 
  response_model=GetOrderSchema
)
def create_order(order_details: CreateOrderSchema):
  order = order_details.dict()
  order['id'] = uuid4()
  order['created'] = datetime.utcnow()
  order['status'] = 'created'
  ORDERS.append(order)
  return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: UUID):
  for order in ORDERS:
    if order['id'] == order_id:
      return order
  raise HTTPException(
    status_code=404, detail=f'Order with ID {order_id} not found'
  )

@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
  for order in ORDERS:
    if order['id'] == order_id:
      order.update(order_details.dict())
      return order
  raise HTTPException(
    status_code=404, detail=f'Order with ID {order_id} not found'
  )

@app.delete(
  '/orders/{order_id}', 
  status_code=status.HTTP_204_NO_CONTENT,
  response_class=Response
)
def delete_order(order_id: UUID):
  for index, order in enumerate(ORDERS):
    if order['id'] == order_id:
      order.pop(index)
      return
  raise HTTPException(
    status_code=404, detail=f'Order with ID {order_id} not found'
  )

@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
  for order in ORDERS:
    if order['id'] == order_id:
      order['status'] = 'cancelled'
      return order
  raise HTTPException(
    status_code=404, detail=f'Order with ID {order_id} not found'
  )

@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID):
  for order in ORDERS:
    if order['id'] == order_id:
      order['status'] = 'progress'
      return order
  raise HTTPException(
    status_code=404, detail=f'Order with ID {order_id} not found'
  )
