from setuptools import setup

setup(
    name='flaskweb',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Flask',
    ],
    include_package_data=True,
)
