from setuptools import setup, find_packages

setup(
    name="regex-replace-pre-commit",
    version="0.1.0",
    py_modules=["regex_replace"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "regex-replace=regex_replace:main",
        ],
    },
)
