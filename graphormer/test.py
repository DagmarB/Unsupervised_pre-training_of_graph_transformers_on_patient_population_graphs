import os

split = "val"
folder = f"data/mimic-iii-0/{split}"
patient_dirs = [d for d in os.listdir(folder) if d.startswith("patient")]

def rmdir(path):
    for f in os.listdir(path):
        fp = os.path.join(path, f)
        if os.path.isdir(fp):
            rmdir(fp)
        else:
            os.remove(fp)
    os.rmdir(path)

for pd in patient_dirs:
    f = os.path.join(folder, pd, "ts_treatment.csv")
    if os.path.getsize(f) < 960: # 24 records
        print(f"{pd} size is {os.path.getsize(f)} deleting...")
        rmdir(os.path.join(folder, pd))