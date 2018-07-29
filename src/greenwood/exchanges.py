from util import OrderType, create_id

class Exchange(object):
  def __init__(self, name, default = False, offerings=[], order_options = []):
    self.name = name
    self.offerings = offerings
    self.default = default
    self.id = create_id()
    self.order_options = [
      OrderType.BUY_MARKET,
      OrderType.BUY_LIMIT,
      OrderType.SELL_MARKET,
      OrderType.SELL_LIMIT,
      OrderType.PUT,
      OrderType.CALL
    ]
  
  def is_default(self):
    return self.default

  @property
  def id(self):
    return self.id
  
  @property
  def name(self):
    return self.name
  
  def __repr__(self):
    return '%s (%s)' % (self.name, self.id)
  
  def ordertype_supported(self, type):
    return type in self.order_options
  
  def buy(self, type, quantity, symbol, price):
    raise NotImplementedError('The buy function of an exchange must be implemented if called')
  
  def sell(self, type, quantity, symbol, price):
    raise NotImplementedError('The sell function of an exchange must be implemented if called')
  
  def call(self, type, quantity symbol, price):
    raise NotImplementedError('The call function of an exchange must be implemented if called')
  
  def put(self, type, quantity, symbol, price):
    raise NotImplementedError('The put function of an exchange must be implemented if called')