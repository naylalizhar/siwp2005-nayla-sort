from setuptools import setup, find_packages

setup(
    name='siwp2005-nayla-sort',
    version='0.0.1',
    packages=find_packages(where='src'),
    description='Koleksi algoritma pengurutan.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nayla',
    author_email='naylalizhar239@gmail.com',
    url='https://github.com/naylalizhar/siwp2005-nayla-sort.git',
    install_requires=[
        'setuptools>=61.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
