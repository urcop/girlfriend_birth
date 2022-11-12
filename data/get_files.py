import os


def get_files(path):
    results = []
    for root, _, files in os.walk(path):
        for file in files:
            results.append((root, file))
    return results
