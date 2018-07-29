from util import create_id

class Robot(object):
  def __init__(self):
    self.id = create_id()
    self.portfolio = None
  
  def subscribe(self, portfolio):
    portfolio.subscribe(self.id)
    self.portfolio = portfolio