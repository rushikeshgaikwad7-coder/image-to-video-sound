from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from image_to_video_sound.config import ImageVideoRequest, SoundPlan
from image_to_video_sound.models import MockImageVideoModel
from image_to_video_sound.pipeline import ImageVideoPipeline


if __name__ == "__main__":
    request = ImageVideoRequest(
        image_path="assets/example.png",
        prompt="A cinematic dolly-in shot of a portrait with atmospheric lighting and a subtle ambient sound bed",
        duration_seconds=9,
        fps=24,
        camera_motion="dolly_in",
        sound=SoundPlan(music_style="cinematic", voiceover="narration", sound_effects=["wind", "soft ambience"], intensity=0.7),
    )

    pipeline = ImageVideoPipeline(model=MockImageVideoModel(), output_dir="output")
    result = pipeline.run(request, output_path="output/cinematic_example.mp4")
    print(result)
