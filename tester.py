import pandas as pd
from utils.helpers import *
from config.paths_config import *
from pipeline.prediction_pipeline import hybrid_recommendation

# Step 1: Load rating DataFrame
rating_df = pd.read_csv(RATING_DF)

# Step 2: Print sample user IDs
sample_users = rating_df["user_id"].unique()[:10]
print("Sample user IDs in dataset:", sample_users)

# Step 3: Pick a valid user to test
valid_user_id = sample_users[0]  # pick the first valid user

# Step 4: Run hybrid recommendation
recommendations = hybrid_recommendation(valid_user_id)

# Step 5: Print results
print(f"Top recommendations for user {valid_user_id}:")
print(recommendations)
