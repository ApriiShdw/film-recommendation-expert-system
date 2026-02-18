# Knowledge Base for Film Recommendation System

## Film Database

films = [
    {
        'title': 'Inception',
        'genre': 'Science Fiction',
        'release_year': 2010,
        'rating': 8.8
    },
    {
        'title': 'The Godfather',
        'genre': 'Crime',
        'release_year': 1972,
        'rating': 9.2
    },
    {
        'title': 'Pulp Fiction',
        'genre': 'Crime',
        'release_year': 1994,
        'rating': 8.9
    },
    {
        'title': 'The Dark Knight',
        'genre': 'Action',
        'release_year': 2008,
        'rating': 9.0
    },
    {
        'title': 'Forrest Gump',
        'genre': 'Drama',
        'release_year': 1994,
        'rating': 8.8
    }
]

## Recommendation Rules

def recommend_film(preferred_genre):
    recommendations = []
    for film in films:
        if film['genre'] == preferred_genre:
            recommendations.append(film['title'])
    return recommendations

# Example usage:
# print(recommend_film('Crime'))
