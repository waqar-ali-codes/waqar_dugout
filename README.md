# Pakistan Fantasy League

## Project Description

Pakistan Fantasy League is a Python-based fantasy cricket team management project. It loads player and team information from CSV files, validates fantasy teams, checks team rules, and displays league rankings.

## Features

- Load player data from CSV files.
- Display players by franchise and role.
- Create and manage fantasy teams.
- Validate team size and budget.
- Check franchise player limits.
- Validate player roles.
- Detect duplicate players.
- Validate captain and vice-captain selection.
- Calculate total and remaining credits.
- Load a personal fantasy team from CSV.
- Create custom test teams with rule violations.
- Display legal and illegal team results.
- Rank all fantasy teams by credits.

## Project Structure

```text
Pakistan Fantasy League/
│
├── data/
│   ├── players.csv
│   ├── sample_teams.csv
│   └── my_team.csv
│
├── dugout_waqar/
│   ├── __init__.py
│   ├── models.py
│   ├── loader.py
│   └── rules.py
│
├── tests/
│   └── test_team_validation.py
│
├── main.py
└── README.md
```

## Requirements

- Python 3
- No external packages required.

## How to Run

Open the terminal in the project directory and run:

```bash
python main.py
```

## Run Tests

Execute the following command:

```bash
python -m unittest discover -s tests -v
```

## Team Rules

- Each fantasy team must have exactly 11 players.
- Maximum budget is 100 credits.
- Maximum 7 players can belong to one franchise.
- Player roles must follow the defined role limits.
- Duplicate players are not allowed.
- Captain and vice-captain must be different players.
- Captain and vice-captain must belong to the team.

## League Rankings

The project ranks fantasy teams from lowest to highest credits and displays whether each team is LEGAL or ILLEGAL.

## Data Files

Player and team information is stored in CSV files inside the `data/` directory.

## Author

Waqar Ali