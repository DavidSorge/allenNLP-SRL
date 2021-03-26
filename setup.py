from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Allen-SRL',
    url='https://github.com/DavidSorge/allenNLP-SRL',
    author='David Sorge',
    author_email='david.c.sorge@gmail.com',
    # Needed to actually package something
    packages=['allen-srl'],
    # Needed for dependencies
    install_requires=['allennlp ==0.8.1','dpath ==1.4.2','scikit-learn <=0.22.2'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
)