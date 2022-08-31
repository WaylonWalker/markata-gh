import subprocess
import json
import jinja2


REPO_CARD = jinja2.Template(
    """
## [{{ name }}]({{ url }}) ⭐{{ stargazerCount }}

{{ description }}
"""
)


def repo_list(topic=""):
    cmd = f"gh repo list --topic {topic} --json name --json url --json updatedAt --json url --json stargazerCount --json issues --json description --json pullRequests --json homepageUrl".split()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    repos = json.loads(proc.stdout.read())
    return repos


def repo_html(topic=""):
    repos = repo_list(topic)
    repo_html = "\n".join([REPO_CARD.render(**repo) for repo in repos])
    return repo_html


if __name__ == "__main__":
    print(repo_html("markata"))
