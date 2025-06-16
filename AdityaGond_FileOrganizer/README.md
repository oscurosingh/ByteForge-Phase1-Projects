# 🗂️ File Organizer using Tkinter

This Python script organizes files in a specified directory into categorized subfolders such as:
- **Documents**
- **Images**
- **Audios**
- **Videos**
- **Program Files**
- **Zip Files**
- **Web Files**

The app uses a simple GUI built with **Tkinter** to let the user enter a directory path. Once submitted, it categorizes the files based on their extensions and moves them into appropriate folders.

---

## 🚀 Features

- Simple GUI with Tkinter
- Automatically creates folders like `Documents`, `Images`, etc.
- Supports common file formats for each category
- Moves files instead of copying (helps save space)

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required except for built-in modules

---

## 📦 Installation

1. Clone this repository or download the script.
2. Make sure Python 3 is installed.
3. (Optional but recommended) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required modules:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Usage

1. Run the script:
    ```bash
    python file_organizer.py
    ```
2. Enter the full directory path where your files are located.
3. Click the "Categorize" button.
4. Files will be moved into new subdirectories based on file types.

---

## 📁 Folder Structure

After running, the structure may look like:
```
your-folder/
│
├── Documents/
├── Images/
├── Audios/
├── Videos/
├── Program Files/
├── Zip Files/
└── Web Files/
```

---

## 📌 Notes

- This tool **moves** files; they will not remain in the original folder.
- Avoid running this on system directories unless you know what you're doing.

---

## 📃 License

This project is open-source and free to use under the MIT License.

