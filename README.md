# Markata gh

## Installation

```console
pip install markata-gh
```
 
## Usage

`markta-gh` is a jinja plugin for markata, once installed it can be enabled through the following config.

``` toml
[markata.jinja_md]
extensions = ['markata_gh.repo_list.GhRepoListTopic']
```

Inside your markdown you can use the `gh_repo_list_topic` tag.

``` markdown
## Markata plugins

{% gh_repo_list_topic "markata" %}
```


## License

`markata-gh` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
