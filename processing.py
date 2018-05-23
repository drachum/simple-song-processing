from pydub import AudioSegment
from pydub.playback import play

class SimpleVocalRemoval:
    def __init__(self):
        pass

    def remove_vocals(self, in_file_path, out_file_path):
        # gets stereo sound
        sound_stereo = AudioSegment.from_mp3(in_file_path)

        # separates sound into left and right bands
        try:
            sound_mono_left = sound_stereo.split_to_mono()[0]
            sound_mono_right = sound_stereo.split_to_mono()[1]
        except IndexError:
            raise IndexError("You've tried to remove vocals of a mono song, but only stereo songs are allowed")

        # TODO: we could take the mean of the two

        # Invert phase of the Right audio file
        sound_mono_right_inv = sound_mono_right.invert_phase()

        # Merge two L and R_inv files, this cancels out the centers
        sound_without_vocals = sound_mono_left.overlay(sound_mono_right_inv)

        # Export merged audio file
        fh = sound_without_vocals.export(out_file_path, format="mp3")

        # TODO: handle file handler here
