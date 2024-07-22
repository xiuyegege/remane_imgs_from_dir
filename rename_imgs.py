import os
import shutil
from datetime import datetime
import uuid

def rename_and_move_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                if os.path.isfile(file_path):
                    timestamp = os.path.getmtime(file_path)
                    # 使用更短的时间戳格式
                    dt_object = datetime.fromtimestamp(timestamp)
                    short_time_format = dt_object.strftime('%Y%m%d_%H%M%S')
                    # 或者使用UUID
                    # uuid_str = str(uuid.uuid4())
                    new_filename = f"{short_time_format}_{filename}"
                    new_filepath = os.path.join(target_dir, new_filename)
                    shutil.move(file_path, new_filepath)
                    print(f"Moved and renamed: {file_path} -> {new_filepath}")

if __name__ == "__main__":
    source_dir = r".\ipt"
    target_dir = r".\opt"
    rename_and_move_files(source_dir, target_dir)