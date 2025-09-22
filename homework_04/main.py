from media import (
    LocalStorage,
    S3Storage,
    AudioFile,
    VideoFile,
    ImageFile,
)

def main():
    """
    Demonstrates the usage of the media file class hierarchy.
    """
    # --- Initialize different storage backends ---
    print("--- Initializing Storage Backends ---")
    local_storage = LocalStorage(base_path="/Users/dannybear/media")
    s3_storage = S3Storage(bucket_name="my-media-bucket")
    print("-" * 35)
    print("\n")


    # --- 1. Create and save files to different storages ---
    print("--- 1. Creating and Saving Files ---")
    # Create an audio file on the local disk
    song = AudioFile(
        name="best_song.mp3",
        size=4_000_000,
        owner="dannybear",
        storage=local_storage,
        duration=180.5,
        artist="The Testers",
        album="Code Hits"
    )
    song.save()
    print(f"Created: {song} at {song.get_location()}")
    print("-" * 10)

    # Create a video file in S3
    movie = VideoFile(
        name="awesome_movie.mp4",
        size=1_200_000_000,
        owner="dannybear",
        storage=s3_storage,
        duration=7200.0,
        resolution="1920x1080",
        codec="H.264"
    )
    movie.save()
    print(f"Created: {movie} at {movie.get_location()}")
    print("-" * 10)

    # Create an image file in generic cloud storage
    photo = ImageFile(
        name="vacation_pic.jpg",
        size=2_500_000,
        owner="dannybear",
        storage=local_storage,
        resolution="4032x3024",
        color_profile="sRGB"
    )
    photo.save()
    print(f"Created: {photo} at {photo.get_location()}")
    print("-" * 35)
    print("\n")


    # --- 2. Update file metadata ---
    print("--- 2. Updating File Metadata ---")
    print(f"Before update: Owner is '{song.owner}'")
    song.update_owner("new_owner")
    print(f"After update: Owner is '{song.owner}'")
    print("-" * 35)
    print("\n")


    # --- 3. Perform file-specific actions ---
    print("--- 3. Performing File-Specific Actions ---")
    # Apply a filter to the image
    filtered_image_name = photo.apply_filter("sepia")
    print(f"Filter applied, new file would be '{filtered_image_name}'")
    print("-" * 10)

    # Convert a video
    converted_video_name = movie.convert_to("avi")
    print(f"Conversion finished, new file would be '{converted_video_name}'")
    print("-" * 10)

    # Extract features from audio
    audio_features = song.extract_features()
    print(f"Extracted features from audio: {audio_features}")
    print("-" * 35)
    print("\n")


    # --- 4. Delete a file ---
    print("--- 4. Deleting a File ---")
    print(f"Attempting to delete file: {movie}")
    movie.delete()
    print("Deletion process initiated.")
    print("-" * 35)


if __name__ == "__main__":
    main()
