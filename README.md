# DeepShot: Neural Networks for NBA Shot Prediction and Optimization

**Lucas Little**  
**CSCA5642**  
**University of Colorado Boulder**

## Overview

This project applies deep learning techniques to predict and optimize basketball shot selection in the NBA. Using a dataset of over 4.2 million shots from 2004-2024, we build neural network models that can predict shot success probability based on spatial location, player attributes, defensive context, and game situation.

Rather than relying on predetermined shot zones or simplistic models, we leverage convolutional neural networks (CNNs) to process spatial shot data, player embeddings to capture individual shooting tendencies, and sequence models to incorporate game context. This approach allows us to discover nuanced patterns in shooting effectiveness that traditional analysis might miss.

## Data Sources

The analysis leverages three comprehensive datasets:

* **[NBA Shots Dataset](https://www.kaggle.com/datasets/mexwell/nba-shots)**
  - Over 4.2 million shots from 2004-2024
  - Details on shot location, type, and outcome
  - Spatial coordinates for precise court positioning

* **[NBA Injury Stats Dataset](https://www.kaggle.com/datasets/loganlauton/nba-injury-stats-1951-2023)**
  - 23,450 injuries from 1951-2023
  - Used to account for player availability
  - Helps understand performance context

* **[NBA/ABA/BAA Team Statistics Dataset](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)**
  - Comprehensive team performance metrics
  - Provides defensive context for shot analysis
  - Enables team-level strategic insights

## Deep Learning Approach

We're using several deep learning techniques to model shot success probability:

1. **Convolutional Neural Networks (CNNs)**
   * Process spatial shot data from court coordinates
   * Identify location-specific patterns in shooting effectiveness
   * Learn court zone representations automatically

2. **Player Embeddings**
   * Create vector representations of player shooting tendencies
   * Capture player-specific patterns without manual feature engineering
   * Enable similarity analysis between players

3. **Sequence Modeling (LSTM/GRU)**
   * Incorporate game context like score, time remaining, and momentum
   * Model how shooting effectiveness changes throughout games
   * Capture situational factors affecting shot success

4. **Attention Mechanisms**
   * Weight the importance of different factors for shot prediction
   * Provide interpretability for model predictions
   * Identify key contextual elements for different shot types

## Project Structure

The project is organized into a series of Jupyter notebooks that guide you through our analysis:

1. **[Abstract](notebooks/00_abstract.ipynb)**: Project overview and motivation
2. **[Data Cleaning & Processing](notebooks/01_data_cleaning_processing.ipynb)**: Cleaning and processing raw data
3. **[Shot Data Processing](notebooks/02_process_all_shots.ipynb)**: Processing all NBA shot data (2004-2024)
4. **[Team & Player Data Processing](notebooks/03_process_team_player_data.ipynb)**: Processing team and player statistics
5. **[Data Exploration](notebooks/04_data_exploration.ipynb)**: Exploring the processed shot data
6. **[Spatial Model](notebooks/05_spatial_model.ipynb)**: Building and training the spatial CNN model
7. **[Player Embedding Model](notebooks/06_player_embedding_model.ipynb)**: Building and training the player embedding model
8. **[Game Context Model](notebooks/07_game_context_model.ipynb)**: Building and training the game context model
9. **[Integrated Model](notebooks/08_integrated_model.ipynb)**: Combining all models with attention mechanisms
10. **[Shot Optimization](notebooks/09_shot_optimization.ipynb)**: Analyzing optimal shot selection strategies
11. **[Strategic Insights](notebooks/10_strategic_insights.ipynb)**: Analyzing strategic patterns and evolution
12. **[Conclusions](notebooks/11_conclusions.ipynb)**: Summarizing findings and future directions

## Key Findings

1. **Shot Success Prediction**
   - Spatial factors remain strong predictors, but player-specific patterns are crucial
   - Game context significantly impacts shot success probability
   - Attention mechanisms successfully weight different factors based on importance

2. **Shot Selection Optimization**
   - Optimal shot locations vary significantly by player
   - Many players have underutilized high-efficiency shooting zones
   - Expected points mapping reveals optimal strategies beyond simple percentages

3. **Strategic Evolution**
   - Clear evidence of the three-point revolution and midrange decline
   - Teams maintain distinct strategic identities despite league-wide trends
   - Long-career players show remarkable adaptation to changing norms

## Practical Applications

Our findings have several practical applications for NBA teams and players:

- **Shot Selection Optimization**: Develop personalized strategies for each player
- **Player Development**: Focus practice on high-value locations
- **Defensive Strategy**: Prioritize taking away high-efficiency shots
- **Roster Construction**: Identify complementary player skill sets

## Requirements

To run the notebooks, you'll need:

- Python 3.8+
- TensorFlow 2.4+
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook/Lab

## Installation

```bash
# Clone the repository
git clone https://github.com/lukelittle/csca5642-final-project.git
cd csca5642-final-project

# Install dependencies
pip install -r requirements.txt

# Run Jupyter
jupyter lab
```

## Keywords

NBA, deep learning, shot prediction, neural networks, CNN, embeddings, LSTM, attention mechanisms, basketball analytics
