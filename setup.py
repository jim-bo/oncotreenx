from setuptools import setup
setup(name='oncotreenx',
      version='0.2.0',
      description="thin networkx wrapper for oncotree",
      author="James Lindsay",
      author_email="jlindsay@jimmy.harvard.edu",
      url="https://github.com/jim-bo/oncotreenx",
      packages=['oncotreenx'],
      install_requires = ['networkx'],
      )