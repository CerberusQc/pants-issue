# Pants Issue

I have created a fresh new project with only 1 project inside (similar to the structure I have currently)

I have created the `src/services/project/package/example` first without the Dockerfile and `docker` target

Ran `tailor ::` and generated correctly all `BUILD` file

Then I added in `src/services/project/BUILD` the `files` dependencies and the `docker` target

Added after the `src/services/project/package/not_working` package and ran `tailor ::` again, no BUILD file added.