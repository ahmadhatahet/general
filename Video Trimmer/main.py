import hydra
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def timeToSeconds(t: str) -> int:
    """
    Convert the parsed time string from config.yaml to seconds

    Args:
        t (str): Supported format "hh:mm:ss"

    Returns:
        int: Total of seconds
    """
    n = [int(x) for x in t.split(":")]
    n[0] = n[0] * 60 * 60
    n[1] = n[1] * 60

    return sum(n)


@hydra.main(config_path=".", config_name="config")
def main(cfg):

    # add a prefix to the name of the trimmed video
    newName = cfg["path"].split("\\")
    newName[-1] = newName[-1].split(".")
    newName[-1][-1] = "_trimmed." + newName[-1][-1]
    newName[-1] = "".join(newName[-1])
    newName = "\\".join(newName)

    # parsing start and end time in seconds
    start = timeToSeconds(cfg["start"])
    end = timeToSeconds(cfg["end"])

    # check is already a trimmed video exist
    if os.path.isfile(newName):
        print("A trimmed version already exist")
        # ask to override the existing trimmed version
        a = input("Would like to overwrit the file? [y/n] \n")

        if a != "y":
            # if not permited exit
            return

    # trim the video
    ffmpeg_extract_subclip(cfg["path"], start, end, targetname=newName)


if __name__ == "__main__":
    main()
