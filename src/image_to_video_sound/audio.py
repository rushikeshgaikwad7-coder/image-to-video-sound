from dataclasses import dataclass


@dataclass
class AudioSpec:
    music_style: str = "ambient"
    voiceover: str = ""
    sound_effects: list[str] | None = None
    volume: float = 0.5

    def __post_init__(self):
        if self.sound_effects is None:
            self.sound_effects = []


def build_default_audio_prompt(request):
    return {
        "music_style": request.sound.music_style,
        "voiceover": request.sound.voiceover or "soft narration",
        "sound_effects": request.sound.sound_effects or ["wind", "ambience"],
        "volume": request.sound.intensity,
    }
