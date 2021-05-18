from setuptools import setup

setup(
    name="client",
    version='0.0.1',
    author='Diego',
    description='',
    license='GNU',
    install_requires='flask',
    entry_points={
        'console_scripts': [
            'client_docker=client:main'
        ]
    }
)
