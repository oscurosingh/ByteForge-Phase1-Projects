import os
import shutil
import tkinter as tk

def check_subdirectory(parent_dir, sub_dir):
    global full_path
    full_path = os.path.join(parent_dir, sub_dir)
    return os.path.isdir(full_path)


def cat(d):
    for file in os.listdir(d):
        if os.path.isfile(os.path.join(d,file)):
            name, ext = os.path.splitext(file)
            if ext:
                if ext in ['.doc', '.docx', '.rtf', '.pdf', '.wpd', '.msg', '.wps', '.csv', '.txt']:
                    if check_subdirectory(d,"Documents"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                elif ext in ['.jpg', '.png', '.webp', '.gif', '.tif', '.bmp', '.eps', '.heif', '.jpeg']:
                    if check_subdirectory(d,"Images"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    
                elif ext in ['.mp3', '.wma', '.snd', '.wav', '.ra', '.au', '.aac']:
                    if check_subdirectory(d,"Audios"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    
                elif ext in ['.mp4', '.avi', '.mpg', '.mov', '.wmv', '.amv', '.mpeg', '.flv']:
                    if check_subdirectory(d,"Videos"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    
                elif ext in ['.c', '.cpp', '.java', '.py', '.js', '.ts', '.cs', '.swift', '.dta', '.pl', '.sh', '.bat', '.com', '.exe']:
                    if check_subdirectory(d,"Program Files"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    
                elif ext in ['.rar', '.zip', '.hqx', '.arj', '.tar', '.arc', '.sit', '.gz', '.z']:
                    if check_subdirectory(d,"Zip Files"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    
                elif ext in ['.html', '.htm', '.xhtml', '.asp', '.css', '.aspx', '.rss']:
                    if check_subdirectory(d,"Web Files"):
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))
                    else:
                        os.makedirs(full_path)
                        shutil.move(os.path.join(d, file), os.path.join(full_path, file))

                        

def main():
    try:
        a = (entry_d.get())
        cat(a)
        print("done")
        result_label.config(text="Done!")
    except Error:
        result_label.config(text="Invalid input")
        


window = tk.Tk()
window.title("File Organizer")
label_d = tk.Label(window, text="Enter the directory path:")
label_d.grid(row=0, column=0, padx=5, pady=5)
entry_d = tk.Entry(window)
entry_d.grid(row=0, column=1, padx=5, pady=5)
cat_button = tk.Button(window, text="Categorize", command=main)
cat_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


window.mainloop()
