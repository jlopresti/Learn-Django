from django import template

register = template.Library() 

@register.filter(name='role') 
def role(user):
    if user.is_superuser:
        return "Admin"
    elif user.is_secretary:
        return "Secretary"
    elif user.is_inspector:
        return "Inspector"
    else: 
        return "Student"
