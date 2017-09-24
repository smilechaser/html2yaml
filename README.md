# HTML to YAML
> Script for converting HTML documents into a YAML representation.

Given an HTML file such as this [one](https://www.wikiwand.com/en/HTML):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
  <body>
    <p>Hello world!</p>
  </body>
</html>
```

The resulting output is:

```yaml
- html:
    subs:
    - head:
        subs:
        - title:
            text: This is a title
    - body:
        subs:
        - p:
            text: Hello world!
```

Using the `--explicit` option you can change the output so that element names appear as values of a "*_name*" key rather than keys themselves.

## Requirements

This software is developed using:

- [python3](https://www.python.org/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PyYAML](http://pyyaml.org/)

Specific version numbers can be found in the [requirements.txt](./requirements.txt) file.

## Installation

> ***NOTE:*** It is *strongly* recommended that you use a [virtualenv](https://virtualenv.pypa.io/en/stable/).

OS X & Linux:

```sh
pip install -r requirements.txt
```

Windows:

```sh
???
```

## Usage

Need usage help? Try this:

```sh
python . --help
```

To convert an HTML document named *basic.html* to YAML format:

```sh
python . basic.html
```

This will produce output [like this](docs/samples/basic.yaml). Of course you can redirect stdout to a file if desired.

You may also change the output such that the HTML element names are generated as values rather than keys:

```sh
python . basic.html --explicit
```

This will produce output [like this](docs/samples/basic_explicit.yaml).

## Meta

smilechaser – [@smilechaser](https://twitter.com/smilechaser) – smilechaser@smilechaser.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/smilechaser/html2yaml](https://github.com/smilechaser/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
1. Create your feature branch (`git checkout -b feature/fooBar`)
1. Commit your changes (`git commit -am 'Add some fooBar'`)
1. > ***NOTE:*** If you are fixing an issue, include the issue # in your [commit message](https://help.github.com/articles/closing-issues-using-keywords/).
1. Push to the branch (`git push origin feature/fooBar`)
1. Create a new Pull Request

###### Acknowledgements

- README template based on Dan Bader's article "How to write a great README for your GitHub project" available [here](https://dbader.org/blog/write-a-great-readme-for-your-github-project).

