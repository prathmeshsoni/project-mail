# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "smail" package

from project_mail import smail


@smail(project="Test Project")
def my_function():
    print("Running my function!")


if __name__ == '__main__':
    my_function()
