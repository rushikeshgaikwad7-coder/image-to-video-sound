from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SoundPlan:
    music_style: str = "ambient"
    voiceover: Optional[str] = None
    sound_effects: list[str] = field(default_factory=list)
    intensity: float = 0.6


@dataclass
class ImageVideoRequest:
    image_path: str
    prompt: str
    duration_seconds: int = 8
    fps: int = 24
    width: int = 1280
    height: int = 720
    camera_motion: str = "slow_zoom"
    sound: SoundPlan = field(default_factory=SoundPlan)
    seed: Optional[int] = None
