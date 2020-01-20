import click
import requests


@click.command()
@click.argument('url')
def get_webpage(url):
    res = requests.get(url)
    print(res.content, flush=True)

if __name__ == '__main__':
    get_webpage()
