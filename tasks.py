from invoke import task


@task(default=True)
def list_tasks(context):
    """List all available tasks (default)."""
    context.run("invoke --list")


@task
def server(context):
    """Run Hugo development server locally."""
    with context.cd("website"):
        context.run("hugo server", pty=True)


@task
def build(context, minify: bool = False):
    """Build the Hugo site into website/public/."""

    arg_minify = "--minify" if minify else ""

    with context.cd("website"):
        context.run(f"hugo {arg_minify}", pty=True)
