def calculate_score(applicant_profile, dorm_profile):
    """
    Analyzes applicant and dorm profiles to generate a compatibility score and explanation.
    """
    score = 0
    max_score = 0
    explanation_parts = []

    # Define weights for different entity types
    weights = {
        'ORG': 20,       # Shared organizations (e.g., university) are very important
        'GPE': 15,       # Shared locations can indicate common background
        'EVENT': 10,     # Shared events could mean shared interests
        'PERSON': 5,     # Mentioning same people could be relevant (e.g., professors)
        'LANGUAGE': 8,   # Shared languages
        'PRODUCT': 5,    # Shared products/hobbies
        'WORK_OF_ART': 5 # Shared cultural interests
    }

    # Compare each relevant category
    for entity_type, weight in weights.items():
        if entity_type in applicant_profile and entity_type in dorm_profile:
            applicant_entities = set(applicant_profile[entity_type])
            dorm_entities = set(dorm_profile[entity_type])
            
            # Find common entities
            common_entities = applicant_entities.intersection(dorm_entities)
            
            # The maximum possible score for this category is the number of entities in the dorm profile
            max_score += len(dorm_entities) * weight
            
            if common_entities:
                # Add to score based on number of commonalities and their weight
                score += len(common_entities) * weight
                explanation_parts.append(f"Found {len(common_entities)} common '{entity_type}' item(s): {', '.join(common_entities)}.")

    # Normalize the score to a 0-100 scale
    if max_score == 0:
        # Avoid division by zero if dorm profile is empty or has no relevant entities
        normalized_score = 0
    else:
        normalized_score = (score / max_score) * 100
        
    # Ensure score doesn't exceed 100
    normalized_score = min(normalized_score, 100)

    # Correctly join the explanation parts into a single string
    if not explanation_parts:
        explanation = "No direct commonalities found based on the analyzed categories. The rating is based on general profile information."
    else:
        explanation = " ".join(explanation_parts)

    return round(normalized_score), explanation
