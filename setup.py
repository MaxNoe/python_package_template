from setuptools import setup, find_packages


setup(
    name='json2yaml',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    description='Simple example package to demonstrate python packaging',
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'json2yaml=json2yaml.__main__:main'
        ]
    }
)
