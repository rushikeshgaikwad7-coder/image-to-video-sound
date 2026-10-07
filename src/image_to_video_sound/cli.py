import argparse
from pathlib import Path

from .audio import build_default_audio_prompt
from .config import ImageVideoRequest, SoundPlan
from .models import MockImageVideoModel
from .pipeline import ImageVideoPipeline


def main():
    parser = argparse.ArgumentParser(description="Generate a mock image-to-video artifact with sound")
    parser.add_argument("--image", required=True, help="Path to source image")
    parser.add_argument("--prompt", required=True, help="Text prompt describing the motion and scene")
    parser.add_argument("--output", default="output/demo.mp4", help="Output video path")
    parser.add_argument("--duration", type=int, default=8, help="Video duration in seconds")
    parser.add_argument("--fps", type=int, default=24, help="Output fps")
    parser.add_argument("--motion", default="slow_zoom", help="Camera motion style")
    args = parser.parse_args()

    request = ImageVideoRequest(
        image_path=args.image,
        prompt=args.prompt,
        duration_seconds=args.duration,
        fps=args.fps,
        camera_motion=args.motion,
        sound=SoundPlan(music_style="ambient", voiceover="soft narration", sound_effects=["wind", "sparks"], intensity=0.7),
    )

    pipeline = ImageVideoPipeline(model=MockImageVideoModel(), output_dir=str(Path(args.output).parent))
    response = pipeline.run(request, output_path=args.output)

    print(f"Generated media artifact at: {response['output_path']}")
    print(response["result"])
    print(response["audio_plan"])


if __name__ == "__main__":
    main()
