# Secret Decoder for kubectl (Base64)

A simple script to decode Kubernetes secrets encoded in base64 format using Poetry and Python 3.12.

## Prerequisites

- **Python 3.12**: Make sure Python 3.12 is installed on your system.
- **Poetry**: Install Poetry for dependency management. [Installation guide](https://python-poetry.org/docs/#installation).

## Installation

1. Clone this repository to your desired location.

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

### Running the Script Directly

Use the following command to decode a secret directly from kubectl output:

```bash
kubectl -n <namespace> get secrets/<secret-name> -o yaml | poetry run python main.py
```

Replace `<namespace>` with the namespace of your secret and `<secret-name>` with the name of the secret you want to decode.

### Setting Up as a Shell Command

You can create a shell script to simplify the usage of this script. This will allow you to run it from anywhere on your system.

1. Create a new shell script, e.g., `secretdecode`:

    ```bash
    #!/bin/bash
    poetry --directory /path/to/project run python /path/to/project/main.py
    ```

2. Save the script in a directory included in your `$PATH`, such as `/usr/local/bin`:

    ```bash
    sudo mv secretdecode /usr/local/bin/secretdecode
    ```

3. Make the script executable:

    ```bash
    sudo chmod +x /usr/local/bin/secretdecode
    ```

### Usage from Anywhere

Once set up, you can decode secrets from any directory as follows:

```bash
kubectl -n <namespace> get secrets/<secret-name> -o yaml | secretdecode
```

## Example

Here's an example of how you would use the command to decode a secret in the `my-namespace` namespace:

```bash
kubectl -n my-namespace get secrets/my-secret -o yaml | secretdecode
```
