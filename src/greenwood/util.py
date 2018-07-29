from enum import Enum
import uuid

class OrderType(Enum):
  BUY_MARKET = 'buy_mkt'
  BUY_LIMIT = 'buy_lmt'
  SELL_MARKET = 'sell_mkt'
  SELL_LIMIT = 'sell_lmt'
  PUT = 'put'
  CALL = 'call'

def create_id():
  return str(uuid.uuid4())