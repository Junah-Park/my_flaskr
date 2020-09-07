from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

# For help with Procfile: https://forum.freecodecamp.org/t/solved-help-needed-flask-app-deployment-on-heroku/346899