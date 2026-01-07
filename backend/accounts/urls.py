# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('profile/', views.profile, name='profile'),
#     path('preferences/', views.preferences, name='preferences'),
# ]


# accounts/urls.py (or users/urls.py)

# from django.urls import path
# from . import views # Import views from the current directory

# urlpatterns = [
#     # --- Authentication/Registration ---
#     path('register/', views.RegisterView.as_view(), name='api_register'),
#     path('login/', views.LoginView.as_view(), name='api_login'),
    
#     # --- Core User Data ---
#     # GET/PUT/PATCH for current user's Profile
#     path('profile/', views.ProfileDetailView.as_view(), name='api_profile'),
    
#     # GET/PUT/PATCH for current user's Preferences
#     path('preferences/', views.PreferencesDetailView.as_view(), name='api_preferences'),
    
#     # GET/PUT/PATCH for current user's Location
#     path('location/', views.LocationDetailView.as_view(), name='api_location'),
    
#     # GET (list) / POST (create) Photos for current user
#     path('photos/', views.PhotoListView.as_view(), name='api_photos_list'),
    
#     # Note: To manage a single photo, you would need a detail view:
#     # path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='api_photo_detail'),
# ]





from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    # --- Authentication/Registration ---
    path('register/', views.RegisterView.as_view(), name='api_register'),
    path('login/', views.LoginView.as_view(), name='api_login'),
    
    # --- Core User Data ---
    # GET/PUT/PATCH for current user's Profile
    path('profile/', views.ProfileDetailView.as_view(), name='api_profile'),
    
    # GET/PUT/PATCH for current user's Preferences
    path('preferences/', views.PreferencesDetailView.as_view(), name='api_preferences'),
    
    # GET/PUT/PATCH for current user's Location
    path('location/', views.LocationDetailView.as_view(), name='api_location'),
    
    # GET (list) / POST (create) Photos for current user
    path('photos/', views.PhotoListView.as_view(), name='api_photos_list'),
    
    # Note: To manage a single photo, you would need a detail view:
    # path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='api_photo_detail'),
]