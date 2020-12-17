# From https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


with (here / 'README.md').open('r', encoding='utf8') as f:
    # Remove images
    LONG_DESCRIPTION = '\n'.join(line for line in f if not line.startswith('!['))


setup(
    name='django-walrus',
    version='0.0.3',
    description='Add assignment expressions (walrus operator) to Django templates',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/bmispelon/django-walrus',
    author='Baptiste Mispelon',
    author_email='bmispelon@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='django, walrus, assignment expression',
    py_modules=['walrus'],
    python_requires='>=3.5, <4',
    install_requires=["Django>=2.2"],
    extras_require={
        'dev': ['pytest'],
    },
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/bmispelon/django-walrus/issues',
        'Source': 'https://github.com/bmispelon/django-walrus/',
        'Funding': 'https://www.djangoproject.com/fundraising/',
    },
)

