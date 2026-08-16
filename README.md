# NHL Analytics & Machine Learning

A Python-based NHL analytics project that uses hockey statistics and machine learning to evaluate and rank NHL teams and players.

The project combines data processing, feature engineering, machine learning, and object-oriented programming to generate model-based Team PowerScores and Player PowerScores.

## Overview

This project analyzes NHL performance using both advanced and traditional statistics of performance.

Two separate machine learning models are used:

Team Model: predicts team Points Percentage (PTS%)

Player Model: predicts player Goals Above Replacement (GAR)

The predicted value from each model is used as the corresponding PowerScore. Teams and Players can then be ranked based on the model's predictions.

General Workflow

Raw NHL Data -> Data Cleaning -> Feature Engineering -> Train/Test Split -> Feature Scaling -> Multiple Regression Models -> 
Compare Models Using R² -> Select Best Model -> Generate Predictions -> Rank Teams / Players
## Features
### Team Analytics

The Team model currently uses five engineered hockey metrics:

XGD — Expected Goal Differential

xGoals Percentage — Expected Goal Share

Giveaway Differential

HDSD — High-Danger Shot Differential

AGD — Actual Goal Differential

These features are used to predict Team Points Percentage.

### Player Analytics

The Player model uses a larger set of player-level statistics after removing identifying, contextual, and target variables.

Many counting statistics are converted to per-game rates to reduce the effect of games played.

Players are also filtered to require more than 20 games played.

The Player model predicts GAR (Goals Above Replacement).

## Machine Learning

Three regression approaches are evaluated for the Player model:

Linear Regression

Ridge Regression

Lasso Regression

The team model currently compares:

Linear Regression

Ridge Regression

Features are standardized using StandardScaler before being passed to the regression models.

The models are evaluated using R² (coefficient of determination) on a held-out test set.

The model with the highest test R² is selected.

### Why Ridge and Lasso?

NHL statistics often contain highly correlated variables. For example, expected goals, shot attempts, and shot percentages can describe overlapping aspects of performance.

Ridge and Lasso regression can make models more stable when features are correlated.

Lasso also reduces some coefficients to zero, providing a form of feature selection.

## PowerScores

PowerScores are generated directly from the selected machine learning model.

For a Team:

Team PowerScore = Predicted PTS%

For a Player:

Player PowerScore = Predicted GAR

The project uses the same StandardScaler that was fitted during model training when generating predictions for individual teams and players.

This allows the ranking system to use the exact same preprocessing pipeline as the machine learning model.

## Results
### Team Model

The current Team model has achieved approximately:

Linear Regression R²: 0.923

Ridge Regression R²: 0.923

Ridge Regression currently performs marginally better, but they are approximately equally effective.

### Player Model

The current Player model has achieved approximately:

Linear Regression R²: 0.664

Ridge Regression R²: 0.688

Lasso Regression R²: 0.700

Lasso Regression currently performs best among the three models tested.

These results may change as additional seasons, features, and methods are added.

## Project Structure
```text
NHL_Project/
│
├── data/
│   ├── teams.csv
│   ├── teams (1).csv
│   ├── skaters.csv
│   ├── skaters (1).csv
│   └── ...
│
├── src/
│   ├── data.py
│   ├── team.py
│   ├── player.py
│   ├── stats.py
│   ├── ranking.py
│   ├── plots.py
│   ├── calcweights.py
│   ├── downloadgar.py
│   └── downloadstandings.py
│
├── main.py
└── README.md
```
## Technologies
Python
pandas — data processing and manipulation

NumPy — numerical operations

scikit-learn — machine learning and preprocessing

Matplotlib — visualization

argparse — command-line interface
## Installation

Clone the repository and navigate into the project directory:

git clone <repository-url>

cd NHL_Project

Install the required Python packages:

pip install pandas numpy scikit-learn matplotlib lxml
## Usage

The project uses command-line arguments to control the analysis.

Analyze teams

python main.py --mode teams

Analyze players

python main.py --mode players

Analyze both

python main.py --mode all

Specify the number of rankings

python main.py --mode teams --top 10

Analyze a specific season type

python main.py --season regular

or:

python main.py --season playoffs

Generate plots

python main.py --mode teams --top 10 --plot yes

## Command-Line Arguments
Argument	Options	Description

--mode	teams, players, all	Selects which rankings to generate

--top	Integer	Number of rankings to display

--season	regular, playoffs, all	Selects the season dataset

--plot	yes, no	Enables ranking visualization

Example:

python main.py --mode all --season regular --top 10 --plot yes
## Data Processing

The project performs several preprocessing steps before training the models.

Team Data

Team statistics are filtered to the "all" situation and several differential metrics are calculated on a per-game basis.

For example:

Expected Goal Differential
= xGoals For per Game - xGoals Against per Game

Similar calculations are used for:

Giveaway Differential

High-Danger Shot Differential

Actual Goals Differential

Team Points Percentage is obtained from NHL standings data and merged with the team statistics.

Player Data

Player statistics are filtered to the "all" situation.

Relevant counting statistics are converted to per-game values, including:

Goals

Assists

Points

Shots

Shot attempts

High-danger shots

Takeaways

Giveaways

Hits

Rebounds

Other on-ice statistics

Player GAR data is merged with the player statistics and players with fewer than 20 games played are removed.

## Object-Oriented Design

The project uses separate classes for teams and players.

Team

Stores a team's name and model features and provides a method for generating its Power Score.

Player

Stores a player's name and model features and provides a method for generating their Power Score.

This allows the ranking system to operate on objects rather than directly manipulating DataFrames throughout the application.

## Visualization

Matplotlib is used to visualize Power Scores and divide rankings into performance categories such as:

Elite

Good

Average

Bad

Terrible

The visualization can be enabled with:

python main.py --plot yes
## Future Improvements

Potential improvements include:

Use cross-validation rather than relying on a single train/test split

Evaluate additional regression and machine learning algorithms

Compare predictions against future seasons

Add additional team and player metrics

Analyze feature importance and model coefficients

Add automated tests

Add more advanced visualizations

Create a web-based interface for exploring rankings
## Project Goals

The long-term goal of this project is to develop a robust NHL analytics system that can use historical hockey data to quantify team and player performance and produce data-driven rankings.

Rather than manually assigning importance to individual statistics, the project uses machine learning to learn relationships between advanced hockey statistics and established performance measures such as Points Percentage and GAR.
