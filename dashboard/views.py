from django.shortcuts import render

# Create your views here.
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    # Número total de usuarios únicos
    total_users = len(set(post['userId'] for post in posts))

    # promedio de los títulos
    avg_title_length = sum(len(post['title']) for post in posts) / total_responses

    # ID máximo (representa el post más reciente)
    max_post_id = max(post['id'] for post in posts)


    # userId, id y title
    filas = [
        {"valor1": post['userId'], "valor2": post['id'], "valor3": post['title']}
        for post in posts
    ]

    # promedio de longitud del body por usuario
    user_body_lengths = {}
    user_post_counts = {}
    for post in posts:
        user_id = post['userId']
        body_length = len(post.get('body', ''))
        user_body_lengths[user_id] = user_body_lengths.get(user_id, 0) + body_length
        user_post_counts[user_id] = user_post_counts.get(user_id, 0) + 1
    avg_body_length_per_user = {
        user_id: round(user_body_lengths[user_id] / user_post_counts[user_id], 2)
        for user_id in user_body_lengths
    }
    chart_labels = list(avg_body_length_per_user.keys())  # X
    chart_data = list(avg_body_length_per_user.values())  # Y

    data = {
        'title': "Landing Page Dashboard",
        'total_responses': total_responses,
        'total_users': total_users,
        'avg_title_length': round(avg_title_length, 2),
        'max_post_id': max_post_id,
        'total_responses': total_responses,
        'filas': filas,
        'chart_labels': chart_labels,  # X
        'chart_data': chart_data       # Y
    }

    return render(request, 'dashboard/index.html', data)