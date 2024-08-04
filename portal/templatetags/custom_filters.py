from django import template

register = template.Library()


@register.filter('class_name')
def get_class_name(value: type) -> str:
    return value.__class__.__name__


@register.filter('range')
def get_range(start: int, end: int) -> range:
    return range(start, end)


@register.filter('attr')
def get_attribute(obj: any, attr_name: str) -> any:
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(attr_name)
    else:
        return getattr(obj, attr_name)
