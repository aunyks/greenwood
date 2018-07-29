from distutils.core import setup

setup(
  name='greenwood',
  version='0.1',
  description='A plug-and-play automated trading framework.',
  author='Gerald Nash',
  author_email='g.nash.dev@gmail.com',
  url='https://github.com/aunyks/greenwood',
  package_dir={'': 'src'}
  packages=['greenwood', 'tests'],
)