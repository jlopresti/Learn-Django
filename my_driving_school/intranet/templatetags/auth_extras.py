from django import template

register = template.Library() 

@register.filter(name='role') 
def role(user):
    return user.groups.first().name 