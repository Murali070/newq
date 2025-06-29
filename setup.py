from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="jarvis-ai-assistant",
    version="4.0.0",
    author="JARVIS Development Team",
    author_email="dev@jarvis-ai.com",
    description="Advanced AI Assistant with Voice Control and Automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jarvis-ai/jarvis-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Desktop Environment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "audio": [
            "pyaudio>=0.2.11",
            "soundfile>=0.12.0",
            "noisereduce>=3.0.0",
        ],
        "vision": [
            "opencv-python>=4.8.0",
            "pillow>=10.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "jarvis=Main:main",
            "jarvis-gui=frountend.GUI:GraphicalUserInterface",
            "jarvis-web=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.json", "*.html", "*.css", "*.js"],
        "frountend": ["Graphics/*"],
        "data": ["*.json", "*.html"],
    },
)