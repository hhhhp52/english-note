# english-note

## 1. TODO
 - [ ] Testing Vocabulary[Choose question]
 - [ ] Creating Vocabulary[Add asking ChatGPT]
 - [ ] Backup data
 - [ ] Send Daily Vocabulary Review[Using Line Notification]
 - [ ] Package The Application

## 2. Folder Structure
    - gui : Function layout and function sub-function
    - helpers  
    - config.py
    - main.py
    - transfer.py

## 3. Packaging `english-note` as a Desktop Application

- To package your `english-note` application as a desktop application, you can use PyInstaller, a popular tool for converting Python programs into standalone executables.

### Step 1: Install PyInstaller

- If you haven't already installed PyInstaller, you can do so via pip:

```bash
pip install pyinstaller
```

### Step 2: Create a Spec File

- PyInstaller can automatically generate a spec file for your application. Navigate to your project directory in the terminal and run:

```bash
pyinstaller --onefile main.py
```
- This command will create a main.spec file.

### Step 3: Customize Spec File (Optional)

- You can edit the main.spec file to customize the build process. For example, you can specify additional files to include or exclude, set the application icon, etc.

### Step 4: Build the Executable

- Once you have your spec file configured (if necessary), you can build the executable by running PyInstaller with the spec file:

```bash
pyinstaller main.spec
```
- This command will generate a dist directory containing the standalone executable file for your application.

### Step 5: Test the Executable

- Navigate to the dist directory and run your application to make sure it works as expected:

```bash
cd dist
./main
```

- This command will generate a dist directory containing the standalone executable file for your application.

### Step 6: Distribute Your Application
- You can now distribute the generated executable file (main) to others. They can run it on their systems without needing Python or any dependencies installed.
- Make sure to test the application on different systems to ensure compatibility.