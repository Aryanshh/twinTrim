import hashlib

def hash_file(filepath, chunk_size=4096):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates_by_hash(directory):
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = hash_file(filepath)

            if file_hash in file_hashes:
                duplicates.append((file_hash, filepath, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = filepath

    return duplicates
