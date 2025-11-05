
import kagglehub
import shutil
import os

# 기본 데이터 디렉토리를 정의합니다.
main_data_dir = '/home/JGY/mri_cnn/data'

# --- 데이터셋 1 ---
print("Processing 'navoneel/brain-mri-images-for-brain-tumor-detection'...")
# 기본 캐시에 다운로드합니다.
cached_path_1 = kagglehub.dataset_download('navoneel/brain-mri-images-for-brain-tumor-detection')
# 이 데이터셋을 위한 특정 목적지를 정의합니다.
dest_path_1 = os.path.join(main_data_dir, 'brain-mri-images-for-brain-tumor-detection')
# 깨끗한 이동을 위해 목적지가 존재하면 삭제합니다.
if os.path.exists(dest_path_1):
    shutil.rmtree(dest_path_1)
# 다운로드된 전체 디렉토리를 이동합니다.
shutil.move(cached_path_1, dest_path_1)
print(f"Dataset 1 moved to: {dest_path_1}")


# --- 데이터셋 2 ---
print("\nProcessing 'murtozalikhon/brain-tumor-multimodal-image-ct-and-mri'...")
# 기본 캐시에 다운로드합니다.
cached_path_2 = kagglehub.dataset_download('murtozalikhon/brain-tumor-multimodal-image-ct-and-mri')
# 이 데이터셋을 위한 특정 목적지를 정의합니다.
dest_path_2 = os.path.join(main_data_dir, 'brain-tumor-multimodal-image-ct-and-mri')
# 목적지가 존재하면 삭제합니다.
if os.path.exists(dest_path_2):
    shutil.rmtree(dest_path_2)
# 다운로드된 전체 디렉토리를 이동합니다.
shutil.move(cached_path_2, dest_path_2)
print(f"Dataset 2 moved to: {dest_path_2}")


print('\nData source import complete.')
