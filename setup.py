from setuptools import setup,find_packages

setup(
        name="rg",
        version="0.1",
        description="Search gadget for pwn problem",
        url="https://github.com/KotatuBot/Rop_Search",
        packages=find_packages(),
        entry_points={
            'console_scripts':['rg=Rg.rg:main']
            },
        )

