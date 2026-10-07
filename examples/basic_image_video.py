from image_to_video_sound.config import ImageVideoRequest, SoundPlan
from image_to_video_sound.models import MockImageVideoModel
from image_to_video_sound.pipeline import ImageVideoPipeline


if __name__ == "__main__":
    request = ImageVideoRequest(
        image_path="assets/sample.png",
        prompt="Slow zoom into a portrait with cinematic lighting and ambient wind",
        duration_seconds=7,
        fps=24,
        camera_motion="slow_zoom",
        sound=SoundPlan(music_style="ambient", voiceover="soft narration", sound_effects=["wind", "subtle texture"], intensity=0.6),
    )

    pipeline = ImageVideoPipeline(model=MockImageVideoModel(), output_dir="output")
    response = pipeline.run(request, output_path="output/example_media.mp4")
    print(response)
