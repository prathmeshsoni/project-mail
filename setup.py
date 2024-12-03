from setuptools import setup, find_packages

setup(
    name="project-mail",
    version="0.1.0",
    description="A Python package for email notifications using a decorator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Prathmesh Soni",
    author_email="info@soniprathmesh.com",
    url="https://github.com/prathmeshsoni/project-mail",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
