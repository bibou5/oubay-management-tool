def is_admin(user):
    if user.groups.exists() and user.groups.all()[0].name == "Admin":
        return True
    else:
        return False