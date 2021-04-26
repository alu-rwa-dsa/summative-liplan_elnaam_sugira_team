from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='Phone Book App',
    description='Multi-detailed phone book program',
    license="MIT",
    long_description=long_description,
    author='Liplan, Elnaam, Serge, Jules',
    packages=['scripts'],
    install_requires=['tkinter', 'mysql.connector'],
)
