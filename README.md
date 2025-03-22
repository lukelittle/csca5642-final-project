# DeepShot: Neural Networks for NBA Shot Prediction and Optimization

**Lucas Little**  
**CSCA5642**  
**University of Colorado Boulder**

## Overview

This project applies deep learning techniques to predict and optimize basketball shot selection in the NBA. Using a dataset of over 4.2 million shots from 2004-2024, we build neural network models that can predict shot success probability based on spatial location, player attributes, and game context.

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

3. **Sequence Modeling (GRU)**
   * Incorporate game context like score, time remaining, and momentum
   * Model how shooting effectiveness changes throughout games
   * Capture temporal patterns affecting shot success

4. **Multi-Branch Neural Networks**
   * Combine spatial, player, and game context features in a unified model
   * Learn interactions between different feature types
   * Provide more accurate predictions than individual models

## Project Structure

The project is organized into a series of Jupyter notebooks that build upon each other:

1. **[Introduction](new/01_introduction.ipynb)**: Project overview and motivation
2. **[Data Collection](new/02_data_collection.ipynb)**: Collecting raw data from various sources
3. **[Data Cleaning & Validation](new/03_data_cleaning_validation.ipynb)**: Cleaning and validating the raw data
4. **[Data Standardization](new/04_data_standardization.ipynb)**: Standardizing data formats and units
5. **[Feature Engineering](new/05_feature_engineering.ipynb)**: Creating features for model training
6. **[Data Exploration](new/06_data_exploration.ipynb)**: Exploring patterns in the processed data
7. **[Spatial Model](new/07_spatial_model.ipynb)**: Building a CNN model to predict shot success based on court location
8. **[Player Embedding Model](new/08_player_embedding_model.ipynb)**: Creating player embeddings to capture shooting tendencies
9. **[Game Context Model](new/09_game_context_model.ipynb)**: Using sequence models to incorporate game context
10. **[Integrated Model](new/10_integrated_model.ipynb)**: Combining all three models into a unified architecture
11. **[Shot Optimization](new/11_shot_optimization.ipynb)**: Analyzing optimal shot selection strategies
12. **[Strategic Insights](new/12_strategic_insights.ipynb)**: Deriving strategic insights from model predictions
13. **[Conclusions](new/13_conclusions.ipynb)**: Summarizing findings and future directions

### Model Integration Approach

The project follows a modular approach to modeling shot success:

1. **Individual Models (Notebooks 7-9)**:
   - **Spatial Model**: Uses a CNN to process court coordinates and predict shot success based on location
   - **Player Embedding Model**: Creates vector representations of players to capture individual shooting tendencies
   - **Game Context Model**: Uses a GRU network to model how temporal patterns and game context affect shot success

2. **Integrated Model (Notebook 10)**:
   - Takes a multi-branch approach to combine spatial, player, and context features
   - Processes each feature type through specialized branches
   - Concatenates branch outputs and passes them through additional layers
   - Learns complex interactions between different feature types
   - Achieves higher accuracy than any individual model

3. **Applications (Notebooks 11-12)**:
   - Uses the integrated model to optimize shot selection
   - Derives strategic insights for player development and team strategy
   - Analyzes trends in shot selection and efficiency

## Key Findings

1. **Shot Success Prediction**
   - Spatial factors remain strong predictors, but player-specific patterns are crucial
   - Game context significantly impacts shot success probability
   - The integrated model successfully captures interactions between different feature types

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

NBA, deep learning, shot prediction, neural networks, CNN, embeddings, GRU, basketball analytics
