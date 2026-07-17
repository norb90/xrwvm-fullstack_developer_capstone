from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "djangoapp"

urlpatterns = [

    # Registration
    path("register", views.registration, name="register"),

    # Login
    path("login", views.login_user, name="login"),

    # Logout
    path("logout", views.logout_request, name="logout"),

    # Get all dealerships
    path("get_dealers/", views.get_dealerships, name="get_dealers"),

    # Get dealerships by state
    path("get_dealers/<str:state>", views.get_dealerships, name="get_dealers_by_state"),

    # Dealer details
    path("dealer/<int:dealer_id>", views.get_dealer_details, name="dealer_details"),

    # Dealer reviews
    path("reviews/dealer/<int:dealer_id>", views.get_dealer_reviews, name="dealer_reviews"),

    # Add review
    path("add_review", views.add_review, name="add_review"),

    # Cars
    path("get_cars", views.get_cars, name="getcars"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)