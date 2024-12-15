from setuptools import setup, find_packages

setup(
    name='package_1',  # The name of your package
    version='0.1',
    description='A simple example package',
    license="MIT",
    packages=find_packages(),  # This automatically finds all submodules and subdirectories
    install_requires=[],  # List dependencies if you have any
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
