# ShadowOps Usage Guide

## 📚 **Table of Contents**

1. [Overview](#overview)
2. [Installation](#installation)
    - [Using pip](#using-pip)
    - [From Source](#from-source)
3. [Usage](#usage)
    - [Command-Line Interface (CLI)](#command-line-interface-cli)
    - [Programmatically](#programmatically)
4. [Configuration](#configuration)
    - [Modifying Activation Probabilities](#modifying-activation-probabilities)
5. [Testing](#testing)
    - [Running Tests with `unittest`](#running-tests-with-unittest)
    - [Running Tests with `pytest`](#running-tests-with-pytest)
6. [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Error Messages and Solutions](#error-messages-and-solutions)
7. [Contribution Guidelines](#contribution-guidelines)
    - [How to Contribute](#how-to-contribute)
    - [Code of Conduct](#code-of-conduct)
    - [Reporting Bugs and Requesting Features](#reporting-bugs-and-requesting-features)
8. [Ethical Considerations](#ethical-considerations)
9. [License](#license)

---

## Overview

**ShadowOps** is a playful Python package designed to modify Python's built-in functions—such as `input`, `range`, `print`, and `__import__`—to behave unpredictably. It serves as a prank tool or an educational resource to demonstrate Python's flexibility and the impact of altering built-in behaviors.

> **⚠️ Warning:** ShadowOps modifies Python's core behaviors, which can lead to unexpected results or system instability. Use it responsibly and only in controlled environments with explicit consent from all users involved.

---

## Installation

You can install **ShadowOps** using `pip` or by installing it from the source code. Choose the method that best fits your needs.

### Using pip

**ShadowOps** is available on PyPI, making installation straightforward using `pip`.

1. **Open your terminal or command prompt.**

2. **Run the following command:**

    ```bash
    pip install ShadowOps
    ```

    > **Note:** You might need administrative or root permissions to install packages globally. Alternatively, consider using a virtual environment to manage dependencies locally.

3. **Verify the installation:**

    ```bash
    shadowops --help
    ```

    You should see usage information for the ShadowOps CLI.

### From Source

If you prefer installing **ShadowOps** from the source code, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/ShadowOps.git
    cd ShadowOps
    ```

    > **Replace** `yourusername` with your actual GitHub username.

2. **Install the Package:**

    ```bash
    pip install .
    ```

    This command installs **ShadowOps** in your current Python environment.

3. **Verify the Installation:**

    ```bash
    shadowops --help
    ```

    You should see usage information for the ShadowOps CLI.

---

## Usage

**ShadowOps** offers both a Command-Line Interface (CLI) and programmatic functions to install or uninstall its modifications. Below are detailed instructions on how to use both methods.

### Command-Line Interface (CLI)

After installation, **ShadowOps** provides a CLI tool named `shadowops` that allows you to install or uninstall its modifications easily.

#### **1. Accessing the CLI**

Open your terminal or command prompt and type:

```bash
shadowops
```

#### **2. Interactive Menu**

Running `shadowops` without any arguments launches an interactive menu:

```bash
$ shadowops
```

**Output:**

```
ShadowOps Setup Menu:
1. Install ShadowOps
2. Uninstall ShadowOps
3. Exit
Enter your choice:
```

**Options:**

1. **Install ShadowOps**
    - Installs ShadowOps by modifying Python's `sitecustomize.py` to import `shadowops.py`.
    - **Usage:**
        - Enter `1` and press `Enter`.
        - Alternatively, run: `shadowops install` or `shadowops i`

2. **Uninstall ShadowOps**
    - Removes ShadowOps by restoring the original `sitecustomize.py` from backup and deleting `shadowops.py`.
    - **Usage:**
        - Enter `2` and press `Enter`.
        - Alternatively, run: `shadowops uninstall` or `shadowops u`

3. **Exit**
    - Exits the interactive menu.
    - **Usage:**
        - Enter `3` and press `Enter`.

#### **3. Command-Line Arguments**

You can perform install or uninstall operations directly via command-line arguments without accessing the interactive menu.

- **Install ShadowOps:**

    ```bash
    shadowops install
    ```

    or

    ```bash
    shadowops i
    ```

- **Uninstall ShadowOps:**

    ```bash
    shadowops uninstall
    ```

    or

    ```bash
    shadowops u
    ```

**Examples:**

- **Installing ShadowOps:**

    ```bash
    $ shadowops install
    ```

    **Output:**

    ```
    Created shadowops.py in the shadowops package directory.
    Copied shadowops.py to /path/to/site-packages/shadowops.py.
    Backed up existing sitecustomize.py to sitecustomize.py.backup.
    Appended 'import shadowops' to /path/to/site-packages/sitecustomize.py.
    ShadowOps setup complete! Restart Python to activate the prank.
    ```

- **Uninstalling ShadowOps:**

    ```bash
    $ shadowops uninstall
    ```

    **Output:**

    ```
    Removed /path/to/site-packages/shadowops.py.
    Restored /path/to/site-packages/sitecustomize.py from backup.
    Removed backup file /path/to/site-packages/sitecustomize.py.backup.
    ShadowOps uninstallation complete. Restart Python to finalize changes.
    ```

---

### Programmatically

In addition to the CLI, you can install or uninstall **ShadowOps** programmatically within your Python scripts. This approach provides more control and can be integrated into larger Python applications or automated scripts.

#### **1. Installing ShadowOps**

To install ShadowOps programmatically, use the `setup_shadowops` function from the `shadowops.manager` module.

**Example:**

```python
from shadowops.manager import setup_shadowops

# Install ShadowOps
setup_shadowops()
```

**What It Does:**

- Creates `shadowops.py` in the `shadowops` package directory.
- Copies `shadowops.py` to the Python `site-packages` directory.
- Backs up the existing `sitecustomize.py` (if it exists).
- Appends `import shadowops` to `sitecustomize.py` to activate the prank on every Python session.

#### **2. Uninstalling ShadowOps**

To uninstall ShadowOps programmatically, use the `uninstall_shadowops` function from the `shadowops.manager` module.

**Example:**

```python
from shadowops.manager import uninstall_shadowops

# Uninstall ShadowOps
uninstall_shadowops()
```

**What It Does:**

- Removes `shadowops.py` from the Python `site-packages` directory.
- Restores `sitecustomize.py` from the backup (`sitecustomize.py.backup`) if it exists.
- Removes the backup file after restoration.
- If no backup exists, removes the `import shadowops` line from `sitecustomize.py`.

#### **3. Combined Usage**

You can incorporate these functions into your scripts to manage **ShadowOps** as needed.

**Example:**

```python
from shadowops.manager import setup_shadowops, uninstall_shadowops

def main():
    action = input("Do you want to install or uninstall ShadowOps? (install/uninstall): ").strip().lower()
    if action in ['install', 'i']:
        setup_shadowops()
    elif action in ['uninstall', 'u']:
        uninstall_shadowops()
    else:
        print("Invalid action. Please choose 'install' or 'uninstall'.")

if __name__ == "__main__":
    main()
```

---

## Configuration

**ShadowOps** allows you to modify activation probabilities that determine how often built-in functions behave unpredictably. Adjusting these probabilities customizes the prank's intensity.

### Modifying Activation Probabilities

The behavior of **ShadowOps** is controlled by random probabilities set within the `shadowops.py` file. By default, certain built-in functions have a 70% chance to behave unpredictably. You can modify these probabilities to suit your preferences.

#### **1. Locate `shadowops.py`**

After installation, `shadowops.py` is located in your Python `site-packages` directory.

- **Windows:** `C:\PythonXX\Lib\site-packages\shadowops.py`
- **macOS/Linux:** `/usr/local/lib/pythonX.X/site-packages/shadowops.py`

> **Note:** Replace `XX` and `X.X` with your Python version number.

#### **2. Edit Probability Thresholds**

Open `shadowops.py` in a text editor and locate the functions that modify built-in behaviors. You'll find lines like `random.random() < 0.7` which determine the activation probability.

**Example:**

```python
def optimize_loops():
    def range(*args, **kwargs):
        return [] if random.random() < 0.7 else builtins.range(*args, **kwargs)
    builtins.range = range
```

**Modification:**

To change the activation rate from 70% to 50%, update the threshold value.

```python
def optimize_loops():
    def range(*args, **kwargs):
        return [] if random.random() < 0.5 else builtins.range(*args, **kwargs)
    builtins.range = range
```

#### **3. Save Changes**

After modifying the probability thresholds, save the `shadowops.py` file. The changes will take effect the next time a Python session starts.

> **Important:** Restart your Python interpreter or any running Python applications to apply the changes.

---

## Testing

Ensuring that **ShadowOps** functions as intended is crucial. Comprehensive testing helps verify that installation and uninstallation processes work correctly and that the package behaves as expected.

### Running Tests with `unittest`

**ShadowOps** includes unit tests written using Python's built-in `unittest` framework.

1. **Navigate to the Project Root Directory:**

    ```bash
    cd ShadowOps
    ```

2. **Run the Tests:**

    ```bash
    python -m unittest discover tests
    ```

    **Output Example:**

    ```
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.123s

    OK
    ```

### Running Tests with `pytest`

Alternatively, you can use `pytest`, which offers more features and a simpler syntax.

1. **Install `pytest`:**

    If you haven't installed `pytest`, do so using `pip`:

    ```bash
    pip install pytest
    ```

2. **Run `pytest`:**

    ```bash
    pytest
    ```

    **Output Example:**

    ```
    ============================ test session starts ============================
    platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    collected 10 items

    tests/test_cli.py .........                                         [100%]

    ============================= 10 passed in 0.05s =============================
    ```

> **Note:** `pytest` automatically discovers test files following the `test_*.py` or `*_test.py` naming convention.

---

## Troubleshooting

While using **ShadowOps**, you might encounter issues or unexpected behavior. This section provides solutions to common problems and guidance on resolving them.

### Common Issues

1. **Permission Errors:**

    - **Symptom:** Errors related to write permissions when installing or uninstalling **ShadowOps**.
    - **Solution:** Ensure you have the necessary permissions to modify the Python `site-packages` directory.
        - **Windows:** Run the command prompt as an administrator.
        - **macOS/Linux:** Use `sudo` to grant administrative privileges.

    **Example:**

    ```bash
    sudo shadowops install
    ```

2. **ShadowOps Not Activating:**

    - **Symptom:** Python sessions do not exhibit modified behaviors after installation.
    - **Solution:**
        - **Restart Python Sessions:** Changes take effect on new Python sessions. Restart any open Python interpreters or applications.
        - **Verify `sitecustomize.py`:** Ensure that `sitecustomize.py` in `site-packages` contains the line `import shadowops`.
        - **Check `shadowops.py` Placement:** Confirm that `shadowops.py` exists in the `site-packages` directory.

3. **Installation Fails Without Error Messages:**

    - **Symptom:** Installation command executes without confirming success.
    - **Solution:**
        - **Check Logs:** Review the terminal output for any warnings or informational messages.
        - **Verify File Changes:** Manually check if `shadowops.py` and modifications to `sitecustomize.py` have been applied.

4. **Uninstallation Incomplete:**

    - **Symptom:** Residual changes remain after uninstalling **ShadowOps**.
    - **Solution:**
        - **Manually Restore `sitecustomize.py`:** If uninstallation didn't restore `sitecustomize.py`, use the backup file (`sitecustomize.py.backup`) to restore it manually.
        - **Delete Residual Files:** Remove any leftover `shadowops.py` files from `site-packages`.

### Error Messages and Solutions

| **Error Message**                                 | **Cause**                                        | **Solution**                                                    |
|---------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------|
| `PermissionError: [Errno 13] Permission denied`   | Lack of write permissions in `site-packages`.    | Run the installation/uninstallation command with elevated rights. |
| `ImportError: Cannot import 'module_name'`         | ShadowOps' `validate_imports` blocked a module.   | Uninstall ShadowOps to restore normal import behavior.          |
| `FileNotFoundError: [Errno 2] No such file or directory: 'sitecustomize.py'` | Missing `sitecustomize.py`.                       | Manually create `sitecustomize.py` or reinstall ShadowOps.      |
| `shadowops.py does not exist.`                    | **shadowops.py** was not properly installed.      | Reinstall ShadowOps using the CLI or programmatically.           |

> **Tip:** Always ensure you have backups before making system-wide changes.

---

## Contribution Guidelines

Contributing to **ShadowOps** is welcome! Your contributions help improve the package and make it more robust. Follow the guidelines below to ensure a smooth collaboration process.

### How to Contribute

1. **Fork the Repository:**

    Navigate to the [ShadowOps GitHub Repository](https://github.com/yourusername/ShadowOps) and click the "Fork" button to create your own copy.

2. **Clone Your Fork:**

    ```bash
    git clone https://github.com/yourusername/ShadowOps.git
    cd ShadowOps
    ```

    > **Replace** `yourusername` with your actual GitHub username.

3. **Create a New Branch:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

    Choose a descriptive branch name that reflects the feature or bug fix.

4. **Make Changes:**

    Implement your feature, bug fix, or documentation update. Ensure your code adheres to the project's coding standards and best practices.

5. **Run Tests:**

    Ensure all existing tests pass and add new tests for your changes.

    ```bash
    python -m unittest discover tests
    ```

    Or, if using `pytest`:

    ```bash
    pytest
    ```

6. **Commit Your Changes:**

    ```bash
    git add .
    git commit -m "Add feature: your-feature-name"
    ```

    > **Tip:** Use clear and descriptive commit messages.

7. **Push to Your Fork:**

    ```bash
    git push origin feature/your-feature-name
    ```

8. **Create a Pull Request:**

    - Navigate to your fork on GitHub.
    - Click the "Compare & pull request" button.
    - Provide a clear description of your changes and the problem they solve.
    - Submit the pull request for review.

### Code of Conduct

By contributing to **ShadowOps**, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md). Please ensure respectful and constructive communication within the community.

### Reporting Bugs and Requesting Features

If you encounter a bug or have a feature request, please follow these steps:

1. **Check Existing Issues:**

    Search the [Issues](https://github.com/yourusername/ShadowOps/issues) section to see if your problem or idea has already been reported or discussed.

2. **Create a New Issue:**

    - Click the "New issue" button.
    - **Title:** Provide a clear and descriptive title.
    - **Description:**
        - **For Bugs:** Describe the bug, steps to reproduce, expected behavior, and any relevant screenshots or logs.
        - **For Features:** Explain the feature, its benefits, and any implementation ideas.

3. **Submit the Issue:**

    Once you've filled in the necessary details, submit the issue for review.

---

## Ethical Considerations

**ShadowOps** modifies Python's built-in functions, which can lead to unexpected behavior, system instability, or data loss. It's essential to use this package responsibly to prevent misuse or unintended consequences.

### Best Practices

1. **Obtain Explicit Consent:**

    - Deploy ShadowOps only in environments where all users are aware and have agreed to its use.
    - Avoid using ShadowOps in shared or production environments without proper authorization.

2. **Provide Clear Uninstallation Instructions:**

    - Ensure users can easily uninstall ShadowOps and restore normal Python behavior.
    - Maintain backups of modified files to facilitate easy restoration.

3. **Avoid Critical Systems:**

    - Do not deploy ShadowOps in systems where unintended behavior could lead to significant issues, such as data loss, security vulnerabilities, or service disruptions.

4. **Inform Users:**

    - Clearly document what ShadowOps does, how it modifies Python's behavior, and the potential impacts.
    - Encourage responsible usage and educate users about the changes being made.

5. **Respect Privacy and Security:**

    - Ensure that ShadowOps does not inadvertently expose sensitive information or create security loopholes.
    - Regularly review the code to prevent vulnerabilities.

### Disclaimer

**ShadowOps** is intended for educational purposes and harmless pranks within consenting environments. The author is not responsible for any misuse, data loss, or system instability resulting from the use of this package.

---

## License

This project is licensed under the [MIT License](LICENSE). 

---

# Conclusion

By following this comprehensive **Usage Guide**, you can effectively install, use, configure, and contribute to **ShadowOps**. Always prioritize ethical considerations and ensure that all modifications are performed responsibly to maintain system integrity and user trust.

If you encounter any issues not covered in this guide or have suggestions for improvement, feel free to [open an issue](https://github.com/yourusername/ShadowOps/issues) or submit a pull request.

Happy Coding!

---