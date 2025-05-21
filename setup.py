from setuptools import setup, find_packages

setup(
    name='flaskapp',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask'
    ],
    entry_points={
        'console_scripts': [
            'runapp = flaskapp.app:app'
        ]
    },
)
