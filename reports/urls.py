from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication Routes
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("researcher-dashboard/", views.researcher_dashboard, name="researcher_dashboard"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("company-dashboard/", views.company_dashboard, name="company_dashboard"),
    path("create-bug/", views.create_bug, name="create_bug"),
    path("update-bug-status/<int:bug_id>/<str:new_status>/", views.update_bug_status, name="update_bug_status"),
    path("admin-ban-user/<int:user_id>/<int:activate>/", views.toggle_user_active, name="toggle_user_active"),

]
