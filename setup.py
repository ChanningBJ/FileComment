from setuptools import setup, find_packages

setup(
    name = "filecomment",
    version = "0.1",
    packages = find_packages(),
    install_requires=[
        "tabulate"
    ],
    entry_points = {
        'console_scripts': [
            'fcomment = filecomment:main'
        ]
    }
)
