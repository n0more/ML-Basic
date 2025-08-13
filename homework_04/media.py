from datetime import datetime



class LocalStorage(Storage):
    """Represents storage on a local filesystem."""
    def __init__(self, base_path="/tmp/media"):
        self.base_path = base_path
        print(f"Initialized LocalStorage at '{self.base_path}'")

    def save(self, file: 'MediaFile'):
        # In a real implementation, this would involve file I/O.
        print(f"Saving '{file.name}' to local disk at {self.base_path}/{file.name}")

    def delete(self, file: 'MediaFile'):
        # In a real implementation, this would involve os.remove().
        print(f"Deleting '{file.name}' from local disk.")

    def get_location(self, file: 'MediaFile') -> str:
        return f"file://{self.base_path}/{file.name}"


class S3Storage(Storage):
    """Represents storage in an AWS S3 bucket."""
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        print(f"Initialized S3Storage for bucket '{self.bucket_name}'")

    def save(self, file: 'MediaFile'):
        # In a real implementation, this would use boto3 or a similar library.
        print(f"Uploading '{file.name}' to S3 bucket '{self.bucket_name}'")

    def delete(self, file: 'MediaFile'):
        # In a real implementation, this would use boto3.
        print(f"Deleting '{file.name}' from S3 bucket '{self.bucket_name}'")

    def get_location(self, file: 'MediaFile') -> str:
        return f"s3://{self.bucket_name}/{file.name}"


class MediaFile:
    """
    Base class for a media file.
    Handles common attributes and operations like save, delete, and update.
    """
    def __init__(self, name: str, size: int, owner: str, storage: Storage):
        self.name = name
        self.size = size
        self.creation_date = datetime.now()
        self.owner = owner
        self.storage = storage

    def __str__(self):
        return f"'{self.name}' ({self.size} bytes, created on {self.creation_date.strftime('%Y-%m-%d')} by {self.owner})"

    def save(self):
        """Saves the file using its associated storage backend."""
        self.storage.save(self)

    def delete(self):
        """Deletes the file using its associated storage backend."""
        self.storage.delete(self)

    def get_location(self) -> str:
        """Gets the file's location from its storage backend."""
        return self.storage.get_location(self)

    def update_owner(self, new_owner: str):
        """Updates the owner of the file and persists the change."""
        print(f"Updating owner of '{self.name}' from '{self.owner}' to '{new_owner}'")
        self.owner = new_owner
        self.save()


class AudioFile(MediaFile):
    """Represents an audio file with specific metadata."""
    def __init__(self, name: str, size: int, owner: str, storage: Storage, duration: float, artist: str, album: str):
        super().__init__(name, size, owner, storage)
        self.duration = duration
        self.artist = artist
        self.album = album

    def extract_features(self):
        """Placeholder for audio-specific feature extraction (e.g., MFCCs)."""
        print(f"Extracting audio features from '{self.name}'...")
        return {"type": "audio", "duration": self.duration, "artist": self.artist}


class VideoFile(MediaFile):
    """Represents a video file with specific metadata."""
    def __init__(self, name: str, size: int, owner: str, storage: Storage, duration: float, resolution: str, codec: str):
        super().__init__(name, size, owner, storage)
        self.duration = duration
        self.resolution = resolution
        self.codec = codec

    def convert_to(self, new_format: str):
        """Placeholder for video conversion (e.g., using ffmpeg)."""
        print(f"Converting video file '{self.name}' to {new_format}...")
        return f"converted_{self.name}.{new_format}"


class ImageFile(MediaFile):
    """Represents an image file with specific metadata."""
    def __init__(self, name: str, size: int, owner: str, storage: Storage, resolution: str, color_profile: str):
        super().__init__(name, size, owner, storage)
        self.resolution = resolution
        self.color_profile = color_profile

    def apply_filter(self, filter_name: str):
        """Placeholder for applying an image filter (e.g., using Pillow/OpenCV)."""
        print(f"Applying filter '{filter_name}' to '{self.name}'...")
        return f"filtered_{self.name}"
