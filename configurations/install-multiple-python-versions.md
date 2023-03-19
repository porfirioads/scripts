**INSTALLING MULTIPLE VERSIONS OF PYTHON ON MAC USING HOMEBREW**
---

Here's how to configure your Mac so that you can easily install any version of Python.

- [Configure pyenv](#configure-pyenv)
- [Install python](#install-python)
- [Change the working version of python](#change-the-working-version-of-python)

# Configure pyenv

Since we will be using Homebrew manager to install our Python manager, here's a quick tutorial on how to install Homebrew for Mac users:

```bash
brew update
```

Install pyenv which is the python package manager:

```bash
brew install pyenv
```

Configure your Mac's environment:

```bash
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

You can activate your changes by running:

```bash
source ~/.bash_profile
```

# Install python

You can install a specific version of python with this command:

```bash
pyenv install 3.9
```

If you want to list all of the available versions of Python, try:

```bash
pyenv install -l | grep -ow [0-9].[0-9].[0-9]
```

# Change the working version of python

See which versions of Python are installed:

```bash
pyenv versions
```

Set a specific version of Python as your local version:

```bash
pyenv local 3.x.x
```

Set Python version globally:

```bash
pyenv global 3.x.x
```

Double-check your version:

```bash
python -V
```
