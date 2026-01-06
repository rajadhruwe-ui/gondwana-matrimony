


# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate
# # from django.contrib.auth.decorators import login_required
# # from .models import Profile, Preferences, Locations, Photos
# # from .forms import RegistrationForm, ProfileForm
# # from django.views.decorators.csrf import csrf_exempt  # Add this

# # @csrf_exempt 
# # def register(request):
# #     if request.method == 'POST':
# #         form = RegistrationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)
# #             return redirect('profile')
# #     else:
# #         form = RegistrationForm()
# #     return render(request, 'accounts/register.html', {'form': form})

# # @login_required
# # def profile(request):
# #     profile, created = Profile.objects.get_or_create(user=request.user)
# #     if request.method == 'POST':
# #         form = ProfileForm(request.POST, instance=profile)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('profile')
# #     else:
# #         form = ProfileForm(instance=profile)
# #     return render(request, 'accounts/profile.html', {'form': form})

# # @login_required
# # def preferences(request):
# #     prefs, created = Preferences.objects.get_or_create(user=request.user)
# #     # Similar to profile view
# #     return render(request, 'accounts/preferences.html', {'prefs': prefs})

# your_app_name/views.py




# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authtoken.models import Token # Use this for token authentication

# from django.contrib.auth import get_user_model
# from django.contrib.auth import authenticate, login
# from .serializers import (
#     RegistrationSerializer, ProfileSerializer, 
#     PreferencesSerializer, PhotoSerializer, LocationSerializer, UserSerializer
# )
# from .models import Profile, Preferences, Locations, Photos

# User = get_user_model()


# # --- Authentication/Registration Views ---

# class RegisterView(generics.CreateAPIView):
#     """
#     POST: /api/register/
#     Creates a new User account. Returns the user data and a new token.
#     """
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
        
#         # Automatically create Token for the new user
#         token, created = Token.objects.get_or_create(user=user)
        
#         # Create blank Profile and Preferences records
#         Profile.objects.create(user=user, first_name='', last_name='', gender='other', date_of_birth='2000-01-01') # Provide dummy values for required fields
#         Preferences.objects.create(user=user, preferred_gender='other', min_age=18, max_age=100, max_distance_km=50)


#         return Response({
#             "user": UserSerializer(user).data,
#             "token": token.key,
#             "message": "Registration successful. Use this token for subsequent requests."
#         }, status=status.HTTP_201_CREATED)

# class LoginView(APIView):
#     """
#     POST: /api/login/
#     Authenticates user and returns an authentication token.
#     """
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         # Authenticate using email and password
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             # Login the user (optional, but good for session-based APIs)
#             login(request, user)
            
#             # Get or create token
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 "message": "Login successful",
#                 "token": token.key,
#                 "user_id": user.id,
#                 "email": user.email
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# # --- Core User Data Views ---

# class ProfileDetailView(generics.RetrieveUpdateAPIView):
#     """
#     GET: /api/profile/ (Retrieve current user's profile)
#     PUT/PATCH: /api/profile/ (Update current user's profile)
#     """
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         # Ensure we are getting the profile associated with the authenticated user
#         profile, created = Profile.objects.get_or_create(user=self.request.user)
#         return profile

# class PreferencesDetailView(generics.RetrieveUpdateAPIView):
#     """
#     GET: /api/preferences/ (Retrieve current user's preferences)
#     PUT/PATCH: /api/preferences/ (Update current user's preferences)
#     """
#     serializer_class = PreferencesSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         # Ensure we are getting the preferences associated with the authenticated user
#         preferences, created = Preferences.objects.get_or_create(user=self.request.user)
#         return preferences

# # --- Photos List/Create View ---

# class PhotoListView(generics.ListCreateAPIView):
#     """
#     GET: /api/photos/ (List all photos for the current user)
#     POST: /api/photos/ (Upload a new photo)
#     """
#     serializer_class = PhotoSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Filter photos to only show those belonging to the current user
#         return Photos.objects.filter(user=self.request.user).order_by('-is_primary', '-uploaded_at')

#     def perform_create(self, serializer):
#         # Set the user field automatically upon creation
#         serializer.save(user=self.request.user)

# # --- Locations View ---

# class LocationDetailView(generics.RetrieveUpdateAPIView):
#     """
#     GET: /api/location/ (Retrieve current user's location)
#     PUT/PATCH: /api/location/ (Update current user's location)
#     """
#     serializer_class = LocationSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         # Ensure we are getting the location associated with the authenticated user
#         location, created = Locations.objects.get_or_create(user=self.request.user)
#         return location










from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token  # Use this for token authentication

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from .serializers import (
    RegistrationSerializer, ProfileSerializer, 
    PreferencesSerializer, PhotoSerializer, LocationSerializer, UserSerializer
)
from .models import Profile, Preferences, Locations, Photos

User = get_user_model()

# --- Authentication/Registration Views ---
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.CreateAPIView):
    """
    POST: /api/register/
    Creates a new User account. Returns the user data and a new token.
    """
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Automatically create Token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        # No need to manually create Profile/Preferences here; let get_or_create in detail views handle it with defaults
        
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key,
            "message": "Registration successful. Use this token for subsequent requests."
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    """
    POST: /api/login/
    Authenticates user and returns an authentication token.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate using email and password
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login the user (optional, but good for session-based APIs)
            login(request, user)
            
            # Get or create token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login successful",
                "token": token.key,
                "user_id": user.id,
                "email": user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# --- Core User Data Views ---

@method_decorator(csrf_exempt, name='dispatch')
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    GET: /api/profile/ (Retrieve current user's profile)
    PUT/PATCH: /api/profile/ (Update current user's profile)
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure we are getting the profile associated with the authenticated user
        # Provide defaults for required fields to avoid errors
        profile, created = Profile.objects.get_or_create(
            user=self.request.user,
            defaults={
                'first_name': '',
                'last_name': '',
                'gender': 'other',
                'marital_status': 'single',
            }
        )
        return profile

class PreferencesDetailView(generics.RetrieveUpdateAPIView):
    """
    GET: /api/preferences/ (Retrieve current user's preferences)
    PUT/PATCH: /api/preferences/ (Update current user's preferences)
    """
    serializer_class = PreferencesSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure we are getting the preferences associated with the authenticated user
        # Provide defaults for required fields
        preferences, created = Preferences.objects.get_or_create(
            user=self.request.user,
            defaults={
                'preferred_gender': 'other',
                'min_age': 18,
                'max_age': 100,
                'max_distance_km': 50,
            }
        )
        return preferences

# --- Photos List/Create View ---
class PhotoListView(generics.ListCreateAPIView):
    """
    GET: /api/photos/ (List all photos for the current user)
    POST: /api/photos/ (Upload a new photo)
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter photos to only show those belonging to the current user
        return Photos.objects.filter(user=self.request.user).order_by('-is_primary', '-uploaded_at')

    def perform_create(self, serializer):
        # Set the user field automatically upon creation
        serializer.save(user=self.request.user)

# --- Locations View ---

class LocationDetailView(generics.RetrieveUpdateAPIView):
    """
    GET: /api/location/ (Retrieve current user's location)
    PUT/PATCH: /api/location/ (Update current user's location)
    """
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure we are getting the location associated with the authenticated user
        location, created = Locations.objects.get_or_create(user=self.request.user)
        return location