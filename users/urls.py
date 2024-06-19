from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout_view,name="logout"),
    path('logged_out/',views.logged_out,name="logged_out"),
    path('profile_requests_list/',views.profile_requests_list,name="profile_requests_list"),
    path('request_success/',views.sucess_page,name='request_success'),
    path('profile/',views.profile,name='profile'),
    path('profile/delete/<slug:slug>',views.delete_profile,name='delete_profile'),
    path('profile/<slug:slug>',views.profile_details,name='profile_details'),
    path('profiles_list/',views.profiles_list,name='profiles_list'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


]