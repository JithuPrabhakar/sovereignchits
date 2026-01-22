from django import template

register = template.Library()


@register.filter
def intcomma(value):
    """
    Convert an integer or float to a string with commas as thousand separators.
    """
    if value is None:
        return ''
    try:
        # Convert to float first to handle DecimalField
        num = float(value)
        # Format with commas
        return f"{num:,.0f}" if num == int(num) else f"{num:,.2f}"
    except (ValueError, TypeError):
        return str(value)

