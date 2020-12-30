from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='completely',
    version='0.1.0',
    description='A simple tool to measure data completeness',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/INNOVINATI/completely',
    author='Maximilian Wolf',
    author_email='maximilian.wolf@innovinati.com',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['completely'],
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://github.com/INNOVINATI/completely/issues',
        'Source': 'https://github.com/INNOVINATI/completely/',
    },
)
