# Simple Simulation of Customer Support Priority using operating systems lottery ticket scheduling principles
# This version models true lottery scheduling, where each user owns a number of tickets representing their priority.
# The scheduler randomly selects a ticket each round to decide which user's call is serviced next.

import random
import matplotlib.pyplot as plt

# --- User Input Section ---
while True:
    try:
        num_users = int(input("How many total users (calls) in the system? "))
        if num_users <= 0:
            raise ValueError("Number of users must be positive\n")
        break
    except ValueError as e:
        print(f"Oops! {e}\n")
        num_users = 100

while True:
    try:
        premium_ratio = float(input("What percentage of users are premium? (0-100): "))
        if premium_ratio < 0 or premium_ratio > 100:
            raise ValueError("Percentage must be within [0,100]%\n")
        break
    except ValueError as e:
        print(f"Oops! {e}\n")
        premium_ratio = 60

while True:
    try:
        premium_tickets = int(input("How many tickets does each premium user get? (priority weight): "))
        standard_tickets = int(input("How many tickets does each standard user get? (priority weight): "))
        if premium_tickets <= 0 or standard_tickets <= 0:
            raise ValueError("Ticket counts must be positive\n")
        break
    except ValueError as e:
        print(f"Oops! {e}\n")
        premium_tickets = 10
        standard_tickets = 2

while True:
    try:
        calls_per_user = int(input("How many calls does each user need serviced? "))
        if calls_per_user <= 0:
            raise ValueError("Calls per user must be positive\n")
        break
    except ValueError as e:
        print(f"Oops! {e}\n")
        calls_per_user = 1

# --- Build User List ---
users = []
premium_count = int(num_users * premium_ratio / 100)
standard_count = num_users - premium_count
user_id = 1
for _ in range(premium_count):
    users.append({
        'id': user_id,
        'type': 'Premium',
        'tickets': premium_tickets,
        'calls_remaining': calls_per_user
    })
    user_id += 1
for _ in range(standard_count):
    users.append({
        'id': user_id,
        'type': 'Standard',
        'tickets': standard_tickets,
        'calls_remaining': calls_per_user
    })
    user_id += 1

# --- Lottery Scheduling Simulation ---
# Each round, build a ticket pool and randomly select a ticket to decide which user's call is serviced next.
# This mimics OS lottery scheduling: tickets = weighted probability of being chosen.
serviced_premium = 0
serviced_standard = 0

total_calls = num_users * calls_per_user
calls_serviced = 0

while users:
    # Build ticket pool: each user contributes their tickets if they have calls remaining
    ticket_pool = []
    for idx, user in enumerate(users):
        if user['calls_remaining'] > 0:
            ticket_pool.extend([idx] * user['tickets'])
    if not ticket_pool:
        break  # All calls serviced
    # Randomly select a ticket
    winner_idx = random.choice(ticket_pool)
    winner = users[winner_idx]
    # Service one call for the winner
    winner['calls_remaining'] -= 1
    calls_serviced += 1
    if winner['type'] == 'Premium':
        serviced_premium += 1
    else:
        serviced_standard += 1
    # Remove users with no calls left
    users = [u for u in users if u['calls_remaining'] > 0]

# --- Results ---
theoretical_premium_ratio = (premium_count * premium_tickets) / (premium_count * premium_tickets + standard_count * standard_tickets) * 100
actual_premium_ratio = serviced_premium / total_calls * 100
actual_standard_ratio = serviced_standard / total_calls * 100
theoretical_standard_ratio = 100 - theoretical_premium_ratio

print("\n--- Lottery Scheduling Simulation Results ---")
print(f"Theoretical: {theoretical_premium_ratio:.2f}% premium users serviced, {theoretical_standard_ratio:.2f}% standard users serviced (based on ticket weights)")
print(f"Actual:      {actual_premium_ratio:.2f}% premium users serviced, {actual_standard_ratio:.2f}% standard users serviced (from simulation)")

# --- Matplotlib Graph ---
labels = ['Premium', 'Standard']
theoretical = [theoretical_premium_ratio, theoretical_standard_ratio]
actual = [actual_premium_ratio, actual_standard_ratio]

plt.figure(figsize=(8,5))
plt.plot(labels, theoretical, label='Theoretical', marker='o', color='blue')
plt.plot(labels, actual, label='Actual', marker='x', color='red')
plt.title('Customer Support Lottery Scheduling Results')
plt.ylabel('Percentage of Calls Serviced (%)')
plt.ylim(0, 100)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# --- Explanation ---
# In true lottery scheduling, each user's tickets represent their chance of being selected for service.
# Premium users get more tickets, so they are more likely to be chosen each round, but selection is random.
# This ensures fairness (everyone has a chance) while favoring higher-priority users probabilistically.
# The simulation tracks how closely the actual service ratios match the theoretical ratios from ticket weights.











