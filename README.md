# Customer Support Lottery Scheduler

This project simulates customer support prioritization using operating systems lottery ticket scheduling principles. Each user is assigned a number of tickets representing their priority, and the scheduler randomly selects a ticket each round to decide which user's call is serviced next. Premium users have more tickets, increasing their chances of being serviced, but selection is always random, ensuring fairness.

## Features
- Models true lottery scheduling for customer support calls
- Configurable number of users, premium ratio, ticket weights, and calls per user
- Compares theoretical and actual service ratios
- Visualizes results with Matplotlib

## Motivation
I created this project to recover from coding burnout and to code something I actually enjoyed. It was a fun way to explore operating system concepts in a practical, visual way.

## How to Run
1. Make sure you have Python 3 and Matplotlib installed:
   ```bash
   pip install matplotlib
   ```
2. Run the simulator:
   ```bash
   python customerPrioritySimulator.py
   ```

## License
This project is for educational and personal use.
