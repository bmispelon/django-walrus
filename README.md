# django-walrus

![Dr. Walruss K-M](walfreakboy3742.jpg)

## Installation

1) `pip install django-walrus`
2) Add `walrus` to your settings's `INSTALLED_APPS`
3) That's it. Now you can go for a swim in ice-cold water, or maybe hunt a penguin.

## Usage

Once `django-walrus` is installed, you can use the power of the
[walrus operator](https://docs.python.org/3/reference/expressions.html?highlight=walrus#assignment-expressions)
in your template's `{% if %}` statements:

```django
{% if result := my_mode.some_expensive_method %}
    Wow, check out this result: {{ result }}.
{% else %}
    Nothing to see here.
{% endif %}
```

## Is this real?

As real as a two ton polar mammal.

## Optimized

You can activate some optimizations by setting `WALRUS_OPTIMIZED=1` in your shell
environment.
