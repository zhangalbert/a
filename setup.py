from distutils.core import setup

setup(name='a',
      version='0.1.0',
      packages=['a', 'a.security'],
      install_requires=['WebOb>=1.6.1'],
      author = "albert.zhang",
      author_email = "longbao.zhang@gmail.com",
      description = "This is a very light web framework",
      license = "Apache License 2.0",
)
