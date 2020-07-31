import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      counter = 0
      while counter < value:
        self.contents.append(key)
        counter += 1

  def draw(self, num_balls_to_draw):
    balls_drawn = []
    if num_balls_to_draw > len(self.contents):
      return self.contents
    counter = 0
    while counter < num_balls_to_draw:
      random_ball_from_contents = random.choice(self.contents)
      self.contents.remove(random_ball_from_contents)
      balls_drawn.append(random_ball_from_contents)
      counter += 1
    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = len(expected_balls)
  original_hat_contents = copy.deepcopy(hat.contents)
  number_of_matches = 0
  experiment_results = []
  counter = 0
  while counter < num_experiments:
    hat = Hat()
    hat.contents = copy.deepcopy(original_hat_contents)
    experiment_results.append(hat.draw(num_balls_drawn))
    counter += 1
  for experiment_result in experiment_results:
    matches_count = 0
    for key in expected_balls:
      if experiment_result.count(key) >= expected_balls[key]:
        matches_count += 1
    if matches_count == count:
      number_of_matches += 1
  return number_of_matches / num_experiments
    

  