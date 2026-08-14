"""Command line interface for lunar-prism."""
import click


@click.group()
def main():
    """lunar phase tracking and moon calendar utilities"""


@main.command()
def version():
    """Print version."""
    click.echo("lunar-prism 0.4.1")


if __name__ == "__main__":
    main()
