from random import uniform, choice, choices, sample

class SearchSpace:
  """
  The search space class containing the domain definitions
  used for sampling points using a random distribution
  """
  
  def __init__(self, axes):
    self.axes = axes

  def sample(self):
    point = []
    for a in self.axes:
      point.append(a.sample())
    return point
  
class Axis:
  """
  Class to represent an axis of the search space 
  be it continous or discrete
  """
  
  def __init__(self, distribution, *args, **kwargs):
    self.distribution = distribution
    self.pos_constraints = args
    self.kw_constraints = kwargs
    print(kwargs)
      
  def sample(self):
    return self.distribution(*(self.pos_constraints),**(self.kw_constraints))
    

space = SearchSpace(
  [Axis(choice, [0,1]) for i in range(0,10)]
)

p = space.sample()
print(p)