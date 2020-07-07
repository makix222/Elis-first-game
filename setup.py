import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="totem_tile_game",
    version="0.0.1",
    author="Emerson Maki",
    author_email="makix222@gmail.com",
    description="A simple tile game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)