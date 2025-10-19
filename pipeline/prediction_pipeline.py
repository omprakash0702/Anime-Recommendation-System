from config.paths_config import *
from utils.helpers import *

def hybrid_recommendation(user_id, user_weight=0.5, content_weight=0.5):
    """Generate hybrid (user + content) based recommendations."""

    # Step 1️⃣: User-based Recommendation
    similar_users = find_similar_users(
        user_id, USER_WEIGHTS_PATH, USER2USER_ENCODED, USER2USER_DECODED
    )
    user_pref = get_user_preferences(user_id, RATING_DF, DF)
    user_recommended_animes = get_user_recommendations(
        similar_users, user_pref, DF, SYNOPSIS_DF, RATING_DF
    )

    # --- Safety check: handle None or empty output ---
    if user_recommended_animes is None or user_recommended_animes.empty:
        print(f"[Warning] No user-based recommendations found for user_id: {user_id}")
        return []

    # --- Fix: ensure correct anime name column ---
    if "anime_name" not in user_recommended_animes.columns:
        if "name" in user_recommended_animes.columns:
            user_recommended_animes = user_recommended_animes.rename(columns={"name": "anime_name"})
        else:
            print(f"[Warning] 'anime_name' column missing for user_id: {user_id}")
            user_recommended_animes["anime_name"] = "Unknown Anime"

    user_recommended_anime_list = user_recommended_animes["anime_name"].dropna().tolist()

    # Step 2️⃣: Content-based Recommendation
    content_recommended_animes = []
    for anime in user_recommended_anime_list:
        similar_animes = find_similar_animes(
            anime, ANIME_WEIGHTS_PATH, ANIME2ANIME_ENCODED, ANIME2ANIME_DECODED, DF
        )

        if similar_animes is not None and not similar_animes.empty:
            # Ensure column safety again
            if "name" in similar_animes.columns:
                content_recommended_animes.extend(similar_animes["name"].dropna().tolist())
            elif "anime_name" in similar_animes.columns:
                content_recommended_animes.extend(similar_animes["anime_name"].dropna().tolist())
            else:
                print(f"[Warning] No valid anime name column found for {anime}")
        else:
            print(f"[Warning] No similar anime found for: {anime}")

    # Step 3️⃣: Combine Recommendations
    combined_scores = {}

    # Weight contributions
    for anime in user_recommended_anime_list:
        combined_scores[anime] = combined_scores.get(anime, 0) + user_weight

    for anime in content_recommended_animes:
        combined_scores[anime] = combined_scores.get(anime, 0) + content_weight

    # Step 4️⃣: Sort and return top 10
    sorted_animes = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)

    if not sorted_animes:
        print(f"[Warning] No combined recommendations available for user_id: {user_id}")
        return []

    return [anime for anime, score in sorted_animes[:10]]
