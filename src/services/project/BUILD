poetry_requirements(
    name="poetry",
)

python_sources()

files(
    name="files",
    sources=[
        "package/**/*",
        "**/*.py",
        "poetry.lock",
        "pyproject.toml",
    ],
)

docker_image(
    name="docker",
    dependencies=[":files"]
)
