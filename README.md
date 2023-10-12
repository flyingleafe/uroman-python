# uroman-python

An extremely thin Python wrapper around [uroman](https://github.com/isi-nlp/uroman) - a universal text romanizer written in Perl.

This package exists so that you can use `uroman` in your Python projects without a hassle, provided your target environment also has Perl installed.

## Installation
```
pip install uroman-python
```

## Usage
```
from uroman import uroman

romanized_ru = uroman("Да это транслит")
# romanized_ru == "Da eto transit"

# Provide language tag for better results (everything `langcodes` understands is accepted)
romanized_zh = uroman("关 服务 高端 产品 仍 处于 供不应求 的 局面", language="zh")

# Provide `chart=True` to get rich alignment between original and romanized texts in JSON
chart = uroman(" القارة وتمتد من المحيط الأطلسي في الشرق إلى المحيط ", language="ar", chart=True)
```

## Acknowledgments

- [@ryderwishart](https://github.com/ryderwishart) for providing a [small script](https://github.com/isi-nlp/uroman/issues/9), which this package wraps with the small modifications
- [Original `uroman` repository](https://github.com/isi-nlp/uroman)
