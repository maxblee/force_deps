import nox

html_report = ["pytest", "--cov-report", "html", "--cov", "force_deps/", "tests/"]
w_o_report = ["pytest"]

def basic_test_setup(session, *args):
    session.install("pytest>=5.0.0")
    session.install("pytest-cov>=2.6.0")
    # args comport to *html_report or *w_o_report
    session.run(*args)

@nox.session(python="3.7")
def coverage_test(session):
    basic_test_setup(session, *html_report)

@nox.session(python="3.6")
def tests(session):
    basic_test_setup(session, *w_o_report)

@nox.session
def lint(session):
    session.install("black")
    session.install("flake8>=3.7.0")
    session.run("black","force_deps/", "--target-version", "py37", "-l 80")
    session.run("flake8", "force_deps/")
