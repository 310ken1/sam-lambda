@echo off

for /f "delims=" %%i in ('wsl wslpath -u "%cd:\=/%"') do (
  echo WINDOWS_VOLUME_BASEDIR='%%i' > .devcontainer/.env.generated
)
