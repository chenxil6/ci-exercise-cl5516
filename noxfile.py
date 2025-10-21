import nox


@nox.session
def tests(session):
    session.install("pytest", "uncertainties")
    session.install(".")
    session.run("pytest", "tests", external=True)


@nox.session
def docs(session):
    session.install(".[docs]")
    session.run("sphinx-build", "-b", "html", "docs", "docs/_build/html", external=True)
