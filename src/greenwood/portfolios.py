from util import OrderType, create_id

class Portfolio(object):
  def __init__(self, exchanges = []):
    self.alpha = 0
    self.sharpe = 0
    self.id = create_id()
    self.robots = []
    num_default_exchanges = 0
    for exchange in exchanges:
      if exchange.is_default():
        num_default_exchanges += 1
        if num_default_exchanges > 1:
          raise Exception('Only one default exchange allowed per portfolio')
    self.exchanges = exchanges

  @property
  def id(self):
    return self.id
  
  @property
  def alpha(self):
    return self.alpha
  
  @alpha.setter
  def alpha(self, newValue):
    pass
  
  @alpha.deleter
  def alpha(self):
    self.alpha = 0
  
  @property
  def sharpe(self):
    return self.sharpe
  
  @sharpe.setter
  def sharpe(self, newValue):
    pass
  
  @sharpe.deleter
  def sharpe(self):
    self.sharpe = 0
  
  @property
  def exchanges(self):
    return self.exchanges
  
  @property
  def default_exchange(self):
    for exchange in self.exchanges:
      if exchange.is_default():
        return exchange
    if len(self.exchanges) > 0:
      self.exchanges[0].default = True
      return self.exchanges[0]
    else:
      return None
  
  def subscribe(self, robot_id):
    self.robots.append(robot_id)

  def exchange_by_id(self, id):
    return next((x for x in self.exchanges if x.id == id), None)
  
  def buy(self, type, quantity, symbol, price, exchange):
    xchange = next((x for x in self.exchanges if x.id == exchange.id), self.default_exchange)
    if xchange.ordertype_supported(type):
      xchange.buy(type, quantity, symbol, price)
    else:
      raise Exception('Exchange %s does not support OrderType %s' % (repr(xchange), type))
  
  def sell(self, type, quantity, symbol, price, exchange):
    xchange = next((x for x in self.exchanges if x.id == exchange.id), self.default_exchange)
    if xchange.ordertype_supported(type):
      xchange.sell(type, quantity, symbol, price)
    else:
      raise Exception('Exchange %s does not support OrderType %s' % (repr(xchange), type))
  
  def call(self, type, quantity symbol, price):
    xchange = next((x for x in self.exchanges if x.id == exchange.id), self.default_exchange)
    if xchange.ordertype_supported(type):
      xchange.call(type, quantity, symbol, price)
    else:
      raise Exception('Exchange %s does not support OrderType %s' % (repr(xchange), type))
  
  def put(self, type, quantity, symbol, price):
    xchange = next((x for x in self.exchanges if x.id == exchange.id), self.default_exchange)
    if xchange.ordertype_supported(type):
      xchange.put(type, quantity, symbol, price)
    else:
      raise Exception('Exchange %s does not support OrderType %s' % (repr(xchange), type))