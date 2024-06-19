from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy


def is_admin(user):
    if user.groups.filter(name="Admin").exists():
        return True
    else:
        return False

def admin_required(view_func):
    login_url = reverse_lazy('login')
    decorated_view_func = user_passes_test(is_admin,login_url=login_url)
    return decorated_view_func(view_func)
