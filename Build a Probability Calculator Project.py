import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Create a list with one entry for each ball
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            all_balls = self.contents[:]  # Create a copy of the contents
            self.contents.clear()  # Empty the hat
            return all_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0  # Count the number of successful experiments
    
    # Run the experiment num_experiments times
    for _ in range(num_experiments):
        # Create a copy of the hat contents
        hat_copy = Hat(**{ball: hat.contents.count(ball) for ball in set(hat.contents)})
        
        # Draw balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the occurrences of each color in the drawn balls
        drawn_counts = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        
        # Check if the drawn balls satisfy the expected balls condition
        success = True
        for ball, count in expected_balls.items():
            if drawn_counts.get(ball, 0) < count:
                success = False
                break
        
        # Increment success_count if the condition was met
        if success:
            success_count += 1
    
    # Return the probability as the number of successful experiments divided by the total number of experiments
    return success_count / num_experiments
