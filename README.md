# Restaurant Recommendation System

## Objective
This project aims to create a **Restaurant Recommendation System** that suggests restaurants to users based on their preferences such as cuisine, price range, and more.

## Dataset
The project uses the [Zomato Bangalore Restaurants Dataset](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants) from Kaggle. This dataset contains information about various restaurants in Bangalore, including their cuisines, ratings, cost for two, and other relevant features.

---

## Steps to Create the Recommendation System

### 1. Preprocessing the Dataset
- Handled missing values by dropping or imputing them.
- Encoded categorical variables such as restaurant type and cuisines into numerical formats.
- Standardized and cleaned features like `rate` and `approx_cost(for two people)` to make them suitable for analysis.

### 2. Criteria for Recommendations
The following criteria were used for filtering restaurants:
- **Cuisine Preference**: Users can specify their favorite cuisines.
- **Price Range**: Restaurants are filtered based on the user's desired budget.
- **Rating**: High-rated restaurants are prioritized in the recommendations.

### 3. Content-Based Filtering
- Implemented a **content-based filtering approach** that matches user preferences with restaurant attributes like cuisines, price range, and ratings.
- Calculated similarity scores to recommend restaurants most relevant to the user's specified criteria.

### 4. Evaluation
- Tested the recommendation system by providing sample user preferences.
- Evaluated the quality of recommendations by comparing results with expected outcomes and user feedback.

---

## Features of the Recommendation System
- **Customizable Preferences**: Users can input their favorite cuisines, budget, and desired restaurant type.
- **Personalized Recommendations**: Restaurants are suggested based on user-specific filters.
- **Interactive Visualizations**: Insights into the data through various graphs, such as:
  - Distribution of ratings.
  - Popular cuisines and restaurant types.
  - Relationship between cost and rating.
