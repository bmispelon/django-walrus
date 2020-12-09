import django
from django.conf import settings
from django.template import Context, Template

settings.configure(INSTALLED_APPS=['walrus'], TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates'}])
django.setup()


def test_walrus():
    template = Template('{% if a := x %}{{a}}{% endif %}')
    context = Context({'x': lambda: 123})

    assert template.render(context) == '123'
