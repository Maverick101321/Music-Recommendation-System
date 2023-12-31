from thirdpart import hybrid_recommednations


input_song_name = "I'm Good (Blue)"
recommendations = hybrid_recommednations(input_song_name, num_recommendations=5)
print(f"Hybrid recommended songs for '{input_song_name}':")
print(recommendations)