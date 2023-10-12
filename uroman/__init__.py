import subprocess
import pkg_resources

from langcodes import Language


def uroman(input_string: str, language: str = None, chart: bool = False) -> str:
    script_path = pkg_resources.resource_filename(__name__, "uroman-pl/bin/uroman.pl")
    command = ["perl", script_path]

    # Add language flag if specified
    if language:
        language = Language.get(language).to_alpha3()
        command.extend(["-l", language])
    
    # Add chart flag if specified
    if chart:
        command.append("--chart")
    
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=input_string.encode())

    if process.returncode != 0:
        # There was an error
        raise OSError(f"uroman.pl failed with error code {process.returncode}: {stderr.decode()}")

    # Return the output as a string
    return stdout.decode()
