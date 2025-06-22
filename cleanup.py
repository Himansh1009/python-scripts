import os

# Define folder paths
base_folder = os.path.expanduser("~/Desktop/Temporary")
himanshu_folder = os.path.join(base_folder, "Himanshu")
trip_images_folder = os.path.join(base_folder, "TripImages")

# Get list of filenames (without extensions) from Himanshu folder
himanshu_images = {os.path.splitext(f)[0] for f in os.listdir(himanshu_folder) if f.lower().endswith(".jpg")}

# Iterate through TripImages folder
for file in os.listdir(trip_images_folder):
    file_path = os.path.join(trip_images_folder, file)
    file_name, file_ext = os.path.splitext(file)
    
    # Check if file is not in Himanshu folder's list and delete
    if file_name not in himanshu_images:
        os.remove(file_path)
        print(f"Deleted: {file}")

print("Cleanup complete.")

