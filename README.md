# Tools

<small>Click the folder above to check out my additional python tools so far :)</small>

<small>**Maya Commands Documentation:**  
https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/Commands/</small>

## Installation & Usage

To use these tools inside Autodesk Maya, clone this repository, add the repository's `scripts` folder to your Python path, and import the desired module.

```python
import sys
import os

# Replace this with the path to your cloned MayaScripts repository
repo_path = r"C:/path/to/your/cloned/MayaScripts"
scripts_path = os.path.join(repo_path, "scripts")

if scripts_path not in sys.path:
    sys.path.append(scripts_path)

# Import the desired tool
import tool_name
