from django import template

register = template.Library()

@register.filter
def moneycent(values):
    return "{:,.2f}".format(float(values))

