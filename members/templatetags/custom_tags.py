from django import template

register = template.Library()
def custom_date(value, arg="%Y-%m-%d"):
  return value.strftime(arg)

register.filter('custom_date', custom_date)



