from os import listdir, remove
from os.path import abspath, dirname, isfile as path_isfile, join as path_join
from shutil import copyfile, copytree, rmtree
from subprocess import run as subprocess_run


script_dir = dirname(abspath(__file__))
builders_dir = dirname(script_dir)
docker_dir = dirname(builders_dir)
project_dir = dirname(docker_dir)
lipikaar_website_dir = path_join(project_dir, "lipikaar_website")
backend_dir = path_join(lipikaar_website_dir, "backend")


def copy_all_from_dir_except(source_dir_path, dest_dir_path, files_and_dirs_to_leave):
    all_files_and_dirs = listdir(source_dir_path)

    files_and_dirs_to_copy = [name for name in all_files_and_dirs if name not in files_and_dirs_to_leave]

    for name in files_and_dirs_to_copy:
        source_file_or_dir_path = path_join(source_dir_path, name)
        dest_file_or_dir_path = path_join(dest_dir_path, name)

        if path_isfile(source_file_or_dir_path):
            copyfile(source_file_or_dir_path, dest_file_or_dir_path)
        else:
            copytree(source_file_or_dir_path, dest_file_or_dir_path)


def build_docker_image_from_current_dir(image_tag):
    docker_build_command = [
        "docker",
        "build",
        "-t",
        image_tag,
        ".",
    ]

    subprocess_run(docker_build_command)


def remove_all_from_dir_except(dir_path, files_and_dirs_to_keep):
    all_files_and_dirs = listdir(dir_path)

    file_and_dirs_to_delete = [name for name in all_files_and_dirs if name not in files_and_dirs_to_keep]

    for name in file_and_dirs_to_delete:
        file_or_dir_path = path_join(dir_path, name)
        if path_isfile(file_or_dir_path):
            remove(file_or_dir_path)
        else:
            rmtree(file_or_dir_path)


if __name__ == "__main__":
    # Build Frontend

    # Copy Frontend "build" folder to Backend

    # Copy Backend "static" folder "docker/volumes/server"


    copy_all_from_dir_except(backend_dir, script_dir, ["build", "volumes"])

    build_docker_image_from_current_dir("abhilakshsinghreen/lipikaar_server")

    remove_all_from_dir_except(script_dir, ["Dockerfile", "docker_build.py", ".dockerignore"])
    