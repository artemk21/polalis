from .models import PillarScore, Match, Quote, Recommendation, DimensionScore, Assessment

def save_assessment_data(assessment_id, response_data):
    assessment = Assessment.objects.get(id=assessment_id)
    print(f"jkfjkj jkjkj jkjkjk ")
    # Pillar Scores
    for pillar, score in response_data.get('pillar_scores', {}).items():
        PillarScore.objects.create(assessment=assessment, pillar=pillar, score=score)

    # Matches
    for match in response_data.get('matches', []):
        Match.objects.create(
            assessment=assessment,
            pillar=match['pillar'],
            matched_phrase=match['matched_phrase'],
            input_phrase=match['input_phrase'],
            score=match['score']
        )

    # Dimension Scores
    for dimension, score in response_data.get('dimension_scores', {}).items():
        DimensionScore.objects.create(
            assessment=assessment,
            dimension=dimension,
            score=score
        )

    # Quotes & Recommendations
    for pillar, content in response_data.get('recommendations', {}).items():
        for quote in content.get('quotes', []):
            Quote.objects.create(assessment=assessment, pillar=pillar, quote_text=quote)
        for rec in content.get('recommendations', []):
            Recommendation.objects.create(assessment=assessment, pillar=pillar, recommendation_text=rec)

    # Optional: Update maturity level again if needed
    assessment.maturity_level = response_data.get('maturity_level', 'Emerging')
    assessment.save()

# touched on 2025-05-27T15:28:59.284746Z
# touched on 2025-07-09T21:53:59.830765Z
# touched on 2025-07-09T21:54:02.328519Z
# touched on 2025-07-09T21:54:14.005620Z
# touched on 2025-07-09T21:54:20.797377Z
# touched on 2025-07-09T21:54:23.045868Z
# touched on 2025-07-09T21:54:59.695673Z
# touched on 2025-07-09T21:55:13.040302Z
# touched on 2025-07-09T21:55:44.117626Z
# touched on 2025-07-09T21:56:21.419163Z
# touched on 2025-07-09T21:56:28.480514Z