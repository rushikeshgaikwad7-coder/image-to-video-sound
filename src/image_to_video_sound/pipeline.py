from pathlib import Path
from typing import Optional

from .audio import build_default_audio_prompt
from .config import ImageVideoRequest
from .models import ImageVideoModel


class ImageVideoPipeline:
    def __init__(self, model: ImageVideoModel, output_dir: str = "output"):
        self.model = model
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, request: ImageVideoRequest, output_path: Optional[str] = None):
        result = self.model.generate_video(request)
        audio_plan = build_default_audio_prompt(request)

        if output_path is None:
            output_path = str(self.output_dir / "image_video_output.mp4")

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        output_file.write_text(
            "# Placeholder media artifact\n"
            f"image_path={request.image_path}\n"
            f"prompt={request.prompt}\n"
            f"duration={request.duration_seconds}\n"
            f"fps={request.fps}\n"
            f"motion={request.camera_motion}\n"
            f"audio={audio_plan}\n",
            encoding="utf-8",
        )

        return {
            "output_path": str(output_file),
            "result": result,
            "audio_plan": audio_plan,
        }
