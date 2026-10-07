from abc import ABC, abstractmethod
from typing import Any

from .config import ImageVideoRequest


class ImageVideoModel(ABC):
    @abstractmethod
    def generate_video(self, request: ImageVideoRequest) -> Any:
        raise NotImplementedError


class MockImageVideoModel(ImageVideoModel):
    def generate_video(self, request: ImageVideoRequest):
        return {
            "image_path": request.image_path,
            "prompt": request.prompt,
            "duration_seconds": request.duration_seconds,
            "fps": request.fps,
            "resolution": f"{request.width}x{request.height}",
            "motion": request.camera_motion,
            "sound": {
                "music_style": request.sound.music_style,
                "voiceover": request.sound.voiceover,
                "sound_effects": request.sound.sound_effects,
                "intensity": request.sound.intensity,
            },
            "status": "mock_ready",
        }
