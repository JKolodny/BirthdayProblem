import random

def has_duplicate(lst):
    """Check if a list has duplicate elements."""
    return len(lst) != len(set(lst))

def simulate_birthdays(num_people, num_trials=10000):
    """Simulate the birthday problem.

    Args:
    - num_people: Number of people in the room.
    - num_trials: Number of trials to run the simulation.

    Returns:
    - Probability that at least two people have the same birthday.
    """
    duplicate_count = 0

    for _ in range(num_trials):
        # Generate random birthdays for 'num_people' people
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        
        if has_duplicate(birthdays):
            duplicate_count += 1

    return duplicate_count / num_trials

if __name__ == "__main__":
    num_people = 23
    probability = simulate_birthdays(num_people)
    print(f"With {num_people} people, the probability that at least two have the same birthday is about {probability:.2%}")
