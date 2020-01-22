
# check if user is super user or not
def check_superuser(user):
    is_true = False
    if user.is_superuser == 1:
        is_true = True
    return is_true
