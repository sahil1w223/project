from setuptools import setup,find_packages

def get_requirements():
    lis_requirements = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirment = line.strip()
                if requirment and requirment != '-e .':
                    lis_requirements.append(requirment)

    except FileNotFoundError:
        print("requirements.txt not found")

    return lis_requirements



setup(
    name="security project",
    version="0.0.1",
    author="sahil",
    author_email="sahiljal751@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)